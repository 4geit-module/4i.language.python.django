# xyz
# Copyright (C) 2014  xyz developers <admin@localhost.lh> (see AUTHORS)
#
# All rights reserved.

from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.contenttypes.models import ContentType

class MyModel(models.Model):
    """
    MyModel
    """


    def save(self, *args, **kwargs):
        super(MyModel, self).save(*args, **kwargs)

    def __unicode__(self):
        return """MyModel (%d)""" % self.id

