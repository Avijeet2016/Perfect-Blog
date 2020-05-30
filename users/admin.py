from django.contrib import admin
from .models import Profile, Contact, About


admin.site.register(Profile)

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_on']
    search_fields = ('name', 'email')

admin.site.register(Contact, ContactAdmin)

admin.site.register(About)