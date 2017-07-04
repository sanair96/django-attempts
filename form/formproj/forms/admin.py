from django.contrib import admin

# Register your models here.

from .models import form

class formAdmin(admin.ModelAdmin):
	list_display = ['name']
	class Meta:
		model = form	

admin.site.register(form, formAdmin)