from django.contrib import admin
from core import models


@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'rating', 'summary', 'company', 'reviewer',
                    'submission_date')
    search_fields = ('title', 'summary')
    list_filter = ('company', 'reviewer', 'submission_date')


@admin.register(models.Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )
