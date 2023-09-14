from django import template

register = template.Library()

@register.filter
def farsi_number(number):
    number = str(number)
    e_table = number.maketrans('0123456789', '۰۱۲۳۴۵۶۷۸۹')
    return number.translate(e_table)

