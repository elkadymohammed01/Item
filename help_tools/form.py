from django import forms
from django.forms import Form, CheckboxInput, Select, Widget, MultiWidget, DateTimeInput


def bootstrapify_widget(widget: Widget):
    attrs = widget.attrs
    bootstrap_class = 'form-control'
    if isinstance(widget, CheckboxInput):
        bootstrap_class = 'form-check'
    elif isinstance(widget, Select):
        bootstrap_class = 'form-select'
    elif isinstance(widget, MultiWidget):
        for subwidget in widget.widgets:
            bootstrapify_widget(subwidget)
    attrs['class'] = f'{attrs.get("class", "")} {bootstrap_class}'


def bootstrapify_form(form: Form):
    for field in form.fields.values():
        bootstrapify_widget(field.widget)


def bootstrapify_form_base_field(form: Form):
    for field in form.base_fields.values():
        bootstrapify_widget(field.widget)


class BootstrapForm(Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        bootstrapify_form(self)
