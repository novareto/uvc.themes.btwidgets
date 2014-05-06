# -*- coding: utf-8 -*-

from dolmen.forms.ztk.widget import number
from uvclight import adapts, name
from . import getTemplate, IBootstrapRequest
from zope.interface import Interface


class NumberWidget(number.NumberWidget):
    adapts(number.IntegerField, Interface, IBootstrapRequest)


class CurrencyDisplayWidget(number.CurrencyDisplayWidget):
    adapts(number.CurrencyField, Interface, IBootstrapRequest)
    name('display')
    template = getTemplate('currencydisplaywidget.cpt')
