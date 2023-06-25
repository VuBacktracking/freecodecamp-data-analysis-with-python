import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates = ['date'], index_col = 'date')

# Clean data
df = df[(df['value'] >= df.value.quantile(0.025)) & (df['value'] <= df.value.quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    df_line = df.copy()
  
    fig, ax = plt.subplots(figsize = (14,4))
    # Draw line plot
    ax.plot(df_line.index, df_line['value'], c = 'red')
    
    # Customiztion
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar_1 = df.copy()
    # Extract and create 'month' and 'year' columns
    df_bar_1['month'] = df_bar_1.index.month
    df_bar_1['year'] = df_bar_1.index.year
    
    # Clean the data 
    df_bar = df_bar_1.groupby(['year',   
    'month'])['value'].mean().unstack()
    df_bar = df_bar.fillna(0)

    # Draw bar plot
    fig = df_bar.plot(kind = 'bar',figsize = (15,5),legend = True, \
                     xlabel = 'Years', ylabel = 'Average Page Views').figure
    
    plt.legend(['January', 'February', 'March', 'April', 'May',\
                'June', 'July', 'August', 'September',\
                'October', 'November', 'December'])

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True) 
    
    df_box['month_num'] = df_box['date'].dt.month
    df_box = df_box.sort_values('month_num', ascending = True)
    
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    df_box['year'] = [d.year for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(nrows = 1, ncols = 2, figsize = (18,6))
    
    ax0 = sns.boxplot(x = 'year', y = 'value', data = df_box,\
                          ax = ax[0])
    ax0.set_ylabel('Page Views')
    ax0.set_xlabel('Year')
    ax0.set_title('Year-wise Box Plot (Trend)')
    
    ax1 = sns.boxplot(x= 'month', y = 'value', data = df_box,\
                          ax = ax[1])
    ax1.set_ylabel('Page Views')
    ax1.set_xlabel('Month')
    ax1.set_title('Month-wise Box Plot (Seasonality)')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
