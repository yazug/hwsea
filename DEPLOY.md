= Deployment Readme

== deployment setup on ubuntu 14.04.01 droplet on digital ocean

* Create droplet
* install required packages
  - vim git nginx sqlite3
* setup DNS
* Create user to recieve git repo for deployment
* Create folder for deployed app
* setup ningx


== Reference page

https://realpython.com/blog/python/kickstarting-flask-on-ubuntu-setup-and-deployment/

demouser
/home/demouser/hwsea.git - bare git repo
/home/www/hwsea - target deployment location
/home/www/env - virtualenv for this app
/home/demouser/hwsea.git/hooks/post-receive - script to checkout files to /home/www/hwsea folder
/etc/supervisor/conf.d/hwsea.conf with entry command  "/home/www/env/bin/python /home/www/env/bin/gunicorn main:app -b localhost:8000"

supervisorctl reread
supervisorctl update
supervisorctl start hwsea


== post-receive script

	#!/bin/sh
	cd /home/www/hwsea
	echo "Deploying to `pwd`"
	git pull
