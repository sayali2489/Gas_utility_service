from django.shortcuts import render, redirect,get_object_or_404
from .models import ServiceRequest
from .forms import ServiceRequestForm
from django.contrib.auth.decorators import login_required
from .models import CustomerAccount
from django.contrib.admin.views.decorators import staff_member_required

@login_required
def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user
            service_request.save()
            return redirect('track_requests')
    else:
        form = ServiceRequestForm()
    return render(request, 'service_requests/service_request_form.html', {'form': form})

@login_required
def track_requests(request):
    requests = ServiceRequest.objects.filter(customer=request.user)
    return render(request, 'service_requests/track_requests.html', {'requests': requests})

@login_required
def view_account(request):
    account = request.user
    return render(request, 'view_account.html', {'account': account})

@staff_member_required
def manage_requests(request):
    requests = ServiceRequest.objects.all()
    return render(request, 'manage_requests.html', {'requests': requests})