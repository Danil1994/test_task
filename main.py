from fastapi import FastAPI

from handler import get_result, filter_by_time, read

app = FastAPI()


@app.get("/results/average")
def get_average_performance():
    data = read('test_database.json')
    benchmarking_results = data['benchmarking_results']
    result = get_result(benchmarking_results)
    return result


@app.get("/results/average/{start_time}/{end_time}")
def get_average_performance_within_time(start_time: str, end_time: str):
    data = read('test_database.json')
    benchmarking_results = data['benchmarking_results']
    filter_results = filter_by_time(benchmarking_results, start_time, end_time)
    result = get_result(filter_results)
    return result
