from django.shortcuts import render
from django.http import HttpResponse

import logging
# Get an instance of a logger
logger = logging.getLogger(__name__)

def home(request):
    return HttpResponse("hello, you are at home")

def signinpage(request):
    return render(request, 'nameless_signin.html', {'key':'secret'})

def signoutpage(request):
    return HttpResponse("You have een signed out.")

def my_view(request, arg1, arg):
    # Log an error message
    logger.error('Something went wrong!')

#def signin(request):
#    passphrase_encrypted = request.POST['passphrase']
#    identt = authenticate(passphrase=passphrase_encrypted)
#    if identt is not None:
#        login(request, user) #TODO: write custom 'login'
#        # Redirect to a success page.
#    else:
#        # Return an 'invalid login' error message.


