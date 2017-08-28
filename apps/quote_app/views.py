from django.shortcuts import render, redirect
from django.contrib import messages
from ..login_app.models import User
from models import Quote
# Create your views here.
def sessionChecker(request):
    try:
        return request.session['user_id']
    except:
        return False

def logout(request):
    request.session.flush()
    return redirect('/')

def index(request):
    if sessionChecker(request) == False:
        return redirect('/')
    context = {
        'quotes': Quote.objects.all(),
        'adds': User.objects.get(id = request.session['user_id']).quote_own.all()
    }
    print context
    return render(request,'quote_app/index.html',context)

def submit_quote(request):
    results = Quote.objects.quoteVal(request.POST)
    if results['status'] == True:
        for error in results['errors']:
            messages.error(request, error)
        return redirect('/quote')
    print results
    return redirect('/quote')

def add_quote(request, quote_id, user_id):
    User.objects.get(id= user_id).quote_own.add(Quote.objects.get(id = quote_id))
    return redirect('/quote')
def remove_quote(request, quote_id, user_id):
    User.objects.get(id= user_id).quote_own.remove(Quote.objects.get(id = quote_id))
    return redirect('/quote')

def show(request, user_id):
    if sessionChecker(request) == False:
        return redirect('/')
    context={
        'user':User.objects.get(id = user_id)
    }
    return render(request,'quote_app/show.html')

