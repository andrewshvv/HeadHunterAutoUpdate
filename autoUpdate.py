__author__ = 'Andrey'

import json
import requests
import time

hours = 2
min = 0
sec = 0
sleepTime = hours*pow(60,2)+min*pow(60,1)+sec

cookieFileName = "cookies.txt"
jobIdFileName = "jobs.txt"
url = 'http://hh.ru/applicant/resumes/touch'

def update(id,cookies):
    payload = {"resume": id , "undirectable":"true"}
    r = requests.post(url=url, data=payload,cookies=cookies)

def cookie_file_transformation(file):

    with open(file, 'r') as content:
        cookieDictionary = json.load(content)
        return { record["name"]:record["value"] for record in cookieDictionary }

def job_update(file):
    with open(file, 'r') as content:
        jobDictionary = json.load(content)
        cookies = cookie_file_transformation(cookieFileName)
        for record in jobDictionary:
            update(record["id"],cookies)

while True:
    job_update(jobIdFileName)
    time.sleep(sleepTime)
