# -*- coding: utf-8 -*-

from dolmen.forms.ztk.widget import text
from uvclight import adapts, name
from . import getTemplate, IBootstrapRequest
from zope.interface import Interface


class TextareaWidget(text.TextareaWidget):
    adapts(text.TextField, Interface, IBootstrapRequest)
    template = getTemplate('textareawidget.cpt')


class DisplayTextareaWidget(TextareaWidget):
    name('display')
    template = getTemplate('pre_text.cpt')
