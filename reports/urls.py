from django.urls import path
from . import views

urlpatterns = [
    # Preacher
    path('preachers/', views.preacher_list, name='preacher_list'),
    path('preachers/add/', views.preacher_add, name='preacher_add'),
    path('preachers/<int:pk>/', views.preacher_detail, name='preacher_detail'),
    path('preachers/<int:pk>/edit/', views.preacher_edit, name='preacher_edit'),
    path('preachers/<int:pk>/delete/', views.preacher_delete, name='preacher_delete'),
    path('preachers/<int:pk>/pdf/', views.preacher_pdf, name='preacher_pdf'),
    path('preachers/<int:pk>/approve/', views.approve_preacher, name='approve_preacher'),
    path('preachers/<int:pk>/reject/', views.reject_preacher, name='reject_preacher'),
    # Team Leader
    path('teamleaders/', views.teamleader_list, name='teamleader_list'),
    path('teamleaders/add/', views.teamleader_add, name='teamleader_add'),
    path('teamleaders/<int:pk>/', views.teamleader_detail, name='teamleader_detail'),
    path('teamleaders/<int:pk>/edit/', views.teamleader_edit, name='teamleader_edit'),
    path('teamleaders/<int:pk>/delete/', views.teamleader_delete, name='teamleader_delete'),
    path('teamleaders/<int:pk>/pdf/', views.teamleader_pdf, name='teamleader_pdf'),
    path('teamleaders/export-excel/', views.export_teamleaders_excel, name='export_teamleaders_excel'),
    # Congregation
    path('congregations/', views.congregation_list, name='congregation_list'),
    path('congregations/add/', views.congregation_add, name='congregation_add'),
    path('congregations/<int:pk>/', views.congregation_detail, name='congregation_detail'),
    path('congregations/<int:pk>/edit/', views.congregation_edit, name='congregation_edit'),
    path('congregations/<int:pk>/delete/', views.congregation_delete, name='congregation_delete'),
    path('congregations/<int:pk>/pdf/', views.congregation_pdf, name='congregation_pdf'),
    path('congregations/export-excel/', views.export_congregations_excel, name='export_congregations_excel'),
    # Field Report
    path('fieldreports/', views.fieldreport_list, name='fieldreport_list'),
    path('fieldreports/add/', views.fieldreport_add, name='fieldreport_add'),
    path('fieldreports/<int:pk>/', views.fieldreport_detail, name='fieldreport_detail'),
    path('fieldreports/<int:pk>/edit/', views.fieldreport_edit, name='fieldreport_edit'),
    path('fieldreports/<int:pk>/delete/', views.fieldreport_delete, name='fieldreport_delete'),
    path('fieldreports/<int:pk>/pdf/', views.fieldreport_pdf, name='fieldreport_pdf'),
    path('fieldreports/export-excel/', views.export_fieldreports_excel, name='export_fieldreports_excel'),
    # Zone
    path('zones/', views.zone_list, name='zone_list'),
    path('zones/add/', views.zone_add, name='zone_add'),
    path('zones/<int:pk>/', views.zone_detail, name='zone_detail'),
    path('zones/<int:pk>/edit/', views.zone_edit, name='zone_edit'),
    path('zones/<int:pk>/delete/', views.zone_delete, name='zone_delete'),
    path('zones/<int:pk>/pdf/', views.zone_pdf, name='zone_pdf'),
    path('zones/export-excel/', views.zone_preachers_excel, name='zone_preachers_excel'),
    path('zones/export-zones-excel/', views.export_zones_excel, name='export_zones_excel'),
    path('autocomplete/preachers/', views.autocomplete_preachers, name='autocomplete_preachers'),
]
