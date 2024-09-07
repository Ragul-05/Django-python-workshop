from django.shortcuts import redirect, render, HttpResponse
from .models import Student

# Create your views here.
def create(request):
    if request.method == "POST":
        roll = request.POST["roll"]
        name = request.POST["name"]
        mark = request.POST.get("mark")

        db = Student.objects.create(roll=roll, name=name, mark=mark)
        db.save()
        return redirect('display')
    return render(request,'index.html')

def display(request):
    db = Student.objects.all()
    return render(request,"display.html", {"data": db})

def edit(request,id):
    data = Student.objects.get(id=id)
    if request.method=='POST':
        data.roll = request.POST["roll"]
        data.name = request.POST["name"]
        data.mark = request.POST.get("mark")
        data.save()
        return redirect("display")
    return render(request,"edit.html",{'data':data})


def delete(request,id):
    data = Student.objects.get(id=id)
    data.delete()
    return redirect('display')