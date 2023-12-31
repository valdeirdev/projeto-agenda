from django.contrib import admin
from contact import models

# Register your models here.
@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name',)

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone', 'category',)
    ordering = ('id',)
    search_fields = ('first_name', 'last_name',)
    list_per_page = 10
    list_max_show_all = 200
    list_display_links = ('first_name', 'last_name',)

