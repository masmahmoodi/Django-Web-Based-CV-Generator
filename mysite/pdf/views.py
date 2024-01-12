from django.shortcuts import render,redirect
from .models import Profile
import pdfkit
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def form(request):
    if request.method  == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')       
        summary = request.POST.get('summary')       
        degree = request.POST.get('degree')       
        school = request.POST.get('school')       
        university = request.POST.get('university')       
        previous_work = request.POST.get('previous_work')
        skills = request.POST.get('skills')
        profile_object = Profile(name=name,email=email,summary=summary,degree=degree,school=school,university=university,previous_work=previous_work,skills=skills)
        profile_object.save()
        return redirect('download/')
    return render(request,"pdf/form.html")


def resume(request,id):
    profile_object = Profile.objects.get(id=id)
    template = loader.get_template("pdf/resume.html")
    html = template.render({"profile_object":profile_object})
    options = {
        "page-size":"Letter",
        "encoding":"UTF-8",
    }
    pdf = pdfkit.from_string(html,False,options)
    response = HttpResponse(pdf,content_type="application/pdf")
    response["Content-Disposition"] = 'attachment'
    filename = "resume.pdf"
    return response
    
    
    
def download_page(request):
    profile_objects = Profile.objects.all()
    return render(request,"pdf/download.html",{"profile_objects":profile_objects})
    
