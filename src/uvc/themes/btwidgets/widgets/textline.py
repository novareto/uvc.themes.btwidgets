# -*- coding: utf-8 -*-

from dolmen.forms.ztk.widget import textline
from uvclight import adapts, name
from . import getTemplate, IBootstrapRequest
from zope.interface import Interface


class TextLineWidget(textline.TextLineWidget):
    adapts(textline.TextLineField, Interface, IBootstrapRequest)
    template = getTemplate('textlinewidget.cpt')

