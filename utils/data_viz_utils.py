"""Utility functions for data visualization notebooks.

This module contains functions used across the data visualization
notebooks in this repository. They provide convenient wrappers for
loading the Canada immigration dataset and for producing simple plots.
"""

from typing import Iterable, Optional

import pandas as pd
import matplotlib.pyplot as plt

CANADA_DATA_URL = (
    "https://s3-api.us-geo.objectstorage.softlayer.net/"
    "cf-courses-data/CognitiveClass/DV0101EN/labs/Data_Files/Canada.xlsx"
)


def load_canada_immigration() -> pd.DataFrame:
    """Load the Canada immigration dataset from the public URL.

    Returns
    -------
    pandas.DataFrame
        The immigration data with rows for countries and columns for years.
    """
    df = pd.read_excel(
        CANADA_DATA_URL,
        sheet_name="Canada by Citizenship",
        skiprows=range(20),
        skipfooter=2,
    )
    return df


def line_plot(
    df: pd.DataFrame,
    columns: Iterable[str],
    *,
    title: Optional[str] = None,
    ylabel: str = "Number of Immigrants",
) -> plt.Axes:
    """Create a line plot for the specified columns of a dataframe.

    Parameters
    ----------
    df : pandas.DataFrame
        The dataframe containing the data to plot. The index should represent
        the x-axis and the columns should contain numeric values.
    columns : Iterable[str]
        A list of column names within ``df`` to plot.
    title : str, optional
        Title for the resulting plot.
    ylabel : str
        Label for the y-axis.

    Returns
    -------
    matplotlib.axes.Axes
        The Axes object of the generated plot. This allows further
        customisation by the caller.
    """
    ax = df[columns].plot(kind="line")
    ax.set_xlabel("Year")
    ax.set_ylabel(ylabel)
    if title:
        ax.set_title(title)
    return ax


__all__ = ["load_canada_immigration", "line_plot"]
