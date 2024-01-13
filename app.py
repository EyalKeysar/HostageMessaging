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
            if('א' in name):
                people.append({'name': name, 'image_link': image_link, 'lettered': False})
            else:    
                people.append({'name': name, 'image_link': image_link, 'lettered': True})
            


@app.route('/')
def index():
    return render_template('index.html', people=people)

@app.route('/form/<person>', methods=['GET', 'POST'])
def form(person):
    if request.method == 'POST':
        text = request.form['ta']
        print(text)
        return jsonify({'status': 'success'})
    else:
        return render_template('form.html', people=people , person=person)

@app.route('/board')
def board():
    numofpeople = len(people)/5
    return render_template('board.html', 
                           unlettered_people=[person for person in people if not person['lettered']], 
                           lettered_people=[person for person in people if person['lettered']], 
                           numofpeopleinarow=numofpeople)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
