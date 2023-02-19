from django.contrib import admin
from property.models import Flat


class AuthorAdmin(admin.ModelAdmin):
    search_fields = ('town','address', 'owner')
    readonly_fields = ["created_at"]

admin.site.register(Flat, AuthorAdmin) 