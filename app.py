import streamlit as st
from todo_logic import add_task,remove_task

st.title("Todo List")

if "tasks" not in st.session_state:
    st.session_state.tasks=[]

task=st.text_input("New Task")

if st.button("Add"):
    st.session_state.tasks=add_task(st.session_state.tasks,task)
for i,t in enumerate(st.session_state.tasks):
    cols=st.columns([0.9,0.1])
    with cols[0]:
        st.write(f"{i+1}. {t}")
    with cols[1]:
        if st.button("❌",key=f"remove_{i}",help="Remove Task"):
            st.session_state.tasks=remove_task(st.session_state.tasks, i)
            break

