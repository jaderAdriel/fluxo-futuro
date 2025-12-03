from django.shortcuts import render

def index(request):
    return render(request, 'pages/meetings/index.html', {})