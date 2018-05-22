from django.shortcuts import render


# Homepage
def home(request):
    return render(request, 'github/base_template.html')
