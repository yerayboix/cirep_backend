from report.models import Incidencia
from django import template

register = template.Library()


@register.filter()
def get_report_state(state):
    return Incidencia.d_s_c.get(state)
