import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
bmi = df['weight'] / (df['height'] / 100) ** 2
df['overweight'] = bmi.apply(lambda x : 1 if x > 25 else 0 ) 
df['cholesterol'] = df['cholesterol'].apply(lambda x : 0 if x == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x : 0 if x == 1 else 1)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = df.melt(id_vars = ['cardio'], value_vars = ['cholesterol', 'gluc', 'smoke', 'alco', 'active','overweight']) 

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = df_cat.groupby(['cardio', 'variable', 'value'], as_index = False)['value'].value_counts()
    df_cat = df_cat.rename(columns = {'count':'total'})
    # Draw the catplot with 'sns.catplot()'
    fig = sns.catplot(x = 'variable', y = 'total', data = df_cat, kind = 'bar', hue = 'value', col = 'cardio').fig

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) & # diastolic pressure is higher than systolic
             (df['height'] >= df['height'].quantile(0.025)) & # height is greater than 2.5th percentile
             (df['height'] <= df['height'].quantile(0.975)) & # height is less than 97.5th percentile
             (df['weight'] >= df['weight'].quantile(0.025)) & # weight is greater than 2.5th percentile
             (df['weight'] <= df['weight'].quantile(0.975))]  # weight is less than 97.5th percentile
# Correlation Matrix

    # Calculate the correlation matrix
    corr = df_heat.corr(method = 'pearson')

    # Generate a mask for the upper triangle
    mask = np.triu(corr)

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize = (12,12))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, mask = mask, fmt = '.1f', annot = True, cmap = 'icefire',\
                 center = 0.08, square= True ,linewidths=0.5, cbar_kws={'shrink':0.5})


    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
