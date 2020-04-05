# Covid-Tor
Tor based website for viewing Coronavirus news and numbers. Written in Flask.

## Imports for application:
---
pip install flask
pip install beautifulsoup4
pip install matplotlib
pip install numpy

### Basemap:
https://www.lfd.uci.edu/~gohlke/pythonlibs/
ctrl+f --> basemap
download appropriate whl file for system
move whl file to project directory
ex:
pip install basemap-1.2.1-cp38-cp38-win_amd64

## Imports for server:
---
apt install tor
apt install nginx
pip install gunicorn

#
#
#

# Running Website on TOR Browser: 

## Make sure to have TOR installed, here is the link: 
https://www.torproject.org/download/

## Project Url:
http://vlvfd2av3kmod5alkegykwtblaogtzknkcnlt642yasko5lyj76o4lyd.onion



#
#
#
# Running website without TOR Browser: 
## STEP 1:
Clone/Download this repository
Go to your Command Prompt and type in the folowing: 
### `cd Covid-Tor`

## STEP 2:
Then afteer that type in: 
### `python3 -m venv venv`


#### ONLY IF USING PYTHON 3.4 OR OLDER:
### `virtualenv venv`

## STEP 3:
### ON MAC AND LINUX: `source venv/bin/activate`
### ON WINDOWS: `.\venv\Scripts\Activate.ps1`

## STEP 4:
Now we install flask: 
### `pip install flask`

## STEP 5:
Finally we Export: 
### `export FLASK_APP=microblog.py`

## STEP 6: 
### `flask run`
RUN THE LINK AT: http://127.0.0.1:5000/


