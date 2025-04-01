from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import sqlite3

router = APIRouter()

class Task(BaseModel):
    task_name: str
    due_date: str
    priority: str
    status: str

# データベース接続を管理する関数
def get_db_connection():
    conn = sqlite3.connect('todo_app.db')
    conn.row_factory = sqlite3.Row
    return conn

# 新しいタスクを追加するエンドポイント
@router.post('/tasks')
def create_task(task: Task):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('''
        INSERT INTO tasks (task_name, due_date, priority, status)
        VALUES (?, ?, ?, ?)
    ''', (task.task_name, task.due_date, task.priority, task.status))
    connection.commit()
    connection.close()
    return {'message': 'タスクが追加されました'}

# 全タスクを取得するエンドポイント
@router.get('/tasks')
def read_tasks():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM tasks')
    tasks = cursor.fetchall()
    connection.close()
    return {'tasks': [dict(task) for task in tasks]}

# タスクを更新するエンドポイント
@router.put('/tasks/{task_id}')
def update_task(task_id: int, task: Task):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('''
        UPDATE tasks
        SET task_name = ?, due_date = ?, priority = ?, status = ?
        WHERE id = ?
    ''', (task.task_name, task.due_date, task.priority, task.status, task_id))
    connection.commit()
    connection.close()
    return {'message': 'タスクが更新されました'}

# タスクを削除するエンドポイント
@router.delete('/tasks/{task_id}')
def delete_task(task_id: int):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('''
        DELETE FROM tasks WHERE id = ?
    ''', (task_id,))
    connection.commit()
    connection.close()
    return {'message': 'タスクが削除されました'}