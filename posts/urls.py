from django.urls import path

from . import views


urlpatterns = [
    path("<int:id>",views.PostView.as_view(),name="post"),
    path("<int:id>/add-comment",views.add_comment,name="add-comment"),
    path("like/<int:id>",views.add_like,name="add-like"),
    path("like/comment/<int:id>/<int:cmnt_id>",views.comment_add_like,name="like-comment"),
    path("like/reply/<int:id>/<int:reply_id>",views.reply_add_like,name="like-reply"),
]
