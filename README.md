# flask_website_scraper
Simple Flask App for web scraping using RQ and Redis message broker.

## Setup and running
We need to install Redis server. Then install all necessary python packages using requirements.txt

```bash
pip install -r requirements.txt
```
Run Redis server, worker.py and run.py:

```bash
$ redis-server
$ python worker.py
$ python run.py
```
Navigate to url http://127.0.0.1:5000/ in browser.

REST API endpoints:
* / (GET, POST) - enter url of website to parse. Returns task_id - id of webscriping job.
* /results/<task_id> (GET) - get status of job execution and get results. Results will be awailable for downloading as links.txt file.
