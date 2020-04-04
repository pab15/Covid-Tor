python -m venv venv
.\venv\Scripts\Activate.ps1
pip install flask
pip install Flask-SQLAlchemy
pip install Flask-WTF
$env:FLASK_APP = "tor.py"
flask run