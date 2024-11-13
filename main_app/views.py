from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home.html')  # step 4 create html files, then step 5 add render


def services(request):
    our_services = ["Bush Camps", "Balloon Tours", "Hunting", "Village Visits", "Kungfu"]
    price = 10000
    date = '15-11-2024'
    return render(request, 'services.html',
                  {'services': our_services, 'price': price, 'date': date})


def about(request):
    return render(request, 'about.html')

# display data in pages
# loops
# if statements
# Templating engine language

#filters
#images
#static files - local bootstrap
#database
#xammp
