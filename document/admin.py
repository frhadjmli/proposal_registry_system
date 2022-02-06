from django.contrib import admin
from .models import Proposal, Message

# Register your models here.
class MessageInline(admin.StackedInline):
    model = Message

@admin.register(Proposal)
class ProposalAdmin(admin.ModelAdmin):
    list_display = ['title', 'semester',
                    'academic_year', 'summary', 'status']
    sortable_by = ['semester', 'academic_year']
    list_filter = ['supervisor', 'status', 'semester', 'academic_year']
    search_fields = ['title', 'supervisor', 'student']
    inlines = [MessageInline]

admin.site.register(Message)