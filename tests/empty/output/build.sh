#!/bin/bash

# xyz
# Copyright (C) 2014  xyz developers <admin@localhost.lh> (see AUTHORS)
#
# All rights reserved.

./manage.py migrate
./manage.py makemigrations
./manage.py migrate
./create_superuser.py
