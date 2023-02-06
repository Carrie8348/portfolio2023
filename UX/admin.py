from django.contrib import admin
from .models import UX_Projects
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(UX_Projects)
class UX_ProjectsAdmin(SummernoteModelAdmin):
    list_display = ('title', 'subtitle', 'created_time')
    summernote_fields = ('introduction')