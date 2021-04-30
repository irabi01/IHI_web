from django.db import models
import datetime
from datetime import datetime
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify
import uuid

# Create your models here.
class Events(models.Model):
    title = models.CharField(max_length = 500)
    caption = models.CharField(max_length = 500)
    event_date = models.DateField()
    event_time = models.CharField(max_length = 20)
    uploaded_date = models.DateTimeField(auto_now_add =True)
    location = models.CharField(max_length = 50, default ='Morogoro')
    image = models.FileField(default='settings.MEDIA_ROOT/logos/anonymous.jpg')
    description = RichTextField()
    class Meta:
        verbose_name_plural = "Events"
    def __str__(self):
        return self.title

class Staffs(models.Model):
    department_list_one = (
        ('','select department'),('EH','Environmental Health and Ecological Sciences'),
        ('IC','Interventions and Clinical Trials'),('HS','Health Systems, Impact Evaluation and Policy'),
        ('TC','Training & Capacity Building')
    )

    department_list_two = (
        ('','select department'),('EH','Environmental Health and Ecological Sciences'),
        ('IC','Interventions and Clinical Trials'),('HS','Health Systems, Impact Evaluation and Policy'),
        ('TC','Training & Capacity Building')
    )

    department_list_three = (
        ('','select department'),('EH','Environmental Health and Ecological Sciences'),
        ('IC','Interventions and Clinical Trials'),('HS','Health Systems, Impact Evaluation and Policy'),
        ('TC','Training & Capacity Building')
    )

    department_list_four = (
        ('','select department'),('EH','Environmental Health and Ecological Sciences'),
        ('IC','Interventions and Clinical Trials'),('HS','Health Systems, Impact Evaluation and Policy'),
        ('TC','Training & Capacity Building')
    )

    directorate_list = (
        ('','select directorate'),('RQA','Research Quality Assurance'),
        ('IRB','Institutional Review Board'),('KMC','Knowledge Management and Communications')
    )

    units_list = (
        ('','select units'),('IA','Internal Audit'),
        ('FM','Finance Management'),('HRM','Human Resources Management'),
        ('PM','Procurement Management'),('BA','Branch Administration'),
        ('ICT','ICT unit'),('GC','Grants and Contracts'),
        ('TCB','Training and Capacity Building'),('LAB','Laboratories'),
        ('DSP','Data Systems and Platforms'),('CT','Clinical Trials'),
        ('CDCIM','Chronic Diseases Clinic in Ifakara and Mwananyamala'),
        ('TRANSPORT','Transport'),
        ('IH','Ifakara Hub')
    )


    image = models.FileField(default='settings.MEDIA_ROOT/logos/anonymous.jpg')
    profile_image = models.FileField(default='settings.MEDIA_ROOT/logos/anonymous.jpg')
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    headline = models.CharField(max_length = 1000, default="")
    environmental_department = models.CharField(max_length = 50, default = "select department", choices = department_list_one, blank = True)
    intervention_department = models.CharField(max_length = 50, default = "select department", choices = department_list_two, blank = True)
    health_department = models.CharField(max_length = 50, default = "select department", choices = department_list_three, blank = True)
    directorate = models.CharField(max_length = 50, default = "select directorate", choices = directorate_list, blank = True)
    units = models.CharField(max_length = 50, default = "select units", choices = units_list, blank = True)
    position = models.CharField(max_length = 50)
    email = models.EmailField(default="", max_length = 100)
    background_and_education = RichTextField()
    professional_experience_and_skills = RichTextField()
    description = RichTextField()
    publication_link = models.URLField(blank = True)
    class Meta:
        verbose_name_plural = "Staffs"
    def __str__(self):
        return self.first_name +" - "+ self.last_name

class Projects(models.Model):
    department_list = (
        ('','select department'),('EH','Environmental Health and Ecological Sciences'),
        ('IC','Interventions and Clinical Trials'),('HS','Health Systems, Impact Evaluation and Policy'),
        ('TC','Training & Capacity Building')
    )
    title = models.CharField(max_length = 500)
    project_leader = models.CharField(max_length = 100, blank = True)
    principal_investigator = models.CharField(max_length = 100, blank = True)
    administrator = models.CharField(max_length = 100, blank = True)
    funding_partner = models.CharField(max_length = 200, blank = True)
    start_date = models.DateField()
    end_date = models.DateField()
    uploaded_date = models.DateTimeField(auto_now_add =True)
    department = models.CharField(max_length = 50, choices = department_list)
    image = models.FileField(default='settings.MEDIA_ROOT/logos/anonymous.jpg')
    description = RichTextUploadingField()
    class Meta:
        verbose_name_plural = "Projects"
    def __str__(self):
        return self.title

class Governance(models.Model):
    governance_list = (
        ('','select governance'),('BOG','Board of Governors'),
        ('BOT','Board of Trustees'),('MC','Management Committee'),
        ('SAC','Scientific Advisory Committee'),('FARC','Finance, Audit and Risk Committee'),
        )
    image = models.FileField(default='settings.MEDIA_ROOT/logos/anonymous.jpg')
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    position = models.CharField(max_length = 100, default = "Director")
    headline = models.CharField(max_length = 1000, default="")
    governance = models.CharField(max_length = 50, choices = governance_list, default = 'MC')
    email = models.EmailField(default="", max_length = 100)
    description = RichTextField()
    publication_link = models.URLField(blank = True)
    class Meta:
        verbose_name_plural = "Governance"
    def __str__(self):
        return self.first_name +" - "+ self.last_name

class News(models.Model):
    title = models.CharField(max_length = 500)
    caption = models.CharField(max_length = 500)
    date = models.DateField()
    location = models.CharField(max_length = 50, default ='Morogoro')
    image = models.FileField(default='settings.MEDIA_ROOT/logos/anonymous.jpg')
    video_file = models.URLField(blank = True, null = True)
    description = RichTextField()


    class Meta:
        verbose_name_plural = "News"

    def __str__(self):
        return self.title


class Spotlight(models.Model):
    headline = models.CharField(max_length = 500)
    description = RichTextField()
    pdf_document = models.FileField()
    photo = models.FileField(default='settings.MEDIA_ROOT/logos/anonymous.jpg')
    class Meta:
        verbose_name_plural = "Spotlights"
    def __str__(self):
        return self.headline

class PolicyBriefs(models.Model):
    headline = models.CharField(max_length = 500)
    description = RichTextField()
    pdf_document = models.FileField()
    photo = models.FileField(default='settings.MEDIA_ROOT/logos/anonymous.jpg')
    class Meta:
        verbose_name_plural = "Policy Briefs"
    def __str__(self):
        return self.headline


class Blog(models.Model):
    title = models.CharField(max_length = 500)
    uploaded_date = models.DateField()
    location = models.CharField(max_length = 50, default ='Morogoro')
    image = models.FileField(default='settings.MEDIA_ROOT/logos/anonymous.jpg')
    description = RichTextField()
    class Meta:
        verbose_name_plural = "Blogs"
    def __str__(self):
        return self.title

class Jobs(models.Model):
    title = models.CharField(max_length = 200)
    description = RichTextField()
    job_document = models.FileField()
    uploaded_date = models.DateTimeField(blank = True, null = True)
    def snippet(self):
        return self.description[: 100]+ '...'
    class Meta:
        verbose_name_plural = "Jobs"
    def __str__(self):
        return self.title

class Calls(models.Model):
    title = models.CharField(max_length = 200)
    description = RichTextField()
    call_document = models.FileField()
    class Meta:
        verbose_name_plural = "Calls"
    def __str__(self):
        return self.title

class Opportunity(models.Model):
    title = models.CharField(max_length = 200)
    description = RichTextField()
    opportunity_document = models.FileField()
    class Meta:
        verbose_name_plural = "Opportunity"
    def __str__(self):
        return self.title

class CED(models.Model):
    name = models.CharField(max_length = 50)
    title = models.CharField(max_length = 200)
    description = RichTextField()
    left_description = RichTextField()
    headline = models.CharField(max_length = 200)
    left_headline = models.CharField(max_length = 200)
    image = models.FileField(default='settings.MEDIA_ROOT/logos/anonymous.jpg')
    document = models.FileField(default='settings.MEDIA_ROOT/logos/anonymous.jpg')
    left_link = models.URLField(blank = True)
    class Meta:
        verbose_name_plural = "Chief Executive Director"
    def __str__(self):
        return self.title


class Publications(models.Model):
    published_date = models.DateField(blank=True)
    title = models.CharField(max_length = 500)
    journal_name= models.CharField(max_length = 100)
    authors = models.CharField(max_length = 1000, default = "")
    website_link = models.CharField(max_length = 200)
    abstract = RichTextField()
    class Meta:
        verbose_name_plural = "Publications"
    def __str__(self):
        return self.title

class InnovationHub(models.Model):
    title = models.CharField(max_length = 500)
    uploaded_date = models.DateTimeField(auto_now_add =True)
    description = RichTextField()
    image = models.FileField(default='settings.MEDIA_ROOT/logos/anonymous.jpg')
    class Meta:
        verbose_name_plural = "Innovation-hub"
    def __str__(self):
        return self.title


class FunndingPartners(models.Model):
    fullname = models.CharField(max_length = 200)
    link = models.URLField()
    class Meta:
        verbose_name_plural = "Funnding Partners"
    def __str__(self):
        return self.fullname


class CollaboratingInstitutions(models.Model):
    fullname = models.CharField(max_length = 200)
    link = models.URLField()
    class Meta:
        verbose_name_plural = "Collaborating Institutions"
    def __str__(self):
        return self.fullname



class AboutCovid19(models.Model):
    title = models.CharField(max_length = 500)
    about_covid_19 = RichTextField()
    class Meta:
        verbose_name_plural = "About COVID-19"
    def __str__(self):
        return self.title


class Covid19Notice(models.Model):
    title = models.CharField(max_length = 500)
    covid_19Notice = RichTextField()
    class Meta:
        verbose_name_plural = "COVID-19 notice"
    def __str__(self):
        return self.title


class Covid19Guidlines(models.Model):
    title = models.CharField(max_length = 500)
    covid_19Guidlines = RichTextField()
    class Meta:
        verbose_name_plural = "COVID-19 Guidlines"
    def __str__(self):
        return self.title


class Covid19HowToStaySafe(models.Model):
    title = models.CharField(max_length = 500)
    covid_19HowToStaySafe = RichTextField()
    class Meta:
        verbose_name_plural = "COVID-19 How to stay safe"
    def __str__(self):
        return self.title


class Covid19Stats(models.Model):
    title = models.CharField(max_length = 500)
    covid_19Stats= RichTextUploadingField()
    class Meta:
        verbose_name_plural = "COVID-19 Stats"
    def __str__(self):
        return self.title


class FAQs(models.Model):
    title = models.CharField(max_length = 200)
    description= RichTextField()
    class Meta:
        verbose_name_plural = "FAQs"
    def __str__(self):
        return self.title

class Contact(models.Model):
    email = models.EmailField()
    description= RichTextField()
    class Meta:
        verbose_name_plural = "Customer contact "
    def __str__(self):
        return self.email


class Subscription(models.Model):
    email = models.EmailField()
    topic= models.CharField(max_length = 100)
    status = models.BooleanField(default = True)
    class Meta:
        verbose_name_plural = "Subscriber "
    def __str__(self):
        return self.email


class SiteVideo(models.Model):
    video_file = models.FileField()
    class Meta:
        verbose_name_plural = "Website video "
