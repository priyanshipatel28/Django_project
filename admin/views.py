from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse 
from .models import *
import random
from .utils import *
# Create your views here.

# def homepage(request):
#     if "email" in request.session:
#         uid = User.objects.get(email = request.session['email'])
#         if uid.role == "Admin":
#             aid = AdminUser.objects.get(user_id = uid)
#             context={
#                 'uid' :uid,
#                 'aid' :aid,
#             }
#             return render(request,"myapp/index.html",context)
#         else:
#             return render(request,"myapp/login.html")
#     return render(request,"myapp/login.html")

# def homepage(request):
#     # ✅ Check if the user is logged in (session contains "email")
#     if "email" in request.session:  
        
#         # ✅ Get the user details using the email stored in the session
#         uid = User.objects.get(email=request.session['email'])  

#         # ✅ Check if the logged-in user is an Admin
#         if uid.role == "Admin":  
            
#             # ✅ Get Admin details (linked to the User model using ForeignKey)
#             aid = AdminUser.objects.get(user_id=uid)  

#             # ✅ Prepare data (context) to send to the HTML page
#             context = {
#                 'uid': uid,  # User details
#                 'aid': aid,  # Admin details
#             }

#             # ✅ Render and show "index.html" with the user's details
#             return render(request, "myapp/index.html", context)  

#         else:  
#             # ❌ If the user is NOT an Admin, show the login page again
#             return render(request, "myapp/login.html")  

#     # ❌ If "email" is NOT in session (user not logged in), show login page
#     return render(request, "myapp/login.html")  

def homepage(request):
    if "email" in request.session:  
        uid = User.objects.get(email=request.session['email'])  

        if uid.role == "Admin":  
            aid = AdminUser.objects.get(user_id=uid)  

            # Fetch counts
            category_count = category.objects.count()
            course_count = Course.objects.count()
            company_count = company.objects.count()

            # Fetch the last 5 records
            last_5_categories = category.objects.all().order_by('-id')[:5]
            last_5_courses = Course.objects.all().order_by('-id')[:5]
            last_5_companies = company.objects.all().order_by('-id')[:5]

            context = {
                'uid': uid,
                'aid': aid,
                'category_count': category_count,
                'course_count': course_count,
                'company_count': company_count,
                'last_5_categories': last_5_categories,
                'last_5_courses': last_5_courses,
                'last_5_companies': last_5_companies,
            }
            print(f"Admin Dashboard: Categories={category_count}, Courses={course_count}, Companies={company_count}")

            return render(request, "myapp/index.html", context)  
        
        elif uid.role == "learners":
            lid = learners.objects.get(user_id=uid)  

            # Fetch counts
            category_count = category.objects.count()
            course_count = Course.objects.count()
            company_count = company.objects.count()

            # Fetch the last 5 records
            last_5_categories = category.objects.all().order_by('-id')[:5]
            last_5_courses = Course.objects.all().order_by('-id')[:5]
            last_5_companies = company.objects.all().order_by('-id')[:5]

            context = {
                'uid': uid,
                'lid': lid,
                'category_count': category_count,
                'course_count': course_count,
                'company_count': company_count,
                'last_5_categories': last_5_categories,
                'last_5_courses': last_5_courses,
                'last_5_companies': last_5_companies,
            }
            print(f"Admin Dashboard: Categories={category_count}, Courses={course_count}, Companies={company_count}")

            return render(request, "myapp/learner_index.html", context)
        
        else:  
            return render(request, "myapp/login.html")  
    
    return render(request, "myapp/login.html")  
 



# def login(request):
#     if "email" in request.session:
#         uid = User.objects.get(email = request.session['email'])
#         if uid.role == "Admin":
#             aid = AdminUser.objects.get(user_id = uid)
#             context={
#                 'uid' :uid,
#                 'aid' :aid,
#             }
#             # request.session['email']=email
#             return render(request,"myapp/index.html",context)
#     # else:
#     if request.POST:
#         try:
#             print("===>> submit button press")
#             email = request.POST["email"]
#             password = request.POST['password']

#             uid = User.objects.get(email=email)
#             if uid.password == password:
#                 if uid.role == 'Admin':
#                     aid = AdminUser.objects.get(user_id = uid)
#                     context={
#                             'uid' :uid,
#                             'aid' :aid,
#                         }

#                         #store data in session
#                     request.session['email']=email
#                     return render(request,"myapp/index.html",context)
#                 else:
#                     lid = learners.objects.get(user_id = uid)
#                     context={
#                             'uid' :uid,
#                             'lid' :lid,
#                         }

#                         #store data in session
#                     request.session['email']=email
#                     return render(request,"myapp/learner_index.html",context)
#             else:
#                 context={
#                         'e_msg' : "invalid password"
#                     }
#                 return render(request,"myapp/login.html",context)
#                 # print("something ====>> ",uid)
#                 # return render(request,"myapp/index.html")
#         except Exception as e:
#             print("====>",e)
#             context = {
#                 'e_msg' : "invalid email or password"
#                 }
#             return render(request,"myapp/login.html",context)
#     else:
#         print("===>> login page")
#         return render(request,"myapp/login.html")
    
def login(request):
    # If the user is already logged in (email exists in session), redirect to index page
    if "email" in request.session:
        uid = User.objects.get(email=request.session['email'])  # Get user details using session email
        if uid.role == "Admin":  # Check if user is an admin
            aid = AdminUser.objects.get(user_id=uid)  # Get admin details
            context = {
                'uid': uid,
                'aid': aid,
            }
            # request.session['email'] = email  # (Commented out) No need to set session again
            return render(request, "myapp/index.html", context)  # Redirect to admin dashboard

    # If request method is POST, process login form submission
    if request.POST:
        try:
            print("===>> submit button pressed")  # Debugging print statement

            email = request.POST["email"]  # Get email from login form
            password = request.POST['password']  # Get password from login form

            uid = User.objects.get(email=email)  # Fetch user details from database using email

            if uid.password == password:  # Check if entered password matches stored password
                if uid.role == 'Admin':  # If user is an admin
                    aid = AdminUser.objects.get(user_id=uid)  # Get admin details
                    context = {
                        'uid': uid,
                        'aid': aid,
                    }

                    # Store email in session to keep the user logged in
                    request.session['email'] = email
                    return render(request, "myapp/index.html", context)  # Redirect to admin dashboard

                else:  # If user is a learner
                    lid = learners.objects.get(user_id=uid)  # Get learner details
                    context = {
                        'uid': uid,
                        'lid': lid,
                    }

                    # Store email in session to keep the user logged in
                    request.session['email'] = email
                    return render(request, "myapp/learner_index.html", context)  # Redirect to learner dashboard

            else:  # If password is incorrect
                context = {
                    'e_msg': "Invalid password"  # Error message for incorrect password
                }
                return render(request, "myapp/login.html", context)  # Reload login page with error message

        except Exception as e:  # If email doesn't exist in the database or any other error occurs
            print("====>", e)  # Print error for debugging
            context = {
                'e_msg': "Invalid email or password"  # Error message for invalid login details
            }
            return render(request, "myapp/login.html", context)  # Reload login page with error message

    else:  # If request method is GET (when user opens login page)
        print("===>> login page")  # Debugging print statement
        return render(request, "myapp/login.html")  # Load login page


def logout(request):
    if "email" in request.session:
        del request.session['email']
        return render(request,"myapp/login.html")
    else:
        return render(request,"myapp/login.html")
    
def newlearner(request):
    if request.POST:
        username = request.POST['username']
        email = request.POST['email']
        contactno = request.POST['contact-no']
        gender = request.POST['gender']
        # city = request.POST['city']
        # qualification = request.POSt['qualification']

        l1 = ['df456','67hj8','78hjk','jk880']
        password = random.choice(l1)+email[2:5]+contactno[2:5]

        uid = User.objects.create(email = email,
                                  password = password,
                                  role = "learners"
                                  )
        if uid :
            lid = learners.objects.create(
                user_id = uid,
                username = username,
                contactno = contactno,
                gender=gender,
                # city=city,
                # qualification=qualification 
                    )
            if lid:
                context = {
                's_msg' : "Successfully Account Created  : ) !! please check your email box for password",
                'gender': gender,
                'lid' :lid,
                'uid' :uid,
                'password' :password 
                }
                sendMailFunction("PASSWORD","password_mail_template",email,context)
                return render(request,"myapp/login.html",context)
        else:
            context = {
                'e_msg' : "something went wrong!"
                }
            return render(request,"myapp/registration.html",context,{'gender': gender})

    else:
        return render(request,"myapp/registration.html")


def profile(request):
    if "email" in request.session:
        if request.POST:
            print("===>>> update page")
            uid = User.objects.get(email = request.session['email'])
            if uid.role == "Admin":
                aid = AdminUser.objects.get(user_id = uid)

                aid.username = request.POST['username']
                aid.contactno = request.POST['contactno']
                
                if "pic" in request.FILES:
                    aid.pic = request.FILES["pic"]

                aid.save()

                context={
                    'uid' :uid,
                    'aid' :aid,
                }
                # request.session['email'] = email
                return render(request,"myapp/profile.html",context)
        else:
            uid = User.objects.get(email = request.session['email'])
            if uid.role == "Admin":
                aid = AdminUser.objects.get(user_id = uid)
                context={
                    'uid' :uid,
                    'aid' :aid,
                }
                # request.session['email'] = email
                return render(request,"myapp/profile.html",context)
    else:
        return render(request,"myapp/login.html")
    
def all_learners(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == "Admin":
            aid = AdminUser.objects.get(user_id = uid)
            learners_all = learners.objects.all()
            context={
                    'uid' :uid,
                    'aid' :aid,
                    'learners_all' : learners_all
                }
                # request.session['email'] = email
            return render(request,"myapp/learners.html",context)       
    else:
        return render(request,"myapp/login.html")

def learner_profile(request):
    if "email" in request.session:
        if request.POST:
            uid=User.objects.get(email = request.session['email'])
            if uid.role == "learners":
                lid=learners.objects.get(user_id=uid)
                
                lid.username=request.POST['user_name']
                lid.contactno=request.POST['contact_no']
                
                if "pic" in request.FILES:
                    lid.pic=request.FILES["pic"]
                lid.save()  

                context={
                    'uid': uid,
                    'lid': lid
                }
                return render(request,"myapp/learners_profile.html",context)
        else:
            uid=User.objects.get(email = request.session['email'])
            if uid.role == "learners":
                lid=learners.objects.get(user_id=uid)
                        
                context={
                            'uid': uid,
                            'lid': lid,
                            
                        }
                return render(request,"myapp/learners_profile.html",context)
    else:
        return render(request,"myapp/login.html")

def add_category(request):
    if "email" in request.session:
        if request.POST:
            uid = User.objects.get(email = request.session['email'])
            if uid.role == "Admin":
                aid = AdminUser.objects.get(user_id = uid)

                if "category_pic" in request.FILES:
                    cid = category.objects.create(user_id = uid,category_name=request.POST['category_name'],category_pic = request.FILES['category_pic'])
                else:
                    cid = category.objects.create(user_id = uid,category_name=request.POST['category_name'])


            
                context={
                        'uid' :uid,
                        'aid' :aid,
                        's_msg' : "successfully category added !!"
                    }
                    # request.session['email'] = email
                return render(request,"myapp/add_category.html",context)     
        else:
            uid = User.objects.get(email = request.session['email'])
            if uid.role == "Admin":
                aid = AdminUser.objects.get(user_id = uid)
            
                context={
                        'uid' :uid,
                        'aid' :aid,
                    }
                    # request.session['email'] = email
                return render(request,"myapp/add_category.html",context)     

def all_category(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == "Admin":
            aid = AdminUser.objects.get(user_id = uid)
            call = category.objects.all() 
            context={
                        'uid' :uid,
                        'aid' :aid,
                        'call' :call,
                    }
                    # request.session['email'] = email


            return render(request,"myapp/all_category.html",context)     
        

#============================for edit of category=======================================
def edit_category(request,pk):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == "Admin":
            aid = AdminUser.objects.get(user_id = uid)
            cid = category.objects.get(id = pk)

            context={
                        'uid' :uid,
                        'aid' :aid,
                        'cid' :cid,
                    }
                    # request.session['email'] = email
            return render(request,"myapp/edit_category.html",context)
#===============================end of edit of category===================================

#===================================updating data of category==========================      
def update_category(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == "Admin":
            aid = AdminUser.objects.get(user_id = uid)
            
            category_id = request.POST['categoryid']

            cid = category.objects.get(id = category_id)

            cid.category_name = request.POST['category_name']
            cid.save()

            if "category_pic" in request.FILES:
                cid.category_pic = request.FILES['category_pic']
                cid.save()

            call = category.objects.all()
            context={
                        'uid' :uid,
                        'aid' :aid,
                        'call' :call
                    }
                    # request.session['email'] = email
            return render(request,"myapp/all_category.html",context)    
#======================================end of updating data of category===================== 

#=====================================delete the data of category=========================
def del_category(request,pk):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == "Admin":
            aid = AdminUser.objects.get(user_id = uid)
            
            cid = category.objects.get(id=pk)

            cid.delete()

            call = category.objects.all()
            context={
                        'uid' :uid,
                        'aid' :aid,
                        'call' :call
                    }
                    # request.session['email'] = email
            return render(request,"myapp/all_category.html",context) 
#=================================delete the data of category===============================
        
#=====================================add data in add_course=============================
def add_course(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        if request.POST:
            if uid.role == "Admin":
                aid = AdminUser.objects.get(user_id = uid)
                lid = learners.objects.all()
                call = category.objects.all()

                category_name = request.POST['category']
                cid = category.objects.get(category_name=category_name)
                print("======> this ",call)
                course_id = Course.objects.create(user_id = uid,
                                                  category_id = cid,
                                                  course_name = request.POST['course_name'],
                                                  course_duration = request.POST['course_duration'],
                                                  fees = request.POST['fees'],
                                                  course_description = request.POST['course_description'],
                                                  course_lecture_flow = request.FILES['course_lecture_flow'],
                                                  course_handbook = request.FILES['course_handbook'],
                                                  course_interview_questions = request.FILES['course_interview_questions'],
                                                  coure_assignments = request.FILES['coure_assignments'],
                                                  coure_pic = request.FILES['coure_pic'],
                                                  course_tutor_name = request.POST['course_tutor_name'],
                                                  video_url=request.POST.get('video_url', ''),
                                                  quiz_url=request.POST.get('quiz_url', ''), 
                                                  )

                if course_id:
                    l = []
                    for learner in lid:  
                        l.append(learner.user_id.email) 

                    print("=========>", l)
                    s_msg = "Successfully Course Detaied Added !!!"
                    context={
                                'uid' :uid,
                                'aid' :aid,
                                'call' :call,
                                's_msg' :s_msg,
                                'course_id' :course_id

                            }
                    sendMailTOAllFunction("NEW COURSE","course_mail_template",l,context)
                    return render(request,"myapp/add_course.html",context) 
                else:
                    e_msg = "Something went wrong !!!"
                    context={
                                'uid' :uid,
                                'aid' :aid,
                                'call' :call,
                                'e_msg' :e_msg

                            }
                            # request.session['email'] = email
                    return render(request,"myapp/add_course.html",context) 

        else:
            if uid.role == "Admin":
                aid = AdminUser.objects.get(user_id = uid)
                call = category.objects.all()
                context={
                            'uid' :uid,
                            'aid' :aid,
                            'call' :call
                        }
                        # request.session['email'] = email
                return render(request,"myapp/add_course.html",context)
#======================================end of add_course===========================

#===================================add all_course==============================
def all_course(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == "Admin":
            aid = AdminUser.objects.get(user_id = uid)
            call = Course.objects.all()
            context={
                        'uid' :uid,
                        'aid' :aid,
                        'call' :call
                    }
                    # request.session['email'] = email
            return render(request,"myapp/all_course_list.html",context) 
#====================================end of all_course=============================

#===================================edit of all_course===========================
def edit_course(request,pk):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == "Admin":
            aid = AdminUser.objects.get(user_id = uid)
            cid = Course.objects.get(id = pk)

            context={
                        'uid' :uid,
                        'aid' :aid,
                   
                        'cid' :cid,
                    }
                    # request.session['email'] = email
            return render(request,"myapp/edit_course.html",context)
#==============================end of edit_courese===================================

#============================for update_course===========================
def update_course(request):
     if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == "Admin":
            aid = AdminUser.objects.get(user_id = uid)
            
            courseid = request.POST['courseid']
            cid = Course.objects.get(id = courseid)

            if request.POST:
                cid.course_name = request.POST['course_name']
                cid.course_duration = request.POST['course_duration']
                cid.fees = request.POST['fees']
                cid.course_description = request.POST['course_description']
                cid.course_tutor_name = request.POST['course_tutor_name']
                cid.video_url = request.POST.get('video_url', '') 
                cid.quiz_url = request.POST.get('quiz_url', '') 

                cid.save()
                if 'course_lecture_flow' in request.FILES:
                    cid.course_lecture_flow = request.FILES['course_lecture_flow']
                if 'course_handbook' in request.FILES:
                    cid.course_handbook = request.FILES['course_handbook']
                if 'course_interview_questions' in request.FILES:
                    cid.course_interview_questions = request.FILES['course_interview_questions']
                if 'coure_assignments' in request.FILES:
                    cid.coure_assignments = request.FILES['coure_assignments']
                if "coure_pic" in request.FILES:
                    cid.coure_pic = request.FILES['coure_pic']
                    
                    
                cid.save()
                courses = Course.objects.all()
                s_msg = "Course Updated Successfully!"
                context = {
                    'uid': uid,
                    'aid': aid,
                    'courses': courses,
                    's_msg': s_msg
                }
                # return render(request, "myapp/all_course_list.html", context)
                return redirect('all_course')

            else:
                context={
                            'uid' :uid,
                            'aid' :aid,
                            'cid' : cid
                        }
                return render(request,"myapp/edit_course.html",context)
                
            #=========================end of update_course====================================

#==============================for del_course==========================
def del_course(request,pk):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == "Admin":
            aid = AdminUser.objects.get(user_id = uid)
            cid = Course.objects.get(id = pk)

            cid.delete()

            call = Course.objects.all()
            s_msg = "Course deleted successfully!"
            context={
                        'uid' :uid,
                        'aid' :aid,
                        'call' :call,
                        's_msg' : s_msg
                     }
                    # request.session['email'] = email
            return render(request,"myapp/all_course_list.html",context) 
#=================================end of del_course============================

#============================for add_comapany====================
def add_company(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        if request.POST:
            if uid.role == "Admin":
                aid = AdminUser.objects.get(user_id = uid)
                # call = company.objects.all()
                
                #this is company_website 
                company_website = request.POST.get('company_website', '').strip()
                if not company_website:  
                    company_website = "https://www.learnvern.com/"
                #this is end for website
                        
                if "company_logo" in request.FILES:
                    company_id = company.objects.create(user_id = uid,
                                                    company_name = request.POST['company_name'],
                                                    company_logo = request.FILES['company_logo'],
                                                    company_description = request.POST['company_description'],
                                                    company_website = company_website,
                                                    email = request.POST['email'],
                                                    phone_number = request.POST['phone_number'],
                                                    location = request.POST['location']
                                                        )
                else:
                    company_id = company.objects.create(user_id = uid,
                                                    company_name = request.POST['company_name'],
                                                    company_description = request.POST['company_description'],
                                                    company_website = company_website,
                                                    email = request.POST['email'],
                                                    phone_number = request.POST['phone_number'],
                                                    location = request.POST['location']
                                                        )
                
                if company_id:
                    s_msg = "Company details added successfully!"
                    context = {
                        'uid': uid,
                        'aid': aid,
                        's_msg': s_msg
                    }
                    return render(request, "myapp/add_company.html", context)
                else:
                    e_msg = "Something went wrong!"
                    context = {
                        'uid': uid,
                        'aid': aid,
                        'e_msg': e_msg
                    }
                    return render(request, "myapp/add_company.html", context)

        else:
            if uid.role == "Admin":
                aid = AdminUser.objects.get(user_id=uid)
                context = {
                        'uid': uid,
                        'aid': aid
                    }
                return render(request, "myapp/add_company.html", context)
                    
#========================end of add_company================================

#===========================for all-company data===========================
def all_company(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == "Admin":
            aid = AdminUser.objects.get(user_id = uid)
            call = company.objects.all()
            context={
                        'uid' :uid,
                        'aid' :aid,
                        'call' :call
                    }
                    # request.session['email'] = email
            return render(request,"myapp/all_company.html",context) 
        
#============================end of all_comapny=======================

#===============================for edit_company========================
def edit_company(request,pk):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == "Admin":
            aid = AdminUser.objects.get(user_id = uid)
            cid = company.objects.get(id = pk)

            context={
                        'uid' :uid,
                        'aid' :aid,
                   
                        'cid' :cid,
                    }
                    # request.session['email'] = email
            return render(request,"myapp/edit_company.html",context)
#===============================end of edit_company=======================

#===============================for update_comapny===================
# ====> here i have used redirect for that i have written :-from django.shortcuts import render,redirect in first lin of code!!!

def update_company(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == "Admin":
            aid = AdminUser.objects.get(user_id = uid)
            
            companyid = request.POST['companyid']
            cid = company.objects.get(id = companyid)

            if request.POST:
                cid.company_name = request.POST['company_name']
                cid.company_website = request.POST['company_website']
                cid.email = request.POST['email']
                cid.company_description = request.POST['company_description']
                cid.location = request.POST['location']
                cid.phone_number = request.POST['phone_number']
                
                cid.save()
                if 'company_logo' in request.FILES:
                    cid.company_logo = request.FILES['company_logo']
                    
                cid.save()
                courses = company.objects.all()
                s_msg = "Course Updated Successfully!"
                context = {
                    'uid': uid,
                    'aid': aid,
                    'companyid' : companyid,
                    's_msg': s_msg
                }
                # return render(request, "myapp/all_company.html", context)
                return redirect('all_company')

            else:
                context={
                            'uid' :uid,
                            'aid' :aid,
                            'cid' : cid
                        }
                return render(request,"myapp/edit_company.html",context)
#=======================end for update_company=======================

#==============================for delete company========================
def del_company(request,pk):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == "Admin":
            aid = AdminUser.objects.get(user_id = uid)
            cid = company.objects.get(id = pk)

            cid.delete()

            call = company.objects.all()
            s_msg = "company deleted successfully!"
            context={
                        'uid' :uid,
                        'aid' :aid,
                        'call' :call,
                        's_msg' : s_msg
                     }
                    # request.session['email'] = email
            return render(request,"myapp/all_company.html",context) 
        
#======================= for learner to show all courses====================

def learner_all_course_list(request):
    if "email" in request.session:
        uid = User.objects.get(email=request.session['email'])
        if uid.role == "learners":
            lid = learners.objects.get(user_id=uid)
            all_courses = Course.objects.all()

            # Fetch courses where learner has already enrolled
            enrolled_courses = add_enroll_course.objects.filter(learners_id=lid)

            # Create a dictionary to store enrollment status for each course
            enrolled_dict = {enroll.course_id.id: enroll.status for enroll in enrolled_courses}

            print("Courses Found:", all_courses)  
            print("Enrolled Courses:", enrolled_courses)
            print("Enrollment Status Dict:", enrolled_dict)

            context = {
                'uid': uid,
                'lid': lid,
                'all_courses': all_courses,  # This should match the template
                'enrolled_dict': enrolled_dict,  # Send enrollment status dictionary
            }
            return render(request, "myapp/learner_all_course_list.html", context)

    return redirect('login')


#==============================end for learner to show!!!=====================

#============================for enroll course=======================
# def enroll_course(request,pk):
#     if "email" in request.session:
#         uid = User.objects.get(email = request.session['email'])
#         if uid.role == "learners":
#             lid = learners.objects.get(user_id =uid)
#             id = Course.objects.get(id=pk)
#             e_id = add_enroll_course.objects.create(user_id = uid,
#                                                     learners_id = lid,
#                                                     course_id = id,
#                                                     fees_status = "PENDING",

#             )
#             if e_id:
#                 s_msg = "Enrollment request send please wait !"

#                 context = {
#                     'uid' : uid,
#                     'lid' : lid,
#                     's_msg' : s_msg
#                 }
#                 return redirect('learner_all_course_list')

                # return render(request,"myapp/learner_all_course_list.html",context)

def enroll_course(request, pk):
    """Handles learner enrollment requests"""
    if "email" in request.session:
        uid = User.objects.get(email=request.session['email'])
        if uid.role == "learners":
            learner = learners.objects.get(user_id=uid)
            course = Course.objects.get(id=pk)

            # Check if learner already requested enrollment
            enrollment, created = add_enroll_course.objects.get_or_create(
                user_id=uid,
                learners_id=learner,
                course_id=course,
                fees_status = "PENDING",
            )

            # If newly created, set status to "PENDING"
            if created:
                enrollment.status = "PENDING"
                enrollment.save()

            # return redirect('read_more', pk=pk)  # Redirect to refresh page
            return redirect('learner_all_course_list')

    return redirect('login') 

#=========================end of enroll course===========================

# #================================all request================================

def all_request(request):
    if "email" in request.session:
        uid = User.objects.get(email=request.session['email'])
        if uid.role == "Admin":
            aid = AdminUser.objects.get(user_id=uid)
            e_id = add_enroll_course.objects.all()  # Fetch all requests
            print("==============>",e_id)
            context = {
                'uid': uid,
                'aid': aid,
                'e_id': e_id,  # Pass all requests to the template
            }
            return render(request, "myapp/all_request.html", context)
    return redirect('login')


#================================end of all request=========================

#===========================for accept==============================
def accept(request,pk):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == "Admin":
            try:
                enrollment= add_enroll_course.objects.get(id = pk)

                learner_name = enrollment.learners_id.username
                learner_email = enrollment.learners_id.user_id.email
                print("========>",learner_email)
                course_name = enrollment.course_id.course_name

                enrollment.status = "APPROVED"
                enrollment.save()

                # s_msg = "successfully password resel !!"
                
                context = {
                    'l_n' : learner_name,
                    'l_e' : learner_email,
                    'c_n' : course_name,
                    # 's_msg' : s_msg
                } 

                sendMailFunction("APPROVE REQUEST", "accept_template", learner_email, context)
                
                return redirect("all_request")
            except add_enroll_course.DoesNotExist:
                return render(request, 'error.html', {'error': 'Enrollment request does not exist.'})
    else:
        return redirect('login')

#===========================end of accept==========================

#================================fro reject=========================
def reject(request,pk):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == "Admin":
            try:
                enrollment= add_enroll_course.objects.get(id = pk)

                learner_name = enrollment.learners_id.username
                learner_email = enrollment.learners_id.user_id.email
                course_name = enrollment.course_id.course_name

                enrollment.status = "REJECTED"
                enrollment.save()

                # s_msg = "successfully password resel !!"
                
                context = {
                    'l_n' : learner_name,
                    'l_e' : learner_email,
                    'c_n' : course_name,
                    # 's_msg' : s_msg
                }

                sendMailFunction("Reject REQUEST", "reject_template", learner_email, context)
                
                return redirect("all_request")
            except add_enroll_course.DoesNotExist:
                return render(request, 'error.html', {'error': 'Enrollment request does not exist.'})
    else:
        return redirect('login')
#==============================end of reject========================

#=================================forget-password========================
def forget_password(request):
    if request.POST:
        email = request.POST['email']
        try:
            uid = User.objects.get(email = email)

            if uid:

                if uid.role == "learners":
                    pass
                elif uid.role == "Admin":
                    aid = AdminUser.objects.get(user_id=uid)
                    otp = random.randint(111111,999999)
                    uid.otp = otp  # Assuming your User model has an `otp` field
                    uid.save()
                    print("=========>",otp)
                    context = {
                        "otp":otp,
                        "aid" : aid
                    }
                    print(f"Email: {email}, User: {uid}, Role: {uid.role}")

                    sendMailFunction("Forgot-password","mail_template",email,context)
                    context = {
                        'email' : email
                    }
                    return render(request,"myapp/reset_password.html",context)
            return render(request, "myapp/forget_password.html", {'e_msg': "Invalid role or operation not supported!"})
        except:

            context = {
                'e_msg' : "invalid email address - does not exists ! "
            }
            return render(request,"myapp/forget_password.html",context)
    else:
        return render(request,"myapp/forget_password.html")
#=============================end f forhet-password=====

#==============================reset-password=================
def reset_password(request):
    if request.POST:
        print("============>",request.POST)

        email = request.POST['email']
        uid = User.objects.get(email = request.POST['email'])
        otp = request.POST["otp"]
        print("===========>>> otp",otp)
        newpassword = request.POST['newpassword']
        repassword = request.POST['confirmpassword']
        if str(uid.otp) == otp:
            if newpassword == repassword:
                uid.password = newpassword
                uid.save()
                s_msg = "successfully password resel !!"
                context = {

                's_msg' : s_msg
            }
            return render(request,"myapp/login.html",context)
        else:
            context = {

                'e_msg' : "invalid otp",
                'email' : email
            }
            return render(request,"myapp/reset_password.html",context)
    else:
        return render(request, "myapp/reset_password.html")
#====================================end of reset password======================

#==============================for read_more==========================
# def read_more(request,pk):
#     return render(request,"myapp/read_more.html")

def read_more(request, pk):
    if "email" in request.session:
        uid = User.objects.get(email=request.session['email'])
        if uid.role == "learners":
            lid = learners.objects.get(user_id=uid)
            course = Course.objects.get(id=pk)
            context = {
                'course': course,  # Pass only this course's data
                'uid' : uid,
                'lid' : lid,
            }
            return render(request, "myapp/read_more.html", context)
    return redirect("login")
#=============================end of read_more===================

#===============================to show all category==============
def all_category_learner(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == "learners":
            lid = learners.objects.get(user_id = uid)
            call = category.objects.all() 
            context={
                        'uid' :uid,
                        'lid' :lid,
                        'call' :call,
                    }


            return render(request,"myapp/all_category_learner.html",context)     
        
#==============================end of category====================

#============================to show all company=====================
def all_company_learner(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == "learners":
            lid = learners.objects.get(user_id = uid)
            call = company.objects.all()
            context={
                        'uid' :uid,
                        'lid' :lid,
                        'call' :call
                    }
                    # request.session['email'] = email
            return render(request,"myapp/all_company_learner.html",context) 
    

#===============================end of company==========================