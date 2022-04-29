from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from alm.models import Cliente, Articulo, Orden, ArticuloOrden

# Register your models here.

@admin.register(Cliente)
class ClienteAdmin(ImportExportModelAdmin):
    list_display = ("nom_cliente", "estado")
    search_fields = ("nom_cliente", "estado")
    list_filter = ("estado",)
    list_per_page = 30

@admin.register(Articulo)
class ArticuloAdmin(ImportExportModelAdmin):
    list_display = ("nom_articulo", "precio")
    search_fields = ("nom_cliente", "estado")
    list_per_page = 30

@admin.register(ArticuloOrden)
class ArticuloOrdenAdmin(ImportExportModelAdmin):
    list_display = ("cant", "articulo", "orden")
    search_fields = ("articulo", "orden")
    raw_id_fields = ("articulo", "orden",)
    list_filter = ("articulo", "orden",)
    list_per_page = 30

class ArticuloOrdenInline(admin.TabularInline):
    model = ArticuloOrden
    extra = 0
    can_delete = True

@admin.register(Orden)
class OrdenAdmin(ImportExportModelAdmin):
    list_display = ("fecha", "cliente")
    search_fields = ("fecha", "cliente")
    raw_id_fields = ("cliente",)
    list_filter = ("fecha", "cliente",)
    list_per_page = 30

    inlines = \
        [
            ArticuloOrdenInline,
        ]