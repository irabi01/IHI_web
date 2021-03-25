from rest_framework import serializers
from .models import (
    Events,
    News,
    Staffs,
    Publications,
    Projects,
    InnovationHub,
    FunndingPartners,
    CollaboratingInstitutions,
    Jobs,
    Calls,
    Opportunity,
    CED,
    Blog,
    Governance,
    Spotlight,
    PolicyBriefs,
    AboutCovid19,
    Covid19Notice,
    Covid19Guidlines,
    Covid19HowToStaySafe,
    Covid19Stats
)



class AboutCovid19Serializer(serializers.ModelSerializer):
    class Meta:
        model = AboutCovid19
        fields = '__all__'


class Covid19NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Covid19Notice
        fields = '__all__'


class Covid19GuidlinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Covid19Guidlines
        fields = '__all__'


class Covid19HowToStaySafeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Covid19HowToStaySafe
        fields = '__all__'


class Covid19StatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Covid19Stats
        fields = '__all__'



class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'

class SpotlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spotlight
        fields = '__all__'


class PolicyBriefsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PolicyBriefs
        fields = '__all__'

class JobsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobs
        fields = '__all__'


class CallsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calls
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'


class OpportunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Opportunity
        fields = '__all__'

class GovernanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Governance
        fields = '__all__'


class CEDSerializer(serializers.ModelSerializer):
    class Meta:
        model = CED
        fields = '__all__'


class EventsLimitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'


class StaffsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staffs
        fields = '__all__'

# class StaffsLimitSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Staffs
#         fields = '__all__'

class PublicationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publications
        fields = '__all__'

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

class NewsLimitSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'

class ProjectsLimitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'

# start serializer_class for each department

class ProjectsEHSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'

class ProjectsICSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'

class ProjectsHSSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'

class ProjectsTCSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'

# end serializer_class for each department

# class InnovationHubSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = InnovationHub
#         fields = '__all__'

class FundingPartnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = FunndingPartners
        fields = '__all__'

class CollaboratingInstitutionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollaboratingInstitutions
        fields = '__all__'
