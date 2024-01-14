from flask import Flask, render_template, request, jsonify, redirect
from dbrepo import DbRepo
app = Flask(__name__)

# Your people data (replace with your actual data)
            

@app.route('/')
def index():
    #redirect to board
    return redirect('/board')

@app.route('/form/<person>', methods=['GET', 'POST'])
def form(person):
    if request.method == 'POST':
        text = request.form['ta']
        DbRepo.letter(person, text)
        return redirect('/board')
    else:
        return render_template('form.html', people=DbRepo.get_people() , person=person, person_image=DbRepo.get_image_link(person))

@app.route('/letter/<person>')
def letter(person):
    return render_template('letter.html', person=person, image_link=DbRepo.get_image_link(person), letter=DbRepo.get_letter(person))

@app.route('/board')
def board():
    people = DbRepo.get_people()
    numofpeople = len(people)/5
    return render_template('board.html', lettered_people=DbRepo.get_lettered_people(), unlettered_people=DbRepo.get_unlettered_people(), numofpeopleinarow=numofpeople)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
