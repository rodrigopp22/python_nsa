import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split

def split_df(df, features, result_col):
    x = df.loc[:, features].values
    y = df.loc[:,[result_col]].values

    return x,y

def scale_dataframe(df):
    df = df.sort_index()
    scaler = MinMaxScaler()
    scaled_df = pd.DataFrame(scaler.fit_transform(df))
    return scaled_df

def run_pca(df: pd.DataFrame, features: list, result_col: str):
    x, y = split_df(df, features, result_col)
    x = StandardScaler().fit_transform(x)
    print(x.head())

    pca = PCA(0.95)
    principal_components = pca.fit_transform(x)
    pca_df = pd.DataFrame(data = principal_components)
    print(pca_df.head())

    df_final = pd.concat([pca_df, df[[result_col]]], axis = 1)

    return df_final


