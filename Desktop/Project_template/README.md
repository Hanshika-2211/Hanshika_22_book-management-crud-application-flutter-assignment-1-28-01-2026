# FastAPI Project Template

A simple and clean FastAPI project template with basic structure and configuration.

## Project Structure

```
fastapi-template/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── api/
│   │   ├── __init__.py
│   │   └── routes/
│   │       ├── __init__.py
│   │       └── example.py
│   └── models/
│       └── __init__.py
├── requirements.txt
├── .env.example
├── .env
├── .gitignore
├── README.md
```

## Setup Instructions

1. **Create virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

4. #Run the project 
python main.py
