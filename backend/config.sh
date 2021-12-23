#!/bin/sh

sudo apt -y install virtualenv

virtualenv . --python=3

. bin/activate
