from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Product
import logging

logger = logging.getLogger(__name__)

def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have Been Logged In!")
            return redirect('home')
        else:
            messages.success(request, "There Was An Error Logging In, Please Try Again...")
            return redirect('home')
    else:
        if request.user.is_authenticated:
            search_query = request.GET.get('search', '')
            records = Product.objects.all().order_by('id')
            total_count = records.count()
            logger.debug(f"Total products in database: {total_count}")
            
            if search_query:
                records = records.filter(
                    Q(product_name__icontains=search_query) |
                    Q(product_number__icontains=search_query) |
                    Q(brand_name__icontains=search_query)
                )
            
            records = records.order_by('id')
            print(records)
            filtered_count = records.count()
            logger.debug(f"Filtered products count: {filtered_count}")
            
            paginator = Paginator(records, 9)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            context = {
                'records': page_obj,
                'search_query': search_query,
                'total_count': total_count,
                'filtered_count': filtered_count
            }
            
            return render(request, 'home.html', context)
        else:
            return render(request, 'home.html', {})

def logout_user(request):
	logout(request)
	messages.success(request, "You Have Been Logged Out...")
	return redirect('home')


def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You Have Successfully Registered! Welcome!")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})

