from django.shortcuts import render

# Create your views here.
from django import forms

from django.forms import ModelForm
from .models import form

class modform(ModelForm):
	class Meta:
		model = form
		fields = '__all__' 

class Formula(forms.Form):
	name = forms.CharField(required=True, max_length = 30)
	contact_email = forms.EmailField(required=True)


def home(request):
	if request.method=='POST':
		resp = modform(request.POST)
		if resp.is_valid():
			resp.save()
			return render(request,'main.html',{'form':resp})
		return	render(request,'main.html',{'form':resp})

	else:
		forms = Formula()
		return render(request,'main.html',{'form' : forms})