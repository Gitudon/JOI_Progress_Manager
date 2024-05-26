import streamlit as st
import pandas as pd
import atcoder as ac
import problems as pb

q=[]
u=[]
s=[]

def message():
    st.title("問題進捗確認")

def input_contents():
    global q, u
    #ここに自動補完するか選択を入れる
    url1=st.text_input("問題ページのURLを入力してください(1問目)")
    if url1!="":
        q.append(ac.url_to_problem_name(url1))
        u.append(url1)
    url2=st.text_input("問題ページのURLを入力してください(2問目)")
    if url2!="":
        q.append(ac.url_to_problem_name(url2))
        u.append(url2)
    url3=st.text_input("問題ページのURLを入力してください(3問目)")
    if url3!="":
        q.append(ac.url_to_problem_name(url3))
        u.append(url3)
    url4=st.text_input("問題ページのURLを入力してください(4問目)")
    if url4!="":
        q.append(ac.url_to_problem_name(url4))
        u.append(url4)
    url5=st.text_input("問題ページのURLを入力してください(5問目)")
    if url5!="":
        q.append(ac.url_to_problem_name(url5))
        u.append(url5)
    url6=st.text_input("問題ページのURLを入力してください(6問目)")
    if url6!="":
        q.append(ac.url_to_problem_name(url6))
        u.append(url6)

def input_students():
    global s
    student1=st.text_input("受講者のAtCoder IDを入力してください(1人目)")
    if student1!="":
        s.append(student1)
    student2=st.text_input("受講者のAtCoder IDを入力してください(2人目)")
    if student2!="":
        s.append(student2)
    student3=st.text_input("受講者のAtCoder IDを入力してください(3人目)")
    if student3!="":
        s.append(student3)
    if s==[]:
        s.append("chokudai")

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

def makegraph():
    name='問題名'
    element=q
    df=pd.DataFrame({
        name: element
    })
    df=addelement(df)
    df= df.set_index(name)
    df = df.style.map(lambda x: 'background-color: #32cd32' if 'AC' in str(x) else 'background-color: #ffa500' if any(substring in str(x) for substring in ["WA", "TLE", "CE", "RE"]) else 'background-color: #ffffff')
    printgraph(df)

def printgraph(df):
    st.write(df)

def manual():
    input_contents()
    input_students()
    if st.button("進捗を確認する"):
        makegraph()

def auto():
    global q, s, u
    course=st.radio("コースを選択してください", ("A-四則演算", "A-条件分岐","B-文字列", "B-forループ", "C-リスト", "S1-whileループ", "S1-多重ループ","S1-多次元リスト","S2-ソート関数","S2-再帰関数"))
    if course=="A-四則演算":
        for url in pb.A1_calc:
            q.append(ac.url_to_problem_name(url))
            u.append(url)
    input_students()
    if st.button("進捗を確認する"):
        makegraph()

def reset():
    q.clear()
    u.clear()
    s.clear()

def main():
    message()
    manual()

if __name__=="__main__":
    main()