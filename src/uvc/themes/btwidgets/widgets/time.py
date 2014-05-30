# -*- coding: utf-8 -*-

from dolmen.forms.ztk.widgets import time
from uvclight import adapts
from . import IBootstrapRequest
from zope.interface import Interface


class TimeFieldWidget(time.TimeFieldWidget):
    adapts(time.TimeField, Interface, IBootstrapRequest)
    defaultHtmlClass = ['field', 'field-time', 'form-control']
    

class TimeFieldDisplayWidget(time.TimeFieldDisplayWidget):
    adapts(time.TimeField, Interface, IBootstrapRequest)
