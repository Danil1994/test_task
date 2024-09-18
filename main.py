import os
from fastapi import FastAPI, HTTPException

from dotenv import load_dotenv
from handler import get_result, filter_by_time, read

load_dotenv()

app = FastAPI()

DEBUG = os.getenv("SUPERBENCHMARK_DEBUG", "False").lower() == "true"


@app.get("/results/average")
def get_average_performance():
    if DEBUG==False:
        raise HTTPException(status_code=503, detail="Feature not ready for production")
    data = read('test_database.json')
    benchmarking_results = data['benchmarking_results']
    result = get_result(benchmarking_results)
    print(DEBUG)
    return result


@app.get("/results/average/{start_time}/{end_time}")
def get_average_performance_within_time(start_time: str, end_time: str):
    if not DEBUG:
        raise HTTPException(status_code=503, detail="Feature not ready for production")
    data = read('test_database.json')
    benchmarking_results = data['benchmarking_results']
    filter_results = filter_by_time(benchmarking_results, start_time, end_time)
    result = get_result(filter_results)
    return result

