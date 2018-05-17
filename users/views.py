# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.http import JsonResponse

from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.shortcuts import render,render_to_response,HttpResponseRedirect
from django.views.generic.base import View
from django.views.generic import FormView, DetailView, DeleteView, ListView, UpdateView, CreateView
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin

from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import Group
from django.core.urlresolvers import reverse_lazy

from .models import UserProfile
from .forms import LoginForm, UserAddForm


class LoginView(View):
    """
    用户登录
    """
    def get(self,request):
        return render(request, 'users/login.html',{})

    def post(self,request):
        # 实例化
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            # 获取用户提交的用户名和密码
            user_name = request.POST.get('username', None)
            pass_word = request.POST.get('password', None)
            # print user_name
            # print pass_word
            # 成功返回user对象,失败None
            user = authenticate(username=user_name, password=pass_word)
            # 如果不是null说明验证成功
            if user is not None:
                if user.is_active:
                    # 只有注册激活才能登录
                    login(request, user)
                    return HttpResponseRedirect(reverse('index'))
                else:
                    return render(request, 'users/login.html', {'msg': '用户名或密码错误', 'login_form': login_form})
            # 只有当用户名或密码不存在时，才返回错误信息到前端
            else:
                return render(request, 'users/login.html', {'msg': '用户名或密码错误','login_form':login_form})

        # form.is_valid（）已经判断不合法了，所以这里不需要再返回错误信息到前端了
        else:
            return render(request,'users/login.html',{'login_form':login_form})


class LogoutView(View):
    """
    用户登出
    """
    def get(self,request):
        logout(request)
        return HttpResponseRedirect(reverse_lazy('user:login'))


class UserListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    template_name = 'users/user_list.html'
    model = UserProfile
    context_object_name = "users"
    permission_required = 'users.can_view_user'
    login_url = reverse_lazy('user:login')


class UserAddView(PermissionRequiredMixin, LoginRequiredMixin, FormView):
    template_name = 'users/user_add.html'
    form_class = UserAddForm
    success_url = reverse_lazy('user:user-list')
    permission_required = 'users.can_add_user'

    def form_valid(self, form):
        username = form.cleaned_data['user']
        password = form.cleaned_data['newpassword1']
        email = form.cleaned_data['email']
        mobile = form.cleaned_data['mobile']
        UserProfile.objects.create_user(
            username = username,
            email = email,
            mobile = mobile,
            password = password,
            is_active = True,
            is_staff = True
        )
        return HttpResponseRedirect(self.get_success_url())


class UserDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = UserProfile
    success_url = reverse_lazy('user:user-list')
    permission_required = 'users.can_delete_user'

    # 重写dispatch方法，在返回之前，加ajax请求判断
    def dispatch(self, *args, **kwargs):
        resp = super(UserDeleteView, self).dispatch(*args, **kwargs)
        if self.request.is_ajax():
            return JsonResponse({"results": "ok"})
        else:
            return resp


# class UserEditView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
#     template_name = 'users/user_edit.html'
#     model = UserProfile
#     form_class = UserAddForm
#     success_url = reverse_lazy('user:user-list')
#     permission_required = 'users.can_change_user'
#
#     def form_valid(self, form):
#         username = form.cleaned_data['user']
#         password = form.cleaned_data['newpassword1']
#         email = form.cleaned_data['email']
#         mobile = form.cleaned_data['mobile']
#         UserProfile.objects.create_user(
#             username=username,
#             email=email,
#             mobile=mobile,
#             password=password,
#             is_active=True,
#             is_staff=True
#         )
#         return HttpResponseRedirect(self.get_success_url())

class GroupListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    template_name = 'users/group_list.html'
    model = Group
    context_object_name = "groups"
    permission_required = 'users.can_view_group'
    login_url = reverse_lazy('admin:login')






# # 邮箱和用户名都可以登录
# # 基于ModelBackend类，因为它有authenticate方法
# class CustomBackend(ModelBackend):
#     def authenticate(self, request, username=None, password=None, **kwargs):
#         try:
#             # 不希望用户存在两个，get只能有一个。两个是get失败的一种原因 Q为使用并集查询
#             user = User.objects.get(Q(username=username)|Q(email=username))
#
#             # django的后台中密码加密：所以不能password==password
#             # User 继承的AbstractUser中有def check_password(self, raw_password):
#             if user.check_password(password):
#                 return user
#         except Exception as e:
#             return None
#
#








#
#

#
#
# class GroupAddView(PermissionRequiredMixin, LoginRequiredMixin, FormView):
#     template_name = 'users/group_add.html'
#     form_class = GroupAddForm
#     success_url = reverse_lazy('permission:group-list')
#     permission_required = 'permission.can_add_group'
#     raise_exception = True
#
#     def form_valid(self, form):
#         name = form.cleaned_data['name']
#
#         User.objects.create_user(username=username,email=email,password=password,is_active=True,is_staff=True)
#         return HttpResponseRedirect(self.get_success_url())
#
#
