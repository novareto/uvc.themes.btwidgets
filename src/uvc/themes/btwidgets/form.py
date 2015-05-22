# -*- coding: utf-8 -*-
# Copyright (c) 2007-2013 NovaReto GmbH
# cklinger@novareto.de


from cromlech.browser import ITemplate
from dolmen.forms.base import interfaces
from dolmen.forms.base.interfaces import IForm
from dolmen.forms.base.widgets import ActionWidget
from dolmen.forms.viewlet.interfaces import IInlineForm
from grokcore.component import adapts, adapter, implementer
from uvc.api.api import get_template
from uvc.themes.btwidgets import IBootstrapRequest


@adapter(IForm, IBootstrapRequest)
@implementer(ITemplate)
def bootstrap_form_template(context, request):
    """default template for the menu"""
    return get_template('form.cpt', __file__)


@adapter(IInlineForm, IBootstrapRequest)
@implementer(ITemplate)
def form_template(context, request):
    """default template for the menu"""
    return get_template('viewletform.cpt', __file__)


class ActionWidget(ActionWidget):
    adapts(
        interfaces.IAction,
        interfaces.IFieldExtractionValueSetting,
        IBootstrapRequest)

    def htmlClass(self):
        return "action btn btn-default"
