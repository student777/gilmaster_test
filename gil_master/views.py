from django.shortcuts import render, get_object_or_404, redirect
from gil_master.models import Post, Comment
from gil_master.forms import PostForm, CommentForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.http import JsonResponse

# Create your views here.


def index(request):
    post_list = Post.objects.all()

    return render(request, 'gil_master/index.html', {
        'post_list': post_list
        }
    )


def test(request):
    post_list = Post.objects.all()
    return render(request, 'gil_master/test.html', {
        'post_list': post_list
        }
    )


def test2(request):
    return render(request, 'gil_master/test2.html')


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comment_form = CommentForm()
    return render(request, 'gil_master/detail.html', {
        'post': post,
        'comment_form': comment_form,
        }
    )


@csrf_exempt
def new(request):
    # print("---- new ----")
    # print("request.GET = {}".format(request.GET))
    # print("request.POST = {}".format(request.POST))
    # print("request.FILES = {}".format(request.FILES))

    lat = request.GET.get('lat', None)
    lng = request.GET.get('lng', None)
    if lat and lng:
        lnglat = '{},{}'.format(lng, lat)
    else:
        lnglat = None

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            # title = form.cleaned_data['title']
            # content = form.cleaned_data['content']
            # photo = form.cleaned_data['photo']
            # post = Post(title=title, content=content, photo=photo)
            form.save()
            messages.info(request, '새 포스팅!')

            return redirect('index')
    else:
        form = PostForm(initial={'lnglat': lnglat})

    return render(request, "gil_master/form.html", {
        'form': form,
    })


@csrf_exempt
def edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid:
            form.save()
            return redirect('index')
    else:
        form = PostForm(instance=post)
    return render(request, 'gil_master/form.html', {
        'form': form,
        })


def comment_new(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            messages.success(request, "새 댓글!")
            return redirect('detail', pk)
    else:
        form = CommentForm()

    return render(request, "gil_master/form.html", {
        'form': form,
    })


@csrf_exempt
def comment_delete(request, pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.method == 'POST':
        comment.delete()
        messages.success(request, '댓글을 삭제했습니다.')
        return JsonResponse({'status': 'ok'})


def delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        messages.success(request, '포스팅을 삭제했습니다.')
        return redirect('index')
    return render(request, 'gil_master/post_delete_confirm.html', {'post': post})
