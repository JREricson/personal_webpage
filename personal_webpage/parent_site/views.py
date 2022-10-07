from django.shortcuts import render



def contact(request):
  return render(request, "parent_site_contact.html", {})

