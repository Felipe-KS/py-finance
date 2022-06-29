from django.contrib import admin

from .models import Tag, People, Method_Payment, Spent, Incoming
# Register your models here.
admin.site.register(Tag)
admin.site.register(People)
admin.site.register(Method_Payment)
admin.site.register(Spent)
admin.site.register(Incoming)