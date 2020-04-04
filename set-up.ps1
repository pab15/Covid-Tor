python -m venv venv
.\venv\Scripts\Activate.ps1
pip install flask
pip install stem
$env:FLASK_APP = "tor.py"
flask run