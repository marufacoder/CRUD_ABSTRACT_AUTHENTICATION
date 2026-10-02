from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from project_app.models import UserModel, ProjectModel

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        student_name = request.POST.get('student_name')
        student_id = request.POST.get('student_id')
        email = request.POST.get('email')
        password = request.POST.get('password')
        c_password = request.POST.get('c_password')
        
        user_exist = UserModel.objects.filter(username=username).exists()
        if user_exist:
            messages.error(request, 'user already exists ')
            return redirect('register_view')
        
        # Check password match
        if password == c_password:
            UserModel.objects.create_user(
                username=username,
                student_name=student_name,
                student_id=student_id,
                email=email,
                password=password,
            )
            return redirect('login_view')

    return render(request, 'register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_info = authenticate(request, username=username, password=password)
        if user_info:
            login(request, user_info)
            return redirect('home_view')
        else:
            print('Invalid credentials........')

    return render(request, 'login.html')


@login_required
def home_view(request):
    return render(request, 'home.html')


def logout_view(request):
    logout(request)
    return redirect('login_view')


# FIXED: Fetches the records from the database and sends them to the template
@login_required
def project_list(request):
    # Get all projects saved in the database
    all_projects = ProjectModel.objects.all()
    
    # Pass them to the HTML template under the key 'project_data'
    return render(request, 'project_list.html', {'project_data': all_projects})


@login_required
def add_project(request):
    if request.method == 'POST':
        project_name = request.POST.get('p_name')
        p_description  = request.POST.get('p_description')
        image = request.FILES.get('image')
        status = request.POST.get('status') # Make sure this matches the name="status" attribute in your HTML select tag
        
        ProjectModel.objects.create(
            project_name = project_name,
            project_description = p_description,
            image = image,
            status = status,
            created_by = request.user
        )
        return redirect('project_list')
    
    return render(request, 'add_project.html')


# FIXED: Cleaned up the broken syntax at the end of your file
@login_required
def update_project(request, p_id):
    project_data = ProjectModel.objects.get(id=p_id)
    if request.method == 'POST':
            project_name = request.POST.get('p_name')
            p_description  = request.POST.get('p_description')
            image = request.FILES.get('image')
            status = request.POST.get('status')

            project_data.project_name = project_name
            project_data.description = p_description
            project_data.status = status
            if image:
                project_data.image = image
          
            project_data.save()
            return redirect('project_list')

    context = {
        'project_data':project_data
    }
    return render(request, 'update_project.html',context)
def delete_project(request,p_id):
    ProjectModel.objects.get(id = p_id).delete()
    return redirect('project_list')