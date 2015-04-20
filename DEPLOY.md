= Deployment Readme

== deployment setup on ubuntu 14.04.01 droplet on digital ocean

* Create droplet
* install required packages
  - vim git nginx
* setup DNS
* Create user to recieve git repo for deployment
* Create folder for deployed app
* setup eningx


== Reference page

https://realpython.com/blog/python/kickstarting-flask-on-ubuntu-setup-and-deployment/


demouser
/home/demouser/hwsea.git - bare git repo
/home/www/hwsea - target deployment location
/home/demouser/hwsea.git/hooks/post-receive - script to checkout files to /home/www/hwsea folder
