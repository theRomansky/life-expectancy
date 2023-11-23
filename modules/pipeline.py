import pandas as pd
import logging
import dill

from datetime import datetime
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import  Pipeline
from sklearn.preprocessing import FunctionTransformer
from sklearn.compose import ColumnTransformer, make_column_selector
from sklearn.model_selection import cross_val_score

from xgboost import XGBRegressor
from catboost import CatBoostRegressor


def filter_data(df: pd.DataFrame) -> pd.DataFrame:
    columns_to_take = [
        'SubRegion',
        'PopDens',
        'PopGrowth%',
        'AdolFertRate',
        'AgriValAdd%GDP',
        'FertRate',
        'GNI/CapAtlas',
        'InflConsPric%',
        'MobileSubs/100',
        'MortRateU5',
        'UrbanPopGrowth%'
    ]

    return df[columns_to_take]


def pipeline() -> None:
    df = pd.read_csv('../data/world_development_data_imputed.csv')

    X = df.drop('LifeExpBirth', axis=1)
    y = df['LifeExpBirth']

    numerical_features = make_column_selector(dtype_include=['int64', 'float64'])
    categorical_features = make_column_selector(dtype_include='object')

    numerical_transformer = Pipeline(steps=[
        ('Scaler', StandardScaler())
    ])

    categorical_transformer = Pipeline(steps=[
        ('Encoder', OneHotEncoder(handle_unknown='ignore'))
    ])

    column_transformer = ColumnTransformer(transformers=[
        ('numerical', numerical_transformer, numerical_features),
        ('categorical', categorical_transformer, categorical_features)
    ])

    preprocessor = Pipeline(steps=[
        ('filter', FunctionTransformer(filter_data)),
        ('column_transformer', column_transformer)
    ])


    models = [
        XGBRegressor(learning_rate=0.245, reg_lambda=0.95, reg_alpha=0.01),
        CatBoostRegressor()
    ]

    best_score = .0
    best_pipe = None
    for model in models:

        pipe = Pipeline([
            ('preprocessor', preprocessor),
            ('regressor', model)
        ])

        score = cross_val_score(pipe, X, y, cv=4, scoring='neg_mean_squared_error')
        logging.info(f'model: {type(model).__name__}, mse_mean: {score.mean():.4f}, acc_std: {score.std():.4f}')
        if score.mean() < best_score:
            best_score = score.mean()
            best_pipe = pipe

    logging.info(f'best model: {type(best_pipe.named_steps["regressor"]).__name__}, mse: {best_score:.4f}')

    best_pipe.fit(X, y)
    model_filename = f'../models/life_expectancy_pipe_{datetime.now().strftime("%Y%m%d%H%M")}.pkl'

    with open(model_filename, 'wb') as file:
        dill.dump(best_pipe, file)

    logging.info(f'Model is saved as {model_filename}')


if __name__ == '__main__':
    pipeline()
