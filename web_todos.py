import streamlit as st
import functions as fn

todos = fn.get_todos()


def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo + "\n")
    fn.write_todos(todos_arg=todos)


st.title("Todo App")
st.subheader("This is my Todo app")
st.write("This app will increase your productivity")

for index, todo in enumerate(todos):
    key_todo = f"{index+1}. {todo}"
    checkbox = st.checkbox(todo, key=key_todo)
    if checkbox:
        todos.pop(index)
        fn.write_todos(todos_arg=todos)
        del st.session_state[key_todo]
        st.experimental_rerun()


st.text_input(label=" ", placeholder="Add new todo",
              on_change=add_todo, key="new_todo")
