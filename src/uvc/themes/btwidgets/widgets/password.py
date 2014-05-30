# -*- coding: utf-8 -*-

from dolmen.forms.ztk.widgets import password as pwd
from uvclight import adapts
from . import getTemplate, IBootstrapRequest
from zope.interface import Interface


class PasswordWidget(pwd.PasswordWidget):
    adapts(pwd.PasswordField, Interface, IBootstrapRequest)
    template = getTemplate('passwordwidget.cpt')
