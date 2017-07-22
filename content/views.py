from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm

# Create your views here.
def post_list(request):
	template_name = 'post_list.html'
	post = Post.objects.all().order_by('created_date')
	context = {'Post' : post}
	print(context)
	return render(request, template_name, context)

def post_new(request):
	template_name = 'new.html'
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author	= request.user
			#post.published_date	= timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)

	form = PostForm()
	context = {'form': form}
	return render(request, template_name, context)

def	post_detail(request, pk):
	post = get_object_or_404(Post,	pk=pk)
	return render(request, 'post_detail.html', {'post': post})
