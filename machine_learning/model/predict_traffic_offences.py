import os
import logging
import glob
import pickle
import numpy as np
import pandas as pd
from prophet import Prophet


class ModelPredictTrafficOffencesColombia:

    def __init__(self, data_csv_path = '', parquet_split_folder='', parquet_split_path='', trainings_path=''):
        self.data_csv_path = data_csv_path
        self.parquet_split_folder = parquet_split_folder
        self.parquet_split_path = parquet_split_path
        self.trainings_path = trainings_path
    
    def csv_to_parquets(self):
        logging.info("CONVIRTIENDO CSV A PARQUETS...")
        df_principal = pd.read_csv(self.data_csv_path)

        if not os.path.exists(self.parquet_split_folder):
            os.makedirs(self.parquet_split_folder)
        
        for n, df in enumerate(np.array_split(df_principal, 10)):
            df.to_parquet(self.parquet_split_path.format(str(n+1)))
        
    def create_dataframe_from_parquets(self):
        logging.info("LEYENDO PARQUETS...")
      
        files = glob.glob(self.parquet_split_folder+'/*.parquet')

        self.df = pd.concat([pd.read_parquet(file) for file in files])
        print(self.df.head())

       
    def train_model(self):
        self.df['FECHA_MULTA'] = pd.to_datetime(self.df['FECHA_MULTA'], format='mixed')

        traffic_offences_monthly = self.df.groupby(self.df['FECHA_MULTA'].dt.to_period('M')).size().reset_index(name='quantity')
        traffic_offences_monthly['FECHA_MULTA'] = traffic_offences_monthly['FECHA_MULTA'].dt.to_timestamp()  
        print(traffic_offences_monthly)

        df_prophet = traffic_offences_monthly.rename(columns={'FECHA_MULTA': 'ds', 'quantity': 'y'})
        
        model = Prophet()   
        model.fit(df_prophet)

        with open(self.trainings_path+'/predict_traffic_offences.pkl', 'wb') as f:
            pickle.dump(model, f)

model = ModelPredictTrafficOffencesColombia(
    data_csv_path="machine_learning/data/traffic_offences_colombia.csv",
    parquet_split_folder="machine_learning/data/parquets",
    parquet_split_path="machine_learning/data/parquets/data_{0}.parquet",
    trainings_path="machine_learning/trainings"
)

#model.csv_to_parquets()
model.create_dataframe_from_parquets()
model.train_model()