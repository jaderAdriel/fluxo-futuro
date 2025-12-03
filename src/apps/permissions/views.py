from django.shortcuts import render

def index(request):
    return render(request, 'pages/permissions/index.html', {})