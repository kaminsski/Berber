import datetime

from django import template

register = template.Library()

@register.filter()
def plus_days(days):
    try:
        days_int = int(days)
        new_date = datetime.date.today() + datetime.timedelta(days=days_int)
        return new_date
    except (TypeError, ValueError):
        return None 
@register.filter()
def to_int(value):
   try:
     return int(value)
   except ValueError:
      print(value)
         
@register.filter
def to_str(value):
    return str(value)