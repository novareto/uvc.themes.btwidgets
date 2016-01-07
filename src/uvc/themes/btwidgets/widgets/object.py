# -*- coding: utf-8 -*-

from dolmen.forms.ztk.widgets import object as obj
from grokcore.component import adapts, name
from . import getTemplate, IBootstrapRequest
from zope.interface import Interface


#class ObjectFieldWidget(obj.FieldWidget):
#    adapts(obj.ObjectField, Interface, IBootstrapRequest)
#    template = getTemplate('objectfieldwidget.cpt')


#class ObjectDisplayWidget(ObjectFieldWidget):
#    name('display')
