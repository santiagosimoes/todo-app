import streamlit as st
import Modules.functions as functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state['new_todo'] + "\n"
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state['new_todo'] = ""


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo.strip(), key=todo.strip())
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo.strip()]
        st.rerun()

st.text_input("", placeholder="Enter the todo here...",
              on_change=add_todo, key='new_todo')
