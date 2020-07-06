from django.shortcuts import render, get_object_or_404,redirect
from django.http import Http404
from .models import BlogModel, Post
import datetime
from .forms import BlogModelForms, My_form_blog, PostModelForm

#Create your view here
# The method based views are using here

def home(request):                   # Geeting data from html form
	# if request.method == "POST":
	# 	print("POST request data",request.POST)
	# 	userget=request.POST.get("title")  # None if no data is provided by normal get method
	# 	print(userget)
	# 	userdic=request.POST["title"]   # It raises standard error if no data is there
	# 	print(userdic)
	# elif request.method == "GET":
	# 	print("GET request data",request.GET)
	# form = SearchForm()
	# if request.method == "POST":
	# 	form = SearchForm(request.POST or None)
	# 	if form.is_valid():
	# 		print(form.cleaned_data)
	# 		BlogModel.objects.create(**form.cleaned_data)
	# 		form =  SearchForm()
	temp_path = "blog/form.html"
	context = {
	   # "form":form
	}
	return render(request,temp_path,context)

def search_form_data(request):                # saving data of django form
	form = SearchForm(request.GET or None)
	print("search_form_data get called")
	if request.method == "POST":
		form = SearchForm(request.POST or None)
		if form.is_valid():
			print(form.cleaned_data)
			BlogModel.objects.create(**form.cleaned_data)
			form =SearchForm()

	temp_path = "blog/form.html"
	context={
	  "form":form
	}
	return render(request,temp_path,context)

def blog_root_urls(request):
	temp_path = "blog/root.html"
	context = {
	}
	return render(request,temp_path,context)

def list_all_data(request):
	queryset = BlogModel.objects.all()
	temp_path = "blog/list_data.html"
	context = {
	   "list_data":queryset
	}
	return render(request,temp_path,context)

def list_all_data_url(request):                 # Geeting data from model form
	queryset = BlogModel.objects.all()
	temp_path = "blog/get_data_url.html"
	context = {
	   "list_data":queryset
	}
	return render(request,temp_path,context)

def delete_data(request, my_id):
	obj = get_object_or_404(BlogModel,id=my_id)
	if request.method == "POST":
		obj.delete()
		return redirect("https://www.google.com/")
	temp_path="blog/delete.html"
	context={
	   "object":obj
	}
	return render(request,temp_path,context)

def dynamic_id(request,my_id):
	#form = get_object_or_404(BlogModel, id=my_id) metjod used when data does not exits
	try:
		form =BlogModel.objects.get(id=my_id)
	except BlogModel.DoesNotExist:
		raise Http404
	temp_path="blog/form_details.html"
	context={
	   "data":form
	}
	return render(request,temp_path,context)

def blog_model_form_search(request):
	print(request.GET)
	print(request.POST)
	context = {
	     
	}
	temp_path = "blog/blog_search.html"
	return render(request,temp_path,context)

def my_form_data(request):                          # Getting data from django form
	initial_data = {
	   "title":"My initial title",
	   "integer":123                  # override this over form fields 
	}
	form = My_form_blog(request.GET or None, initial=initial_data)
	if request.method == "POST":
		form = My_form_blog(request.POST or None)
		if form.is_valid():
			print(form.cleaned_data)
			print(form.cleaned_data.get("title"))
			print(form.cleaned_data.get("slug"))
			print(form.cleaned_data.get("slug123"))      # None
			# print(form.cleaned_data["slug123"])          # raise error when None
			BlogModel.objects.create(**form.cleaned_data)
			form = My_form_blog()

	temp_path = "blog/my_form.html"
	context = {
	     "form":form
	}
	return render(request,temp_path,context)

def blog_model_form(request):
	initial_data={"title":"My title"}
	obj =BlogModel.objects.get(id=6) # get earlyy data
	form = BlogModelForms(request.POST or None,initial=initial_data,instance=obj)
	if form.is_valid():
		form.save()
		form = BlogModelForms()
	context = {
	     'form':form
	}
	temp_path = "blog/form_create_details.html"
	return render(request,temp_path,context)


def form_details_view(request):
	form = BlogModel.objects.get(id=2)
	context = {
	     'form':form
	}
	temp_path = "blog/form_details.html"
	return render(request,temp_path,context)

def post_form(request):
	form = PostModelForm(request.GET or None)
	if request.method == "POST":
		form = PostModelForm(request.POST or None)
		if form.is_valid():
			obj = form.save(commit=False)       # hold data to save to database
			obj.title="myrushi"                 # Forcefully save database
			obj.save()                          # save the data to database
			form=PostModelForm()
			# if form.has_error:
			# 	print(form.error.as_text())
			# 	print(form.error.as_json())
	context = {
	     'form':form
	}
	temp_path = "blog/form_details.html"
	return render(request,temp_path,context)

def filter_form(request):
	# textForm=PostModelForm(request.GET or None)
	# if request.method == "POST":
	# 	textForm=PostModelForm(request.POST or None)
	# 	if textForm.is_valid():
	# 		textForm.save()
	# 		textForm=PostModelForm()
	temp_path="blog/filterForm.html"
	context={
	  'textForm':"This is text",
	  "today":datetime.datetime.now().today(),
	  "list_data":['rushi','rushikesh','thakur']
	}
	return render(request,temp_path,context)



