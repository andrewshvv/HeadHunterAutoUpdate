__author__ = 'Andrey'

import json
import requests
import time

hours = 0
min = 5
sec = 0
sleepTime = (hours*pow(60,2))+(min*pow(60,1))+sec

cookieFileName = "cookies.txt"
jobIdFileName = "jobs.txt"
url = 'http://hh.ru/applicant/resumes/touch'

def update(id,cookies):
    payload = {"resume": id , "undirectable":"true"}
    r = requests.post(url=url, data=payload,cookies=cookies)

def cookie_file_transformation(file):
    content = open(file,"r")
    cookieDictionary = json.load(content)
    return { record["name"]:record["value"] for record in cookieDictionary }

def job_update(file):
    content = open(file,"r")
    jobDictionary = json.load(content)
    cookies = cookie_file_transformation(cookieFileName)
    for record in jobDictionary:
        update(record["id"],cookies)

while True:
    job_update(jobIdFileName)
    time.sleep(sleepTime)
