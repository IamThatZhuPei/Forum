# coding: utf-8
from django import forms
from django.contrib.auth.models import User

__author__ = '朱沛'


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']

