# -*- coding: utf-8 -*-

from dolmen.forms.ztk.widgets import choice
from uvclight import adapts, name
from . import getTemplate, IBootstrapRequest
from zope.interface import Interface


class ChoiceFieldWidget(choice.ChoiceFieldWidget):
    adapts(choice.ChoiceField, Interface, IBootstrapRequest)
    template = getTemplate('choicefieldwidget.cpt')
    defaultHtmlClass = ['field', 'field-choice', 'form-control']


class ChoiceDisplayWidget(ChoiceFieldWidget):
    name('display')
    template = getTemplate('choicedisplaywidget.cpt')


class RadioFieldWidget(choice.RadioFieldWidget):
    adapts(choice.ChoiceField, Interface, IBootstrapRequest)
    name('radio')
    template = getTemplate('radiofieldwidget.cpt')
