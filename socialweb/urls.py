from django.urls import path
from socialweb import views

urlpatterns = [
    path('register/',views.RegistrationForm.as_view(),name="signup"),
    path('signin/',views.UserLoginForm.as_view(),name="sign-in"),
    path('index/',views.IndexView.as_view(),name="home"),
    path('logout/',views.sign_out_view,name="sign-out"),
    path('add/post/',views.PostFormView.as_view(),name="add-post"),
    path("posts/<int:id>/comment/add/",views.add_comments,name="add-comments"),
    path("post/<int:id>/like/add/",views.like_posts,name="add-likes"),
    path('profile/',views.ProfileView.as_view(),name="profile"),
    path("user/<int:id>/follower/add", views.add_follower, name="add-follower"),
    path("people",views.ListPeopleView.as_view(),name="people"),
    path("users/profile/<int:id>/change",views.EditprofileView.as_view(),name="edit-profile"),
    path("comment/<int:id>/remove",views.comment_delete,name="comment-delete"),
    path("post/<int:id>/remove",views.post_delete,name="post-delete"),
    # path('update/',views.ProfileUpdateView.as_view(),name="profile-update"),
]
