from django.contrib import admin
from ZhuanPan.models import *
# Register your models here.

class RewardAdmin(admin.ModelAdmin):
    list_display = ('phone', 'content', 'if_exchange', 'fail_message', 'time')
    list_filter = ('time',)
    ordering = ('-time',)

admin.site.register(Reward, RewardAdmin)
admin.site.register(Consume)