from Doc_app.models import Document
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.conf import settings
from . forms import DocumentForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.utils import timezone
import datetime

        
@login_required
def save(request):
    form = DocumentForm(request.POST, request.FILES)
    if request.method == 'POST':
        if request.user.is_authenticated:
            user=request.user.id
            print(user)
            user_obj=User.objects.get(pk=user)
            print(user_obj)
            pdf_day_limit=Document.objects.filter(user=user_obj.pk).filter(uploaded_at__date=timezone.now()).count()
            print(pdf_day_limit)
            # breakpoint()
            if pdf_day_limit==5:
                messages.info(request,"you have reached the daily limit wait unitill 12 pm to upload more")
                return redirect('upload')
            else:    
                if form.is_valid():
                    new_doc=Document.objects.create(
                        user_id=user,
                        description=form.cleaned_data['description'],
                        document=form.cleaned_data['document'],
                    )
                    new_doc.save()
                    return redirect('upload')
    else:
        form = DocumentForm()
    return render(request, 'Doc_app/base.html', {
        'form': form
    })


def index(request):
    form=DocumentForm
    return render(request, 'Doc_app/login.html', {
        'form': form
    })

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'You are now logged in')
            return redirect('upload')
        else:
            messages.error(request,'Invalid Credantials')
            return redirect('index')
    else:
        return render(request,'Doc_app/login.html')

def upload_page(request):
    form=DocumentForm
    doc=Document.objects.all()
    if request.user.is_authenticated:
            today = datetime.date.today()
            print(today)
            current_month = datetime.date.today().month
            current_year = datetime.date.today().year
            user=request.user.id
            user_obj=User.objects.get(pk=user)
            print(user_obj)
            pdf_list=Document.objects.all().filter(user=user_obj.pk)
            print(pdf_list)
            if request.method == 'GET':
                report_type = request.GET.get('report_type')
                if report_type == 'sort_by_name':
                    user_data = Document.objects.filter(user=User.objects.get(username=request.user.username)).order_by('description')
                    return render(request, 'Doc_app/upload.html',{'form':form,'context':user_data})
                elif report_type=='current_month':
                    user_data = Document.objects.filter(user=User.objects.get(username=request.user.username)).filter(uploaded_at__month=current_month)
                    return render(request, 'Doc_app/upload.html', {'form':form,'context': user_data})
                elif report_type=='current_year':
                    user_data = Document.objects.filter(user=User.objects.get(username=request.user.username)).filter(uploaded_at__year=current_year)
                    return render(request, 'Doc_app/upload.html', {'form':form,'context': user_data})
                elif report_type=='doc_range':
                    start_date = request.POST['startdate']
                    end_date = request.POST['enddate']
                    print(start_date,end_date)
                    user_data = Document.objects.filter(user=User.objects.get(username=request.user.username)).filter(uploaded_at__range=[start_date, end_date])
                    print(user_data)
                    return render(request, 'Doc_app/upload.html', {'form':form,'context': user_data})
            elif request.method=='POST':
            # breakpoint()
                start_date = request.POST['startdate']
                end_date = request.POST['enddate']
                user_data = pdf_list.filter(user=request.user, uploaded_at__range=[start_date,end_date])
                return render(request, 'Doc_app/upload.html', {'form':form,'context': user_data})
            return render(request, 'Doc_app/upload.html',{'form':form,'context':pdf_list})

   

def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']  
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
           
            if User.objects.filter(username=username).exists():
                messages.error(request,'Username already taken!')
                

            else:
                user = User.objects.create_user( password=password1, username=username, first_name=first_name, last_name=last_name)
                user.save()
                messages.success(request, 'User is successfully registered!')
                return redirect('index')
        else:
            messages.error(request,'Password did not match!')
        return redirect('register')
    else:
        return render(request,'Doc_app/register.html')
@login_required
def logout(request):
    auth.logout(request)
    messages.success(request,'You have been logout!!')
    return redirect("index")

def contact(request):
    return render(request,'Doc_app/contact.html')
