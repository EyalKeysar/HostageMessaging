from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Your people data (replace with your actual data)
people = []
with open('output.txt', 'r', encoding='utf-8') as r:
    for line in r.readlines():
        name, image_link = line.strip().split(': ')
        if(',' in name):
            name = name[:name.index(',')]
        if('ז"ל' not in name):
            people.append({'name': name, 'image_link': image_link})

@app.route('/')
def index():
    return render_template('index.html', people=people)

@app.route('/form')
def form():
    return render_template('form.html', people=people)

@app.route('/board')
def board():
    numofpeople = len(people)/5
    return render_template('board.html', people=people, numofpeopleinarow=numofpeople)

if __name__ == '__main__':
    app.run(debug=True)
