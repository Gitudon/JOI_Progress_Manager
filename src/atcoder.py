import requests
from bs4 import BeautifulSoup
import json
import streamlit as st
import time

def unix_time():
    current_unix_time = int(time.time())
    one_month_ago = current_unix_time - (30 * 24 * 60 * 60)
    return one_month_ago

def url_to_problem_name(url):
    #urlから問題名を取得する
    if url=="":
        return ""
    html = requests.get(url)
    soup = BeautifulSoup(html.content, "html.parser")
    for tag in soup.select("title"):
        return tag.text

def get_result_json(user_id):
    #user_idから結果を取得する
    if user_id=="":
        return ""
    url_api = "https://kenkoooo.com/atcoder/atcoder-api/v3/user/submissions?from_second="+str(unix_time())+"&user=" + user_id
    res = requests.get(url_api)
    data = json.loads(res.text)
    return data

def get_result(url, data):
    # urlからcontest_nameとproblem_nameを取得する
    parts = url.split("/")
    if len(parts) < 7:
        return ""
    contest_name = parts[4]
    problem_name = parts[6]
    result=[]
    for d in data:
        if d["contest_id"] == contest_name and d["problem_id"] == problem_name:
            result.append(d["result"])
    if result==[]:
        return ""
    final_result = result[-1]
    return final_result