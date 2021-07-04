from django import template

register = template.Library()

@register.filter
def attr(form, name_arg):
    attrs = form.field.widget.attrs
    try:
        name, arg = name_arg.split('=')
        attrs[name] = arg
        rendered = str(form)
    except:
        pass           
    return form  