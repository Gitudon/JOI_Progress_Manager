import streamlit as st
import pandas as pd
import atcoder as ac

q=[]
u=[]
s=[]

def message():
    st.title("問題進捗確認")

def input_contents():
    global q, s, u
    url1=st.text_input("問題ページのURLを入力してください(1問目)")
    q.append(ac.url_to_problem_name(url1))
    u.append(url1)
    url2=st.text_input("問題ページのURLを入力してください(2問目)")
    q.append(ac.url_to_problem_name(url2))
    u.append(url2)
    url3=st.text_input("問題ページのURLを入力してください(3問目)")
    q.append(ac.url_to_problem_name(url3))
    u.append(url3)
    url4=st.text_input("問題ページのURLを入力してください(4問目)")
    q.append(ac.url_to_problem_name(url4))
    u.append(url4)
    url5=st.text_input("問題ページのURLを入力してください(5問目)")
    q.append(ac.url_to_problem_name(url5))
    u.append(url5)
    s.append(st.text_input("受講者のAtCoder IDを入力してください(1人目)"))
    s.append(st.text_input("受講者のAtCoder IDを入力してください(2人目)"))
    s.append(st.text_input("受講者のAtCoder IDを入力してください(3人目)"))

def addelement(df):
    n=0
    for student in s:
        if student!="":
            n+=1
    for i in range(n):
        data=ac.get_result_json(s[i])
        buf=[]
        for url in u:
            buf.append(ac.get_result(url, data))
        df[s[i]]=buf
    return df 

def checker():
    n=0
    for question in q:
        if question=="":
            n+=1
    if n>1:
        return False
    return True

def makegraph():
    name='問題名'
    if checker():
        df=pd.DataFrame({
            name: [q[0], q[1], q[2], q[3], q[4]]
        })
        df=addelement(df)
        df= df.set_index(name)
        df = df.style.map(lambda x: 'background-color: #32cd32' if 'AC' in str(x) else 'background-color: #ffa500' if any(substring in str(x) for substring in ["WA", "TLE", "CE", "RE"]) else 'background-color: #ffffff')
        printgraph(df)

def printgraph(df):
    st.write(df)

def main():
    message()
    input_contents()
    if st.button("進捗を確認する"):
        makegraph()

if __name__=="__main__":
    main()