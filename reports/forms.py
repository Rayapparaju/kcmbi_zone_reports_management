from django import forms
from .models import PreacherPersonalInfo, TeamLeaderPersonalData, CongregationUpdate, KCMBIFieldReport, Zone

class ZoneForm(forms.ModelForm):
    class Meta:
        model = Zone
        fields = '__all__'
        widgets = {
            'zone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. ZN-001'}),
            'zone_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Zone Name'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Location'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Description'}),
        }

class PreacherPersonalInfoForm(forms.ModelForm):
    class Meta:
        model = PreacherPersonalInfo
        exclude = ('user', 'team_leader_ref', 'is_approved', 'is_rejected')
        widgets = {
            'name_of_preacher': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name of Preacher'}),
            'team_leader_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Team Leader Name'}),
            'cell_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cell Number'}),
            'preacher_address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Preacher Address'}),
            'congregation_address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Congregation Address'}),
            'email_address': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
            'bank_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Bank Name'}),
            'account_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Account Number'}),
            'ifsc_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'IFSC Code'}),
        }

class TeamLeaderPersonalDataForm(forms.ModelForm):
    class Meta:
        model = TeamLeaderPersonalData
        exclude = ('user',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Address'}),
            'email_address': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
            'cell_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cell Number'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'bank_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Bank Name'}),
            'account_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Account Number'}),
            'ifsc_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'IFSC Code'}),
            'number_of_kcmbis_submitting': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number of KCMBIs Submitting'}),
        }

class CongregationUpdateForm(forms.ModelForm):
    class Meta:
        model = CongregationUpdate
        exclude = ('preacher_ref',)
        widgets = {
            'name_of_preacher': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name of Preacher'}),
            'name_of_village': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name of Village'}),
            'month_of_reporting': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. January 2025'}),
            'bible_studies_meetings_count': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Bible Studies/Meetings Count'}),
            'baptisms_count': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Baptisms Count'}),
            'names_of_baptized_people': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Names of Baptized People'}),
            'church_members_count': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Church Members Count'}),
            'benevolent_aid_received': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Benevolent Aid Received'}),
            'average_weekly_giving': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Average Weekly Giving'}),
            'inspiring_stories': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Inspiring Stories'}),
        }

class KCMBIFieldReportForm(forms.ModelForm):
    class Meta:
        model = KCMBIFieldReport
        exclude = ('team_leader_ref',)
        widgets = {
            'team_leader': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Team Leader'}),
            'meeting_date_time': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'kcmbi_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'KCMBI Number'}),
            'class_topic_or_text': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Class Topic or Text'}),
            'meeting_address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Meeting Address'}),
            'preachers_in_attendance': forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'placeholder': '1. Preacher Name\n2. Preacher Name\n3. Preacher Name'}),
            'group_concerns': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Group Concerns'}),
        }

    def __init__(self, *args, **kwargs):
        team_leader = kwargs.pop('team_leader_obj', None)
        super().__init__(*args, **kwargs)
        if team_leader:
            self.fields['zone'].queryset = Zone.objects.filter(team_leader=team_leader)
            self.fields['zone'].empty_label = '-- Select Zone --'
