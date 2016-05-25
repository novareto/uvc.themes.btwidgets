# -*- coding: utf-8 -*-

from dolmen.forms.ztk.widgets import time
from grokcore.component import adapts
from . import IBootstrapRequest, getTemplate
from zope.interface import Interface


class TimeFieldWidget(time.TimeFieldWidget):
    adapts(time.TimeField, Interface, IBootstrapRequest)
    defaultHtmlClass = ['field', 'field-time', 'form-control']
    template = getTemplate('timewidget.cpt')
    

class TimeFieldDisplayWidget(time.TimeFieldDisplayWidget):
    adapts(time.TimeField, Interface, IBootstrapRequest)
