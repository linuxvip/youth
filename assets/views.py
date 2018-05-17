#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django.http import JsonResponse
from django.db.models import Q
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.exceptions import ObjectDoesNotExist

from models import Assets, Idc, AssetGroup, ASSET_TYPE, ASSET_STATUS
from forms import AssetForm, IdcForm, AssetGroupForm

from permission.models import AssetPermission
from django.contrib.auth.models import User, Group

# Create your views here.


# class AssetListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
#     model = Assets
#     context_object_name = "assets"
#     template_name = 'assets/assets_list.html'
#     permission_required = 'assets.can_view_asset'
#     # raise_exception = True
#     login_url = reverse_lazy('admin:login')
#     paginate_by = 10
#
#     def get_queryset(self):
#         asset_find = Assets.objects.all()
#         # 获取前端get请求参数
#         idc_name = self.request.GET.get('idc', '')
#         group_name = self.request.GET.get('group', '')
#         asset_type = self.request.GET.get('asset_type', '')
#         status = self.request.GET.get('status', '')
#         keyword = self.request.GET.get('keyword', '')
#         # export = request.GET.get("export", '')
#
#         # 通过前端get请求参数，筛选
#         if idc_name:
#             asset_find = asset_find.filter(idc__name__contains=idc_name)
#         if group_name:
#             asset_find = asset_find.filter(group__name__contains=group_name)
#         if asset_type:
#             asset_find = asset_find.filter(asset_type__contains=asset_type)
#         if status:
#             asset_find = asset_find.filter(status__contains=status)
#
#         if keyword:
#             asset_find = asset_find.filter(
#             Q(hostname__icontains = keyword) |
#             Q( ip__contains = keyword)
#             )
#         return asset_find
#
#     def get_context_data(self, **kwargs):
#         context = super(AssetListView, self).get_context_data(**kwargs)
#         idc_info = Idc.objects.all()
#         group_info = AssetGroups.objects.all()
#
#         # 返回前端需要的数据（机房信息、资产组信息、资产类型、资产状态、搜索关键字）
#         context['idc_info'] = idc_info
#         context['group_info'] = group_info
#         context['asset_type'] = ASSET_TYPE
#         context['asset_status'] = ASSET_STATUS
#
#         # 获取前端传过来的数据，然后在返回去
#         keyword = self.request.GET.get('keyword', "")
#         idc_name = self.request.GET.get('idc', "")
#         group_name = self.request.GET.get('group',"")
#         assettype = self.request.GET.get('asset_type',"")
#         status = self.request.GET.get('status',"")
#         print self.request.user
#
#
#         context['keyword'] = keyword
#         context['idc_name'] = idc_name
#         context['group_name'] = group_name
#         context['assettype'] = assettype
#         context['status'] = status
#         return context


class AssetListView(PermissionRequiredMixin, LoginRequiredMixin, TemplateView):
    # context_object_name = "assets"
    template_name = 'assets/assets_list.html'
    permission_required = 'assets.can_view_asset'
    raise_exception = True
    # login_url = reverse_lazy('user:login')
    paginate_by = 10

    def get_context_data(self, **kwargs):
        # 获取当前登录用户user
        current_user = self.request.user
        # print current_user

        # 如果是superuser 返回全部资产信息
        if current_user.is_superuser:
            asset_find = Assets.objects.all()

        # 如果非superuser 查找对应权限 返回具有权限的资产信息
        else:
            # 通过user获取所在组，用户可能属于多个组，不能用get
            current_group = Group.objects.filter(user=current_user)
            # print current_group
            # 获取用户组的 资产组权限, 可能是多个
            user_group_permission = AssetPermission.objects.filter(group__in=current_group)

            # 定义资产组列表
            group_list = []
            for i in user_group_permission:
                for assetgroup in i.assetsgroup.all():
                    group_list.append(assetgroup)
            asset_find = Assets.objects.filter(group__in=group_list)

        # 获取机房信息
        idc_info = Idc.objects.all()
        # 获取主机组信息
        group_info = AssetGroup.objects.all()

        # 获取前端get请求参数
        idc_name = self.request.GET.get('idc', '')
        group_name = self.request.GET.get('group', '')
        asset_type = self.request.GET.get('asset_type', '')
        status = self.request.GET.get('status', '')
        keyword = self.request.GET.get('keyword', '')

        # 通过前端get请求参数，筛选
        if idc_name:
            asset_find = asset_find.filter(idc__name__contains=idc_name)
        if group_name:
            asset_find = asset_find.filter(group__name__contains=group_name)
        if asset_type:
            asset_find = asset_find.filter(asset_type__contains=asset_type)
        if status:
            asset_find = asset_find.filter(status__contains=status)

        if keyword:
            asset_find = asset_find.filter(
            Q(hostname__icontains=keyword) |
            Q( ip__contains=keyword)
            )

        # 返回前端需要的数据（机房信息、资产组信息、资产类型、资产状态、搜索关键字、匹配特定权限的具体资产信息）
        context = {
            'idc_name': idc_name,
            'group_name': group_name,
            'assettype': asset_type,
            'status': status,
            'keyword': keyword,

            'idc_info': idc_info,
            'group_info': group_info,
            'asset_type': ASSET_TYPE,
            'asset_status': ASSET_STATUS,
            'assets': asset_find
        }

        kwargs.update(context)
        return super(AssetListView, self).get_context_data(**kwargs)


class AssetAddView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = Assets
    # 如果指定了form_class，则不能指定 fields
    # fields = ['name','description','url','memo']
    form_class = AssetForm
    template_name = "assets/assets_add.html"
    success_url = reverse_lazy('assets:asset-list')
    permission_required = 'assets.can_add_asset'
    raise_exception = True


class AssetDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Assets
    success_url = reverse_lazy('assets:asset-list')
    permission_required = 'assets.can_delete_asset'
    raise_exception = True

    # 重写dispatch方法，在返回之前，加ajax请求判断
    def dispatch(self, *args, **kwargs):
        resp = super(AssetDeleteView, self).dispatch(*args, **kwargs)
        if self.request.is_ajax():
            return JsonResponse({"results": "ok"})
        else:
            return resp


class AssetEditView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Assets
    form_class = AssetForm
    template_name = "assets/assets_edit.html"
    success_url = reverse_lazy('assets:asset-list')
    permission_required = 'assets.can_change_asset'
    raise_exception = True


class IdcListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    model = Idc
    context_object_name = "idcs"
    template_name = 'assets/idc_list.html'
    permission_required = 'assets.can_view_idc'
    raise_exception = True


class IdcAddView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = Idc
    # 如果指定了form_class，则不能指定 fields
    # fields = ['name','description','url','memo']
    form_class = IdcForm
    template_name = "assets/idc_add.html"
    success_url = reverse_lazy('assets:idc-list')
    permission_required = 'assets.can_add_idc'
    raise_exception = True


class IdcDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Idc
    success_url = reverse_lazy('assets:idc-list')
    permission_required = 'assets.can_delete_idc'
    raise_exception = True

    # 重写dispatch方法，在返回之前，加ajax请求判断
    def dispatch(self, *args, **kwargs):
        resp = super(IdcDeleteView, self).dispatch(*args, **kwargs)
        if self.request.is_ajax():
            return JsonResponse({"results": "ok"})
        else:
            return resp


class IdcEditView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Idc
    form_class = IdcForm
    template_name = "assets/idc_edit.html"
    success_url = reverse_lazy('assets:idc-list')
    permission_required = 'assets.can_change_idc'
    raise_exception = True


class AssetGroupListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    model = AssetGroup
    context_object_name = "assetgroups"
    template_name = 'assets/asset_group_list.html'
    permission_required = 'assets.can_view_assetgroup'
    raise_exception = True


class AssetGroupAddView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = AssetGroup
    # 如果指定了form_class，则不能指定 fields
    # fields = ['name','description','url','memo']
    form_class = AssetGroupForm
    template_name = "assets/asset_group_add.html"
    success_url = reverse_lazy('assets:asset-group-list')
    permission_required = 'assets.can_add_assetgroup'
    raise_exception = True


class AssetGroupDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = AssetGroup
    success_url = reverse_lazy('assets:asset-group-list')
    permission_required = 'assets.can_delete_idc'
    raise_exception = True

    # 重写dispatch方法，在返回之前，加ajax请求判断
    def dispatch(self, *args, **kwargs):
        resp = super(AssetGroupDeleteView, self).dispatch(*args, **kwargs)
        if self.request.is_ajax():
            return JsonResponse({"results": "ok"})
        else:
            return resp


class AssetGroupEditView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = AssetGroup
    form_class = AssetGroupForm
    template_name = "assets/asset_group_edit.html"
    success_url = reverse_lazy('assets:asset-group-list')
    permission_required = 'assets.can_change_assetgroup'
    raise_exception = True