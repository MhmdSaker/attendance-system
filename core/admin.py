from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources

# Register your models here.

from .models import (
  Student,
  Faculty,
  Instructor,
  Course
  )





class StudentAdminStyle(ImportExportModelAdmin,admin.ModelAdmin):
  list_display = ("aca_id","name","faculty","levels", "Date_ofj")
  list_filter  = (
                  "levels",
                  "faculty"

                  )
  search_fields = (
    "name",
    "aca_id",
    "aca_em",
    
  )
  
  fields  = (
    "name",
    "aca_id",
    "aca_em",
    "password",
    "faculty",
    "Date_ofj",
    "levels",
    "Attnder",
    # 'add_data_from_excel'
  )
  
  readonly_fields = (
    "Attnder",
    'add_data_from_excel'
  )


  

class InstructorAdminStyle(ImportExportModelAdmin,admin.ModelAdmin):
  
  list_display = (
    "name",

  )
  list_filter = (
    'ins_course',
  )
  

class CourseAdminStyle(ImportExportModelAdmin,admin.ModelAdmin):
  list_display = (
    "coden",
    "name",
    "Term",
    "level",
    "student_in_course"

  )
  fields = (
    
    "name",
    "coden",
    "inst",
    "Term",
    
    "Days",
    "level",
    "faculty",
    "student_in_course",
    "attending_table",
  )
  
  readonly_fields = (
    "student_in_course",
    "attending_table"
  )


admin.site.index_title = "New Mansoura University"
admin.site.site_header = "New Mansoura University"
admin.site.site_title = "NMU"



admin.site.register(Student, StudentAdminStyle)
admin.site.register(Faculty)
admin.site.register(Instructor, InstructorAdminStyle)
admin.site.register(Course, CourseAdminStyle)