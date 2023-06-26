import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    # Create scatter plot
    year =  df['Year']
    csiro = df['CSIRO Adjusted Sea Level']
    ax = plt.scatter(x = year, y = csiro)
    
    # Create first line of best fit
    res = linregress(year, csiro)
    fx = np.array([i for i in range (year.min(), 2051)])
    fy = res.intercept + res.slope * fx
    ax = plt.plot(fx, fy, color  = 'red')
    
    # Create second line of best fit
    new_year = df[df['Year'] >= 2000]['Year']
    new_csiro = df[df['Year'] >= 2000]['CSIRO Adjusted Sea Level']
    
    new_res = linregress(new_year, new_csiro)
    new_fx = np.array([i for i in range(new_year.min(), 2051)])
    new_fy = new_res.intercept + new_res.slope * new_fx
    
    ax = plt.plot(new_fx, new_fy, color = 'green')
    
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()