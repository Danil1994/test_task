import json
from datetime import datetime


def read(path: str) -> dict:
    with open(path, 'r') as file:
        data = json.load(file)
    return data


def filter_by_time(benchmarking_results: list, start_time: str, end_time: str) -> (list, str):
    if end_time < start_time:
        raise ValueError("End time should be greater than or equal to start time")

    start_time = datetime.fromisoformat(start_time)
    end_time = datetime.fromisoformat(end_time)

    # Filters data
    filtered_results = [
        result for result in benchmarking_results
        if start_time <= datetime.fromisoformat(result['timestamp']) <= end_time
    ]

    return filtered_results


def get_result(benchmarking_results: list) -> dict:
    # calculate the average performance
    total_entries = len(benchmarking_results)
    average_token_count = sum(d['token_count'] for d in benchmarking_results) / total_entries
    average_time_to_first_token = sum(d['time_to_first_token'] for d in benchmarking_results) / total_entries
    average_time_per_output_token = sum(d['time_per_output_token'] for d in benchmarking_results) / total_entries
    average_total_generation_time = sum(d['total_generation_time'] for d in benchmarking_results) / total_entries

    average_results = {
        "average_token_count": average_token_count,
        "average_time_to_first_token": average_time_to_first_token,
        "average_time_per_output_token": average_time_per_output_token,
        "average_total_generation_time": average_total_generation_time
    }

    return (average_results)
