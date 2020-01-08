from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomePage, name='home_page'),
    path('about/', views.About, name='about_page'),
    path('contact/', views.ContactPage, name='contact_page'),
    path('dashboard/', views.DashboardPage, name='dashboard_page'),
    path('dashboard/blog/view/posts/', views.ViewBlogPostsPage, name='view_blog_posts_dash_page'),
    path('dashboard/blog/view/comments/', views.ViewBlogCommentsPage, name='view_blog_comments_dash_page'),
    path('dashboard/blog/add/post/', views.AddBlogPostPage, name='add_blog_post_dash_page'),
    path('dashboard/blog/delete/post/<int:post_id>', views.DeleteBlogPost, name='delete_blog_post_dash_page'),
    path('dashboard/projects/view/', views.ViewProjectsPage, name='view_projects_dash_page'),
    path('dashboard/projects/add/', views.AddProjectPage, name='add_project_dash_page'),
    path('dashboard/contact_form/responses/', views.ViewContactResponsesPage, name='view_contact_response_dash_page'),
    path('dashboard/feedback/responses/', views.ViewFeedbackResponsesPage, name='view_feedback_response_dash_page'),
    path('user/login/', views.LoginPage, name='login_page'),
    path('user/logout/', views.Logout, name='logout_page'),
    path('user/signup/', views.SignupPage, name='signup_page'),
    path('user/forgot_password/', views.LoginPage, name='forgot_password_page'),
]