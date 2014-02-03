from flask_wtf import Form as BaseForm

class StripFilter():
    def __call__(self, value):
        if value is not None and hasattr(value, 'strip'):
            return value.strip()
        else:
            return value


class Form(BaseForm):
    """ A form that strips the values of all its fields. """
    _decorated = False

    def process(self, *args, **kwargs):
        if not self._decorated:
            self._decorated = True
            for field in self._fields.itervalues():
                field.filters = [StripFilter()] + list(field.filters)

        super(Form, self).process(*args, **kwargs)
