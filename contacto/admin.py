from django.contrib import admin

# Register your models here.

from .models import Contacto

class ContactoAdmin(admin.ModelAdmin):
    model = Contacto
    fieldsets = (
        (('Mensaje'), {
            # 'classes': ('collapse',),
            'fields': (('nombre',),('email',) ,('asunto'),
                       ('mensaje',),
                       ), }),
    )
    list_display = ['nombre', 'fecha']
    search_fields = ('nombre', 'email','celular' , 'mensaje')
    list_filter = ['nombre', 'fecha', ]

admin.site.register(Contacto, ContactoAdmin)

