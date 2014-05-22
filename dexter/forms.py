from flask_wtf import Form as BaseForm
from wtforms import SelectMultipleField, widgets, SelectField as WTFSelectField, RadioField as WTFRadioField
from wtforms.fields.html5 import IntegerField as WTFIntegerField
from wtforms.widgets import HTMLString, html_params
from wtforms.widgets import Select as SelectWidget

class StripFilter():
    def __call__(self, value):
        if value is not None and hasattr(value, 'strip'):
            return value.strip()
        else:
            return value


class Form(BaseForm):
    """ A form that strips the values of all its fields. """
    _decorated = False

    def __init__(self, *args, **kwargs):
        self._obj = kwargs.get('obj')
        super(Form, self).__init__(*args, **kwargs)

    def process(self, *args, **kwargs):
        if not self._decorated:
            self._decorated = True
            for field in self._fields.itervalues():
                field.filters = [StripFilter()] + list(field.filters)

        super(Form, self).process(*args, **kwargs)


class MultiCheckboxField(SelectMultipleField):
    """
    A multiple-select, except displays a list of checkboxes.

    Iterating the field will produce subfields, allowing custom rendering of
    the enclosed checkbox fields.
    """
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


class IntegerField(WTFIntegerField):
    def process_formdata(self, valuelist):
        if valuelist:
            try:
                if valuelist[0]:
                    self.data = int(valuelist[0])
                else:
                    self.data = None
            except ValueError:
                self.data = None
                raise ValueError(self.gettext('Not a valid integer value'))


# ---------------

class ExtendedSelectWidget(SelectWidget):
    """
    Add support of choices with ``optgroup`` to the ``Select`` widget.
    """
    def __call__(self, field, **kwargs):
        kwargs.setdefault('id', field.id)
        if self.multiple:
            kwargs['multiple'] = True
        html = ['<select %s>' % html_params(name=field.name, **kwargs)]
        for item1, item2 in field.choices:
            if isinstance(item2, (list,tuple)):
                group_label = item1
                group_items = item2
                html.append('<optgroup %s>' % html_params(label=group_label))
                for inner_val, inner_label in group_items:
                    html.append(self.render_option(inner_val, inner_label, inner_val == field.data))
                html.append('</optgroup>')
            else:
                val = item1
                label = item2
                html.append(self.render_option(val, label, val == field.data))
        html.append('</select>')
        return HTMLString(''.join(html))


class SelectField(WTFSelectField):
    """
    Update SelectField so that populate_obj sets empty values
    to None, instead of 'None' or ''.

    Also adds support for opt-groups.
    """
    widget = ExtendedSelectWidget()

    def populate_obj(self, obj, name):
        super(SelectField, self).populate_obj(obj, name)

        if hasattr(obj, name):
            val = getattr(obj, name, None)
            if val == '' or val == 'None':
                setattr(obj, name, None)

    def pre_validate(self, form):
        """
        Don't forget to validate also values from embedded lists.
        """
        for item1,item2 in self.choices:
            if isinstance(item2, (list, tuple)):
                group_label = item1
                group_items = item2
                for val,label in group_items:
                    if val == self.data:
                        return
            else:
                val = item1
                label = item2
                if val == self.data:
                    return
        raise ValueError(self.gettext('Not a valid choice!'))

class RadioField(WTFRadioField):
    """
    Update RadioField so that populate_obj sets empty values
    to None, instead of 'None' or ''.
    """
    def populate_obj(self, obj, name):
        super(RadioField, self).populate_obj(obj, name)

        if hasattr(obj, name):
            val = getattr(obj, name, None)
            if val == '' or val == 'None':
                setattr(obj, name, None)
