from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from reports.models import PreacherPersonalInfo, TeamLeaderPersonalData, CongregationUpdate, KCMBIFieldReport, Zone
from reports.forms import ZoneForm

@login_required
def dashboard_view(request):
    user = request.user
    role = getattr(user, 'profile', None).role if hasattr(user, 'profile') else 'admin'

    # Manual zone creation for team leader
    zone_form = None
    if role == 'team_leader':
        leader = getattr(user, 'teamleader_profile', None)
        if request.method == 'POST' and 'add_zone' in request.POST:
            zone_form = ZoneForm(request.POST)
            if leader:
                zone_form.fields['team_leader'].queryset = TeamLeaderPersonalData.objects.filter(id=leader.id)
            if zone_form.is_valid():
                zone = zone_form.save(commit=False)
                if leader:
                    zone.team_leader = leader
                zone.save()
                messages.success(request, f'Zone {zone.zone_number} created successfully!')
                return redirect('dashboard')
        else:
            zone_form = ZoneForm()
            if leader:
                zone_form.fields['team_leader'].queryset = TeamLeaderPersonalData.objects.filter(id=leader.id)
                zone_form.fields['team_leader'].initial = leader
                zone_form.fields['team_leader'].widget = forms.HiddenInput()

    if role == 'preacher':
        preacher = getattr(user, 'preacher_profile', None)
        total_preachers = 1
        total_leaders = 0
        preacher_zone = preacher.zone if preacher else None
        total_zones = 1 if preacher_zone else 0
        total_congregations = CongregationUpdate.objects.filter(preacher_ref=preacher).count() if preacher else 0
        total_field_reports = 0
        recent_preachers = PreacherPersonalInfo.objects.filter(user=user) if preacher else PreacherPersonalInfo.objects.none()
        recent_leaders = TeamLeaderPersonalData.objects.none()
        recent_zones = Zone.objects.filter(pk=preacher_zone.pk) if preacher_zone else Zone.objects.none()
        preacher_leader_name = preacher.team_leader_ref.name if preacher and preacher.team_leader_ref else ''
        recent_congregations = CongregationUpdate.objects.filter(preacher_ref=preacher).order_by('-created_at')[:5] if preacher else CongregationUpdate.objects.none()
        recent_field_reports = KCMBIFieldReport.objects.none()

    elif role == 'team_leader':
        leader = getattr(user, 'teamleader_profile', None)
        leader_name = leader.name if leader else user.username
        total_preachers = PreacherPersonalInfo.objects.filter(team_leader_ref=leader).count() if leader else 0
        total_leaders = 1
        total_zones = Zone.objects.filter(team_leader=leader).count() if leader else 0
        team_zones = Zone.objects.filter(team_leader=leader).values_list('id', flat=True) if leader else []
        total_congregations = CongregationUpdate.objects.filter(zone__id__in=team_zones).count() if leader else 0
        total_field_reports = KCMBIFieldReport.objects.filter(team_leader_ref=leader).count() if leader else 0
        recent_preachers = PreacherPersonalInfo.objects.filter(team_leader_ref=leader).order_by('-created_at')[:5] if leader else PreacherPersonalInfo.objects.none()
        recent_leaders = TeamLeaderPersonalData.objects.filter(user=user) if leader else TeamLeaderPersonalData.objects.none()
        recent_zones = Zone.objects.filter(team_leader=leader).order_by('zone_number')[:5] if leader else Zone.objects.none()
        recent_congregations = CongregationUpdate.objects.filter(zone__id__in=team_zones).order_by('-created_at')[:5] if leader else CongregationUpdate.objects.none()
        recent_field_reports = KCMBIFieldReport.objects.filter(team_leader_ref=leader).order_by('-created_at')[:5] if leader else KCMBIFieldReport.objects.none()
        zones_with_preachers = Zone.objects.filter(team_leader=leader).prefetch_related('preachers').order_by('zone_number') if leader else []

    else:
        total_preachers = PreacherPersonalInfo.objects.count()
        total_leaders = TeamLeaderPersonalData.objects.count()
        total_zones = Zone.objects.count()
        total_congregations = CongregationUpdate.objects.count()
        total_field_reports = KCMBIFieldReport.objects.count()
        recent_preachers = PreacherPersonalInfo.objects.order_by('-created_at')[:5]
        recent_leaders = TeamLeaderPersonalData.objects.order_by('-created_at')[:5]
        recent_zones = Zone.objects.order_by('zone_number')[:5]
        recent_congregations = CongregationUpdate.objects.order_by('-created_at')[:5]
        recent_field_reports = KCMBIFieldReport.objects.order_by('-created_at')[:5]

    context = {
        'role': role,
        'leader_name': leader_name if role == 'team_leader' else None,
        'preacher_leader_name': preacher_leader_name if role == 'preacher' else None,
        'preacher_zone': preacher_zone if role == 'preacher' else None,
        'total_preachers': total_preachers,
        'total_leaders': total_leaders,
        'total_zones': total_zones,
        'total_congregations': total_congregations,
        'total_field_reports': total_field_reports,
        'recent_preachers': recent_preachers,
        'recent_leaders': recent_leaders,
        'recent_zones': recent_zones,
        'recent_congregations': recent_congregations,
        'recent_field_reports': recent_field_reports,
        'zones_with_preachers': zones_with_preachers if role == 'team_leader' else [],
        'zone_form': zone_form,
    }
    return render(request, 'dashboard/dashboard.html', context)
