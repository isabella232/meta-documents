from __future__ import absolute_import

from django.db import models

class meta_receipt(models.Model):
    receipt_date = models.DateField(blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2,
                                 blank=True, null=True)
    currency = models.CharField(max_length=3, blank=True, null=True)
    provider = models.CharField(max_length=40, blank=True, null=True)


'''
from . import application


model = application['model']
globals()[model.__name__] = model
del model
'''