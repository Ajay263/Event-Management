from django.contrib import admin
from .models import Event, EventRegistration, BarcodeScan, AboutSection, Stat  # Import Stat

class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'location', 'created_by', 'view_registered_users')

    def view_registered_users(self, obj):
        return f'<a href="/admin/events/event/{obj.id}/registered_users/">View Registered Users</a>'
    view_registered_users.allow_tags = True
    view_registered_users.short_description = 'Registered Users'


@admin.register(BarcodeScan)
class BarcodeScanAdmin(admin.ModelAdmin):
    list_display = ['user', 'event', 'scan_time', 'time_taken']
    list_filter = ['event', 'scan_time', 'time_taken']
    search_fields = ['user__username', 'event__name']
    ordering = ['time_taken', 'scan_time']  # Orders by the shortest time first, then by scan time


class StatInline(admin.TabularInline):
    model = Stat  # Reference Stat directly here
    extra = 1  # Allows adding multiple stats


class AboutSectionAdmin(admin.ModelAdmin):
    inlines = [StatInline]
    list_display = ('subtitle','image')


admin.site.register(AboutSection, AboutSectionAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(EventRegistration)
