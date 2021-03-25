from django.contrib import admin
from .models import *
# Register your models here.
#
#
#

@admin.register(News)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title','id','date','location')
admin.site.register(Events)
admin.site.register(Publications)
admin.site.register(Projects)
admin.site.register(Governance)
admin.site.register(Staffs)
# admin.site.register(News)
admin.site.register(InnovationHub)
admin.site.register(FunndingPartners)
admin.site.register(CollaboratingInstitutions)
admin.site.register(Calls)
admin.site.register(Jobs)
admin.site.register(Opportunity)
admin.site.register(CED)
admin.site.register(Blog)
admin.site.register(Spotlight)
admin.site.register(PolicyBriefs)
admin.site.register(AboutCovid19)
admin.site.register(Covid19Notice)
admin.site.register(Covid19Guidlines)
admin.site.register(Covid19HowToStaySafe)
admin.site.register(Covid19Stats)
admin.site.register(FAQs)
admin.site.register(Contact)
admin.site.register(SiteVideo)
admin.site.register(Subscription)
