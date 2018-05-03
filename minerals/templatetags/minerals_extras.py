import random

from django import template

from minerals.models import Mineral


register = template.Library()

# Not used in favor of handling random ID generation in the view, rather than
# through the template
"""
@register.simple_tag
def get_random_id():
    ids = Mineral.objects.all().values_list('id', flat=True)
    return random.choice(ids)
"""


@register.filter
def get_item(dictionary, key):
    """Adds the dictionary.get() function as a filter for the templates"""
    return dictionary.get(key)


@register.filter
def rem_underscore(string):
    """Removes underscores from a string and replaces with a space"""
    return string.replace('_', ' ')


@register.inclusion_tag('minerals/mineral_groups.html')
def mineral_group_list(current_group=None):
    """Returns dict of mineral groups to display in filter"""
    groups = (Mineral.objects.values_list('group', flat=True)
                             .distinct())
    groups = list(groups)
    groups.sort()
    return {'groups': groups, 'current_group': current_group}


@register.inclusion_tag('minerals/mineral_specific_gravities.html')
def mineral_specific_gravity_list(current_specific_gravity=None):
    """Returns dict of mineral specific gravities to display in filter"""
    specific_gravities = (Mineral.objects
                                 .values_list('specific_gravity', flat=True)
                                 .distinct())
    specific_gravities = list(specific_gravities)
    specific_gravities.sort()
    if not specific_gravities[0]:
        specific_gravities = specific_gravities[1:]
    return {'specific_gravities': specific_gravities,
            'current_specific_gravity': current_specific_gravity}
