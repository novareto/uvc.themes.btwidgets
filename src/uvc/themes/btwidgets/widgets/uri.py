# -*- coding: utf-8 -*-

from dolmen.forms.ztk.widgets import uri
from uvclight import adapts, name
from . import getTemplate, IBootstrapRequest
from zope.interface import Interface


class URIWidget(uri.URIWidget):
    adapts(uri.URIField, Interface, IBootstrapRequest)
    template = getTemplate('uriwidget.cpt')


class URIDisplayWidget(uri.URIDisplayWidget):
    adapts(uri.URIField, Interface, IBootstrapRequest)
    name('display')
    template = getTemplate('uridisplaywidget.pt')
