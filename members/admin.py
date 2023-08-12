from django.contrib import admin
from members.models import Employee
# Register your models here.

class MemberAdmin(admin.ModelAdmin):
  list_display = ("employee_id","firstname", "lastname","phone", "joined_date","city","department")

admin.site.register(Employee, MemberAdmin)