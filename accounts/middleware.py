from django.shortcuts import redirect
from django.contrib import messages


class PreacherApprovalMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = request.user
        if user.is_authenticated:
            role = getattr(user, 'profile', None).role if hasattr(user, 'profile') else None
            if role == 'preacher':
                preacher = getattr(user, 'preacher_profile', None)
                if preacher and not preacher.is_approved:
                    allowed_paths = ['/accounts/logout/', '/accounts/login/']
                    if request.path not in allowed_paths:
                        from django.contrib.auth import logout
                        logout(request)
                        messages.error(request, 'Your account is pending approval. Contact admin.')
                        return redirect('login')
        return self.get_response(request)
