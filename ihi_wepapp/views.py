from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets, permissions
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .filters import *
from django.db.models import Q

# from .forms import (
# EventForm, PublicationsForm, InnovationHubForm,
# StaffsForm, CollaboratingPartnersForm, NewsForm,
# FundingPartnersForm, JobForm, CEDForm, BlogForm, CallsForm, OpportunityForm
# )


from .models import *

#
# @login_required
# class home_view(request):
#     template_view = 'pages/dashboard.html'
#     return render(request, template_view, {})@login_required

# @login_required
def home_view(request):
    # if request.method == "POST":
    #     subscriptionFunction(request)
    #     return redirect('home_view')
    get_website_video = ""
    get_job = Jobs.objects.all().order_by('-id')[:3]
    get_events = Events.objects.all().order_by('-id')[:3]
    get_news = News.objects.all().order_by('-id')[:3]
    get_projects = Projects.objects.all().order_by('-id')[:3]
    try:
        get_website_video = SiteVideo.objects.latest('id')
    except Exception as e:
        print('************** Upload video to display on the page *****************')

    context = {
        'get_job': get_job,
        'get_events': get_events,
        'get_news': get_news,
        'get_projects': get_projects,
        'get_website_video': get_website_video
    }
    template_name = 'pages/home.html'
    return render(request, template_name, context)


def journalPaper(request):
    get_publications = Publications.objects.all().order_by('-published_date')
    get_events = Events.objects.all().order_by('-id')[:2]
    mypubfilter = PublicationFilter(request.GET, queryset = get_publications)
    get_publications = mypubfilter.qs
    context = {
        'get_publications': get_publications,
        'get_events': get_events,
        'mypubfilter': mypubfilter
    }
    template_name = 'pages/publications/journalpaper.html'
    return render(request, template_name, context)


def policyBriefsPage(request):
    get_policy_briefs = PolicyBriefs.objects.all().order_by('-id')
    context = {
        'get_policy_briefs': get_policy_briefs,
    }
    template_name = 'pages/publications/policybriefs.html'
    return render(request, template_name, context)

def spotlightsPage(request):
    get_spotlights = Spotlight.objects.all().order_by('-id')
    context = {
        'get_spotlights': get_spotlights,
    }
    template_name = 'pages/publications/spotlights.html'
    return render(request, template_name, context)


def spotlightDetails(request, id):
    get_single_spotlight = get_object_or_404(Spotlight, pk = id )
    context = {
        'get_single_spotlight': get_single_spotlight,
    }
    template_name = 'pages/publications/spotlightDetails.html'
    return render(request, template_name, context)


def contactPage(request):
    if request.method == "POST":
        get_email = request.POST.get('email')
        get_message = request.POST.get('message')
        contact_object = Contact(
            email = get_email,
            description = get_message
        )
        contact_object.save()
        messages.success(request, f'Thanks for contact us, we will contact you soon!')
        return redirect('contactPage')
    template_name = 'pages/contacts.html'
    return render(request, template_name, {})


def jobsPage(request):
    get_job = Jobs.objects.all().order_by('-id')
    context = {
        'get_job':get_job,
    }
    template_name = 'pages/noticeboard/jobs.html'
    return render(request, template_name, context)


def callsPage(request):
    get_calls = Calls.objects.all().order_by('-id')
    # get_events = Events.objects.all().order_by('-id')[:2]
    context = {
        'get_calls':get_calls,
        # 'get_events': get_events
    }
    template_name = 'pages/noticeboard/calls.html'
    return render(request, template_name, context)


def announcementsPage(request):
    get_opportunity = Opportunity.objects.all().order_by('-id')
    # get_events = Events.objects.all().order_by('-id')[:2]
    context = {
        'get_opportunity':get_opportunity,
        # 'get_events': get_events
    }
    template_name = 'pages/noticeboard/announcements.html'
    return render(request, template_name, context)


def partnerPage(request):
    get_partner = FunndingPartners.objects.all()
    get_partner_collaborating = CollaboratingInstitutions.objects.all()
    context = {
        'get_partner': get_partner,
        'get_partner_collaborating': get_partner_collaborating,
    }
    template_name = 'pages/partners.html'
    return render(request, template_name, context)


def projectsPage(request):
    get_projects = Projects.objects.all().order_by('-id')
    get_project_all_filter = ProjectsFilter(request.GET, queryset = get_projects)
    get_projects = get_project_all_filter.qs

    context = {
        'get_projects': get_projects,
        'get_project_all_filter': get_project_all_filter,
    }
    template_name = 'pages/projects.html'
    return render(request, template_name, context)


def projectDetails(request, id):
    get_single_project = get_object_or_404(Projects, pk = id)
    context = {
        'get_single_project': get_single_project
    }
    template_name = 'pages/projectDetails.html'
    return render(request, template_name, context)


def eventsPage(request):
    get_events = Events.objects.all().order_by('-id')
    get_calls = Calls.objects.all().order_by('-id')[:3]
    context = {
        'get_events':get_events,
        'get_calls':get_calls
    }
    template_name = 'pages/news/events.html'
    return render(request, template_name, context)


def eventDetails(request, id):
    get_single_event = get_object_or_404(Events, pk = id)
    context = {
        'get_single_event': get_single_event
    }
    template_name = 'pages/news/eventDetails.html'
    return render(request, template_name, context)


def newsPage(request):
    get_news = News.objects.all().order_by('-id')
    get_calls = Calls.objects.all().order_by('-id')[:3]
    context = {
        'get_news':get_news,
        'get_calls':get_calls
    }
    template_name = 'pages/news/news.html'
    return render(request, template_name, context)

def newsDetails(request, id):
    get_single_news = get_object_or_404(News, pk = id)
    context = {
        'get_single_news': get_single_news
    }
    template_name = 'pages/news/newsDetails.html'
    return render(request, template_name, context)


def blogPage(request):
    get_blog = Blog.objects.all().order_by('-id')
    get_calls = Calls.objects.all().order_by('-id')[:3]
    context = {
        'get_blog':get_blog,
        'get_calls':get_calls
    }
    template_name = 'pages/news/blog.html'
    return render(request, template_name, context)


def blogDetails(request, id):
    get_single_blog = get_object_or_404(Blog, pk = id)
    context = {
        'get_single_blog': get_single_blog
    }
    template_name = 'pages/news/blogDetails.html'
    return render(request, template_name, context)


def staffPage(request):
    get_staff = Staffs.objects.all().order_by('-id')
    # search = request.GET.get('q')
    # if search:
    #     get_staff = get_staff.filter(
    #         Q(first_name__icontains = search)
    #     )


    staff_filter = StaffFilter(request.GET, queryset = get_staff)
    # get_staff = staff_filter.qs

    paginator = Paginator(staff_filter.qs, 30)
    page = request.GET.get('page')
    total_staff = paginator.get_page(page)

    context = {
        'get_staff': total_staff,
        'staff_filter': staff_filter,
        # 'get_filter_staff': get_filter_staff
    }
    template_name = 'pages/about/staff.html'
    return render(request, template_name, context)


def staffDetails(request, id, first_name, last_name):
    get_single_staff = get_object_or_404(Staffs, pk = id)
    context = {
        'get_staff': get_single_staff
    }
    template_name = 'pages/about/staffDetails.html'
    return render(request, template_name, context)


def historyPage(request):
    template_name = 'pages/about/ourhistory.html'
    return render(request, template_name, {})


def whowearePage(request):
    template_name = 'pages/about/whoweare.html'
    return render(request, template_name, {})


def branchesPage(request):
    template_name = 'pages/about/branches.html'
    return render(request, template_name, {})


def unitAndDepartmentPage(request):
    template_name = 'pages/about/unitanddepartment.html'
    return render(request, template_name, {})


def researchPlatformPage(request):
    template_name = 'pages/about/researchplatform.html'
    return render(request, template_name, {})


def isoPage(request):
    template_name = 'pages/iso.html'
    return render(request, template_name, {})

def governancePage(request):
    get_bog = Governance.objects.filter(governance = 'BOG')
    get_bot = Governance.objects.filter(governance = 'BOT')
    get_sac = Governance.objects.filter(governance = 'SAC')
    get_farc = Governance.objects.filter(governance = 'FARC')
    get_mc = Governance.objects.filter(governance = 'MC')
    context = {
        'get_bog': get_bog,
        'get_bot': get_bot,
        'get_sac': get_sac,
        'get_farc': get_farc,
        'get_mc': get_mc,
    }
    template_name = 'pages/about/governance.html'
    return render(request, template_name, context)

def cedPage(request):
    get_ced = CED.objects.latest('id')
    context = {
        'get_ced': get_ced
    }
    template_name = 'pages/about/ced.html'
    return render(request, template_name, context)


def researchPage(request):
    template_name = 'pages/ourwork/research.html'
    return render(request, template_name, {})


def trainingPage(request):
    template_name = 'pages/ourwork/training.html'
    return render(request, template_name, {})


def servicePage(request):
    template_name = 'pages/ourwork/services.html'
    return render(request, template_name, {})


def faqsPage(request):
    get_faqs = FAQs.objects.all()
    content = {
        'faqs': get_faqs
    }
    print(content)
    template_name = 'pages/faqs.html'
    return render(request, template_name, content)


def subscriptionFunction(request):
    if request.method == "POST":
        get_email = request.POST.get('email_address')
        get_topic = request.POST.get('topic')
        subscribe_object = Subscription(
            email = get_email,
            topic = get_topic
        )
        subscribe_object.save()
        print(f'Thanks for subscribe in our website. You will receive updated { get_topic } from our website.')
        return redirect('subscriptionFunction')
    # context = {
    #     'email': get_email,
    #     'topic': get_topic
    # }
    template_name = 'pages/subscribe.html'
    return render(request, template_name, {})



def vcptuPage(request):
    template_name = 'pages/vcptu.html'
    return render(request, template_name, {})



# @login_required
# def staff_list_view(request):
#     get_staff = Staffs.objects.all().order_by('-id')
#     template_name = 'pages/staffList.html'
#     context = {
#         'staffs':get_staff,
#     }
#     return render(request, template_name, context)



# # @login_required
# # def project_list_view(request):
# #     get_project = Projects.objects.all().order_by('-id')
# #     template_name = 'pages/projectList.html'
# #     context = {
# #         'projects':get_project,
# #     }
# #     return render(request, template_name, context)


# @login_required
# def news_list_view(request):
#     get_news = News.objects.all().order_by('-id')
#     template_name = 'pages/newsList.html'
#     context = {
#         'allnews':get_news,
#     }
#     return render(request, template_name, context)


# @login_required
# def job_list_view(request):
#     get_job = Jobs.objects.all().order_by('-id')
#     template_name = 'pages/jobsList.html'
#     context = {
#         'alljob':get_job,
#     }
#     return render(request, template_name, context)



# @login_required
# def blog_list_view(request):
#     get_blog = Blog.objects.all().order_by('-id')
#     template_name = 'pages/blogList.html'
#     context = {
#         'blogs':get_blog,
#     }
#     return render(request, template_name, context)




# @login_required
# def calls_list_view(request):
#     get_calls = Calls.objects.all().order_by('-id')
#     template_name = 'pages/callsList.html'
#     context = {
#         'calls':get_calls,
#     }
#     return render(request, template_name, context)



# @login_required
# def opportunity_list_view(request):
#     get_opportunity = Opportunity.objects.all().order_by('-id')
#     template_name = 'pages/opportunityList.html'
#     context = {
#         'opportunities':get_opportunity,
#     }
#     return render(request, template_name, context)



# @login_required
# def ced_list_view(request):
#     get_ced = CED.objects.all().order_by('-id')
#     template_name = 'pages/cedList.html'
#     context = {
#         'ceds':get_ced,
#     }
#     return render(request, template_name, context)



# @login_required
# def event_list_view(request):
#     get_events = Events.objects.all().order_by('-id')
#     template_name = 'pages/eventList.html'
#     context = {
#         'allevents':get_events,
#     }
#     return render(request, template_name, context)


# @login_required
# def publication_list_view(request):
#     get_publications = Publications.objects.all().order_by('-published_date')
#     template_name = 'pages/publicationsList.html'
#     context = {
#         'allpublication':get_publications,
#     }
#     return render(request, template_name, context)


# @login_required
# def add_partner_view(request):
#     if request.method == 'POST':
#         form = FundingPartnersForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, f'New funding partner added successfully')
#             return redirect('add_partner_view')
#     else:
#         form = FundingPartnersForm()
#     context = {
#         'form':form
#     }
#     template_name = 'pages/addPartners.html'
#     return render(request, template_name, context)



# @login_required
# def add_collaborating_view(request):
#     if request.method == 'POST':
#         form = CollaboratingPartnersForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, f'New collaborating institutions added successfully')
#             return redirect('add_partner_view')
#     else:
#         form = CollaboratingPartnersForm()
#     context = {
#         'form':form
#     }
#     template_name = 'pages/addPartners.html'
#     return render(request, template_name, context)



# @login_required
# def add_staff(request):
#     if request.method == 'POST':
#         form = StaffsForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             messages.success(request, f'New staff added successfully')
#             return redirect('add_staff')
#     else:
#         form = StaffsForm()
#     context = {
#         'form':form
#     }
#     template_name = 'pages/addStaff.html'
#     return render(request, template_name, context)


# # @login_required
# # def add_projects(request):
# #     if request.method == 'POST':
# #         form = ProjectsForm(request.POST, request.FILES)
# #         if form.is_valid():
# #             form.save()
# #             messages.success(request, f'New project added successfully')
# #             return redirect('add_projects')
# #     else:
# #         form = ProjectsForm()
# #     context = {
# #         'form':form
# #     }
# #     template_name = 'pages/addproject.html'
# #     return render(request, template_name, context)




# @login_required
# def add_job(request):
#     if request.method == 'POST':
#         form = JobForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             messages.success(request, f'New job added successfully')
#             return redirect('add_job')
#     else:
#         form = JobForm()
#     context = {
#         'form':form
#     }
#     template_name = 'pages/addJob.html'
#     return render(request, template_name, context)



# @login_required
# def add_ced(request):
#     if request.method == 'POST':
#         form = CEDForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             messages.success(request, f'Chief Executive Director added successfully')
#             return redirect('add_ced')
#     else:
#         form = CEDForm()
#     context = {
#         'form':form
#     }
#     template_name = 'pages/addCED.html'
#     return render(request, template_name, context)



# @login_required
# def add_calls(request):
#     if request.method == 'POST':
#         form = CallsForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             messages.success(request, f'New call added successfully')
#             return redirect('add_calls')
#     else:
#         form = CallsForm()
#     context = {
#         'form':form
#     }
#     template_name = 'pages/addCalls.html'
#     return render(request, template_name, context)



# @login_required
# def add_blog(request):
#     if request.method == 'POST':
#         form = BlogForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             messages.success(request, f'New blog added successfully')
#             return redirect('add_blog')
#     else:
#         form = BlogForm()
#     context = {
#         'form':form
#     }
#     template_name = 'pages/addBlog.html'
#     return render(request, template_name, context)



# @login_required
# def add_opportunity(request):
#     if request.method == 'POST':
#         form = OpportunityForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             messages.success(request, f'New opportunity added successfully')
#             return redirect('add_opportunity')
#     else:
#         form = OpportunityForm()
#     context = {
#         'form':form
#     }
#     template_name = 'pages/addOpportunity.html'
#     return render(request, template_name, context)


# @login_required
# def add_publications(request):
#     if request.method == 'POST':
#         form = PublicationsForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, f'New publications added successfully')
#             return redirect('add_publications')
#     else:
#         form = PublicationsForm()
#     context = {
#         'form':form
#     }
#     template_name = 'pages/addPublications.html'
#     return render(request, template_name, context)


# @login_required
# def add_news(request):
#     if request.method == 'POST':
#         form = NewsForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             messages.success(request, f'New news added successfully')
#             return redirect('add_news')
#     else:
#         form = NewsForm()
#     context = {
#         'form':form
#     }
#     template_name = 'pages/addNews.html'
#     return render(request, template_name, context)


# @login_required
# def add_event(request):
#     if request.method == 'POST':
#         form = EventForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             messages.success(request, f'New event added successfully')
#             return redirect('add_event')
#     else:
#         form = EventForm()
#     context = {
#         'form':form
#     }
#     template_name = 'pages/addEvent.html'
#     return render(request, template_name, context)


# @login_required
# def delete_staff(request, id):
#     get_staff = Staffs.objects.get(pk = id)
#     get_staff.delete()
#     messages.success(request, f'staff deleted successfully')
#     return redirect('staff_list_view')




# @login_required
# def delete_job(request, id):
#     get_job = Jobs.objects.get(pk = id)
#     get_job.delete()
#     messages.success(request, f'Job deleted successfully')
#     return redirect('job_list_view')



# @login_required
# def delete_blog(request, id):
#     get_blog = Blog.objects.get(pk = id)
#     get_blog.delete()
#     messages.success(request, f'Blog deleted successfully')
#     return redirect('blog_list_view')



# @login_required
# def delete_calls(request, id):
#     get_call = Calls.objects.get(pk = id)
#     get_call.delete()
#     messages.success(request, f'Call deleted successfully')
#     return redirect('calls_list_view')



# @login_required
# def delete_opportunity(request, id):
#     get_opportunity = Opportunity.objects.get(pk = id)
#     get_opportunity.delete()
#     messages.success(request, f'Opportunity deleted successfully')
#     return redirect('opportunity_list_view')


# @login_required
# def delete_ced(request, id):
#     get_ced = CED.objects.get(pk = id)
#     get_ced.delete()
#     messages.success(request, f'CED deleted successfully')
#     return redirect('CED_list_view')



# # @login_required
# # def delete_project(request, id):
# #     get_project = Projects.objects.get(pk = id)
# #     get_project.delete()
# #     messages.success(request, f'project deleted successfully')
# #     return redirect('project_list_view')


# @login_required
# def delete_news(request, id):
#     get_news = News.objects.get(pk = id)
#     get_news.delete()
#     messages.success(request, f'news deleted successfully')
#     return redirect('news_list_view')


# @login_required
# def delete_event(request, id):
#     get_event = Events.objects.get(pk = id)
#     get_event.delete()
#     messages.success(request, f'event deleted successfully')
#     return redirect('event_list_view')



# @login_required
# def delete_publication(request, id):
#     get_publication = Publications.objects.get(pk = id)
#     get_publication.delete()
#     messages.success(request, f'publication deleted successfully')
#     return redirect('publication_list_view')


# @login_required
# def update_staff(request, id):
#     # get_staff = Staffs.objects.get(pk = id)
#     instance = get_object_or_404(Staffs, pk = id)
#     form = StaffsForm(request.POST or None, request.FILES or None, instance = instance)
#     if form.is_valid():
#         instance = form.save(commit = False)
#         instance.save()
#         messages.success(request, f'staff updated successfully')
#         return redirect('staff_list_view')
#     context = {
#         'form':form
#     }
#     template_name = 'pages/addStaff.html'
#     return render(request, template_name, context)


# # @login_required
# # def update_project(request, id):
# #     # get_staff = Staffs.objects.get(pk = id)
# #     instance = get_object_or_404(Projects, pk = id)
# #     form = ProjectsForm(request.POST or None, request.FILES or None, instance = instance)
# #     if form.is_valid():
# #         instance = form.save(commit = False)
# #         instance.save()
# #         messages.success(request, f'project updated successfully')
# #         return redirect('project_list_view')
# #     context = {
# #         'form':form
# #     }
# #     template_name = 'pages/addproject.html'
# #     return render(request, template_name, context)



# @login_required
# def update_job(request, id):
#     # get_staff = Staffs.objects.get(pk = id)
#     instance = get_object_or_404(Jobs, pk = id)
#     form = JobForm(request.POST or None, request.FILES or None, instance = instance)
#     if form.is_valid():
#         instance = form.save(commit = False)
#         instance.save()
#         messages.success(request, f'job updated successfully')
#         return redirect('job_list_view')
#     context = {
#         'form':form
#     }
#     template_name = 'pages/addJob.html'
#     return render(request, template_name, context)



# @login_required
# def update_blog(request, id):
#     # get_staff = Staffs.objects.get(pk = id)
#     instance = get_object_or_404(Blog, pk = id)
#     form = BlogForm(request.POST or None, request.FILES or None, instance = instance)
#     if form.is_valid():
#         instance = form.save(commit = False)
#         instance.save()
#         messages.success(request, f'Blog updated successfully')
#         return redirect('blog_list_view')
#     context = {
#         'form':form
#     }
#     template_name = 'pages/addBlog.html'
#     return render(request, template_name, context)




# @login_required
# def update_calls(request, id):
#     # get_staff = Staffs.objects.get(pk = id)
#     instance = get_object_or_404(Calls, pk = id)
#     form = CallsForm(request.POST or None, request.FILES or None, instance = instance)
#     if form.is_valid():
#         instance = form.save(commit = False)
#         instance.save()
#         messages.success(request, f'Call updated successfully')
#         return redirect('calls_list_view')
#     context = {
#         'form':form
#     }
#     template_name = 'pages/addCalls.html'
#     return render(request, template_name, context)



# @login_required
# def update_ced(request, id):
#     # get_staff = Staffs.objects.get(pk = id)
#     instance = get_object_or_404(CED, pk = id)
#     form = CEDForm(request.POST or None, request.FILES or None, instance = instance)
#     if form.is_valid():
#         instance = form.save(commit = False)
#         instance.save()
#         messages.success(request, f'CED updated successfully')
#         return redirect('ced_list_view')
#     context = {
#         'form':form
#     }
#     template_name = 'pages/addCED.html'
#     return render(request, template_name, context)



# @login_required
# def update_opportunity(request, id):
#     # get_staff = Staffs.objects.get(pk = id)
#     instance = get_object_or_404(Opportunity, pk = id)
#     form = OpportunityForm(request.POST or None, request.FILES or None, instance = instance)
#     if form.is_valid():
#         instance = form.save(commit = False)
#         instance.save()
#         messages.success(request, f'Opportunity updated successfully')
#         return redirect('opportunity_list_view')
#     context = {
#         'form':form
#     }
#     template_name = 'pages/addOpportunity.html'
#     return render(request, template_name, context)



# @login_required
# def update_publication(request, id):
#     # get_staff = Staffs.objects.get(pk = id)
#     instance = get_object_or_404(Publications, pk = id)
#     form = PublicationsForm(request.POST or None, instance = instance)
#     if form.is_valid():
#         instance = form.save(commit = False)
#         instance.save()
#         messages.success(request, f'publication updated successfully')
#         return redirect('publication_list_view')
#     context = {
#         'form':form
#     }
#     template_name = 'pages/addPublications.html'
#     return render(request, template_name, context)


# @login_required
# def update_news(request, id):
#     # get_staff = Staffs.objects.get(pk = id)
#     instance = get_object_or_404(News, pk = id)
#     form = NewsForm(request.POST or None, request.FILES or None, instance = instance)
#     if form.is_valid():
#         instance = form.save(commit = False)
#         instance.save()
#         messages.success(request, f'news updated successfully')
#         return redirect('news_list_view')
#     context = {
#         'form':form
#     }
#     template_name = 'pages/addNews.html'
#     return render(request, template_name, context)


# @login_required
# def update_event(request, id):
#     # get_staff = Staffs.objects.get(pk = id)
#     instance = get_object_or_404(Events, pk = id)
#     form = EventForm(request.POST or None, request.FILES or None, instance = instance)
#     if form.is_valid():
#         instance = form.save(commit = False)
#         instance.save()
#         messages.success(request, f'event updated successfully')
#         return redirect('event_list_view')
#     context = {
#         'form':form
#     }
#     template_name = 'pages/addEvent.html'
#     return render(request, template_name, context)
