# -*- coding: utf-8 -*-
# Copyright (c) 2007-2013 NovaReto GmbH
# cklinger@novareto.de


import uvclight

from dolmen.forms.base import interfaces
from dolmen.forms.base.widgets import ActionWidget
from uvc.themes.btwidgets import IBootstrapRequest
from cromlech.browser import ITemplate
from dolmen.forms.base.interfaces import IForm
from grokcore.component import adapts, adapter, implementer


@adapter(IForm, IBootstrapRequest)
@implementer(ITemplate)
def bootstrap_form_template(context, request):
    """default template for the menu"""
    return uvclight.get_template('form.cpt', __file__)


class ActionWidget(ActionWidget):
    adapts(
        interfaces.IAction,
        interfaces.IFieldExtractionValueSetting,
        IBootstrapRequest)

    def htmlClass(self):
        return "action btn btn-default"
