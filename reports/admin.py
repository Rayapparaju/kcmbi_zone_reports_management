from django.contrib import admin
from .models import PreacherPersonalInfo, TeamLeaderPersonalData, CongregationUpdate, KCMBIFieldReport, Zone

class ZoneAdmin(admin.ModelAdmin):
    list_display = ('zone_number', 'zone_name', 'team_leader', 'location', 'created_at')
    list_filter = ('team_leader',)
    search_fields = ('zone_number', 'zone_name', 'location')
    list_per_page = 25

class PreacherPersonalInfoAdmin(admin.ModelAdmin):
    list_display = ('name_of_preacher', 'team_leader_name', 'zone_info', 'cell_number', 'email_address', 'linked_user', 'created_at')
    list_filter = ('created_at', 'team_leader_name')
    search_fields = ('name_of_preacher', 'team_leader_name', 'email_address')
    readonly_fields = ('created_at', 'updated_at')
    list_per_page = 25
    def linked_user(self, obj):
        if obj.user:
            return f"{obj.user.username} ({obj.user.profile.get_role_display()})"
        return '-'
    linked_user.short_description = 'User Account'
    def zone_info(self, obj):
        if obj.zone:
            return f"{obj.zone.zone_number} - {obj.zone.zone_name or ''}"
        return '-'
    zone_info.short_description = 'Zone'

class TeamLeaderPersonalDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'cell_number', 'email_address', 'number_of_kcmbis_submitting', 'linked_user', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email_address')
    readonly_fields = ('created_at', 'updated_at')
    list_per_page = 25
    def linked_user(self, obj):
        if obj.user:
            return f"{obj.user.username} ({obj.user.profile.get_role_display()})"
        return '-'
    linked_user.short_description = 'User Account'

class CongregationUpdateAdmin(admin.ModelAdmin):
    list_display = ('name_of_preacher', 'zone_info', 'name_of_village', 'month_of_reporting', 'church_members_count', 'created_at')
    list_filter = ('month_of_reporting', 'created_at')
    search_fields = ('name_of_preacher', 'name_of_village')
    readonly_fields = ('created_at', 'updated_at')
    list_per_page = 25
    def zone_info(self, obj):
        if obj.zone:
            return f"{obj.zone.zone_number} - {obj.zone.zone_name or ''}"
        return '-'
    zone_info.short_description = 'Zone'

class KCMBIFieldReportAdmin(admin.ModelAdmin):
    list_display = ('team_leader', 'zone_info', 'kcmbi_number', 'meeting_date_time', 'class_topic_or_text', 'created_at')
    list_filter = ('meeting_date_time', 'team_leader')
    search_fields = ('team_leader', 'kcmbi_number', 'class_topic_or_text')
    readonly_fields = ('created_at', 'updated_at')
    list_per_page = 25
    def zone_info(self, obj):
        if obj.zone:
            return f"{obj.zone.zone_number}"
        return '-'
    zone_info.short_description = 'Zone'

admin.site.register(Zone, ZoneAdmin)
admin.site.register(PreacherPersonalInfo, PreacherPersonalInfoAdmin)
admin.site.register(TeamLeaderPersonalData, TeamLeaderPersonalDataAdmin)
admin.site.register(CongregationUpdate, CongregationUpdateAdmin)
admin.site.register(KCMBIFieldReport, KCMBIFieldReportAdmin)
