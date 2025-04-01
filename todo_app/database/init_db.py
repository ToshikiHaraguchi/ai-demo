import sqlite3

# SQLiteデータベースの初期化
conn = sqlite3.connect('todo_app.db')
cursor = conn.cursor()

# タスクテーブルの作成
try:
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task_name TEXT NOT NULL,
        due_date DATE NOT NULL,
        priority TEXT CHECK(priority IN ("高", "中", "低")),
        status TEXT CHECK(status IN ("完了", "未完了")) DEFAULT "未完了"
    );
    ''')
    print('タスクテーブルが作成されました。')
except sqlite3.Error as e:
    print(f'エラー発生: {e}')

# データベース接続を閉じる
conn.commit()
conn.close()