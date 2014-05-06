# -*- coding: utf-8 -*-

from dolmen.forms.ztk.widget import time
from uvclight import adapts, name
from . import getTemplate, IBootstrapRequest
from zope.interface import Interface


class TimeFieldWidget(time.TimeFieldWidget):
    adapts(time.TimeField, Interface, IBootstrapRequest)


class TimeFieldDisplayWidget(time.TimeFieldDisplayWidget):
    adapts(time.TimeField, Interface, IBootstrapRequest)