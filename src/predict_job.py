'''In this module it is executed the prediction job.'''
import pandas as pd
import numpy as np
from sklearn.ensemble import ExtraTreesClassifier


class PredictJob():
    '''
    A class containing the predict job.
    '''

    def predict(self, model: ExtraTreesClassifier, df: pd.DataFrame) -> np.array:
        '''
        Predict the target variable using the provided model and Pandas DataFrame.
        
        Args:
            model (ExtraTreeClassifier): The trained classification model.
            df (pd.DataFrame): The input DataFrame containing features for prediction.
        
        Returns:
            yhat (np.array): A numpy array containing predictions.
        '''
        yhat = model.predict(df)

        return yhat
