import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(
        df['Year'],
        df['CSIRO Adjusted Sea Level']
    )

    # First line of best fit
    result = linregress(
        df['Year'],
        df['CSIRO Adjusted Sea Level']
    )

    x_pred = range(
        df['Year'].min(),
        2051
    )

    y_pred = (
        result.slope * x_pred
        + result.intercept
    )

    ax.plot(x_pred, y_pred)

    # Second line of best fit (2000 onwards)
    df_recent = df[df['Year'] >= 2000]

    result_recent = linregress(
        df_recent['Year'],
        df_recent['CSIRO Adjusted Sea Level']
    )

    x_recent = range(
        2000,
        2051
    )

    y_recent = (
        result_recent.slope * x_recent
        + result_recent.intercept
    )

    ax.plot(x_recent, y_recent)

    # Labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')

    # Save plot and return data for testing
    fig.savefig('sea_level_plot.png')
    return plt.gca()
