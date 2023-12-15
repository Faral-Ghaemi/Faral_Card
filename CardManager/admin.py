from django.contrib import admin
from .models import Team, Members, Projects, TimeCard

# تنظیمات اختیاری برای نمایش بهتر مدل‌ها در پنل مدیریت
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', )  # فیلدهایی که می‌خواهیم در لیست نمایش داده شوند

class MembersAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number', 'email', 'team')

class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('name', 'team')

class TimeCardAdmin(admin.ModelAdmin):
    list_display = ('user', 'project', 'start_time', 'end_time', 'work_duration')

# ثبت مدل‌ها با تنظیمات مربوطه
admin.site.register(Team, TeamAdmin)
admin.site.register(Members, MembersAdmin)
admin.site.register(Projects, ProjectsAdmin)
admin.site.register(TimeCard, TimeCardAdmin)
