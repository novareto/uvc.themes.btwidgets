# -*- coding: utf-8 -*-

from dolmen.forms.ztk.widgets import date
from grokcore.component import adapts
from . import IBootstrapRequest, getTemplate
from zope.interface import Interface


class DateFieldWidget(date.DateFieldWidget):
    adapts(date.DateField, Interface, IBootstrapRequest)
    defaultHtmlClass = ['field', 'field-date', 'form-control']
    template = getTemplate('datewidget.cpt')


class DateFieldDisplayWidget(date.DateFieldDisplayWidget):
    adapts(date.DateField, Interface, IBootstrapRequest)
