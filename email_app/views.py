from django.shortcuts import render
from .forms import EmailForm
from .models import Email
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def get_email(request):
    form = EmailForm(request.POST or None)
    page_params = {
        'form': form,
    }
    if form.is_bound and form.is_valid():
        obj = form.save(commit=False)
        obj.ip_address = get_client_ip(request)
        obj.save()
    return render(request, 'index.html', page_params)

# Create your views here.
