from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from django.contrib import messages

# Create your views here.

# 요청 정보를 받아서..
def index(request):
    # 게시글을 가져와서..
    articles = Article.objects.order_by("-pk")
    # Template에 전달한다.
    context = {"articles": articles}
    return render(request, "articles/index.html", context)


@login_required
def create(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            article_form = ArticleForm(request.POST, request.FILES)
            if article_form.is_valid():
                article_form.save()
                messages.success(request, "글 작성이 완료되었습니다.")
                return redirect("articles:index")
        else:
            article_form = ArticleForm()
        context = {"article_form": article_form}
        return render(request, "articles/form.html", context=context)
    else:
        # 다양한 해결책 존재
        # 로그인창으로 보내기
        return redirect("accounts:login")


def detail(request, pk):
    # 특정 글을 가져온다.
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    # template에 객체 전달
    context = {
        "article": article,
        "comments": article.comment_set.all(),
        "comment_form": comment_form,
    }
    return render(request, "articles/detail.html", context)


@login_required
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == "POST":
        # POST : input 값 가져와서, 검증하고, DB에 저장
        article_form = ArticleForm(request.POST, request.FILES, instance=article)
        if article_form.is_valid():
            # 유효성 검사 통과하면 저장하고, 상세보기 페이지로
            article_form.save()
            messages.success(request, "글이 수정되었습니다.")
            return redirect("articles:detail", article.pk)
        # 유효성 검사 통과하지 않으면 => context 부터해서 오류메시지 담긴 article_form을 랜더링
    else:
        # GET : Form을 제공
        article_form = ArticleForm(instance=article)
    context = {"article_form": article_form}
    return render(request, "articles/form.html", context)


@login_required
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.image.delete(save=True)
    article.delete()
    return redirect("articles:index")


@login_required
def comment_create(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.save()
    return redirect("articles:detail", article.pk)


def comments_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect("articles:detail", article_pk)
