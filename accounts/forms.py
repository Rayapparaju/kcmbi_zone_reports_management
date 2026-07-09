from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile
from reports.models import PreacherPersonalInfo, TeamLeaderPersonalData, Zone

class AdminRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Username'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirm Password'})

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            UserProfile.objects.create(user=user, role='admin')
        return user

class PreacherRegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))
    name_of_preacher = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name as Preacher'}))
    team_leader_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Team Leader Name'}))
    zone = forms.ModelChoiceField(queryset=Zone.objects.none(), required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    cell_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cell Number'}))
    preacher_address = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Your Address'}))
    congregation_address = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Congregation Address'}))
    bank_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Bank Name'}))
    account_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Account Number'}))
    ifsc_code = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'IFSC Code'}))
    aadhar_card_photo = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))
    preacher_photo = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['zone'].queryset = Zone.objects.all()

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Username already taken')
        return username

    def clean(self):
        cd = super().clean()
        if cd.get('password') != cd.get('confirm_password'):
            raise forms.ValidationError('Passwords do not match')
        return cd

    def save(self):
        data = self.cleaned_data
        user = User.objects.create_user(
            username=data['username'],
            email=data['email'],
            password=data['password']
        )
        UserProfile.objects.create(user=user, role='preacher')
        team_leader = TeamLeaderPersonalData.objects.filter(
            name__iexact=data['team_leader_name']
        ).first()
        preacher = PreacherPersonalInfo.objects.create(
            user=user,
            name_of_preacher=data['name_of_preacher'],
            team_leader_name=data['team_leader_name'],
            team_leader_ref=team_leader,
            zone=data.get('zone'),
            cell_number=data['cell_number'],
            preacher_address=data['preacher_address'],
            congregation_address=data['congregation_address'],
            email_address=data['email'],
            bank_name=data['bank_name'],
            account_number=data['account_number'],
            ifsc_code=data['ifsc_code'],
            aadhar_card_photo=data['aadhar_card_photo'],
            preacher_photo=data['preacher_photo'],
        )
        return user, preacher

class TeamLeaderRegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}))
    address = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Address'}))
    cell_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cell Number'}))
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    bank_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Bank Name'}))
    account_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Account Number'}))
    ifsc_code = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'IFSC Code'}))
    number_of_kcmbis_submitting = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number of KCMBIs Submitting'}))
    aadhar_card_photo = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Username already taken')
        return username

    def clean(self):
        cd = super().clean()
        if cd.get('password') != cd.get('confirm_password'):
            raise forms.ValidationError('Passwords do not match')
        return cd

    def save(self):
        data = self.cleaned_data
        user = User.objects.create_user(
            username=data['username'],
            email=data['email'],
            password=data['password']
        )
        UserProfile.objects.create(user=user, role='team_leader')
        leader = TeamLeaderPersonalData.objects.create(
            user=user,
            name=data['name'],
            address=data['address'],
            email_address=data['email'],
            cell_number=data['cell_number'],
            date_of_birth=data['date_of_birth'],
            bank_name=data['bank_name'],
            account_number=data['account_number'],
            ifsc_code=data['ifsc_code'],
            number_of_kcmbis_submitting=data['number_of_kcmbis_submitting'],
            aadhar_card_photo=data['aadhar_card_photo'],
        )
        return user, leader
