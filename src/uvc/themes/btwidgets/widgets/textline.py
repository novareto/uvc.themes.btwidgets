# -*- coding: utf-8 -*-

from dolmen.forms.ztk.widgets import textline
from grokcore.component import adapts
from . import getTemplate, IBootstrapRequest
from zope.interface import Interface


class TextLineWidget(textline.TextLineWidget):
    adapts(textline.TextLineField, Interface, IBootstrapRequest)
    template = getTemplate('textlinewidget.cpt')
    defaultHtmlClass = ['field', 'field-textline', 'form-control']
