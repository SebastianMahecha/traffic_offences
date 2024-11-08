from fastapi import APIRouter, Depends, status, Body
from fastapi.responses import JSONResponse
from typing import List
import httpmodels.machine_learning as machine_learning_httpmodels
import httpmodels.general as general_httpmodels
import services.machine_learning as machine_learning_services
from dataclasses import asdict
import json

router = APIRouter()

@router.get(
    "/predict/{date}", 
    response_model=machine_learning_httpmodels.PredictQuantityTrafficOffences,
    responses={
        200: {"description": "Predict found", "content":  {"application/json": {"example":{"status":"success","message":"","data":{"prediction":225,"lower_bound":210,"upper_bound":240}}}}},
        400: {"description": "Predict not found", "content":  {"application/json": {"example":{"status":"error","message":"Predict not found.","data":None}}}},

    }
)
def predict_quantity_traffic_offences(
    date: str
):
    response = machine_learning_services.predict_quantity_traffic_offences(date)   

    return JSONResponse(
            status_code=status.HTTP_200_OK, 
            content=asdict(response)
    )

