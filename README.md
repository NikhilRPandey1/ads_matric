## Create virtual environment
``` python3 -m venv ven ```

## Activate virtual environment
## Install requirement file
``` pip3 install -r requirements.txt ```

## Create database
``` ad_metrics_db ```

## Insert 100 record in the database
``` python app/populate_db_script.py ```

## Create a .env file at root level of project and put your info
``` 
DATABASE_URL=postgresql+asyncpg://username:password@localhost:5432/ad_metrics_db
CELERY_BROKER_URL=redis://localhost:6379/0
CELERY_RESULT_BACKEND=redis://localhost:6379/0
SECRET_KEY=your-secret-key
DEBUG=False
 ```

## Run the application 
``` uvicorn app.main:app ```

Once server start, hit the url '127.0.0.1:8000/docs'