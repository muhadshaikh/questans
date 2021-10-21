from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import Question, Student, Teacher
from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import Count, Sum, Max, Min, Avg
from django.contrib.auth.forms import UserCreationForm
import re
# from django import forms
# from .forms import RegisterForm
# from .modelss import Register
# Create your views here.


def student(request):
    Student_date = Student.objects.all()
    #Student_date= Student.objects.filter(marks=70)
    #Student_date= Student.objects.exclude(marks=70)
    #Student_date= Student.objects.order_by('city')
    #Student_date= Student.objects.order_by('-marks')
    #Student_date= Student.objects.order_by('city')
    #Student_date= Student.objects.order_by('id').reverse()
    #Student_date= Student.objects.order_by('id').reverse()[:5]
    #Student_date= Student.objects.values('name','city')
    #Student_date= Student.objects.values_list('id', 'name', named=True)
    #Student_date= Student.objects.using('default')
    #Student_date= Student.objects.order_by('id').reverse()
    # Student_date= Student.objects.dates('pass_data', 'year')

    # union
    # qs1 = Student.objects.values_list('id', 'name', named=True)
    # qs2 = Teacher.objects.values_list('id', 'name', named=True)
    # Student_date = qs2.union(qs1)

    # intersection
    # qs1 = Student.objects.values_list('id', 'name', named=True)
    # qs2 = Teacher.objects.values_list('id', 'name', named=True)
    # Student_date = qs2.intersection(qs1)

    # deffrence
    # qs1 = Student.objects.values_list('id', 'name', named=True)
    # qs2 = Teacher.objects.values_list('id', 'name', named=True)
    # Student_date = qs1.difference(qs2)

    # And
    #Student_date = Student.objects.filter(id=6) & Student.objects.filter(roll=106)

    # OR
    # Student_date = Student.objects.filter(id=6) | Student.objects.filter(roll=107)
    # print("Return", Student_date)
    # print()
    # print("SQL Query", Student_date.query)
    # return render(request, 'student.html', {'students':Student_date})

    # get
    # student_data = Student.objects.get(pk=1)

    # first
    # student_data = Student.objects.first()

    #student_data = Student.objects.last()

    # student_data = Student.objects.latest('pass_data')

    # student_data = Student.objects.earliest('pass_data')

    # Student_date = Student.objects.filter(name__istartswith='s')
    # Student_date = Student.objects.filter(roll__isnull=False)
    # Student_date = Student.objects.all().aggregate(Sum('marks'))
    # print("Return", Student_date)
    # print()

    # Student_date = Student.objects.all().aggregate(Max('marks'))
    # print("Return", Student_date)
    # print()

    # Student_date = Student.objects.all().aggregate(Min('marks'))
    print("Return", Student_date)
    print()

    print(Student_date.query)
    return render(request, 'student.html', {'students': Student_date})


def home(request):
    if 'q' in request.GET:
        q = request.GET['q']
        # quests=Question.objects.filter(title__icontains=q).order_by('id')
        # quests=Question.objects.filter(title__icontains=q).name__startswith=('A')
        # quests=Question.objects.filter(title__icontains=q).none()
        # quests=Question.objects.filter(title__icontains=q)
        # quests=Question.objects.order_by('title')
        quests = Question.objects.filter(title__icontains=q).order_by('id')
        print('quest', quests)
    else:
        quests = Question.objects.all().order_by('id')
    paginator = Paginator(quests, 3)
    page_num = request.GET.get('page', 1)
    quests = paginator.page(page_num)
    return render(request, 'home.html', {'quests': quests})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def Register(request):
    # print("we have passed.......", bool(re.match('^(?=.*[0-9]$)(?=.*[a-zA-Z])', '@hasAlphanum123')))
    # print("0000000.....", bool(re.match('^(?=.*[0-9]$)(?=.*[a-zA-Z])', 'muhad')))
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        print("we have passed.......", password1)
        print("we have passed.......", bool(
            re.match('^(?=.*[0-9]$)(?=.*[a-zA-Z])', password1)))
        # if first_name is None:
            # messages.info(request, 'first name should not be empty')
            # return redirect('register')
        # elif last_name is None:
        #     messages.info(request, 'last name should not be empty')
        #     return redirect('register')
        # elif email is None:
        #     messages.info(request, 'email should not be empty')
        #     return redirect('register')
        # elif username is None:
        #     messages.info(request, 'username should not be empty')
        #     return redirect('register')
        # elif password1 is None:
        #     messages.info(request, 'password should not be empty')
        #     return redirect('register')
        if first_name == '':
            messages.info(request, 'first name should not be empty')
            return redirect('register')
        elif last_name == '':
            messages.info(request, 'last name should not be empty')
            return redirect('register')
        elif email == '':
            messages.info(request, 'email should not be empty')
            return redirect('register')
        elif username == '':
            messages.info(request, 'username should not be empty')
            return redirect('register')
        elif password1 =='':
            messages.info(request, 'password should not be empty')
            return redirect('register')
        elif password2 == '':
            messages.info(request, 'password should not be empty')
            return redirect('register')

        if first_name == '0-9':
            print("insideif..............", )
        elif len(first_name) < 4:
            messages.info(request, 'first Name must be  4 char long or more')
            return redirect('register')
        else:
            messages.info(request, 'first Name must be  in character field')
            return redirect('register')
        
        if last_name == '0-9':
            print("insideif.....")
        elif len(last_name) < 4:
            messages.info(request, 'last Name must be  4 char long or more')
            return redirect('register')
        else:
            messages.info(request, 'last Name must be  in character field')
            return redirect('register')


        if re.match('^(?=.*[0-9]$)(?=.*[a-zA-Z])', password1):
            print("insideif..............", )
        elif len(password1) < 6:
            messages.info(request, 'password must be 6 char long or more')
            return redirect('register')
        elif password1 == password2:
            messages.info(request, 'password must be same')
            return redirect('register')
        else:
            messages.info(request, 'password must have one numeric value and one special character')
            return redirect('register')

        if re.match('[a-zA-Z]', first_name):
            print("insideif..............", )
        elif len(first_name) < 4:
            messages.info(request, 'first Name must be  4 char long or more')
            return redirect('register')
        else:
            messages.info(request, 'first Name must be  in character field')
            return redirect('register')
        
        if re.match('[a-zA-Z]', last_name):
            print("insideif.....")
        elif len(last_name) < 4:
            messages.info(request, 'last Name must be  4 char long or more')
            return redirect('register')
        else:
            messages.info(request, 'last Name must be  in character field')
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username Taken')
            return redirect('register')
            print("username")
        elif len(username) < 4:
            messages.info(request, 'User Name must be  4 char long or more')
            return redirect('register')
        else:
            user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
            user.save()
            print('user created')
            return redirect('login')

        # if password1==password2:
        #     if User.objects.filter(username=username).exists():
        #         messages.info(request, 'Username Taken')
        #         return redirect('register')
        #     elif User.objects.filter(email=email).exists():
        #         messages.info(request, 'Email Taken')
        #         return redirect('register')
            # elif first_name:
            #     if len(first_name) < 4:
            #         messages.info(request, 'first Name must be  4 char long or more')
            #         return redirect('register')
            # elif last_name:
            #     if len(last_name) < 4:
            #         messages.info(request, 'last Name must be  4 char long or more')
            #         return redirect('register')

            # else:
            #     user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name,last_name=last_name)
            #     user.save();
            #     print('user created')
            #     return redirect('login')

        # else:
        #     messages.info(request,'password not matching...')
        #     print('password not matching...')
        #     return redirect('register')

    else:
        return render(request, 'register.html')


def registerPage(request):
    form = UserCreationForm()
    context = {'form'}
    return render(request, 'index.html', context)
