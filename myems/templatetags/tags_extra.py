from django import template

register = template.Library()


@register.filter(name='running_total')
def do_sum(score_list):
    return sum(score_list)
