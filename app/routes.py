from flask import render_template, request, redirect, url_for
from app import app
import json
import os

def load_quiz(quiz_name):
    with open(os.path.join('quizzes', f'{quiz_name}.json')) as f:
        return json.load(f)

@app.route('/')
@app.route('/index')
def index():
    quizzes = ['js_quiz', 'cloud_quiz']
    return render_template('index.html', quizzes=quizzes)

@app.route('/quiz/<quiz_name>', methods=['GET', 'POST'])
def quiz(quiz_name):
    quiz_data = load_quiz(quiz_name)
    if request.method == 'POST':
        answers = request.form.to_dict()
        score = 0
        for i, question in enumerate(quiz_data['questions']):
            if answers.get(f'q{i}') == question['correct']:
                score += 1
        return redirect(url_for('result', score=score, total=len(quiz_data['questions'])))
    return render_template('quiz.html', quiz_data=quiz_data)

@app.route('/result')
def result():
    score = request.args.get('score')
    total = request.args.get('total')
    return render_template('result.html', score=score, total=total)
