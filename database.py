import sqlite3

# Conectar y crear la tabla si no existe
conn = sqlite3.connect('scores.db')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS scores (
                name TEXT,
                score INTEGER)''')
conn.commit()


def save_score(name, score):
    cur.execute("INSERT INTO scores (name, score) VALUES (?, ?)", (name, score))
    conn.commit()


def get_top_scores(limit=5):
    cur.execute(
        "SELECT name, score FROM scores ORDER BY score DESC LIMIT ?", (limit,))
    return cur.fetchall()
