'''Module responsible for training jobs.'''
import pandas as pd
import numpy as np
from sklearn.ensemble import ExtraTreesClassifier
from typing import Tuple


class TrainJob:
    '''
    This class encapsulates the training process for an Extra Trees classifier
    model for predicting online order availability.
    '''

    def train(self, df: pd.DataFrame) -> ExtraTreesClassifier:
        '''
        Trains an Extra Trees classifier model using the provided DataFrame.

        Args:
            df (pd.DataFrame): The input DataFrame containing restaurant data.

        Returns:
            ExtraTreesClassifier: The trained Extra Trees classifier model.
        '''

        x, y = self._split_data(df)
        ET_model = ExtraTreesClassifier()
        ET_model.fit(x, y)

        return ET_model

    def _split_data(self, df: pd.DataFrame) -> Tuple[pd.DataFrame, np.array]:
        '''
        Splits the input DataFrame into features and labels for training.

        Args:
            df (pd.DataFrame): The input DataFrame containing restaurant data.

        Returns:
            Tuple[pd.DataFrame, np.array]: A tuple containing the features (x) and labels (y).
        '''

        x = df.drop('online_order', axis=1)
        y = df['online_order']

        return x, y
