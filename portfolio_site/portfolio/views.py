from django.shortcuts import render

def index(request):
    return render(request, 'portfolio/index.html')

def about(request):
    return render(request, 'portfolio/about.html')

def projects(request):
    return render(request, 'portfolio/projects.html')

def resume(request):
    return render(request, 'portfolio/resume.html')

def contact(request):
    return render(request, 'portfolio/contact.html')

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        print("Received name:", name)
    return render(request, 'contact.html')
