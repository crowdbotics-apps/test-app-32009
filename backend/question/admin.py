from django.contrib import admin
from .models import Answer, InputType, Option, Question, QuestionOption

# admin.site.register(Option)
admin.site.register(Question)
admin.site.register(QuestionOption)
admin.site.register(Answer)
admin.site.register(InputType)

# Register your models here.
ModelField= lambda model: type('Subclass'+model.__name__,(admin.ModelAdmin,),{
	'list_display':[x.name for x in model._meta.fields],	
})

admin.site.register(Option,ModelField(Option))
