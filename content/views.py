from django.shortcuts import render
from .models import Post

# Create your views here.
def post_list(request):
	template_name = 'post_list.html'
	post = Post.objects.all().order_by('created_date')
	context = {'Post' : post}
	print(context)
	return render(request, template_name, context)
