from django.contrib import admin
from .models import BlogModel, Post
# Register your models here.
    

class PostModelAdmin(admin.ModelAdmin):

		fields = [
            'title',
            'slug',
            'content',
            'integer',
            'email',
            'publish',
            'publish_date',
            'update',
            'timestamp',
            'new_content',
		]

		# class Meta:
		# 	model = BlogModel

		readonly_fields = ['update','timestamp', 'new_content']

		def new_content(self, instance, *args, **kwargs):  # the first take list and second take dictionary
			return str(instance.age)                     # Adding new content to page

class PostMyModel(admin.ModelAdmin):

      fields = [
        'title',
        'slug',
        'image',
        'height_field',
        'width_field',
        'content',
        'draft',
        'publish',
        'updated',
        'timestamp',
        'new_content_post', 
      ]

      readonly_fields = ['updated','timestamp','new_content_post']

      class Meta:
            model = Post

      def new_content_post(self,instance,*args,**kwargs):   # access this using intances
            return str(instance.title)

admin.site.register(BlogModel, PostModelAdmin)
admin.site.register(Post, PostMyModel)

# def register(self, model_or_iterable, admin_class=None, **options):
#       myModels = [models.Project, models.Client, models.About]  # iterable list
#       admin.site.register(myModels)