from django.urls import path, include
from . import views
from rest_framework import routers
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home_view, name = 'home_view'),
    path('publications/journals-paper/', views.journalPaper, name = 'journalPaper'),
    path('publications/policy-briefs/', views.policyBriefsPage, name = 'policyBriefsPage'),
    path('publications/spotlights/', views.spotlightsPage, name = 'spotlightsPage'),
    path('publications/spotlights/spotlight/<int:id>/details/', views.spotlightDetails, name = 'spotlightDetails'),
    path('contact-us/', views.contactPage, name = 'contactPage'),
    path('frequently-asked-questions/', views.faqsPage, name = 'faqsPage'),
    path('our-job-posts/', views.jobsPage, name = 'jobsPage'),
    path('our-partners/', views.partnerPage, name = 'partnerPage'),
    path('our-projects/', views.projectsPage, name = 'projectsPage'),
    path('our-projects/project/<int:id>/details/', views.projectDetails, name = 'projectDetails'),
    path('our-events/', views.eventsPage, name = 'eventsPage'),
    path('our-events/<int:id>/details/', views.eventDetails, name = 'eventDetails'),
    path('our-news/', views.newsPage, name = 'newsPage'),
    path('our-news/<int:id>/details/', views.newsDetails, name = 'newsDetails'),
    path('our-blog/', views.blogPage, name = 'blogPage'),
    path('our-blog/<int:id>/details/', views.blogDetails, name = 'blogDetails'),
    path('our-calls/', views.callsPage, name = 'callsPage'),
    path('our-history/', views.historyPage, name = 'historyPage'),
    path('our-opportunity/', views.announcementsPage, name = 'announcementsPage'),
    path('our-research/', views.researchPage, name = 'researchPage'),
    path('our-training/', views.trainingPage, name = 'trainingPage'),
    path('our-services/', views.servicePage, name = 'servicePage'),
    path('our-staff/', views.staffPage, name = 'staffPage'),
    path('who-we-are/', views.whowearePage, name = 'whowearePage'),
    path('our-governance/', views.governancePage, name = 'governancePage'),
    path('iso-9001:2015/', views.isoPage, name = 'isoPage'),
    path('research-platform/', views.researchPlatformPage, name = 'researchPlatformPage'),
    path('our-branches/', views.branchesPage, name = 'branchesPage'),
    path('ced-message/', views.cedPage, name = 'cedPage'),
    path('our-units-and-departments/', views.unitAndDepartmentPage, name = 'unitAndDepartmentPage'),
    path('our-staff/<int:id>/<str:first_name>/<str:last_name>/details/', views.staffDetails, name = 'staffDetails'),
    path('subscribe/', views.subscriptionFunction, name = 'subscriptionFunction'),
    path('vector-control-product-testing-unit/', views.vcptuPage, name = 'vcptuPage'),


]
