from django.contrib import admin
from tracker_app.models import ScrumManager, Project, Developer
# Register your models here.

admin.site.register(ScrumManager)
admin.site.register(Project)
admin.site.register(Developer)
