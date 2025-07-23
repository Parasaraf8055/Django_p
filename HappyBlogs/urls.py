from django.urls import path
from . import views

urlpatterns = [
    path("",views.All_blogs,name="All_blogs"),
    path("create/",views.create_blog,name="create_blog"),
    path("update/<int:id>",views.update_blog,name="update_blog"),
    path("delete/<int:id>",views.delete_blog,name="delete_blog"),
]


