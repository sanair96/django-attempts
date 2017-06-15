from django.contrib import admin

# Register your models here.

from .models import form

class formAdmin(admin.ModelAdmin):
	list_display = ['name']
	class Meta:
		model = Store	

admin.site.register(form, formAdmin)