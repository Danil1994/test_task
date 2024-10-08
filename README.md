# SuperBenchmark
SuperBenchmark is a FastAPI application designed to manage and query benchmarking results for Large Language Models (LLMs).

## Install

1. Clone repo:

   --Clone with SSH `git clone https://github.com/Danil1994/test_task.git`

   --Clone with HTTPS `git clone git@github.com:Danil1994/test_task.git`
2. Go to your project folder: `path/to/the/proj`.
3. Load your .env file like .env.example.
4. Activate your virtual env.
5. Install requirements.txt: `pip install -r requirements.txt`.

## Project Setup:

* The application includes a DEBUG mode that allows fetching data directly from the test_database.json file, which mimics a database (data storage format is defined as needed).
* The DEBUG mode is configurable through the SUPERBENCHMARK_DEBUG environment variable.
* If DEBUG is set to False, the application will raise an error indicating that the feature is not ready for production.

## Run

1. Run server: `fastapi dev main.py`
2. Go to link `http://127.0.0.1:8000/results/average` in your browser.


Available Endpoints:
* HTTP GET /results/average

	Returns the average performance statistics across all benchmarking results.

* HTTP GET /results/average/{start_time}/{end_time}

	Returns the average performance statistics for benchmarking results within the specified time window.

Benchmarking Data Format:

Each benchmarking result includes the following fields:

* request_id: Unique identifier for the benchmarking request.
* prompt_text: The input prompt text used for the LLM.
* generated_text: The output text generated by the LLM.
* token_count: The number of tokens in the generated text.
* time_to_first_token: The time taken to generate the first token (in milliseconds).
* time_per_output_token: The average time per output token (in milliseconds).
* total_generation_time: The total time to generate the response (in milliseconds).
* timestamp: The timestamp when the benchmarking result was recorded.

Example Data for test_database.json:
``` 
{
	"benchmarking_results": [
		{
			"request_id": "1",
			"prompt_text": "Translate the following English text to French: 'Hello, how are you?'",
			"generated_text": "Bonjour, comment ça va?",
			"token_count": 5,
			"time_to_first_token": 150,
			"time_per_output_token": 30,
			"total_generation_time": 300,
			"timestamp": "2024-06-01T12:00:00"
		},
		{
			"request_id": "2",
			"prompt_text": "Summarize the following article: 'Artificial intelligence is transforming the world.'",
			"generated_text": "AI is changing the world.",
			"token_count": 6,
			"time_to_first_token": 200,
			"time_per_output_token": 25,
			"total_generation_time": 350,
			"timestamp": "2024-06-01T13:00:00"
		},
		{
			"request_id": "3",
			"prompt_text": "Generate a creative story about a space adventure.",
			"generated_text": "Once upon a time, in a galaxy far away, a group of astronauts embarked on a thrilling journey.",
			"token_count": 18,
			"time_to_first_token": 300,
			"time_per_output_token": 20,
			"total_generation_time": 660,
			"timestamp": "2024-06-01T14:00:00"
		},
		{
			"request_id": "4",
			"prompt_text": "Explain the concept of blockchain technology.",
			"generated_text": "Blockchain is a decentralized ledger of all transactions across a network.",
			"token_count": 10,
			"time_to_first_token": 250,
			"time_per_output_token": 35,
			"total_generation_time": 600,
			"timestamp": "2024-06-02T10:00:00"
		},
		{
			"request_id": "5",
			"prompt_text": "What are the benefits of renewable energy?",
			"generated_text": "Renewable energy reduces carbon emissions and helps combat climate change.",
			"token_count": 12,
			"time_to_first_token": 180,
			"time_per_output_token": 28,
			"total_generation_time": 516,
			"timestamp": "2024-06-02T11:00:00"
		}
	]
}
```