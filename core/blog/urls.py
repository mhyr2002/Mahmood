from django.urls import path
from blog.views import *
# from blog.feeds import LatestEntriesFeed
#setare baes mishe ke tamami tavabe mojod dar in calss import she


app_name='blog'
urlpatterns = [
    path('',blog_view,name='index'),
    path('search/',blog_search,name='search'),
    path('<int:pid>',blog_single,name='single'),
    # path('category/<str:cat_name>',blog_view,name='category'),
    # path('tag/<str:tag_name>',blog_view,name='tag'),
    # path('author/<str:author_username>',blog_view,name='author'),
    # path("latest/feed/", LatestEntriesFeed()),
    # # path('post-<int:pid>',test,name='test'),
]