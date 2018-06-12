from io import BytesIO
from reportlab.pdfgen import canvas

from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from reportlab.lib.utils import ImageReader

from .models import Logiciel
from .models import Batiment
from .models import Version
from .models import Demande
from .forms import DemandeForm

import datetime

def formulaire(request):
	logiciels=Logiciel.objects.all()
	batiments=Batiment.objects.all()
	result="null"
	if request.method == "POST":
		try:
			res = Demande(nom=request.POST.get('nom'),prenom=request.POST.get('prenom'),email=request.POST.get('email'),phone=request.POST.get('phone'),batiment_id=request.POST.get('batiment'),bureau=request.POST.get('bureau'),logiciel_id=request.POST.get('logiciel'),version_id=request.POST.get('version'),os=request.POST.get('os'),host=request.POST.get('host'))
			res.save()
			buffer = BytesIO()
			p = canvas.Canvas(buffer)
			p.drawImage(ImageReader('geeps/static/img/geeps2.png'), 50, 740,230,100, mask='auto')
			p.drawCentredString(279, 710,"Demande de renouvellement de licence")
			p.drawCentredString(279, 650,res.nom+" "+res.prenom)
			p.drawCentredString(279, 600,res.email)
			p.drawCentredString(279, 550,res.phone)
			p.drawCentredString(279, 500,"Batiment : "+res.batiment.nom)
			p.drawCentredString(279, 450,"Logiciel : "+res.logiciel.nom)
			p.drawCentredString(279, 400,"Version : "+res.version.nom)
			p.drawCentredString(279, 350,"Système : "+res.os)
			p.drawCentredString(279, 300,"Host ID : "+res.host)
			p.drawCentredString(279, 250,"Date : "+convertDatetimeToString(res.created_date))
			p.save()
			pdf = buffer.getvalue()
			buffer.close()
			email=EmailMessage(
			    "[GEEPS] Demande de renouvellement de licence "+res.logiciel.nom,
			    convertDatetimeToString(res.created_date)+"\n\nDemande de renouvellement de licence de "+res.logiciel.nom+" de "+res.nom+" "+res.prenom+" pour le systeme "+res.os+".",
			    'admin@geeps.centralesupelec.fr',
			    ['cri@geeps.centralesupelec.fr']
			)
			email.attach(res.logiciel.nom+'-'+res.version.nom+'-'+res.nom+'-'+res.prenom+'-'+convertDatetimeToString(res.created_date)+'.pdf', pdf, 'application/pdf')
			email.send(fail_silently=False)
			send_mail(
			    "[GEEPS] License renewal request - Demande de renouvellement de licence"+res.logiciel.nom,
			    convertDatetimeToString(res.created_date)+
			    "\n\nYour "+res.logiciel.nom+" renewal request for "+res.os+" operating system has been taken into account."+
			    "\n\nVotre demande de renouvellement de "+res.logiciel.nom+" pour le système "+res.os+" a bien ete prise en compte."+
			    "\n\nLe CRI du GeePs",
			    'admin@geeps.centralesupelec.fr',
			    [res.email],
			    fail_silently=False,
			)
			result=res.pk
		except Exception as e:
			result="error"
			print(e)
	return render(request, 'geeps/formulaire.html',{'logiciels': logiciels,'batiments': batiments,'result':result})

def getReleaseListByLogiciel(request, id):
	logiciel = Logiciel.objects.get(id=id)
	versions = Version.objects.all().filter(logiciel=logiciel)
	return HttpResponse(serializers.serialize('json',versions),content_type='json')

def convertDatetimeToString(o):
	DATE_FORMAT = "%Y-%m-%d" 
	TIME_FORMAT = "%H:%M:%S"

	if isinstance(o, datetime.date):
	    return o.strftime(DATE_FORMAT)
	elif isinstance(o, datetime.time):
	    return o.strftime(TIME_FORMAT)
	elif isinstance(o, datetime.datetime):
	    return o.strftime("%s %s" % (DATE_FORMAT, TIME_FORMAT))



