# Text line widget

from dolmen.forms.base.markers import Marker, NO_VALUE
from dolmen.forms.base.widgets import FieldWidget
from dolmen.forms.ztk.fields import BaseField, registerSchemaField
from dolmen.forms.ztk.widgets import getTemplate

from grokcore import component as grok
from zope.i18nmessageid import MessageFactory
from zope.schema import interfaces as schema_interfaces

_ = MessageFactory("dolmen.forms.base")


class TextLineField(BaseField):
    """A text line field.
    """

    def __init__(self, title,
                 minLength=0,
                 maxLength=None,
                 **options):
        super(TextLineField, self).__init__(title, **options)
        self.minLength = minLength
        self.maxLength = maxLength

    def isEmpty(self, value):
        return value is NO_VALUE or not value

    def validate(self, value, form):
        error = super(TextLineField, self).validate(value, form)
        if error is not None:
            return error
        if not isinstance(value, Marker) and len(value):
            assert isinstance(value, basestring)
            if self.minLength and len(value) < self.minLength:
                return _(u"This text is too short.")
            if self.maxLength and len(value) > self.maxLength:
                return _(u"This text is too long.")
        return None


# BBB
TextLineSchemaField = TextLineField


class TextLineWidget(FieldWidget):
    grok.adapts(TextLineField, None, None)
    template = getTemplate('textlinewidget.cpt')
    defaultHtmlClass = ['field', 'field-textline']
    defaultHtmlAttributes = set(['readonly', 'required', 'autocomplete',
                                 'maxlength', 'pattern', 'placeholder',
                                 'size', 'style', 'disabled'])


def TextLineSchemaFactory(schema):
    field = TextLineField(
        schema.title or None,
        identifier=schema.__name__,
        description=schema.description,
        required=schema.required,
        readonly=schema.readonly,
        minLength=schema.min_length,
        maxLength=schema.max_length,
        interface=schema.interface,
        constrainValue=schema.constraint,
        defaultFactory=schema.defaultFactory,
        defaultValue=schema.default or NO_VALUE)
    return field


def register():
    registerSchemaField(TextLineSchemaFactory, schema_interfaces.ITextLine)
