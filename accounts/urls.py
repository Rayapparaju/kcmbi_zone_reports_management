from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/admin/', views.register_admin, name='register_admin'),
    path('register/preacher/', views.register_preacher, name='register_preacher'),
    path('register/teamleader/', views.register_teamleader, name='register_teamleader'),
    path('profile/', views.profile_view, name='profile'),
    path('autocomplete/team-leaders/', views.autocomplete_team_leaders, name='autocomplete_team_leaders'),
    path('autocomplete/zones-by-leader/', views.zones_by_team_leader, name='zones_by_team_leader'),
]
