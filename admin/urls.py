"""
URL configuration for brainhub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),

    path('', views.homepage, name='home'),
    # path('about/', views.aboutpage, name='about'),
    # path('contact/', views.contactpage, name='contact-us'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('newlearner/', views.newlearner, name='newlearner'),
    path('profile/', views.profile, name='profile'),
    path('all-learners/', views.all_learners, name='all-learners'),
    # Add a new URL pattern for learner profile
    path('learner_profile/', views.learner_profile, name='learner_profile'),
    #============for category=================
    path('add-category/', views.add_category, name='add-category'),
    path('all-category/', views.all_category, name='all-category'),
    path('edit_category/<int:pk>', views.edit_category, name='edit_category'),
    path('update_category/', views.update_category, name='update_category'),
    path('del_category/<int:pk>', views.del_category, name='del_category'),
    #=============end of category=======================

    #==============for course====================
    path('add_course/', views.add_course, name='add_course'),
    path('all_course/', views.all_course, name='all_course'),
    path('edit_course/<int:pk>', views.edit_course, name='edit_course'),
    path('update_course/', views.update_course, name='update_course'),
    path('del_course/<int:pk>', views.del_course, name='del_course'),
    #=====================end of course=====================

    #===================foe company=========================
    path('add_company/', views.add_company, name='add_company'),
    path('all_company/', views.all_company, name='all_company'),
    path('edit_company<int:pk>/', views.edit_company, name='edit_company'),
    path('update_company/', views.update_company, name='update_company'),
    path('del_company/<int:pk>', views.del_company, name='del_company'),
    #=====================end of company=======================

    #========================for request=======================
    path('all_request/', views.all_request, name='all_request'),
    path('accept/<int:pk>', views.accept, name='accept'),
    path('reject/<int:pk>', views.reject, name='reject'),
    #=========================end of request====================


    #=========================for learner======================
    path('learner_all_course_list/', views.learner_all_course_list, name='learner_all_course_list'),
    path('enroll_course/<int:pk>', views.enroll_course, name='enroll_course'),
    path('read_more/<int:pk>', views.read_more, name='read_more'), 
    path('all-category-learner/', views.all_category_learner, name='all-category-learner'),
    path('all_company-learner/', views.all_company_learner, name='all_company-learner'), 
    #========================end of learners====================

    #==========================otp===============================
    path('forget_password/', views.forget_password, name='forget_password'),
    path('reset_password/', views.reset_password, name='reset_password'),
    #==============================end of otp===================


]

# http://127.0.0.1:8000/myapp/home/
# http://127.0.0.1:8000/myapp/about/

# http://127.0.0.1:8000/ -- actual url
