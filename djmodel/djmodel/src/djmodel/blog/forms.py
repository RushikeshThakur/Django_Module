from django import forms
from .models import BlogModel, Post
from django.utils.text import slugify

# You can customize the thing by overriding the field in models 

class BlogModelForms(forms.ModelForm):
	title        = forms.CharField(max_length=250,widget=forms.TextInput(
		                                                 attrs={
		                                                    "placeholder":"Your title"
		                                                 }))
	slug         = forms.CharField(required=False)
	content      = forms.CharField(required=False, widget=forms.Textarea(
		                                       attrs={
                                                        "placeholder":"Your content",
                                                        "Class":"myclass",
                                                        "id":"my id",
                                                        "cols":20,
                                                        "rows":10
		                                             }))
	publish      = forms.CharField()
	view_count   = forms.IntegerField(initial=0)

	class Meta:
		model = BlogModel
		fields = [
            'title',
            'slug',
            'content',
            'publish',
            'view_count',
            'publish_date'
		]

class My_form_blog(forms.Form):
	SOME_CHOICE = [                  # This is a list of tuples
           ("first","First"),
           ("second","Second"),
           ("third","Third"),
		]

	YEARS = [x for x in range(2020,3030)]           # for date fileds

	INTEGER = [tuple([x,x]) for x in range(0,100)]  # for integer fileds
	# This is pure form fields and create method is to used to store data
	title        = forms.CharField(label="title",error_messages={"required":"Title is required"},required=True, widget=forms.TextInput(
		                                                 attrs={
		                                                    "placeholder":"Your title"
		                                                 }))
	date          = forms.DateField(initial="2020-10-10" ,widget=forms.SelectDateWidget(years=YEARS))
	slug          = forms.CharField(required=False)
	content       = forms.CharField(widget=forms.Select(choices=SOME_CHOICE))
	integer       = forms.IntegerField(initial=10,widget=forms.Select(choices=INTEGER)) # integer as a choices
	email         = forms.EmailField()
	# slug         = forms.CharField(required=False)
	# content      = forms.CharField(required=False, widget=forms.Textarea(
	# 	                                       attrs={
 #                                                        "placeholder":"Your content",
 #                                                        "Class":"myclass",
 #                                                        "id":"my id",
 #                                                        "cols":20,
 #                                                        "rows":10
	# 	                                             }))
	# publish      = forms.CharField()
	# view_count   = forms.IntegerField(initial=0)
	# publish_date = forms.DateField()
	def clean_integer(self,*args,**kwargs):  # validation for form data(integer) fields
		integer = self.cleaned_data.get("integer")
		if integer<10:
			raise forms.ValidationError("Filed Must be greater then 10")
		else:
			return integer
			#return 100  use this if we want to keep persistance value  

	# def clean_title(self,*args,**kwargs):     # validation for form data(title) fields
	# 	title = self.cleaned_data.get("title")
	# 	if len(title)<10:
	# 		raise forms.ValidationError("Ensure that title must be greater then 10 character")
	# 	else:
	# 		return title



class PostModelForm(forms.ModelForm):

	# INT = [tuple([x,x]) for x in range(0,10)] # used for select option

	# YEAR = [x for x in range(2020,2030)]      # used for selectdatewedgit

	# title = forms.CharField(required=True,error_messages={"required":"This fields is required"},widget=forms.TextInput(attrs={
	# 	                                                         "placeholder":"Your title post"
	# 	                                                     }))
	# slug  = forms.CharField(required=True,error_messages={"required":"The slug field is required"},widget=forms.TextInput(attrs={
 #                                                   "placeholder":"Your slug"
	# 	                                       }))
	# content = forms.CharField(widget=forms.Textarea(attrs={
 #                                                  "cols":12,
 #                                                  "rows":1
	# 	                                       }))
	# height_field = forms.IntegerField(widget=forms.Select(choices=INT))
	# width_field  = forms.IntegerField(widget=forms.Select(choices=INT))
	# publish = forms.DateField(initial="2020-30-05",widget=forms.SelectDateWidget(years=YEAR))

	class Meta:
		model=Post
		fields = [       # The fields is wan to display
		  # "user" 
           "title",
           "slug",
           "content",
           "image",
           "height_field",
           "width_field",
           "content",
           "draft",
           "publish"
		]

		help_text = {                         # For heip text
		   "title":"Must be unique",
		   "slug":"Must be unique"
		}

		labels = {                            # for labels
		  "title":"Title Name",
		  "slug":"Slug Name"
		}

		# error_messages = {                          # For error messages
		#    "title": {
		#        "max_length":"Fields is too long..",
		#        "required":"Title is required post"
		#    },
		#    "slug": {
		#        "max_length":"Fields is too long..",
		#        "required":"slug fields is required post",
		#        "uniqe":"slug fields must be unique post"
		#    }

		# }

	def __init__(self, *args, **kwargs):                       # for error messages  
		super(PostModelForm, self).__init__(*args, **kwargs)
		self.fields['title'].widget = forms.TextInput(attrs={
                                                     "cols":12,
                                                     "rows":5,
                                                     "placeholder":"New title"
		                                         })
		self.fields['title'].error_messages = {
		       "max_length":"Fields is too long..",
		       "required":"Title is required post"
		    }

		self.fields['slug'].error_messages = {
		       "max_length":"Fields is too long..",
		       "required":"Title is required post"
		    }

		# exclude = ["title"]       # The field that don't want to display

	# def save(self,commit=True,*args,**kwargs):         # overriding the save method to save data before
	# 	obj = super(PostModelForm,self).save(commit=False,*args,**kwargs) # operation get perform
	# 	obj.height_field = 10   # set a default value before save fire.
	# 	obj.slug=slugify(obj.title)
	# 	obj.width_field = 10
	# 	if commit:
	# 		obj.save()
	# 	else:
	# 		return obj

	# def clean_title(self,*args,**kwargs):          # Validation for title fields
	# 	title = self.cleaned_data.get("title")
	# 	if len(title)<4:
	# 		raise forms.ValidationError("Title Must be greater then 5")
	# 	else:
	# 		return title
