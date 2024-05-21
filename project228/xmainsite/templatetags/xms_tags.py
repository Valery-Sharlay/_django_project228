from django import template
from xmainsite.models import PcType

register = template.Library()


@register.inclusion_tag('xmainsite/type_list.html')
def show_types(type_selected=0):
    types = PcType.objects.all()
    return {'types': types, 'type_selected': type_selected}


