# -*- coding: utf-8 -*-

from dolmen.forms.ztk.widgets import collection as col
from grokcore.component import adapts, name
from . import getTemplate, IBootstrapRequest
from zope.interface import Interface


class MultiChoiceDisplayFieldWidget(col.MultiChoiceFieldWidget):
    adapts(col.SetField, col.ChoiceField, Interface, IBootstrapRequest)
    name('display')
    template = getTemplate('multichoicedisplayfieldwidget.cpt')

    def renderableChoice(self):
        current = self.inputValue()
        base_id = self.htmlId()
        for i, choice in enumerate(self.choices()):
            if choice.token in current:
                yield {'title': choice.title,
                       'id': base_id + '-' + str(i)}
