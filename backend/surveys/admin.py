from django.contrib import admin
from .models import Survey, Question, Option, Response, Answer

admin.site.register(Survey)
admin.site.register(Question)
admin.site.register(Option)
admin.site.register(Response)
admin.site.register(Answer)