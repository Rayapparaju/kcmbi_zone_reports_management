from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from reports.models import TeamLeaderPersonalData, Zone
from .forms import AdminRegisterForm, PreacherRegisterForm, TeamLeaderRegisterForm

def register_admin(request):
    if request.method == 'POST':
        form = AdminRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Admin registration successful!')
            return redirect('dashboard')
        messages.error(request, 'Registration failed. Please correct the errors.')
    else:
        form = AdminRegisterForm()
    return render(request, 'accounts/register_admin.html', {'form': form})

def register_preacher(request):
    if request.method == 'POST':
        form = PreacherRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user, preacher = form.save()
            login(request, user)
            messages.success(request, f'Preacher "{preacher.name_of_preacher}" registered successfully!')
            return redirect('dashboard')
        messages.error(request, 'Registration failed. Please correct the errors.')
    else:
        form = PreacherRegisterForm()
    return render(request, 'accounts/register_preacher.html', {'form': form})

def register_teamleader(request):
    if request.method == 'POST':
        form = TeamLeaderRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user, leader = form.save()
            login(request, user)
            messages.success(request, f'Team Leader "{leader.name}" registered successfully!')
            return redirect('dashboard')
        messages.error(request, 'Registration failed. Please correct the errors.')
    else:
        form = TeamLeaderRegisterForm()
    return render(request, 'accounts/register_teamleader.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            role = getattr(user, 'profile', None).role if hasattr(user, 'profile') else None
            if role == 'preacher':
                preacher = getattr(user, 'preacher_profile', None)
                if preacher and not preacher.is_approved:
                    if preacher.is_rejected:
                        messages.error(request, 'Your registration has been rejected. Contact admin.')
                    else:
                        messages.error(request, 'Your account is pending admin approval.')
                    return render(request, 'accounts/login.html')
            login(request, user)
            return redirect('dashboard')
        messages.error(request, 'Invalid username or password.')
    return render(request, 'accounts/login.html')

@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html')

def logout_view(request):
    logout(request)
    return redirect('home')


def autocomplete_team_leaders(request):
    term = request.GET.get('term', '')
    leaders = TeamLeaderPersonalData.objects.filter(name__icontains=term).values('id', 'name', 'cell_number', 'email_address')[:50]
    return JsonResponse(list(leaders), safe=False)


def zones_by_team_leader(request):
    leader_id = request.GET.get('leader_id')
    zones = Zone.objects.filter(team_leader_id=leader_id).values('id', 'zone_number', 'zone_name')
    return JsonResponse(list(zones), safe=False)
