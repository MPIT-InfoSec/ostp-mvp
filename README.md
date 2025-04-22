# OSTP MVP
OSTP MVP

## How to setup?
Go to project's root folder or directory in a shell/terminal

1. python3 -m venv .venv

2. source .venv/bin/activate

3. pip install --upgrade pip

4. pip install -r requirements.txt

5. pip install -r requirements-dev.txt

## How to run?
Go to project's root folder or directory in a shell/terminal

1. source .venv/bin/activate

2. Check if ostp-mvp/.env has relevant OpenAI key

3. uvicorn app.main:app --reload

4. Open http://127.0.0.1:8000/ in browser

5. deactivate (to deactivate the venv)



