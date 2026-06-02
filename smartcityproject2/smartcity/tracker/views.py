from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, IssueForm
from .models import Issue,Notification


def home(request):
    return render(request, 'home.html')


def register(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')

    else:
        form = RegisterForm()

    return render(
        request,
        'register.html',
        {'form': form}
    )


@login_required
def dashboard(request):

    total = Issue.objects.filter(
        user=request.user
    ).count()

    pending = Issue.objects.filter(
        user=request.user,
        status='Pending'
    ).count()

    progress = Issue.objects.filter(
        user=request.user,
        status='In Progress'
    ).count()

    resolved = Issue.objects.filter(
        user=request.user,
        status='Resolved'
    ).count()

    context = {
        'total': total,
        'pending': pending,
        'progress': progress,
        'resolved': resolved
    }

    return render(
        request,
        'dashboard.html',
        context
    )


@login_required
def report_issue(request):

    if request.method == 'POST':

        form = IssueForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():
            issue = form.save(commit=False)
            issue.user = request.user
            issue.save()

            return redirect('my_issues')

    else:
        form = IssueForm()

    return render(
        request,
        'report_issue.html',
        {'form': form}
    )


@login_required
def my_issues(request):

    query = request.GET.get('q')

    issues = Issue.objects.filter(
        user=request.user
    ).order_by('-created_at')

    if query:
        issues = issues.filter(
            title__icontains=query
        )

    return render(
        request,
        'my_issues.html',
        {'issues': issues}
    )


@login_required
def notifications(request):

    notes = Notification.objects.filter(
        user=request.user
    ).order_by('-created_at')

    return render(
        request,
        'notifications.html',
        {'notes': notes}
    )