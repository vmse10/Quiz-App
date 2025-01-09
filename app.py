from flask import Flask, render_template, request, redirect, url_for, session
import psycopg2
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# PostgreSQL database connection details
DB_HOST = "127.0.0.1"
DB_NAME = "questions_db"
DB_USER = "postgres"
DB_PASSWORD = "1010"

def get_db_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    return conn

# Exam names mapping
exam_names = {
    1: 'PCAP',
    # Add more exams as needed
}

@app.route('/')
def index():
    # Fetch distinct exams from the 'questions' table
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT DISTINCT exam FROM questions')
    exam_ids = [row[0] for row in cursor.fetchall()]
    cursor.close()
    conn.close()

    return render_template('select_exam.html', exam_ids=exam_ids, exam_names=exam_names)

@app.route('/start_quiz', methods=['POST'])
def start_quiz():
    exam_id = request.form.get('exam_id')
    if exam_id:
        exam_id = int(exam_id)
        session.clear()
        session['exam_id'] = exam_id
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT id FROM questions WHERE exam = %s', (exam_id,))
        question_ids = [row[0] for row in cursor.fetchall()]
        cursor.close()
        conn.close()
        num_questions = min(30, len(question_ids))
        session['question_ids'] = random.sample(question_ids, num_questions)  # Adjust as needed
        session['current_index'] = 0
        session['correct_answers'] = 0
        session['incorrect_answers'] = 0
        session['answers'] = []
        session['incorrect'] = False
        return redirect(url_for('quiz'))
    else:
        return redirect(url_for('index'))

@app.route('/quiz')
def quiz():
    if 'exam_id' not in session:
        return redirect(url_for('index'))

    if session['current_index'] >= len(session['question_ids']):
        return redirect(url_for('result'))

    question_id = session['question_ids'][session['current_index']]
    incorrect = session.get('incorrect', False)
    current_question_number = session['current_index'] + 1
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT id, question, code, options, answer, multiplea FROM questions WHERE id = %s', (question_id,))
    question = cursor.fetchone()
    cursor.close()
    conn.close()

    exam_name = exam_names.get(session['exam_id'], f'Exam {session["exam_id"]}')

    return render_template(
        'index.html',
        question=question,
        incorrect=incorrect,
        correct_answers=session['correct_answers'],
        incorrect_answers=session['incorrect_answers'],
        current_question_number=current_question_number,
        exam_name=exam_name
    )

@app.route('/submit', methods=['POST'])
def submit():
    if 'exam_id' not in session:
        return redirect(url_for('index'))

    question_id = session['question_ids'][session['current_index']]
    selected_answers = request.form.getlist('answer')
    print(f"Selected answers: {selected_answers}")  # Log selected answers to the console

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT answer, multiplea FROM questions WHERE id = %s', (question_id,))
    correct_answer, multiplea = cursor.fetchone()
    
    correct_answers_set = set(map(str.strip, correct_answer.split(', '))) if multiplea else {correct_answer.strip()}
    
    if multiplea:
        selected_answers_set = set(map(str.strip, selected_answers))
        if selected_answers_set == correct_answers_set:
            session['correct_answers'] += 1
            session['answers'].append((question_id, selected_answers))
            session['current_index'] += 1
            session['incorrect'] = False
        else:
            session['incorrect'] = True
            session['incorrect_answers'] += 1
    else:
        if selected_answers:
            selected_answer = selected_answers[0].strip()
        else:
            selected_answer = ''
        if selected_answer == correct_answers_set.pop():
            session['correct_answers'] += 1
            session['answers'].append((question_id, selected_answer))
            session['current_index'] += 1
            session['incorrect'] = False
        else:
            session['incorrect'] = True
            session['incorrect_answers'] += 1

    cursor.close()
    conn.close()

    if session['current_index'] >= len(session['question_ids']):  # Adjust number of questions as needed
        return redirect(url_for('result'))

    return redirect(url_for('quiz'))

@app.route('/review')
def review():
    if 'exam_id' not in session:
        return redirect(url_for('index'))
    session['incorrect'] = False
    if session['incorrect_answers'] > 0:
        session['incorrect_answers'] -= 1
    return redirect(url_for('quiz'))

@app.route('/next_question', methods=['POST'])
def next_question():
    if 'exam_id' not in session:
        return redirect(url_for('index'))
    session['incorrect'] = False
    session['current_index'] += 1
    return redirect(url_for('quiz'))

@app.route('/result')
def result():
    if 'exam_id' not in session:
        return redirect(url_for('index'))

    total_questions = len(session['question_ids'])
    correct_answers = session['correct_answers']
    incorrect_answers = session['incorrect_answers']
    percentage = (correct_answers / total_questions) * 100
    exam_name = exam_names.get(session['exam_id'], f'Exam {session["exam_id"]}')
    return render_template(
        'result.html',
        correct_answers=correct_answers,
        incorrect_answers=incorrect_answers,
        percentage=percentage,
        exam_name=exam_name
    )

if __name__ == '__main__':
    app.run(debug=True)
