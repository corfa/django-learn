from django.contrib import admin
from .models import Contact, Group
class ContactAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'email', 'address')  
    search_fields = ('user__username', 'phone_number')  

class GroupAdmin(admin.ModelAdmin):
    list_display = ('name',)  
    filter_horizontal = ('contacts',)  

admin.site.register(Contact, ContactAdmin)
admin.site.register(Group, GroupAdmin)
