from django.contrib import admin

# Register your models here.

from application.models import user,book,contact
admin.site.register(user)
admin.site.register(book)
admin.site.register(contact)