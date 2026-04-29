import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    # linregress over the entire dataset
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # Create an array of years from 1880 to 2050
    years_extended = pd.Series(range(1880, 2051))
    
    # Plot the line of best fit
    ax.plot(years_extended, intercept + slope * years_extended, 'r', label='Best Fit Line 1880-2050')

    # Create second line of best fit
    # Filter for data from year 2000 onwards
    df_recent = df[df['Year'] >= 2000]
    
    # linregress over the recent dataset
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    
    # Create an array of years from 2000 to 2050
    years_recent_extended = pd.Series(range(2000, 2051))
    
    # Plot the second line of best fit
    ax.plot(years_recent_extended, intercept_recent + slope_recent * years_recent_extended, 'green', label='Best Fit Line 2000-2050')

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    ax.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
