from django.contrib import admin
from .models import perfiles_plantas
from import_export.admin import ImportExportModelAdmin
from import_export import resources


class serviciosresource(resources.ModelResource):
    fields =('id', 'plant_name', 'humidity_excellent', 'humidity_regular', 'humidity_bad')
    
    class Meta:
        model = perfiles_plantas

@admin.register(perfiles_plantas)
class perfiles_plantas(ImportExportModelAdmin):
    resource_class = serviciosresource
    # readonly_fields=('id')
    list_display = ['id', 'plant_name', 'humidity_excellent', 'humidity_regular', 'humidity_bad'] #Propiedades visibles del campo
    # list_filter=['categoria', 'disponibilidad']  #Añadir buscar por filtro
    list_per_page=15    #Cantidad de items por pagina
    # list_editable=['disponibilidad',]