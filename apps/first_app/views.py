# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.db import models
from models import *

from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

#dependencies for file upload
from models import Document
from forms import DocumentForm
from django.db.models import Q

#dependencies for tesseract
from PIL import Image
import pytesseract
import argparse
import cv2
import os

def index(request):
    context = {
        "vehicles" : Vehicle.objects.all()
    }
    return render(request, 'first_app/home.html', context)

def process(request):
    Vehicle.objects.create(name= request.POST["name"], vin = request.POST["vin"])
    return redirect('/')

def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('list'))
    else:
        form = DocumentForm()  # A empty, unbound form
    # Load documents for the list page
    documents = Document.objects.all()
    # Render list page with the documents and the form
    return render(
        request,
        'first_app/list.html',
        {'documents': documents, 'form': form}
    )
def scan(request):
    print (request.POST['url'])                             
    form = DocumentForm()
    documents = Document.objects.all()
    image = cv2.imread(request.POST['url'])
    print (image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)           #Photo prep, converts to black and white. 
    filename = "{}.png".format(os.getpid())                  #Creates png file inside of root folder, find solution after you complete project
    cv2.imwrite(filename, gray)
    print ('Thank GOD! It hasn"t broken yet')
    text = pytesseract.image_to_string(Image.open(filename)) #Tesseract OCR
    print (text)
    my_list = text.split("\n")
    for x in my_list:                                        #Validation to parse strings, need to add more.
        if len(x) == 17:
            vin = x
    print (my_list)
    return HttpResponse("SCAN complete, the vin number is: " + vin)



