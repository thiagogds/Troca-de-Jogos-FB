#-*- coding: utf-8 -*-
from django import forms
from django.core.validators import EMPTY_VALUES

class PhoneWidget(forms.MultiWidget):
    def __init__(self, attrs=None):
        widgets = (
            forms.TextInput(attrs=attrs),
            forms.TextInput(attrs=attrs))
        super(PhoneWidget, self).__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            p = value.partitionsplit('-')
            return [p[0], p[-1]]
        return [None, None]

class PhoneField(forms.MultiValueField):
    widget = PhoneWidget

    def __init__(self, *args, **kwargs):
        fields = (
            forms.IntegerField(),
            forms.CharField())
        super(PhoneField, self).__init__(fields, *args, **kwargs)

    def compress(self, data_list):
        if data_list:
            if data_list[0] in EMPTY_VALUES:
                raise forms.ValidationError(u'DDD inválido.')
            if len(str(data_list[0])) != 2:
                raise forms.ValidationError(u'DDD deve ter 2 caracteres.')
            if data_list[1] in EMPTY_VALUES:
                raise forms.ValidationError(u'Número inválido.')
            number = ''.join(data_list[1].split('-'))
            if len(number) != 8:
                raise forms.ValidationError(u'Número deve ter oito dígitos.')
            if not number.isdigit():
                raise forms.ValidationError(u'Número deve ter somente dígitos')
            if number.startswith('0') or number.startswith('1'):
                raise forms.ValidationError(u'Número não pode começar com %s.' % number[0])
            ddd = str(data_list[0])
            return '%s-%s' % (ddd, number)
        return None
