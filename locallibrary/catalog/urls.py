#from django.urls import path
#from . import views
#from django.conf.urls import url, path



#urlpatterns = [
 #   url(r'^$', views.index, name='index'),
  #  url(r'^books/$', views.BookListView.as_view(), name='books'),
   # url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
#]


#urlpatterns = [
 #   path('', views.index, name='index'),
  #  path('books/', views.BookListView.as_view(), name='books'),
#]



from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
    re_path(r'^mybooks/$', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    re_path(r'^book/(?P<pk>[-\w]+)/renew/$', views.renew_book_librarian, name='renew-book-librarian'),
    path('author/create/', views.AuthorCreate.as_view(), name='author_create'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author_update'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author_delete'),
]
