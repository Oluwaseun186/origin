from app import app
import sqlite3


def test_homepage():
    tester = app.test_client()

    
    test_content = 'Test Task 123'
    response = tester.post('/add', data={'content': test_content}, follow_redirects=True)
    assert response.status_code == 200
    assert test_content.encode() in response.data

  
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute('SELECT id FROM tasks WHERE content = ?', (test_content,))
    row = c.fetchone()
    conn.close()
    assert row is not None, "Task was not inserted."
    task_id = row[0]


    response = tester.get(f'/delete/{task_id}', follow_redirects=True)
    assert response.status_code == 200
    assert test_content.encode() not in response.data

    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute('SELECT * FROM tasks WHERE id = ?', (task_id,))
    assert c.fetchone() is None
    conn.close()

