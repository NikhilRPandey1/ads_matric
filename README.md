## Create virtual environment
``` python3 -m venv ven ```

## Activate virtual environment
## Install requirement file
``` pip3 install -r requirements.txt ```

## Create database
``` ad_metrics_db ```

## Insert 100 record in the database
``` python app/populate_db_script.py ```

## Create a .env file at root level of project and setup your database connection path
``` postgresql+asyncpg://nikhilpandey:root@localhost:5432/ad_metrics_db ```

## Run the application 
``` uvicorn app.main:app ```

Once server start, hit the url '127.0.0.1:8000/docs'