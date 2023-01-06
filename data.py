import pandas as pd
import numpy as np

def dataLimit(df : pd.DataFrame, init: str, final: str, fieldname = "datetime") -> pd.DataFrame:
  """
  @brief: Dado um dataframe, uma data inicial e uma data final, retorna um dataframe com os índices cuja data na coluna 'fieldname' esteja entre essas.
  
  @param df: DataFrame a ser utilizado
  @param init: Data inicial
  @param final: Data Final
  @param fieldname: Nome do campo com as datas
  
  @return: DataFrame com as datas no período Indicado
  """
  df_new = df[df[fieldname] >= init]
  df_new = df_new[df_new[fieldname] <= final]
  
  return df_new
