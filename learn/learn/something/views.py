from django.shortcuts import render
import psycopg2


# Create your views here.

def home(request):
	items = [10,10,10,10]
	return render(request,'home.ht',{'items':items})

def two(request):
	conn = psycopg2.connect("dbname = 'learn' user ='postgres' host = '' password = 'sandeep'")
	cur = conn.cursor()
	cur.execute("""SELECT email FROM auth_user""")
	rows = cur.fetchall()
	return render(request,'2.ht',{'awesome':rows})