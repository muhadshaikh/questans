from django.contrib import admin
from .models import *
# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    list_display=('title','user')
    search_fields=('title','detail')
admin.site.register(Question, QuestionAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','roll','city','marks',
    'pass_data']
admin.site.register(Student, StudentAdmin)


class TeacherAdmin(admin.ModelAdmin):
    list_display=['id','name','empnum','city','salary',
    'join_date']
admin.site.register(Teacher, TeacherAdmin)

# admin.site.register(Answer)
# admin.site.register(Comment)
# admin.site.register(UpVote)
# admin.site.register(DownVote)