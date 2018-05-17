#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render, HttpResponse
import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView, View
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db.models import Q

from models import Domain, ADD_AREA
from forms import DomainForm

# Create your views here.


class DomainListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    model = Domain
    context_object_name = "domains"
    template_name = 'domain/domain_list.html'
    paginate_by = 6
    http_method_names = ['get','post']
    permission_required = 'domain.can_view_domain'
    raise_exception = True

    def get_queryset(self):
        object_list = Domain.objects.all().order_by('-add_time')

        add_area = self.request.GET.get('add_area',"")
        keyword = self.request.GET.get('keyword',"")
        if add_area:
            object_list = object_list.filter(add_area__contains = add_area)

        if keyword:
            object_list = object_list.filter(
            Q(domain_name__contains = keyword) |
            Q(ip__contains=keyword) |
            Q(applicant__contains=keyword))
        return object_list

    def get_context_data(self, **kwargs):
        context = super(DomainListView, self).get_context_data(**kwargs)
        add_area_num = self.request.GET.get('add_area', "")
        keyword = self.request.GET.get('keyword',"")

        add_area = ADD_AREA
        context['add_area'] = add_area
        context['add_area_num'] = add_area_num
        context['keyword'] = keyword
        return context



class DomainAddView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = Domain
    # 如果指定了form_class，则不能指定 fields
    # fields = ['name','description','url','memo']
    form_class = DomainForm
    template_name = "domain/domain_add.html"
    success_url = reverse_lazy('domain:domain-list')
    permission_required = 'domain.can_add_domain'
    raise_exception = True


class DomainDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Domain
    success_url = reverse_lazy('domain:domain-list')
    permission_required = 'domain.can_delete_domain'
    raise_exception = True

    # 重写dispatch方法，在返回之前，加ajax请求判断
    def dispatch(self, *args, **kwargs):
        resp = super(DomainDeleteView, self).dispatch(*args, **kwargs)
        if self.request.is_ajax():
            return JsonResponse({"results": "ok"})
        else:
            return resp


class DomainEditView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Domain
    form_class = DomainForm
    template_name = "domain/domain_edit.html"
    success_url = reverse_lazy('domain:domain-list')
    permission_required = 'domain.can_change_domain'
    raise_exception = True
