# -*- coding: utf-8 -*-

from dolmen.forms.ztk.widgets import link
from grokcore.component import adapts, name
from . import IBootstrapRequest, getTemplate
from zope.interface import Interface


class LinkFieldWidget(link.LinkFieldWidget):
    adapts(link.IField, Interface, IBootstrapRequest)
    name('link')
    template = getTemplate('linkfieldwidget.cpt')
