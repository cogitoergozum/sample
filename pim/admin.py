from django.contrib import admin


from models import Student, Ledger
# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display = ('id_number', 'fullname')

admin.site.register(Student, StudentAdmin)
admin.site.register(Ledger)