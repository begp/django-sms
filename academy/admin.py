from django.contrib import admin


from .models import Subject, Section, Grade, TeacherAssignment, Room


class SectionAdmin(admin.ModelAdmin):
    list_display = ("grade", "section", "room")


class RoomAdmin(admin.ModelAdmin):
    list_display = ("block", "room")


class TeacherAssignAdmin(admin.ModelAdmin):
    list_display = ("teacher", "subjects", "grades")


class SubjectAdmin(admin.ModelAdmin):
    list_display = ("name", "grade")


admin.site.register(Section, SectionAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Grade)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(TeacherAssignment)
