from django.shortcuts import render
from imageapp.models import Image

# Create your views here.
def imageView(request):
    if request.method == 'POST':
        formdata = request.POST
        name = formdata.get('nm')
        email = formdata.get('em')
        age = formdata.get('ag')
        img = Image(name=name, email=email, age=age)
        img.save()
    return render(request,'index.html')


