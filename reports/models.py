from django.db import models
from django.contrib.auth.models import User

class Zone(models.Model):
    team_leader = models.ForeignKey('TeamLeaderPersonalData', on_delete=models.CASCADE, related_name='zones')
    zone_number = models.CharField(max_length=50)
    zone_name = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['zone_number']

    def __str__(self):
        return f"Zone {self.zone_number} - {self.team_leader.name}"

class PreacherPersonalInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name='preacher_profile')
    name_of_preacher = models.CharField(max_length=255)
    team_leader_name = models.CharField(max_length=255)
    team_leader_ref = models.ForeignKey('TeamLeaderPersonalData', on_delete=models.SET_NULL, null=True, blank=True, related_name='preachers')
    zone = models.ForeignKey(Zone, on_delete=models.SET_NULL, null=True, blank=True, related_name='preachers')
    cell_number = models.CharField(max_length=20)
    preacher_address = models.TextField()
    congregation_address = models.TextField()
    email_address = models.EmailField()
    aadhar_card_photo = models.ImageField(upload_to='aadhar_photos/')
    bank_name = models.CharField(max_length=255)
    account_number = models.CharField(max_length=50)
    ifsc_code = models.CharField(max_length=20)
    preacher_photo = models.ImageField(upload_to='preacher_photos/')
    is_approved = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_of_preacher

class TeamLeaderPersonalData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name='teamleader_profile')
    name = models.CharField(max_length=255)
    address = models.TextField()
    email_address = models.EmailField()
    cell_number = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    bank_name = models.CharField(max_length=255)
    account_number = models.CharField(max_length=50)
    ifsc_code = models.CharField(max_length=20)
    aadhar_card_photo = models.ImageField(upload_to='leader_aadhar/')
    number_of_kcmbis_submitting = models.IntegerField(default=0)
    team_leader_photo = models.ImageField(upload_to='leader_photos/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class CongregationUpdate(models.Model):
    name_of_preacher = models.CharField(max_length=255)
    preacher_ref = models.ForeignKey('PreacherPersonalInfo', on_delete=models.SET_NULL, null=True, blank=True, related_name='congregation_updates')
    zone = models.ForeignKey(Zone, on_delete=models.SET_NULL, null=True, blank=True, related_name='congregation_updates')
    name_of_village = models.CharField(max_length=255)
    month_of_reporting = models.CharField(max_length=50)
    bible_studies_meetings_count = models.IntegerField(default=0)
    baptisms_count = models.IntegerField(default=0)
    names_of_baptized_people = models.TextField(blank=True)
    church_members_count = models.IntegerField(default=0)
    benevolent_aid_received = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    average_weekly_giving = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    church_photo = models.ImageField(upload_to='church_photos/')
    other_photo = models.ImageField(upload_to='other_photos/', blank=True)
    inspiring_stories = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name_of_preacher} - {self.name_of_village}"

class KCMBIFieldReport(models.Model):
    team_leader = models.CharField(max_length=255)
    team_leader_ref = models.ForeignKey('TeamLeaderPersonalData', on_delete=models.SET_NULL, null=True, blank=True, related_name='field_reports')
    zone = models.ForeignKey(Zone, on_delete=models.SET_NULL, null=True, blank=True, related_name='field_reports')
    meeting_date_time = models.DateTimeField()
    kcmbi_number = models.CharField(max_length=50)
    class_topic_or_text = models.CharField(max_length=255)
    meeting_address = models.TextField()
    preachers_in_attendance = models.TextField(blank=True)
    meeting_photo = models.ImageField(upload_to='meeting_photos/')
    group_concerns = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.team_leader} - {self.kcmbi_number}"
