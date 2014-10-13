# -*- coding: utf-8 -*-

from dolmen.forms.ztk.widgets import bool
from grokcore.component import adapts
from . import getTemplate, IBootstrapRequest
from zope.interface import Interface


class CheckBoxWidget(bool.CheckBoxWidget):
    adapts(bool.BooleanField, Interface, IBootstrapRequest)
    template = getTemplate('checkboxwidget.cpt')


class CheckBoxDisplayWidget(bool.CheckBoxDisplayWidget):
    adapts(bool.BooleanField, Interface, IBootstrapRequest)
