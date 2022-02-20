from django import template

register = template.Library()
def split(valu, key):
    return valu.split(key)