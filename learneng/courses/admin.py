from django.contrib import admin

from embed_video.admin import AdminVideoMixin

from .models import Lessons, Topics


class AdminVideo(AdminVideoMixin, admin.ModelAdmin):
    pass


admin.site.register(Lessons, AdminVideo)
admin.site.register(Topics)
