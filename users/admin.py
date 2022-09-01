from django.contrib.admin import ModelAdmin, site
from django.contrib.auth.admin import UserAdmin
from users.models import Profile


class ProfileModelAdmin(ModelAdmin):
    readonly_fields = ('created', 'updated',)
    search_fields = ('id', 'user', 'branch', 'phone_number')
    list_display = ('id', 'user', 'branch', 'phone_number')
    list_display_links = ('id',)
    list_filter = ('branch', 'user__email')
    date_hierarchy = 'created'

site.register(Profile, ProfileModelAdmin)
