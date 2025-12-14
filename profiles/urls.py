from django.urls import path

from . import views

urlpatterns = [
    path("",views.mainpage,name="main-page"),
    path("home",views.homepage,name="home-page"),
    path("feed",views.feedpage,name="feed-page"),
    path("fyp",views.fyp,name="fyp"),
    path("follow/<str:username>",views.follow,name="follow"),
    path("profile/edit",views.EditProfile.as_view(),name="edit-profile"),
    path("search-users/",views.search_users,name="search-users"),
    path("chats/<str:username>",views.ChatView.as_view(),name="chat-page"),
    path("messages",views.MessageView.as_view(),name="message-list-page"),
    path("messages/<str:username>",views.MessageView.as_view(),name="message-page"),
    path("search-user-messages/",views.search_user_messages,name="search-user-messages"),
    path("favicon.ico", views.favicon_view),
    path("<str:username>",views.ProfilePage.as_view(),name="user-page"),

]