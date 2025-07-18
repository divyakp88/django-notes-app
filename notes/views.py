from django.shortcuts import render,redirect,get_object_or_404
from .models import NoteTable

# Create your views here.
#def home(request):
    #return render(request,'home.html')

def index(request):
    return render(request,'index.html')

def note_list(request):
    notev=NoteTable.objects.filter(user=request.user).order_by('-created_at')
    return render(request,'note_list.html',{'notev':notev})

def note_create(request):
    if request.method=='POST':
        title=request.POST['title']
        desc=request.POST['desc']
        NoteTable.objects.create(user=request.user,title=title,desc=desc)
        return redirect('note_list')
    else:
        return render(request,'note_create.html')
    

def note_update(request,pk):
    note=get_object_or_404(NoteTable,pk=pk,user=request.user)
    if request.method=='POST':
        note.title=request.POST.get('title')
        note.desc=request.POST.get('desc')
        note.save()
        return redirect('note_list')
    else:
        return render(request,'note_update.html',{'note':note})

def note_delete(request,pk):
    note=get_object_or_404(NoteTable,pk=pk,user=request.user)  
    if request.method=="POST":
        note.delete()
    return redirect('note_list')      
