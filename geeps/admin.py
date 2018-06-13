from django.contrib import admin
from .models import Batiment
from .models import Logiciel
from .models import Version
from .models import Demande
from django.http import HttpResponse
import csv
import datetime

admin.site.register(Logiciel)
admin.site.register(Version)
admin.site.register(Batiment)

class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)
        writer.writerow(["ActivationLabel", "MatlabRelease", "HostID", "Name", "Firstname", "Email", "Bureau", "Telephone", "Batiment", "OperatingSystem"])

        for obj in queryset:
            print(obj)
            row = writer.writerow([getattr(obj, "prenom")+"-"+getattr(obj, "nom")+"-"+getattr(obj, "version").nom+"-"+convertDatetimeToString(getattr(obj, "created_date")),getattr(obj, "version").nom,getattr(obj, "host"),getattr(obj, "nom"),getattr(obj, "prenom"),getattr(obj, "email"),getattr(obj, "bureau"),getattr(obj, "phone"),getattr(obj, "batiment").nom,getattr(obj, "os")])
        return response

    export_as_csv.short_description = "Export Selected"


@admin.register(Demande)
class DemandeAdmin(admin.ModelAdmin, ExportCsvMixin):
	list_display = ("nom","prenom","batiment","bureau","logiciel","os","host","created_date")
	list_filter = ("created_date", "nom", "prenom", "batiment", "logiciel", "version")
	actions = ["export_as_csv"]


def convertDatetimeToString(o):
    DATE_FORMAT = "%Y-%m-%d" 
    TIME_FORMAT = "%H:%M:%S"

    if isinstance(o, datetime.date):
        return o.strftime(DATE_FORMAT)
    elif isinstance(o, datetime.time):
        return o.strftime(TIME_FORMAT)
    elif isinstance(o, datetime.datetime):
        return o.strftime("%s %s" % (DATE_FORMAT, TIME_FORMAT))
