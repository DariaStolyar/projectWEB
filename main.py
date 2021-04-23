import json
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def first():
    return render_template('first.html')


@app.route('/math')
def math():
    with open("sss.json", "rt", encoding="utf8") as f:
        news_list = json.loads(f.read())
    return render_template('math.html', tasks=news_list)


@app.route('/math/<int:number>')
def mathzad(number):
    with open("sss.json", "rt", encoding="utf8") as f:
        news_list = json.loads(f.read())
    return render_template('ma.html', q=number, tasks=news_list)


@app.route('/math/<int:number>/<int:a>/<int:b>/<int:c>')
def mathzadotv(number, a, b, c):
    with open("sss.json", "rt", encoding="utf8") as f:
        news_list = json.loads(f.read())
    return render_template('maotv.html', q=number, a=a, b=b, c=c, tasks=news_list)


@app.route('/geo')
def geo():
    with open("sss.json", "rt", encoding="utf8") as f:
        news_list = json.loads(f.read())
    return render_template('geometry.html', tasks=news_list)


@app.route('/geo/<int:number>')
def geozad(number):
    with open("sss.json", "rt", encoding="utf8") as f:
        news_list = json.loads(f.read())
    return render_template('geo.html', q=number, tasks=news_list)


@app.route('/geo/<int:number>/<int:a>/<int:b>/<int:c>')
def geozadotv(number, a, b, c):
    with open("sss.json", "rt", encoding="utf8") as f:
        news_list = json.loads(f.read())
    return render_template('geootv.html', q=number, a=a, b=b, c=c, tasks=news_list)


@app.route('/new', methods=['POST', 'GET'])
def new():
    with open("sss.json", "rt", encoding="utf8") as f:
        news_list = json.loads(f.read())
    if request.method == 'GET':
        return render_template('new.html', tasks=news_list)
    elif request.method == 'POST':
        with open('sss.json', 'r', encoding="utf8") as f:
            json_data = json.load(f)
            print(request.form['sex'])
            if request.form['sex'] == "male":
                json_data["math"] = json_data["math"]
                json_data["math"].append([request.form['a'], request.form['b'], request.form['c'], request.form['d']])
                json_data["geometry"] = json_data["geometry"]
            else:
                json_data["math"] = json_data["math"]
                json_data["geometry"] = json_data["geometry"]
                json_data["geometry"].append([request.form['a'], request.form['d'], request.form['b'], request.form['c']])
        with open('sss.json', 'w', encoding='utf8') as cat_file:
            cat_file.write(json.dumps(json_data))
        return render_template('new_ok.html', tasks=news_list)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
