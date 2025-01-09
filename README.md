# Quiz App

A simple Flask-based quiz application that stores and retrieves multiple-choice questions from a PostgreSQL database. The project demonstrates how to:

- Connect to a PostgreSQL database using **psycopg2**
- Create and seed a table with sample questions
- Retrieve questions, present them to the user via a Flask web interface, and track correct/incorrect answers
- Provide a final summary (results) to the user after completing the quiz

## Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Prerequisites](#prerequisites)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Project Structure](#project-structure)
7. [Database Schema](#database-schema)
8. [Customization](#customization)
9. [License](#license)

---

## Project Overview

This project allows users to select a particular **exam** (e.g., PCAP) and attempt up to 30 randomly chosen questions from that exam category. Answers are either single-choice or multiple-choice depending on the question. Upon submission, the user is immediately informed if the answer is incorrect (with an option to review or skip to the next question). A final results page is shown once the quiz is completed.

---

## Features

- **Multiple Exam Support**: Easily add different exams (e.g., PCAP, custom exams) by adding questions with unique exam IDs.
- **Random Questions**: By default, up to 30 random questions are selected for each quiz session.
- **Single or Multiple Answers**: The database records whether the question expects a single answer (`multiplea = False`) or multiple answers (`multiplea = True`).
- **Review / Skip**: If a user answers incorrectly, they can choose to review the question or move on to the next one.
- **Simple UI**: A minimal design using HTML/CSS, powered by Flask’s templating engine.

---

## Prerequisites

1. **Python 3.7+**
2. **Flask** (Install via `pip install flask`)
3. **psycopg2** (Install via `pip install psycopg2`)
    - On some systems, you may need additional libraries (like `libpq-dev` on Debian/Ubuntu) before installing psycopg2.
4. **PostgreSQL** (Version 9.6+ should work fine)
    - Make sure you have created a PostgreSQL user and database. Update connection details in the code accordingly.

---

## Installation

1. **Clone** this repository (or download the ZIP) and navigate into the project folder:

    ```bash
    git clone https://github.com/yourusername/quiz-app.git
    cd quiz-app
    ```

2. **Create a virtual environment** (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate   # On Linux/Mac
    .\venv\Scripts\activate    # On Windows
    ```

3. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

    If you don’t have a `requirements.txt` yet, you can create one containing at least:

    ```text
    Flask
    psycopg2
    ```

4. **Configure database details** in the code (if needed):
    - Inside `question.py` and `app.py`, update the PostgreSQL connection credentials (`DB_HOST`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`) so they match your local PostgreSQL setup.

---

## Usage

### 1. Create and Seed the Database

Run `question.py` once to create the `questions` table (if it doesn’t exist) and insert the sample data:

```bash
python question.py
```

This script will:
- Connect to the PostgreSQL database
- Drop the existing `questions` table (if it exists)
- Create a fresh `questions` table with the necessary columns
- Insert all the sample questions

### 2. Start the Flask App

Run `app.py` to start the Flask development server:

```bash
python app.py
```

By default, Flask will run at [http://127.0.0.1:5000](http://127.0.0.1:5000).  
Open your browser and navigate to that address to see the quiz app’s home screen, where you can select an exam.

### 3. Interact with the Quiz

1. **Select Exam**: Choose an exam from the displayed buttons (e.g., *PCAP*).
2. **Answer Questions**: You’ll see the question, optional code snippet, and multiple or single possible answers.
3. **Submit**: Click **Submit**. If your answer is incorrect, a modal will appear letting you review or move on.
4. **Finish**: Continue until all the questions are answered. A final **Result** page will show your score and percentage.

---

## Project Structure

Here is an overview of the key files in the repository:

```
quiz-app/
├── app.py
├── question.py
├── templates/
│   ├── index.html
│   ├── result.html
│   ├── select_exam.html
├── static/ (optional folder if you have static assets)
├── README.md
└── requirements.txt
```

- **question.py**  
  Creates/drops the `questions` table in PostgreSQL and seeds it with sample data.

- **app.py**  
  Main Flask application. Manages routes for quiz selection, question presentation, answer submission, and result display.

- **templates/**  
  - **index.html** – Main quiz UI (display questions, code snippets, possible answers, etc.).
  - **result.html** – Final results page.
  - **select_exam.html** – Exam selection page.

---

## Database Schema

The `questions` table is created in `question.py`:

```sql
CREATE TABLE questions (
    id SERIAL PRIMARY KEY,
    question TEXT,
    code TEXT,
    options TEXT,
    answer TEXT,
    multiplea BOOLEAN,
    category INTEGER,
    exam INTEGER
);
```

- **id**: Auto-increment primary key
- **question**: Text of the question
- **code**: Any optional code snippet (e.g., Python code) associated with the question
- **options**: The possible choices, separated by `;;-;`
- **answer**: The correct answer(s). If multiple answers, they’re separated by `;;-;` or commas
- **multiplea**: Boolean indicating whether multiple answers are allowed
- **category**: Category ID for potential future grouping
- **exam**: An integer referencing which “exam” this question belongs to

---

## Customization

- **Add More Exams**
- **Add questions with different exam IDs:**
  - e.g. exam=2 for a second exam. Then define a mapping in app.py:

```python
exam_names = {
    1: 'PCAP',
    2: 'Another Exam',
    # etc.
}
```

- **Change Number of Questions**
  - By default, min(30, len(question_ids)) is used to show 30 questions or the total available if fewer than 30. Adjust as needed in app.py.
- **Styling**
  - The application uses minimal custom CSS. You can update the style blocks in the HTML templates or add your own .css files under a static/ folder.
 
## License

- MIT License
- Copyright (c) 2025 Vitor Silva

- Permission is hereby granted, free of charge, to any person obtaining a copy.


 
  
