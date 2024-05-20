import numpy as np
import pandas as pd


def read_pattern(file_path: str) -> np.ndarray:
    dataframe = pd.read_csv(file_path, sep=r'\s+', header=None)
    return dataframe.to_numpy()