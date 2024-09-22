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
    post_first = Post.objects.filter(status=1).order_by('-counted_view')[0]
    
    posts_second_third =Post.objects.filter(status=1).order_by('-counted_view')[1:3]
    return {
        'post_first': post_first,
        'posts_second_third' : posts_second_third
        }

#function for counting comment
@register.simple_tag(name='comment_count')
def function(pid):
    return Comment.objects.filter(post=pid,approved=True).count()

@register.inclusion_tag('blog/admin-selected-blog.html')
def admin_selected_blog():
    posts = Post.objects.filter(status=1).order_by('admin_selected' , 'updated_date')
    post = posts[0]
    if post.admin_selected == False :
        post = Post.objects.filter(status=1).order_by('-created_date')[0]
    return {'post': post}
        