from django import template 
from blog.models import Post,Comment
from blog.models import Category

register = template.Library()

# @register.simple_tag
# def abc(a):
#     a = a + 1
#     return a

@register.inclusion_tag('blog/blog-post-category.html')
def postcategories():
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dic= {}
    for name in categories :
        cat_dic[name] = posts.filter(category=name).count()
    return {'categories': cat_dic}


@register.inclusion_tag('blog/blog-popular-post.html')
def most_view_posts():
    posts =Post.objects.filter(status=1).order_by('-counted_view')[0:3]
    post_first = posts[0]
    post_second = posts[1]
    post_third = posts[2]

    return {
        'post_first': post_first,
        'post_second' : post_second,
        'post_third' : post_third
        }

#function for counting comment
@register.simple_tag(name='comment_count')
def function(pid):
    return Comment.objects.filter(post=pid,approved=True).count()

@register.inclusion_tag('blog/admin-selected-blog.html')
def admin_selected_blog():
    posts = Post.objects.filter(status=1).order_by('-updated_date' )
    posts = posts.filter(admin_selected=True)
    post = posts[0]
    if post.admin_selected == False :
        post = Post.objects.filter(status=1).order_by('-created_date')[0]
    return {'post': post}
        