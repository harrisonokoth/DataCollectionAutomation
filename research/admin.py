from django.contrib import admin
from .models import PrivacyRisk, RegulatoryFramework, Evaluation

admin.site.register(PrivacyRisk)
admin.site.register(RegulatoryFramework)
admin.site.register(Evaluation)
