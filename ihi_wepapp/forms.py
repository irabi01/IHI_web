# from django import forms
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm

# from .models import (
#     Events, Staffs,Jobs,
#     Publications, News, Blog, Calls, Opportunity,CED,
#     InnovationHub,
#     FunndingPartners,
#     CollaboratingInstitutions
# )


# class FundingPartnersForm(forms.ModelForm):
#     class Meta:
#         model = FunndingPartners
#         fields = ['fullname', 'link']


# class CollaboratingPartnersForm(forms.ModelForm):
#     class Meta:
#         model = CollaboratingInstitutions
#         fields = ['fullname', 'link']


# class StaffsForm(forms.ModelForm):
#     class Meta:
#         model = Staffs
#         fields = ['image', 'profile_image', 'first_name',
#             'last_name', 'headline', 'department1', 'department2', 'department3', 'department4',
#             'governance1','governance2','governance3', 'directorate', 'units', 'position', 'email',
#             'background_and_education',
#             'professional_experience_and_skills',
#             'description', 'publication_link']


# class NewsForm(forms.ModelForm):
#     class Meta:
#         model = News
#         fields = ['title', 'image', 'description','location', 'uploaded_date']

#         widgets = {
#             'uploaded_date': forms.DateInput(attrs={'type':'date'}),
#         }


# class EventForm(forms.ModelForm):
#     class Meta:
#         model = Events
#         fields = ['title', 'event_date',
#         'event_time', 'location',
#         'image', 'description']

#         widgets = {
#             'event_date': forms.DateInput(attrs={'type':'date'}),
#         }



# class JobForm(forms.ModelForm):
#     class Meta:
#         model = Jobs
#         fields = ['title', 'description',
#         'job_document']



# class CallsForm(forms.ModelForm):
#     class Meta:
#         model = Calls
#         fields = ['title', 'description',
#         'call_document']



# class OpportunityForm(forms.ModelForm):
#     class Meta:
#         model = Opportunity
#         fields = ['title', 'description',
#         'opportunity_document']



# class CEDForm(forms.ModelForm):
#     class Meta:
#         model = CED
#         fields = ['name','title', 'description','headline',
#         'image']


# class BlogForm(forms.ModelForm):
#     class Meta:
#         model = Blog
#         fields = ['title', 'uploaded_date', 'location', 'description',
#         'image']

#         widgets = {
#             'uploaded_date': forms.DateInput(attrs={'type':'date'}),
#         }



# class PublicationsForm(forms.ModelForm):
#     class Meta:
#         model = Publications
#         fields = ['published_date', 'title', 'journal_name',
#         'authors', 'website_link',
#         'abstract']

#         widgets = {
#             'published_date': forms.DateInput(attrs={'type':'date'}),
#         }



# class InnovationHubForm(forms.ModelForm):
#     class Meta:
#         model = InnovationHub
#         fields = ['title', 'image', 'description']


# class ProjectsForm(forms.ModelForm):
#     class Meta:
#         model = Projects
#         fields = ['title','project_leader', 'principal_investigator', 'administrator', 'funder', 'image', 'department', 'description', 'start_date', 'end_date', 'duration']
