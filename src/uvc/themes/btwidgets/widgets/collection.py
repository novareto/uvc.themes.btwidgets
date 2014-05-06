# -*- coding: utf-8 -*-

from dolmen.forms.ztk.widgets import collection as col
from uvclight import adapts, name
from . import getTemplate, IBootstrapRequest
from zope.interface import Interface


class MultiGenericFieldWidget(col.MultiGenericFieldWidget):
    adapts(col.ICollectionField, Interface, Interface, IBootstrapRequest)
    template = getTemplate('multigenericfieldwidget.cpt')


class ListGenericFieldWidget(col.ListGenericFieldWidget):
    adapts(col.ListField, Interface, Interface, IBootstrapRequest)
    template = getTemplate('multigenericfieldwidget.cpt')


class MultiGenericDisplayFieldWidget(MultiGenericFieldWidget):
    name('display')
    template = getTemplate('multigenericdisplayfieldwidget.cpt')


class MultiObjectFieldWidget(col.MultiObjectFieldWidget):
    adapts(col.ICollectionField, col.ObjectField, Interface, IBootstrapRequest)
    template = getTemplate('multiobjectfieldwidget.cpt')


class ListObjectFieldWidget(col.ListObjectFieldWidget):
    adapts(col.ListField, col.ObjectField, Interface, IBootstrapRequest)
    template = getTemplate('listobjectfieldwidget.cpt')


class RegularMultiObjectFieldWidget(MultiGenericFieldWidget):
    name('input-list')


class RegularListObjectFieldWidget(ListGenericFieldWidget):
    name('input-list')


class MultiChoiceFieldWidget(col.MultiChoiceFieldWidget):
    adapts(col.SetField, col.ChoiceField, Interface, IBootstrapRequest)
    template = getTemplate('multichoicefieldwidget.cpt')


class MultiSelectFieldWidget(MultiChoiceFieldWidget):
    name('multiselect')
    template = getTemplate('multiselectfieldwidget.cpt')


class MultiChoiceDisplayFieldWidget(MultiChoiceFieldWidget):
    name('display')
    template = getTemplate('multichoicedisplayfieldwidget.cpt')
