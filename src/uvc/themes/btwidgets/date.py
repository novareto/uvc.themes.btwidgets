# -*- coding: utf-8 -*-

from dolmen.forms.ztk.widget import date
from uvclight import adapts
from . import IBootstrapRequest
from zope.interface import Interface


class DateFieldWidget(date.DateFieldWidget):
    adapts(date.DateField, Interface, IBootstrapRequest)


class DateFieldDisplayWidget(date.DateFieldDisplayWidget):
    adapts(date.DateField, Interface, IBootstrapRequest)
