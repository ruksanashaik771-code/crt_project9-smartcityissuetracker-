from django.contrib import admin
from .models import Issue,Notification
admin.site.register(Notification)

@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'category',
        'status',
        'location',
        'created_at'
    )

    list_filter = (
        'status',
        'category'
    )

    search_fields = (
        'title',
        'location'
    )


