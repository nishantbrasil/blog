from django.shortcuts import render

# Create your views here.
def post_list(request):
	template_name = 'post_list.html'
	context = {}
	return render(request, template_name, context)
