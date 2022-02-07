from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from django.forms import ModelForm
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
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups', 'user_type')
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'user_type',)
    list_editable = ('is_staff', 'is_active',)


class ProposalInline(admin.StackedInline):
    model = Proposal.supervisor.through
    extra = 0


class StudentTopicForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(StudentTopicForm, self).__init__(*args, **kwargs)
        self.fields['user'].queryset = User.objects.filter(user_type='ST')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):

    # Filters users who are students when creating student
    form = StudentTopicForm
    # raw_id_fields = ['user']

    list_display = ('user_id', 'full_name', 'std_number', 'field', 'taken_unit', 'passed_unit',)
    sortable_by = ('std_number',)
    search_fields = ('std_number',)


class SupervisorTopicForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(SupervisorTopicForm, self).__init__(*args, **kwargs)
        self.fields['user'].queryset = User.objects.filter(user_type='SU')


@admin.register(Supervisor)
class SupervisorAdmin(admin.ModelAdmin):

    form = SupervisorTopicForm
    list_display = ('user_id', 'full_name', 'user', 'academic_rank', 'working_area',)
    sortable_by = ('academic_rank',)
    inlines = (ProposalInline,)


admin.site.register(HOD)
admin.site.register(DprtAdmin)

