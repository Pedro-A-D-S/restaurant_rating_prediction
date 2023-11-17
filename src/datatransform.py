'''This file contains the transformations necessary on the dataset.'''
import pandas as pd
from sklearn.preprocessing import LabelEncoder


class DataTransformer:

    def __init__(self, df: pd.DataFrame):
        '''
        Initializer containing Pandas DataFrame that's going to be transformed.
        '''
        self.df = df

    def drop_cols(self, df: pd.DataFrame) -> pd.DataFrame:
        '''
        Drops a list of columns.

        Args:
            df (pd.DataFrame): The dataframe to be transformed.

        Returns:
            df (pd.DataFrame): The dataframe after dropping the list of columns.
        '''
        cols = ['url', 'phone', 'rate']
        df = df.drop(columns=cols, axis=1)

        return df

    def rename_cols(self, df: pd.DataFrame) -> pd.DataFrame:
        '''
        Renames columns from dataset.

        Args:
            df (pd.DataFrame): The dataframe to be transformed.

        Returns:
            df (pd.DataFrame): The dataframe after the list of columns to be renamed.
        '''
        cols = {
            'approx_cost(for two people)': 'cost',
            'listed_in(type)': 'type',
            'listed_in(city)': 'city'
        }
        df = df.rename(columns=cols)

        return df

    def transform_cost(self, df: pd.DataFrame) -> pd.DataFrame:
        '''
        Applies transformation in for the cost column.

        Args:
            df (pd.DataFrame): The dataframe to be transformed.

        Returns:
            df (pd.DataFrame): The dataframe after the transformation.
        '''
        df['cost'] = df['cost'].fillna(-1).astype(
            str).apply(lambda x: x.replace(',', ''))
        df['cost'] = df['cost'].astype('int64')

        return df

    def transform_online_order(self, df: pd.DataFrame) -> pd.DataFrame:
        '''
        Transforms the online order column.

        Args:
            df (pd.DataFrame): The dataframe to be transformed.

        Returns:
            df (pd.DataFrame): The dataframe after the transformation.
        '''
        map_info = {'Yes': 1, 'No': 0}
        df['online_order'] = df['online_order'].map(map_info)
        df['online_order'] = pd.to_numeric(df['online_order'])

        return df

    def transform_book_table(self, df: pd.DataFrame) -> pd.DataFrame:
        '''
        Transforms the book table column.

        Args:
            df (pd.DataFrame): The dataframe to be transformed.

        Returns:
            df (pd.DataFrame): The dataframe after the transformation.
        '''
        map_info = {'Yes': 1, 'No': 0}
        df['book_table'] = df['book_table'].map(map_info)
        df['book_table'] = pd.to_numeric(df['book_table'])

        return df

    def label_encoder(self, df: pd.DataFrame) -> pd.DataFrame:
        '''
        Encodes a list of columns.

        Args:
            df (pd.DataFrame): The dataframe to be transformed.

        Returns:
            df (pd.DataFrame): The dataframe after the transformation.
        '''
        le = LabelEncoder()

        df['location'] = le.fit_transform(df['location'])
        df['rest_type'] = le.fit_transform(df['rest_type'])
        df['cuisines'] = le.fit_transform(df['cuisines'])
        df['menu_item'] = le.fit_transform(df['menu_item'])

        return df
