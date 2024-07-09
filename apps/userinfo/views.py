from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from .forms import UserEditForm
from django.core.paginator import Paginator
from django.db.models import Count, Sum


User = get_user_model()

@login_required
def profile(request):
    
    orders = Order.objects.filter(payment__is_paid=True, user=request.user).order_by('-created_at')[:9]
    profile_songs = [order.song for order in orders]
    
    
    if request.method == 'POST':
        form = UserEditForm(request.POST, request.FILES, instance=request.user)  # request.user는 현재 로그인한 사용자의 인스턴스
        if form.is_valid():
            form.save()
            return redirect('home')  # 프로필 페이지로 리다이렉트
        else:
            return render(request, 'accounts/profile.html', {'form': form, 'profile_songs': profile_songs})
    else:
        form = UserEditForm(instance=request.user)  # 폼을 초기화할 때 현재 사용자 정보로 채웁니다
    
    return render(request, 'accounts/profile.html', {'form': form, 'profile_songs': profile_songs})
