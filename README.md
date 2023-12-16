# Demo Mini Project

# This is the README for Demo Mini Project
**How to run app**

 **Through code**
* python version: `3.11.4`
1. Inside the repository folder, activate virtual environment: `source venv/bin/activate`
2. Install dependencies: `pip install -r requirements.txt`
3. Run server: `uvicorn app.main:app --reload --host 0.0.0.0 --port 8000`

 **Through docker-compose**
1. Inside the repository folder, build an image of service: `sudo docker build -t demo-mini-project .`
2. Run the built docker image:  `sudo docker-compose up -d`

Use the provided base URL and extend it with the specific endpoint URL to make API calls to that endpoint:
* BASE URL: `http://0.0.0.0:8000/demo-mini-project/api/v1`


**Env variables**
* APP_NAME=`demo-mini-project`
