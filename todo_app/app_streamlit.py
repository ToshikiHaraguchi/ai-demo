import streamlit as st
import requests

# APIのベースURL
API_URL = 'http://127.0.0.1:8080'

# タスク追加フォーム
st.title('Todoアプリ')

with st.form(key='task_form'):
    task_name = st.text_input('タスク名')
    due_date = st.date_input('期限')
    priority = st.selectbox('優先度', ['高', '中', '低'])
    status = st.selectbox('状態', ['未完了', '完了'])
    submit_button = st.form_submit_button(label='タスクを追加')

    if submit_button:
        response = requests.post(f'{API_URL}/tasks', json={
            'task_name': task_name,
            'due_date': str(due_date),
            'priority': priority,
            'status': status
        })
        if response.status_code == 200:
            st.success('タスクが追加されました')
        else:
            st.error('タスク追加に失敗しました')

# タスク取得
response = requests.get(f'{API_URL}/tasks')
if response.status_code == 200:
    tasks = response.json().get('tasks', [])
    st.subheader('タスクリスト')
    for task in tasks:
        st.write(f'タスク名: {task["task_name"]}, 期限: {task["due_date"]}, 優先度: {task["priority"]}, 状態: {task["status"]}')