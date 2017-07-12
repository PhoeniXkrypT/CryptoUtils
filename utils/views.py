# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import View

from .forms import RSA1Form, RSA2Form

import crack

# Create your views here.
def mainview(request):
    return render(request, 'utils/main.html')

class RSA1(View):
    form_class = RSA1Form
    title = "RSA: Common modulus with relatively prime public exponents"
    def get(self, request):
        form = self.form_class()
        context = {'form': form, 'title': self.title, 'result': ''}
        return render(request, 'utils/rsa_common.html', context)

    def post(self, request):
        form = self.form_class(request.POST)
        context = {'form': form, 'title': self.title, 'result': ''}
        if form.is_valid():
            N = form.cleaned_data['N']
            e1 = form.cleaned_data['e1']
            c1 = form.cleaned_data['C1']
            e2 = form.cleaned_data['e2']
            c2 = form.cleaned_data['C2']
            context['result'] = crack.rsa_commod(int(N), int(e1), int(c1), int(e2), int(c2))
        return render(request, 'utils/rsa_common.html', context)

class RSA2(View):
    form_class = RSA2Form
    title = "RSA: Blinding Attack"
    def get(self, request):
        form = self.form_class()
        context = {'form': form, 'title': self.title, 'result': ''}
        return render(request, 'utils/rsa_common.html', context)

    def post(self, request):
        form = self.form_class(request.POST)
        context = {'form': form, 'title': self.title, 'result': ''}
        if form.is_valid():
            N = form.cleaned_data['N']
            e = form.cleaned_data['e']
            m = form.cleaned_data['m']
            val = crack.rsa_msg_blind(int(N), int(e), int(m))
            context['result'] = val
        return render(request, 'utils/rsa_common.html', context)