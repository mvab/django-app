from django.contrib import admin
from .models import Page

class PageAdmin(admin.ModelAdmin):
    list_display = ("title", "update_date") # what field to show in the tables column at the pages list
    ordering = ("title",) # sort by
    search_fields = ("title",) # search by




# Register your models here.
admin.site.register(Page, PageAdmin)
