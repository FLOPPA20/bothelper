import sqlite3


def create_table():
    con = sqlite3.connect("questions")
    cur = con.cursor()
    cur.execute("CREATE TABLE questions(id integer primary key,question,answer,answered)")
    con.commit()
    con.close()


def add_question(question):
    con = sqlite3.connect("questions")
    cur = con.cursor()
    cur.execute("""
INSERT INTO questions (question,answered) VALUES( ? , 0 )
""",(question,))
    con.commit()
    con.close()


def otvet(id,answer):
    con = sqlite3.connect("questions")
    cur = con.cursor()
    cur.execute("""
UPDATE questions SET answer = ?, answered = 1 WHERE id = ?
""",(answer,id))
    con.commit()
    con.close()
    
def found(question):
    con = sqlite3.connect("questions")
    cur = con.cursor()
    cur.execute("""
SELECT id FROM questions WHERE question = ?
""",(question,))
    id = cur.fetchall()[0][0]
    con.close()
    return id




































def found_answer(id):
    con = sqlite3.connect("questions")
    cur = con.cursor()
    cur.execute("""
SELECT answer FROM questions WHERE id = ?
""",(id,))
    answer = cur.fetchall()[0][0]
    con.close
    return answer