from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import FileUploadForm
from .models import Document
from django.contrib.auth.models import User
from django.db.models import Q

@login_required
def home(request):
    if request.method == 'POST':   
        f_form = FileUploadForm(request.POST, request.FILES)
        if f_form.is_valid():
            new_file = f_form.save(commit=False)
            new_file.owner = request.user
            new_file.save()
            messages.success(request, f'Your File has been uploaded!')
            return redirect('knowl-home')
    else:
        f_form = FileUploadForm()

    files = Document.objects.filter(Q(owner=request.user) | Q(shared_with=request.user))

    context = {
        'f_form': f_form,
        'files' : files
    }

    return render(request, 'knowl/home.html', context)


@login_required
def share_file(request, file_id):
    file = get_object_or_404(Document, id=file_id, owner=request.user)

    shared_users = file.shared_with.all()

    available_users = User.objects.exclude(id=request.user.id).exclude(id__in=shared_users)

    if request.method == 'POST':
        shared_users = request.POST.getlist('shared_users')
        file.shared_with.set(shared_users)
        return redirect('knowl-home')

    context = {'file': file, 'users': available_users}

    return render(request, 'knowl/share_file.html', context)