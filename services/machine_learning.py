
import httpmodels.machine_learning as machine_learning_httpmodels
import httpmodels.general as general_httpmodels
import pandas as pd
import pickle


with open('machine_learning/trainings/predict_traffic_offences.pkl', 'rb') as f:
    model = pickle.load(f)

def predict_quantity_traffic_offences(date):
    
    future = pd.DataFrame({'ds': [pd.to_datetime(date)]})

    forecast = model.predict(future)
    
    data = machine_learning_httpmodels.PredictData(
        prediction = round(forecast['yhat'].iloc[0],2),
        lower_bound = round(forecast['yhat_lower'].iloc[0],2),
        upper_bound = round(forecast['yhat_upper'].iloc[0],2)
    )
    return  machine_learning_httpmodels.PredictQuantityTrafficOffences(
        status = "success",
        message = "",
        data = data
    )
