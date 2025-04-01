-- Todoアプリのデータベーススキーマ

CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task_name TEXT NOT NULL,
    due_date DATE NOT NULL,
    priority TEXT CHECK(priority IN ('高', '中', '低')),
    status TEXT CHECK(status IN ('完了', '未完了')) DEFAULT '未完了'
);