### Introduction

This is a platform for humanity students to write their essays. It is mainly for the early career humanity and social science students. We want to create a GPT-based platform that is specifically useful for usual homeworks, tutorial essays, and writing samples. 

Democratize Humanity! Give students more time to study Computer Science and Statistics!

Yes, I have a love-hate relationship with the humanity. I wish to make the positive side dominates. 

### Project Structure 
```js
    humanitygpt/
    ├── backend/
    │   ├── app/
    │   │   ├── __init__.py
    │   │   ├── models/
    │   │   │   ├── __init__.py
    │   │   │   ├── user.py
    │   │   │   ├── project.py
    │   │   │   ├── note.py
    │   │   │   └── pdf.py
    │   │   ├── routes/
    │   │   │   ├── __init__.py
    │   │   │   ├── projects.py
    │   │   │   ├── notes.py
    │   │   │   └── pdfs.py
    │   │   ├── utils/
    │   │   │   ├── __init__.py
    │   │   │   └── auth.py
    │   │   ├── config.py (not version controlled)
    │   │   └── config.example.py (version controlled)
    │   ├── .env (not version controlled)
    │   ├── .env.example (version controlled)
    │   ├── requirements.txt
    │   └── run.py
    └── README.md
```

### Full Potential Structure

```js
    humanitygpt/
    ├── backend/
    │   ├── app/
    │   │   ├── __init__.py
    │   │   ├── models/
    │   │   │   ├── __init__.py
    │   │   │   ├── user.py
    │   │   │   ├── project.py
    │   │   │   ├── note.py
    │   │   │   └── pdf.py
    │   │   ├── routes/
    │   │   │   ├── __init__.py
    │   │   │   ├── projects.py
    │   │   │   ├── notes.py
    │   │   │   └── pdfs.py
    │   │   ├── services/
    │   │   │   ├── __init__.py
    │   │   │   ├── pdf_service.py
    │   │   │   ├── note_service.py
    │   │   │   └── gpt_service.py
    │   │   ├── utils/
    │   │   │   ├── __init__.py
    │   │   │   └── auth.py
    │   │   └── config.py
    │   ├── migrations/
    │   ├── tests/
    │   │   ├── __init__.py
    │   │   ├── test_auth.py
    │   │   ├── test_projects.py
    │   │   ├── test_notes.py
    │   │   └── test_pdfs.py
    │   ├── .env
    │   ├── requirements.txt
    │   └── run.py
    ├── frontend/
    │   ├── public/
    │   │   └── index.html
    │   ├── src/
    │   │   ├── components/
    │   │   │   ├── Header.js
    │   │   │   ├── Footer.js
    │   │   │   ├── ProjectList.js
    │   │   │   ├── NoteEditor.js
    │   │   │   └── PDFViewer.js
    │   │   ├── pages/
    │   │   │   ├── Home.js
    │   │   │   ├── Login.js
    │   │   │   ├── Register.js
    │   │   │   ├── Dashboard.js
    │   │   │   ├── Project.js
    │   │   │   └── PaperEditor.js
    │   │   ├── services/
    │   │   │   ├── api.js
    │   │   │   └── auth.js
    │   │   ├── App.js
    │   │   └── index.js
    │   ├── package.json
    │   └── README.md
    ├── docker-compose.yml
    └── README.md
```