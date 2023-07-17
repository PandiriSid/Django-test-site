from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection

def home(request):
    return render(request, 'home.html')

def form(request):
    # if request.method == POST :
    #     form = MyForm()
    # else:
    #     form = MyForm()
    return render(request, 'form_template.html')

def submit_details(request):
    if request.method == 'POST' :
        
        form_data = request.POST
        first_name = form_data['first_name']
        last_name = form_data['last_name']
        age = int(form_data['age'])
        gender = form_data['gender']
        if gender =='male':
            gender = 'M'
        else:
            gender='F'
        birth_place = form_data['birth_place']
        # birth_place = request.POST.get('birth_place')
        department = form_data['department']
        print("All the details submitted are: ", first_name, last_name, age, gender, birth_place, department)
        print(age, type(age))
        cursor = connection.cursor()
        raw_query = """ insert into dbo.Faculty values( %s, %s,%s, %s,%s ,%s) """
        values = (first_name, last_name, age, gender, birth_place, department)
        cursor.execute(raw_query,values)
        return render(request, "successful.html")
    
def view_faculty(request):
    if request.method!='POST':
        return render(request, 'view_template.html')
    if request.method=='POST':
        if 'submit_button1' in request.POST:
            form_data = request.POST
            cursor = connection.cursor()
            raw_query = """ select * from dbo.Faculty where first_name = %s"""
            value = (form_data.get('first_name'),)
            print(value)
            details = cursor.execute(raw_query,value)
            return render(request, "view_template.html", {'details1':details})
        elif 'submit_button2' in request.POST:
            cursor = connection.cursor()
            query = """ select * from dbo.Faculty"""
            details = cursor.execute(query)
            print(details)
            return render(request, "view_template.html",{'details2':details})
        
def submitted(request):
    if request.method=='POST':

        if 'go_to_home' in request.POST:
            return render(request, "home.html")

        if 'insert_more' in request.POST:
            return render(request, "form_template.html")