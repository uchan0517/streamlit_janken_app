import streamlit as st
import random

st.title("じゃんけんアプリ")

genre = st.radio(
    "", # ラジオボタンの内容
    ["グー", "チョキ", "パー"] # ラジオボタンの選択項目
)

if "kati" not in st.session_state:
    st.session_state.kati = 0
if "make" not in st.session_state:
    st.session_state.make = 0

def janken (PLAYER,CPU):
    if PLAYER == CPU:
        return ("あいこ")
    elif PLAYER == "グー":
        if CPU == "パー":
            return  ("負け")
        elif CPU == "チョキ":
            return  ("勝ち")
    elif PLAYER == "チョキ":
        if CPU == "パー":
            return  ("勝ち")
        elif CPU == "グー":
            return  ("負け")
    elif PLAYER == "パー":
        if CPU == "チョキ":
            return  ("負け")
        elif CPU == "グー":
            return  ("勝ち")

a= ["グー","チョキ","パー"]
CPU=random.choice(a)

if st.button("決定"):
    a= ["グー","チョキ","パー"]
    CPU=random.choice(a)
    kekka=janken(genre,CPU)
    st.write("PLAYER", genre)
    st.write("CPU",CPU )  
    st.write("結果",kekka)

    if kekka == "勝ち":
        st.session_state.kati += 1
    elif kekka == "負け":
        st.session_state.make += 1
    kakuritu = int(st.session_state.kati/(st.session_state.kati+st.session_state.make)*100)
    st.write(f"{st.session_state.kati}勝{st.session_state.make}敗  勝率{kakuritu}%")