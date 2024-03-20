import json
import os
from flask import Flask, request, render_template, redirect, url_for
from datetime import datetime
import sqlite3
from model import *
import pandas as pd

app = Flask(__name__)

tasks = [
    {'title': 'Task 1', 'date': '2022-01-01', 'description': 'Do something', 'id': 1},
    {'title': 'Task 2', 'date': '2022-01-02', 'description': 'Do something else', 'id': 11}
]
tasks *= 10

models = load_models("./models/models", ECGNet)

def get_q(is_1, acc_id=0):
    conn = sqlite3.connect('Users.db')
    if is_1:
        df = pd.read_sql_query("SELECT * FROM Queue WHERE finished=0", conn)
    else:
        df = pd.read_sql_query(f"SELECT * FROM Queue WHERE finished=1 AND account_id={acc_id}", conn)

    # Преобразование DataFrame в массив словарей
    records = df.to_dict(orient='records')
    cur = conn.cursor()
    if (len(records) == 0):
        return []
    for i in records:
        cur.execute(('''SELECT name,surname FROM Auth WHERE id = '{}';''').format(i["account_id"]))
        skin = cur.fetchall()

        i["name"] = skin[0][0] + " " + skin[0][1]

    for record in records:
        record["data"] = eval(record["data"])
        # print(records[0]["data"]['NORM'])
        record["data"] = {key: int(float(value) * 100) for key, value in record["data"].items() if float(value) > 0}
        record["data"] = dict(sorted(record["data"].items()))

    return records


@app.route('/', methods=['GET', 'POST'])
def task_list():
    tasks = get_q(True)
    return render_template('main.html', tasks=tasks, id=tasks[0]['id'])


@app.route('/registration', methods=['GET', 'POST'])
def reg():
    if request.method == 'POST':
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        email = request.form.get('email')
        password = request.form.get('password')
        is_doctor = 1 if request.form.get('checkbox') == 'on' else 0
        conn = sqlite3.connect('Users.db')
        cur = conn.cursor()
        sql_insert = '''INSERT INTO Auth VALUES(NULL,'{}','{}','{}','{}','{}');'''.format(first_name, last_name, email,
                                                                                          password, is_doctor)
        cur.execute(sql_insert)
        cur.close()
        conn.commit()
        conn.close()

        return redirect(url_for('login'))
    return render_template('reg.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        conn = sqlite3.connect('Users.db')
        cur = conn.cursor()
        cur.execute(('''SELECT password,is_doctor,id FROM Auth
                                                               WHERE login = '{}';
                                                               ''').format(email))
        pas = cur.fetchall()
        cur.close()
        # print(pas[0][0], password)
        if pas[0][0] != password:
            return render_template('auth.html')
        elif (pas[0][1] == 1):
            # return render_template('/')
            return redirect(url_for("task_list"))
            # return render_template('main.html', tasks=tasks, id=1)
        else:
            return redirect(url_for(f"profile_id", id=pas[0][2]))

        conn.close()
    return render_template('auth.html')


@app.route('/<int:id>', methods=['GET', 'POST'])
def get_id(id):
    if request.method == 'POST':
        conclusion = request.form.get('conclusion')

        conn = sqlite3.connect('Users.db')
        cur = conn.cursor()
        cur.execute('''UPDATE Queue SET finished = ?, conclusion = ? WHERE id = ?;''', (1, conclusion, id))
        cur.close()
        conn.commit()
        conn.close()
        return redirect(url_for("task_list"))
    tasks = get_q(True, id)
    return render_template('main.html', tasks=tasks, id=id)


@app.route('/<int:id>/', methods=['GET', 'POST'])
def profile_id(id):
    if request.method == 'POST':
        file = request.files['file']
        data = np.load(file)

        pred = json.dumps(get_predictions(data, models))

        conn = sqlite3.connect('Users.db')
        cur = conn.cursor()
        cur.execute(
            '''INSERT INTO Queue VALUES(NULL,'{}','{}','{}',0,NULL);'''.format(id, pred,
                                                                               datetime.now().strftime("%d-%m-%Y")))
        conn.commit()
        new_id = cur.lastrowid
        cur.close()
        conn.close()
        p = f"./static/profiles/{id}"
        if not os.path.exists(p):
            os.makedirs(p)
        p += f"/{new_id}"
        os.makedirs(p)
        p += f"/{new_id}.png"
        to_img(data, p)
        return redirect(url_for(f"profile_id", id=id))
    tasks = get_q(False, id)
    return render_template('Upload.html', tasks=tasks)


@app.route('/<int:account_id>/<int:id>', methods=['GET', 'POST'])
def profile_account_id(account_id, id):
    tasks = get_q(False, account_id)
    conn = sqlite3.connect('Users.db')
    cur = conn.cursor()
    cur.execute(('''SELECT conclusion FROM Queue WHERE id = '{}';''').format(id))
    stroka = cur.fetchone()[0]

    return render_template('profile.html', tasks=tasks, id=id, stroka=stroka)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
