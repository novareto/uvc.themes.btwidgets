from uvclight import Form, Fields, context, layer
from zope.interface import Interface
from zope import schema
from . import IBootstrapRequest


class IDemoWidgets(Interface):

    txt = schema.Text(
        title=u'Text field')

    txtline = schema.TextLine(
        title=u'Text line field')

    password = schema.Password(
        title=u'Password Field')

    integer = schema.Int(
        title=u'Integer field')

    floater = schema.Float(
        title=u'Float field')

    timer = schema.Time(
        title=u'Time field')

    dater = schema.Date(
        title=u'Date field')

    datetimer = schema.Datetime(
        title=u'Date & time field')

    choice1 = schema.Choice(
        title=u'Choice field (normal)',
        values=('1', '2', '3'))

    choice2 = schema.Choice(
        title=u'Choice field (radio)',
        values=('1', '2', '3'))

    list1 = schema.List(
        title=u'List field (normal)',
        value_type=schema.TextLine())

    list2 = schema.Set(
        title=u'Set field (normal)',
        value_type=schema.Choice(values=('1', '2', '3')))

    list3 = schema.Set(
        title=u'Set multiselect field',
        value_type=schema.Choice(values=('1', '2', '3')))


class DemoForm(Form):
    context(Interface)
    layer(IBootstrapRequest)

    fields = Fields(IDemoWidgets)

    def update(self):
        self.fields['choice2'].mode = 'radio'
        self.fields['list3'].mode = 'multiselect'
        Form.update(self)
