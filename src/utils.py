import numpy as np
import pandas as pd


def read_pattern(file_path: str) -> np.ndarray:
    """
    Return a matrix of 1's and 0's from a given txt file also containing 1's and 0's.
    """

    dataframe = pd.read_csv(file_path, sep=r'\s+', header=None)
    return dataframe.to_numpy()
