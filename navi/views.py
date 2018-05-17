#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django.http import JsonResponse
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin

from models import NAVI
from forms import NaviForm

# Create your views here.


class NaviListView(LoginRequiredMixin, ListView):
    model = NAVI
    context_object_name = "navis"
    template_name = 'navi/navi_list.html'

    # permission_required = 'navi.can_view_navi'
    # raise_exception = True
    login_url = reverse_lazy('user:login')


class NaviManageView(LoginRequiredMixin, ListView):
    model = NAVI
    context_object_name = "navis"
    template_name = 'navi/navi_manage.html'
    # permission_required = 'navi.can_view_navi'
    # raise_exception = True


class NaviDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = NAVI
    success_url = reverse_lazy('navi:navi-index')
    permission_required = 'navi.can_delete_navi'
    raise_exception = True

    # 重写dispatch方法，在返回之前，加ajax请求判断
    def dispatch(self, *args, **kwargs):
        resp = super(NaviDeleteView, self).dispatch(*args, **kwargs)
        if self.request.is_ajax():
            return JsonResponse({"results": "ok"})
        else:
            return resp


class NaviAddView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = NAVI
    # 如果指定了form_class，则不能指定 fields
    # fields = ['name','description','url','memo']
    form_class = NaviForm
    template_name = "navi/navi_add.html"
    success_url = reverse_lazy('navi:navi-manage')
    permission_required = 'navi.can_add_navi'
    raise_exception = True


class NaviEditView(UpdateView):
    model = NAVI
    form_class = NaviForm
    template_name = "navi/navi_edit.html"
    success_url = reverse_lazy('navi:navi-manage')
