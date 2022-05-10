from django.shortcuts import render
from django.core.paginator import Paginator
from django.core.mail import send_mail
from .models import Contacts,Posts
from datetime import datetime
from django.conf import settings

import json
from math import ceil


with open("config.json") as js:
    para = json.load(js)["para"]


def home(req):
    # pagination logic
      
    posts = Posts.objects.all()
    p = Paginator(posts, para["posts_in_page"])
    page_number = req.GET.get('page')
    page_obj = p.get_page(page_number)
    
    # display total page number logic
    page_len = []
    for i in range(ceil(len(posts)/para["posts_in_page"])):
        page_len.append(i+1)

    # print(len(req.GET.get('page'))

    context = {"blog_name":"Learning Python",
               "sub_name" : "A blog For A Beginners ",
               "posts":posts,
               "page_len": page_len,
               "page_obj": page_obj,
               "linkdin_link" : "https://linkedin.com/in/shishir-patel-95a655180",
               "git_link" : "https://github.com/Shishir364", 
               "tut_link" : ""
               }
    return render(req , "index.html",context )

def about(req):
    return render(req ,"about.html", para)

def contact(req):
    return render(req, "contact.html", para)

def submit(req):
    if req.method == "POST":
        name = req.POST['name']
        email = req.POST['email']
        phone_num = req.POST['phone_num']
        mess = req.POST['mess']
        date = datetime.now()
        # save contacts to database system
        contact = Contacts(name=name, email=email, phone_num=phone_num, mess=mess, date=date)
        contact.save()
        # for useing in templates 
        context = {
                   "blog_name":"Learning Python",
                   "name" : name,
                   "linkdin_link" : "https://linkedin.com/in/shishir-patel-95a655180",
                   "git_link" : "https://github.com/Shishir364", 
                   "tut_link" : ""
               }
        # for sending mails
        send_mail(
                    "We want to touch with you : " + name,
                    mess,
                    settings.EMAIL_HOST_USER,
                    settings.EMAIL_RECEIVING_USER,
                    fail_silently=False,
                )

        return render(req, "contact.html", context)

def post(req,slug):
    posts = Posts.objects.all().filter(slug = slug)
    context = {"blog_name":"Learning Python",
               "posts":posts,
               "linkdin_link" : "https://linkedin.com/in/shishir-patel-95a655180",
               "git_link" : "https://github.com/Shishir364", 
               "tut_link" : ""
               }
    
    return render(req , "post.html",context)
