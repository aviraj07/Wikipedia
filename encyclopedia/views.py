from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.http import HttpResponse, request
from django.urls import reverse
import markdown2
import random

from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def content(request, name):
    try:
        html = markdown2.markdown(util.get_entry(name))
    except TypeError:
        return render(request,"encyclopedia/error.html",{
            "error": "Page not found."
        })
    return render(request,"encyclopedia/content.html",{
        "contents": html,"name":name
    })


def search(request):
    
        name = request.GET.get('q',None)
        try:
            html = markdown2.markdown(util.get_entry(name))
        except TypeError:
            all = []
            all = util.list_entries()
            res = []
            for text in all:
                if name.upper() in text.upper():
                    res.append(text)
            if len(res) == 0:
                return render(request,"encyclopedia/error.html",{
                    "error": "No such file found."
                })
            return render(request,"encyclopedia/list.html",{
            "contents": res,"name":name
        })
        return render(request,"encyclopedia/content.html",{
            "contents": html,"name":name
        })
        
def new_page(request):
    if request.method == "POST":
        title = request.POST.get('title')
        textarea = request.POST.get('write')
        lists = []
        lists = util.list_entries()
        if title in lists:
            return render(request,"encyclopedia/error.html",{
                "error": "Entry already exits of that name."
            })
        util.save_entry(title, textarea)
        return HttpResponseRedirect(reverse('content',args=[title]))

    else:
        return render(request, "encyclopedia/new_page.html")    

def edit(request, name):

    if request.method == "POST":
        title= request.POST.get('title')
        textarea = request.POST.get('write')
        util.save_entry(title, bytes(textarea,'utf8'))
        html = markdown2.markdown(util.get_entry(title))
        return HttpResponseRedirect(reverse('content',args=[title]))
        

    else:
        htmle = util.get_entry(name)
        return render(request,"encyclopedia/edit.html",{
            "content":htmle, "name":name
        })

def randoms(request):
    all = []
    all = util.list_entries()
    title = random.choice(all)
    html = markdown2.markdown(util.get_entry(title))
    return HttpResponseRedirect(reverse('content',args=[title]))
