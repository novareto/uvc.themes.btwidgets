# -*- coding: utf-8 -*-

from dolmen.forms.ztk.widgets import email
from uvclight import adapts, name
from . import IBootstrapRequest
from zope.interface import Interface


class EmailWidget(email.EmailWidget):
    adapts(email.EmailField, Interface, IBootstrapRequest)


class EmailDisplayWidget(email.EmailDisplayWidget):
    adapts(email.EmailField, Interface, IBootstrapRequest)
    name('display')
