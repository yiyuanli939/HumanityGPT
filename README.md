### Introduction

This is a platform for humanity students to write their essays. It is mainly for the early career humanity and social science students. We want to create a GPT-based platform that is specifically useful for usual homeworks, tutorial essays, and writing samples. 

Democratize Humanity! Give students more time to study Computer Science and Statistics!

Yes, I have a love-hate relationship with the humanity. I wish to make the positive side dominates. 

### Project Structure 

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