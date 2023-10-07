
"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.

"""

import pandas as pd
import re

def ingest_data():
    df=pd.read_fwf('clusters_report.txt',widths=[9,16,16,77])
    df=df.ffill()
    df=df.groupby(df.columns[0]).agg({df.columns[1]: 'first', df.columns[2]: 'first', df.columns[3]: lambda x: ' '.join(x)}).reset_index()
    df=df.rename(columns={'Cluster':'cluster','Cantidad de':'cantidad_de_palabras_clave','Porcentaje de':'porcentaje_de_palabras_clave','Principales palabras clave':'principales_palabras_clave'})
    df.drop(0,axis=0,inplace=True)
    df['cluster'] = df['cluster'].astype(int)
    df = df.sort_values('cluster')
    df['cantidad_de_palabras_clave'] = df['cantidad_de_palabras_clave'].astype(int)
    df['porcentaje_de_palabras_clave']=df['porcentaje_de_palabras_clave'].str.replace('%', '', regex=True)
    df['porcentaje_de_palabras_clave'] = df['porcentaje_de_palabras_clave'].str.replace(',', '.', regex=True).astype(float)
    df['principales_palabras_clave']=df['principales_palabras_clave'].str.replace('\s+', ' ', regex=True)
    df['principales_palabras_clave']=df['principales_palabras_clave'].str.replace(',+', ',', regex=True)
    df['principales_palabras_clave'] = df['principales_palabras_clave'].apply(lambda x: x.replace('.', ''))

    return df

# Llama a la función con el nombre del archivo "clusters_report.txt" como argumento
new_f = ingest_data()
print(new_f)