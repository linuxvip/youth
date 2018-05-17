# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.http import JsonResponse

from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.shortcuts import render,render_to_response,HttpResponseRedirect
from django.views.generic.base import View
from django.views.generic import FormView, DetailView, DeleteView, ListView, UpdateView, CreateView
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User, Group
from permission.forms import GroupAddForm, PermissionForm
from django.core.urlresolvers import reverse_lazy
from permission.models import AssetPermission
from django.utils.translation import ugettext, ugettext_lazy as _
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin





class PermissionAddView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = AssetPermission
    form_class = PermissionForm
    success_url = reverse_lazy('permission:permission-list')
    template_name = 'permissions/permission_add.html'
    permission_required = 'permission.can_add_permissions'
    raise_exception = True

    def get_context_data(self, **kwargs):
        context = super(PermissionAddView, self).get_context_data(**kwargs)
        context['title'] = _('Create Permission')
        return context

    def form_valid(self, form):
        group = form.cleaned_data['group']
        group.permissions.clear()
        group.save()
        self.object = form.save()
        return super(PermissionAddView, self).form_valid(form)

    def get_form(self, form_class=None):
        form = super(PermissionAddView, self).get_form(form_class)
        # form.fields['perm'].widget.attrs.update({'checked' : 'checked'})
        return form


class PermissionListView(PermissionRequiredMixin,LoginRequiredMixin,ListView):
    model = AssetPermission
    context_object_name = "permissions"
    template_name = 'permissions/permission_list.html'
    permission_required = 'permission.can_view_permissions'
    raise_exception = True


class PermissionEditView(PermissionRequiredMixin,LoginRequiredMixin,UpdateView):
    model = AssetPermission
    form_class = PermissionForm
    success_url = reverse_lazy('permission:permission-list')
    template_name = 'permissions/permission_edit.html'
    permission_required = 'permission.can_change_permissions'
    raise_exception = True

    def get_context_data(self, **kwargs):
        context = super(PermissionEditView, self).get_context_data(**kwargs)
        context['title'] = 'Update Permission'
        return context

    def form_valid(self, form):
        user = form.cleaned_data['user']
        permissionset = form.cleaned_data['permissions']
        user.user_permissions.clear()
        user.user_permissions.add(*permissionset)
        user.save()
        self.object = form.save()
        return super(PermissionEditView, self).form_valid(form)


class PermissionDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = AssetPermission
    success_url = reverse_lazy('permission:permission-list')
    permission_required = 'permission.can_delete_permissions'
    raise_exception = True

    # 重写dispatch方法，在返回之前，加ajax请求判断
    def dispatch(self, *args, **kwargs):
        resp = super(PermissionDeleteView, self).dispatch(*args, **kwargs)
        if self.request.is_ajax():
            return JsonResponse({"results": "ok"})
        else:
            return resp