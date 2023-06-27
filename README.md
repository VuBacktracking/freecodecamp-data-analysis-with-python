# Freecodecamp Data Analysis With Python
5 Projects in Data Analysis With Python Course on freecodecamp
This repository contains projects completed as part of the FreeCodeCamp Data Analysis with Python curriculum. Each project focuses on applying data analysis techniques using Python and various libraries. Below, you will find a brief description of each project and instructions for running them.
## Project 1: Mean-Variance-Standard Deviation Calculator
**Description**:\
Create a function named `calculate()` in `mean_var_std.py` that uses Numpy to output the mean, variance, standard deviation, max, min, and sum of the rows, columns, and elements in a 3 x 3 matrix.
The input of the function should be a list containing 9 digits. The function should convert the list into a 3 x 3 Numpy array, and then return a dictionary containing the mean, variance, standard deviation, max, min, and sum along both axes and for the flattened matrix.
## Project 2: Demographic Data Analyzer
**Description**:\
You must use Pandas to answer the following questions:
  * How many people of each race are represented in this dataset? This should be a Pandas series with race names as the index labels. (race column)
  * What is the average age of men?
  * What is the percentage of people who have a Bachelor's degree?
  * What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
  * What percentage of people without advanced education make more than 50K?
  * What is the minimum number of hours a person works per week?
  * What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
  * What country has the highest percentage of people that earn >50K and what is that percentage?
  * Identify the most popular occupation for those who earn >50K in India.
## Project 3: Medical Data Visualizer
**Description**:\
In this project, you will visualize and make calculations from medical examination data using matplotlib, seaborn, and pandas. The dataset values were collected during medical examinations.\
Create a chart similar to `examples/Figure_1.png`, where we show the counts of good and bad outcomes for the `cholesterol`, `gluc`, `alco`, `active`, and `smoke` variables for patients with `cardio`=1 and `cardio`=0 in different panels.\
Create a correlation matrix using the dataset. Plot the correlation matrix using seaborn's `heatmap()`. Mask the upper triangle. The chart should look like `examples/Figure_2.png`.
## Project 4: Page View Time Series Visualizer
**Description**:
- Create a `draw_line_plot` function that uses Matplotlib to draw a line chart similar to `examples/Figure_1.png`. The title should be `Daily freeCodeCamp Forum Page Views 5/2016-12/2019`. The label on the x-axis should be `Date` and the label on the y-axis should be `Page Views`.
- Create a `draw_bar_plot` function that draws a bar chart similar to `examples/Figure_2.png`. It should show the average daily page views for each month grouped by year. The legend should show month labels and have a title of `Months`. On the chart, the label on the x-axis should be `Years` and the label on the y-axis should be `Average Page Views`.
- Create a `draw_box_plot` function that uses Seaborn to draw two adjacent box plots similar to `examples/Figure_3.png`. These box plots should show how the values are distributed within a given year or month and how it compares over time. The title of the first chart should be `Year-wise Box Plot (Trend)` and the title of the second chart should be `Month-wise Box Plot (Seasonality)`. Make sure the month labels on the bottom start at `Jan` and the x and y axis are labeled correctly. The boilerplate includes commands to prepare the data.
## Project 5: Sea Level Predictor
**Description**:\
You will analyze a dataset of the global average sea level change since 1880. You will use the data to predict the sea level change through year 2050.
Use the data to complete the following tasks:
Use Pandas to import the data from `epa-sea-level.csv`.
Use `matplotlib` to create a scatter plot using the Year column as the x-axis and the CSIRO Adjusted Sea Level column as the y-axis.
Use the `linregress` function from `scipy.stats` to get the slope and y-intercept of the line of best fit. Plot the line of best fit over the top of the scatter plot. Make the line go through the year 2050 to predict the sea level rise in 2050.
Plot a new line of best fit just using the data from year 2000 through the most recent year in the dataset. Make the line also go through the year 2050 to predict the sea level rise in 2050 if the rate of rise continues as it has since the year 2000.
The x label should be `Year`, the y label should be `Sea Level (inches)`, and the title should be `Rise in Sea Level`.
Unit tests are written for you under `test_module.py`.
The boilerplate also includes commands to save and return the image.

## Usage
Follow the instructions provided in each project's respective Jupyter Notebook file to run the code and perform the data analysis tasks.

### Contributing
Contributions to this project are not accepted as this is for educational purposes only.

## License
This project is licensed under the MIT License.

## Acknowledgments
The FreeCodeCamp community for providing the Data Analysis with Python curriculum.
Any additional acknowledgments or credits.
