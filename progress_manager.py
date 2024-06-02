import streamlit as st
import pandas as pd
import atcoder as ac
import problems as pb

q=[]
u=[]
s=[]

def message():
    st.title("問題進捗確認")
    st.write("AtCoderの問題の進捗を確認することができます。")
    st.write("表が出てこなかったらボタンを連打してください。")

def input_contents():
    global q, u
    #ここに自動補完するか選択を入れる
    select=st.selectbox(label="選択してください",options=("手動入力","A-四則演算", "A-条件分岐","B-文字列", "B-forループ", "C-リスト", "C- 1次予選過去問","S1-whileループ","S1-多重ループ","S1-多次元リスト","S2-ソート関数","S2-再帰関数"))
    if select=="手動入力":
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
    else:
        if select=="A-四則演算":
            u=pb.A_calc
        elif select=="A-条件分岐":
            u=pb.A_if
        elif select=="B-文字列":
            u=pb.B_string
        elif select=="B-forループ":
            u=pb.B_for
        elif select=="C-リスト":
            u=pb.C_list
        elif select=="C- 1次予選過去問":
            u=pb.C_kakomon
        elif select=="S1-whileループ":
            u=pb.S1_while
        elif select=="S1-多重ループ":
            u=pb.S1_multi
        elif select=="S1-多次元リスト":
            u=pb.S1_multi_list
        elif select=="S2-ソート関数":
            u=pb.S2_sort
        elif select=="S2-再帰関数":
            u=pb.S2_recursive
        for url in u:
            q.append(ac.url_to_problem_name(url))

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
    name2='URL'
    url=u
    df=pd.DataFrame({
        name: element,
        name2: url
    })
    df=addelement(df)
    df= df.set_index(name)
    
    df = df.style.map(lambda x: 'background-color: #32cd32' if 'AC' in str(x) else 'background-color: #ffa500' if any(substring in str(x) for substring in ["WA", "TLE", "CE", "RE"]) else 'background-color: #ffffff')
    printgraph(df)

def printgraph(df):
    st.dataframe(
        df,
        column_config={
            "URL": st.column_config.LinkColumn("URL"),
        },
    )

def main():
    message()
    input_contents()
    input_students()
    if st.button("進捗を確認する"):
        makegraph()

if __name__=="__main__":
    main()