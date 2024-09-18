from typing import Union

from fastapi import FastAPI
from datetime import datetime

app = FastAPI()


@app.get("/results/average")
def get_average_performance():
    pass


@app.get("/results/average/{start_time}/{end_time}")
def get_average_performance_within_time(start_time:datetime, end_time:datetime):
    pass
