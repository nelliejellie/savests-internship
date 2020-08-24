from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import EmailPostForm
from django.core.mail import send_mail

# Create your views here.
def index(request):
    user = User.objects.all()
    sent = False
    recievers = []
    for users in user:
        recievers.append(users.email)
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print (cd)
            subject = cd['sender']
            message = cd['email_body']
            send_mail(subject, message, 'admin@savest.com', recievers)
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'index.html', {'form': form,'sent':sent})