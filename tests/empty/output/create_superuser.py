#!/usr/bin/env python2

# xyz
# Copyright (C) 2014  xyz developers <admin@localhost.lh> (see AUTHORS)
#
# All rights reserved.

import os

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "xyz.settings")

    from django.contrib.auth.models import User
    from django.db.utils import IntegrityError
    try:
        User.objects.create_superuser('admin', 'admin@localhost.lh', 'admin')
    except IntegrityError:
        print('superuser "admin" already created')
    else:
        print('superuser "admin" created')
