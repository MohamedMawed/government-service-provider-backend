from .models import *
from accounts.forms import UserCreationForm, UserDetailForm
from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from accounts.models import User


class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    list_display = ('username', 'email', 'full_name','lat','lng','national_id','postal_code')

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('username', 'user_type', 'full_name', 'email',
                                           'date_joined', 'password_unhashed')
        else:
            return ('')

    # def get_actions(self, request):
    #     # Disable delete
    #     actions = super(CustomUserAdmin, self).get_actions(request)
    #     del actions['delete_selected']
    #     return actions

    # def has_delete_permission(self, request, obj=None):
    #     # Disable delete
    #     return False

    def changelist_view(self, request, extra_context=None):
        extra_context = {'title': 'Select Customer.'}
        return super(CustomUserAdmin, self).changelist_view(request, extra_context=extra_context)

    def get_fieldsets(self, request, obj=None):
        fieldsets = list(UserAdmin.fieldsets)
        if obj:
            fieldsets[0] = ('User Credentials',
                            {
                                'fields': ('username', 'password', 'password_unhashed')
                            })
            fieldsets[1] = ('Personal Information', {
                'fields': ('full_name', 'email','lat','lng','national_id','postal_code'),
            })
            fieldsets[2] = ('Permissions', {
                'fields': ('active',),
            })
            fieldsets[3] = ('Important dates', {
                'fields': ('date_joined',),
            })
        else:
            fieldsets[0] = ('User Credentials',
                            {
                                'fields': ('username', 'password1', 'password2', 'email', 'full_name','lat','lng','national_id','postal_code')
                            })
            del fieldsets[1:4]
            # fieldsets[1] = []
            # fieldsets[2] = []
            # fieldsets[3] = []

        return fieldsets
    # def get_form(self, request, *args, **kwargs):
    #      form = super(CustomUserAdmin, self).get_form(request, *args, **kwargs)
    #      form.password_unhashed = form.get['password1']
    #      return form


UserAdmin.add_fieldsets = (
    (None, {
        'classes': ('wide',),
        'fields': ('username', 'email', 'password1', 'password2', 'full_name','lat','lng','national_id','postal_code'),
    }),

)
admin.site.register(User, CustomUserAdmin)
admin.site.site_header = "Online MP Administration"
admin.site.site_title = "Online MP Administration"
admin.site.index_title = "Welcome to MP Administration"
admin.site.unregister(Group)
