from airflow import DAG
from airflow.models.baseoperator import chain
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from airflow.decorators import dag, task
from datetime import datetime, timedelta
import requests
import json
import requests
import time
import logging


def _proceso():
    #logueo api
    url_login_ws = ""
    #ruta endpoint etl
    url_etl = ""
    headers_login_ws  = {"Accept": "application/json"}
    params_login_ws = {

       "username": "",
        "password": ""
    }

    response =requests.post(url_login_ws, headers = headers_login_ws, data=json.dumps(params_login_ws))

    response2 =requests.post(url_login_ws, headers = headers_login_ws, data=json.dumps(params_login_ws))
   
    token_ws = response2.json()

    logging.info("Process_Name: etl  ")
    logging.info("Date: " + time.strftime("%c"))

    if response.status_code != 200:
        logging.info('Request_Login: Error ')
        logging.info('Status_Code: ' + str(response.status_code))  
    else:
        logging.info("Request_Login: Success")

    my_headers = {'Authorization' : 'Bearer {' + token_ws + '}'}
    response_etl = requests.post(url_etl,  headers={'Authorization': 'Bearer ' + token_ws })

    if response_etl.status_code != 200:
        logging.info('Request_ETL: Error ')
        logging.info('Status_Code_ETL: ' + str(response_etl.status_code))  
    else:
        logging.info('Request_ETL: Success')
        logging.info('Status_Code_ETL: ' + str(response_etl.status_code))      
    logging.info('Proceso OK')

dag = DAG(
    description="etl",
    dag_id="etl",
    start_date=days_ago(1),
    schedule_interval="* * * * *",
    tags=["etl"],
    catchup=False,
)
with dag:

    python_task = PythonOperator(
        task_id="python_task",
        python_callable=_proceso,
    )
   

chain(python_task)

