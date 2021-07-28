pip install virtualenv
mkdir flaskappenv
python3 -m venv flaskappenv
source flaskappenv/bin/activate
pip install -r requirements.txt
export FLASK_APP=app.py
export FLASK_DEBUG=0
flask run
