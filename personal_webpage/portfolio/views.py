from django.http import request
from django.shortcuts import redirect, render
from .forms import ContactForm as PortfolioContactForm
from .models import Project
from django.views.generic import ListView, DetailView
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib import messages

from django.conf import settings


def home(request):
    context = {"projects": Project.objects.all()}

    return render(request, "portfolio/portfolio_home.html", context)


def contact(request):
    print(settings.EMAIL_HOST_USER)
    print(settings.DEFAULT_RECEIVING_EMAIL)
    if request.method == "POST":
        form = PortfolioContactForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data

            email_sender_name = cleaned_data["email_sender_name"]
            email_subject = cleaned_data["email_subject"]
            email_sender_email = cleaned_data["email_sender_email"]
            email_content = cleaned_data["email_content"]

            try:
                send_mail(
                    f"personal website email from <{email_sender_email}> subject<{email_subject}>",
                    f"""
                    sender name: <{email_sender_name}>
                    sender email: <{email_sender_email}>
                    subject: <{email_subject}>

                    message:
                    {email_content}



    
                    """,
        
                    settings.EMAIL_HOST_USER,
                    [settings.DEFAULT_RECEIVING_EMAIL],
                )
            except:
                messages.error(
                    request,
                    "There was a problem sending your email, but your request has been logged",
                )

            messages.success(request, "Your email has been sent.")
            return HttpResponseRedirect("./")

    else:
        form = PortfolioContactForm()

    return render(request, "portfolio/portfolio_contact.html", {"form": form})


def about(request):
    # posts = Post.objects.all()
    return render(request, "portfolio/portfolio_about.html", {})


class ProjectListView(ListView):
    model = Project
    template_name = "portfolio/portfolio_projects.html"
    context_object_name = "projects"
    ordering = ["-date_posted"]
    paginate_by = 5


class ProjectDetailView(DetailView):
    model = Project
    template_name = "portfolio/portfolio_project.html"
