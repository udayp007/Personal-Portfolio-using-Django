from django.shortcuts import render
from .models import Profile, Project, Skill


def home(request):
    profile = Profile.objects.first()  # Get your profile info
    projects = Project.objects.all()  # Get all projects
    skills = Skill.objects.all()  # Get all skills

    return render(request, 'main/home.html', {
        'profile': profile,
        'projects': projects,
        'skills': skills
    })



from django.shortcuts import render, redirect
from .forms import ContactForm

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        print("log1",form)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to home after form submission
    else:
        form = ContactForm()
        print("log2",form)

    return render(request, 'main/contact.html', {'form': form})






