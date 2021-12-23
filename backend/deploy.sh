#!/bin/sh

#apt-get update
#apt-get upgrade

sudo apt-get -y install build-essential libpq-dev python3-dev

#apt-get install postgresql-contrib

sudo apt-get -y install nginx

sudo apt-get -y install supervisor

sudo systemctl enable supervisor
sudo systemctl start supervisor

sudo apt-get -y install python3-virtualenv

#config database
#su - postgres

#createuser carlos
#createdb developer --owner carlos
#psql -c "ALTER USER carlos WITH PASSWORD 'carlos'"

adduser robotica

gpasswd -a robotica sudo
#su - carlos
