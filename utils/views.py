# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import View

from .forms import RSA1Form

import crack

# Create your views here.
def mainview(request):
    return render(request, 'utils/main.html')

class RSA1(View):
    form_class = RSA1Form
    def get(self, request):
        form = self.form_class()
        context = {'form': form, 'message': ''}
        return render(request, 'utils/rsa1.html', context)

    def post(self, request):
        form = self.form_class(request.POST)
        context = {'form': form, 'message': ''}
        if form.is_valid():
            N = form.cleaned_data['N']
            e1 = form.cleaned_data['e1']
            c1 = form.cleaned_data['C1']
            e2 = form.cleaned_data['e2']
            c2 = form.cleaned_data['C2']
            context['message'] = crack.rsa1(int(N), int(e1), int(c1), int(e2), int(c2))
        return render(request, 'utils/rsa1.html', context)
