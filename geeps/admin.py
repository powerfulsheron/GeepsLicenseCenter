from django.contrib import admin
from .models import Batiment
from .models import Logiciel
from .models import Version
from .models import Demande
from django.http import HttpResponse
import csv

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
        writer.writerow(field_names)

        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])
        return response

    export_as_csv.short_description = "Export Selected"


@admin.register(Demande)
class DemandeAdmin(admin.ModelAdmin, ExportCsvMixin):
	list_display = ("nom","prenom","batiment","bureau","logiciel","os","host","created_date")
	list_filter = ("created_date", "nom", "prenom", "batiment", "logiciel", "version")
	actions = ["export_as_csv"]


