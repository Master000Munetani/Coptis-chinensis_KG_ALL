from django.contrib import admin
from .models import MyNode
# Register your models here.

class MyNodeAdmin(admin.ModelAdmin):
    list_display = ["name", "leixing"]
    search_fields = ["name"]
    list_filter = ["leixing"]

admin.site.register(MyNode, MyNodeAdmin)
