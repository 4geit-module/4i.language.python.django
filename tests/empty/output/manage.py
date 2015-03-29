#!/usr/bin/env python2

# xyz
# Copyright (C) 2014  xyz developers <admin@localhost.lh> (see AUTHORS)
#
# All rights reserved.

import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "xyz.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
