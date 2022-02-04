from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

from .models import User, Student, Supervisor, HOD, DprtAdmin
from document.models import Proposal


@admin.register(User)
class UserAdmin(DefaultUserAdmin):

    def save_model(self, request, obj, form, change):

        if request.POST.get('user_type') == 'DA':
            obj.is_staff = True
            obj.is_superuser = True
        obj.save()

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'user_type')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
    )
    fieldsets = (
        (None, {'fields': ('username', 'password',)}),
        ('Personal info', {'fields': (
            'first_name', 'last_name', 'email',
        )}),

        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions',),
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined',)}),
    )
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups',)
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'user_type',)
    list_editable = ('is_staff', 'is_active',)


class ProposalInline(admin.StackedInline):
    model = Proposal


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):

    list_display = ('user_id', 'full_name', 'std_number', 'field', 'taken_unit', 'passed_unit',)
    sortable_by = ('std_number',)
    search_fields = ('std_number',)


@admin.register(Supervisor)
class SupervisorAdmin(admin.ModelAdmin):

    list_display = ('user_id', 'full_name', 'user', 'academic_rank', 'working_area',)
    sortable_by = ('academic_rank',)
    inlines = (ProposalInline,)


admin.site.register(HOD)
admin.site.register(DprtAdmin)

