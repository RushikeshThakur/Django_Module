from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.db.models.signals import post_save, pre_save
from django.utils.timesince import timesince
from django.conf import settings

PUBLISH_CHOICE = [
  ('draft' , 'Draft'),      # the first field is to store in databse and second one for Views
  ('publish','Publish'),
  ('private','Private')
]

def upload_location(instance, filename):
    #filebase, extension = filename.split(".")
    #return "%s/%s.%s" %(instance.id, instance.id, extension)
    PostModel = instance.__class__
    new_id = PostModel.objects.order_by("id").last().id + 1
    """
    instance.__class__ gets the model Post. We must use this method because the model is defined below.
    Then create a queryset ordered by the "id"s of each object, 
    Then we get the last object in the queryset with `.last()`
    Which will give us the most recently created Model instance
    We add 1 to it, so we get what should be the same id as the the post we are creating.
    """
    return "%s/%s" %(new_id, filename)

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    image = models.FileField(upload_to=upload_location, 
            null=True, 
            blank=True,
            verbose_name='image', 
            # width_field="width_field", 
            # height_field="height_field"
            )
    height_field = models.IntegerField(default=0)
    width_field  = models.IntegerField(default=0)
    content      = models.TextField()
    draft        = models.BooleanField(default=False)
    publish      = models.DateField(auto_now=False, auto_now_add=False)
    updated      = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp    = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):           # Assign the name to each title fields
    	return self.title        # Set as a title as field to the model data

    class Meta:
    	verbose_name_plural = "Post_models"   # Assign the name to the model 
    	unique_together = [('title','slug')]


# Create your models here.
class BlogModel(models.Model):
	#id = models.AutoField(primary_key=True) # this field don't auto increate
	#id =models.IntegerField(primary_key=True) # this field will increment the count
	id           = models.BigAutoField(primary_key=True) # this allow us to take huge value
	active       = models.BooleanField(default=True)
	title        = models.CharField(
		                   max_length=250,
		                   verbose_name='New Title',
		                   unique=True,
		                   error_messages={
		                        'unique': 'This is not unique try another one .... '
		                   },
		                   help_text="Please use the unique title."
		                   )
	integer      = models.BigIntegerField(default=0,verbose_name="Integer")
	email        = models.EmailField(max_length=250,verbose_name="Email")
	slug         = models.SlugField(null=True, blank=True)
	content      = models.TextField(null=True, blank=True)	# this is used in admin and form as well for large text
	publish      = models.CharField(max_length=250, choices=PUBLISH_CHOICE , default='Draft') # default show first
	view_count   = models.IntegerField(default=0)
	publish_date = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now)
	update       = models.DateTimeField(auto_now=True) # when save is occured
	timestamp    = models.DateTimeField(auto_now_add=True) # when save in DB occured
    
    # def save(self, *args, **kwargs):    # This method override the data before going to Database
    #     if not self.slug:
    #     	self.slug = slugify(self.title) 
    #     super(BlogModel, self).save(*args, **kwargs) 


	class Meta:
		verbose_name = 'Title'
		verbose_name_plural = 'Posts'
		unique_together = [('title','content')]

	def __str__(self):              # this is for python3
		#return "something"         # this will give somthing to all record
		return self.title           # this will give title to all records

	# @property
	# def age(self):
	# 	if self.publish == 'publish':
	# 		now  = datetime.now()
	# 		publish_time = datetime.combine(
 #                             self.publish_date,
 #                             datetime.now().min.time() 
	# 			           )
	# 		try:
	# 		     diffrenece = now - publish_time
	# 		except:
	# 		      return "unknown"
	# 		 if diffrenece <= timedelta(minutes=1):
	# 		     return "just know"
	# 		 return '{time} ago'.format(time = timesince(publish_time).split(',')[0])
	# 	return "Not Publish" 

	def get_absolute_url(self):
		return f"/product/{self.id}/"


def Blog_model_pre_save_recevier(sender, instance, *args, **kwargs):
	print("before save")
	if not instance.slug:
		instance.slugify = slugify(instance.title)

#It don't need save method to save a data

pre_save.connect(Blog_model_pre_save_recevier, sender=BlogModel)

def Blog_model_post_save_recevier(sender, instance, created, *args, **kwargs):
	print('After data is save')
	if not instance.slug and instance.title:	
		instance.slug = slugify(instance.title)	
		instance.save()	

post_save.connect(Blog_model_post_save_recevier, sender=BlogModel)


# class MyModel(models.Model):
# 	id      = models.BigAutoField(primary_key=True)
#     # active  = models.BooleanField(default=True)
#     title   = models.CharField(max_length=250,unique=True,help_text="Must be enter")
#     slug    = models.SlugField(null=False,blank=True)
#     content = models.TextField(null=False,blank=False)




