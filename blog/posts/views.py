import urllib.request
from allauth.socialaccount.models import SocialAccount, SocialToken
from django.shortcuts import render
from django.http import HttpResponseRedirect
import xml.etree.ElementTree as ET

from posts.models import Posts
from posts.forms import CommentForm, PostForm


def user_contacts(request):
    user = request.user
    social_account = SocialAccount.objects.get(user=user)
    social_token = SocialToken.objects.get(account=social_account)
    access_token = social_token.token
    url = 'https://www.google.com/m8/feeds/contacts/default/full' + '?access_token=' + access_token + '&max-results=100'
    req = urllib.request.Request(url, headers={
        'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.30 (KHTML, like Gecko) Ubuntu/11.04 Chromium/12.0.742.112 Chrome/12.0.742.112 Safari/534.30"})
    contacts = urllib.request.urlopen(req).read()
    contacts_xml = ET.fromstring(contacts)

    results = []

    for entry in contacts_xml.findall('{http://www.w3.org/2005/Atom}entry'):
        for address in entry.findall('{http://schemas.google.com/g/2005}email'):
            email = address.attrib.get('address')
            results.append(email)

    context = {
        "results": results
    }
    return render(request, 'contacts.html', context)


def home(request):
    post_list = Posts.objects.all()
    context = {
        "title": "All posts",
        "post_list": post_list
    }

    return render(request, "home.html", context)


def create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form
    }
    return render(request, "form_create.html", context)


def detail(request, pk):
    post = Posts.objects.get(id=pk)
    comments = post.comments.all()

    form = CommentForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.post = post
        instance.save()
        return HttpResponseRedirect(post.get_absolute_url())

    context = {
        "post": post,
        "comments": comments,
        "form": form
    }
    return render(request, "detail.html", context)
