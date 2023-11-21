import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np


def draw_plot():
  # Read data from file
  df = pd.read_csv('epa-sea-level.csv')
  x = df['Year']
  y = df['CSIRO Adjusted Sea Level']
  x_2050 = np.arange(1880, 2051)
  df_2000 = df[df['Year'] >= 2000]
  x_2000 = df_2000['Year']
  y_2000 = df_2000['CSIRO Adjusted Sea Level']
  x_2000_2050 = np.arange(2000, 2051)

  # Create scatter plot

  fig, ax = plt.subplots()
  ax.scatter(x, y)
  # Create first line of best fit
  result = linregress(x, y)
  ax.plot(x_2050,
          result.intercept + result.slope * x_2050,
          color='red',
          label='First best fit')

  # Create second line of best fit

  result2 = linregress(x_2000, y_2000)
  ax.plot(x_2000_2050,
          result2.intercept + result2.slope * x_2000_2050,
          color='green',
          label='Second best fit (>2000)')
  # Add labels and title
  ax.set_title('Rise in Sea Level')
  ax.set_xlabel('Year')
  ax.set_ylabel('Sea Level (inches)')
  ax.legend()

  # Save plot and return data for testing (DO NOT MODIFY)
  plt.savefig('sea_level_plot.png')
  return plt.gca()
