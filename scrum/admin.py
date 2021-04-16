from django.contrib import admin
from scrum.models import Project

class ProjectAdminView(admin.ModelAdmin):
    list_display = ('name', 'sigla','description')
    list_filter = ('sigla',)

admin.site.register(Project, ProjectAdminView)
