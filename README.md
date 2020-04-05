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

<br/>
<br/>
<br/>

# Running Website on TOR Browser: 

## Make sure to have TOR installed, here is the link: 
https://www.torproject.org/download/

## Project Url:
http://vlvfd2av3kmod5alkegykwtblaogtzknkcnlt642yasko5lyj76o4lyd.onion



<br/>
<br/>
<br/>

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

# Configuring Ubuntu Server to host app:

## Set up firewall:
Install Uncomplicated Firewall:
### `sudo apt install ufw`
Enable All Outgoing Traffic:
### `sudo ufw default allow outgoing`
Deny Incoming Traffic:
### `sudo ufw deny incoming`
Allow SSH for Remote Access:
### `sudo ufw allow ssh`
Allow Http/Tcp Traffic:
### `sudo ufw allow http/tcp`
Enable Firewall Settings:
### sudo ufw enable`

## Install requirements:
Get Virtual Environment:
### `sudo apt install python3-venv`
Setup Vitual Environment:
### `python3 -m venv venv`
Activate Virtual Environment:
### `source venv/bin/activate`

Next Install All Pip dependencies for your project

## Install nginx and gunicorn:
## (STAY IN VIRTUAL ENVIRONMENT)

### `apt install nginx`
### `pip install gunicorn`

## Set nginx enabled sites:
Remove (or unlink) Default Config:
### sudo rm /etc/nginx/sites-enabled/default`
Add New Config For Project:
### sudo nano /etc/nginx/sites-enabled/[projectfoldername]

Add Lines:
`server {
	listen 80;
	server_name [yourip];

	location /static {
		alias [full/path/to/staticfolder];
	}
	
	location / {
		proxy_pass http://localhost:8000;
		include /etc/nginx/proxy_params;
		proxy_redirect off;
	}
}`

Now Restart Nginx:
### `/etc/init.d/nginx restart`
### `gunicorn -w 3 [appmodulefolder]:[appname]`

## Configure Tor:

Add GPG signing keys:
### `sudo gpg —keyserver keys.gnupg.net —recv 886DDD89`
### `sudo gpg —export A3C4F0F979CAA22CDBA8F512EE8CBC9E886DDD89 | sudo apt-key add -`
### `sudo wget http://nginx.org/keys/nginx_signing.key`
### `apt-key add nginx_signing.key`

Install Tor:

### `apt install tor`

Edit Torrc:

### `sudo nano /etc/tor/torrc`

Add lines:
`HiddenServiceDir /var/lib/tor/hidden_service/
HiddenServicePort 80 [ipusedearlier]:80`

Create Service Directory (hostname will be here) and Restart:

### `mkdir /var/lib/tor/hidden_service/`
### `/etc/init.d/nginx restart`
### `/etc/init.d/tor restart`

## Grab Hostname and Load Site:

### `sudo cat /var/lib/tor/hidden_service/hostname`

Congrats, your nginx/tor server should be operational!
