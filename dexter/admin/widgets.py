from cgi import escape

from wtforms import widgets
from wtforms.compat import text_type
from wtforms.widgets.core import html_params, HTMLString


class CheckboxSelectWidget(widgets.Select):
    """ Select widget that is a list of checkboxes
    """

    def __call__(self, field, **kwargs):
        if 'id' in kwargs:
            del kwargs['id']
        class_ = kwargs.pop('class', '').replace('form-control', '')

        kwargs['class'] = ''
        kwargs['name'] = field.name

        html = ['<div class="checkbox-list %s">' % class_]
        for val, label, selected in field.iter_choices():
            html.append(self.render_option(val, label, selected, **kwargs))
        html.append('</div>')
        return HTMLString(''.join(html))

    @classmethod
    def render_option(cls, value, label, selected, **kwargs):
        options = dict(kwargs, value=value)
        options['type'] = 'checkbox'
        if selected:
            options['checked'] = True
        return HTMLString('<div class="checkbox"><label><input %s> %s</label></div>' % (html_params(**options), escape(text_type(label))))
