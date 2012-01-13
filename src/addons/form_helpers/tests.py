#-*- coding: utf-8 -*-
from django.test import TestCase
from django import forms
from widgets import PhoneField

class SomeForm(forms.Form):
    phone = PhoneField()

class PhoneFieldTest(TestCase):
    def test_validate_only_digits(self):
        form = SomeForm({'phone_0': '21', 'phone_1': '96186180'})
        self.assertTrue(form.is_valid())
        self.assertEquals(form.cleaned_data['phone'], '21-96186180')

    def test_validate_phone_with_dash(self):
        form = SomeForm({'phone_0': '21', 'phone_1': '9618-6180'})
        self.assertTrue(form.is_valid())
        self.assertEquals(form.cleaned_data['phone'], '21-96186180')

    def test_fail_when_ddd_is_not_digit(self):
        form = SomeForm({'phone_0': 'X21', 'phone_1': '9618-6180'})
        self.assertFalse(form.is_valid())

    def test_limit_max_of_2_digits_ddd(self):
        form = SomeForm({'phone_0': '222', 'phone_1': '9618-6180'})
        self.assertFalse(form.is_valid())

    def test_limit_min_of_2_digits_ddd(self):
        form = SomeForm({'phone_0': '2', 'phone_1': '9618-6180'})
        self.assertFalse(form.is_valid())

    def test_limit_min_of_8_digits_phone(self):
        form = SomeForm({'phone_0': '22', 'phone_1': '618-6180'})
        self.assertFalse(form.is_valid())

    def test_shouldnt_accept_phone_with_8_letters(self):
        form = SomeForm({'phone_0': '22', 'phone_1': 'asdfghjk'})
        self.assertFalse(form.is_valid())

    def test_shouldnt_accept_phone_starting_with_0(self):
        form = SomeForm({'phone_0': '22', 'phone_1': '06291621'})
        self.assertFalse(form.is_valid())

    def test_shouldnt_accept_phone_starting_with_1(self):
        form = SomeForm({'phone_0': '22', 'phone_1': '16291621'})
        self.assertFalse(form.is_valid())
