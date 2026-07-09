from django.shortcuts import redirect
from django.contrib import messages

def role_required(allowed_roles):
    def decorator(view_func):
        def _wrapped(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect('login')
            profile = getattr(request.user, 'profile', None)
            if profile and profile.role in allowed_roles:
                return view_func(request, *args, **kwargs)
            messages.error(request, 'You do not have permission to access this page.')
            return redirect('dashboard')
        return _wrapped
    return decorator

def preacher_required(view_func):
    return role_required(['admin', 'preacher'])(view_func)

def teamleader_required(view_func):
    return role_required(['admin', 'team_leader'])(view_func)
