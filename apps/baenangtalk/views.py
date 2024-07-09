from .models import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect, get_object_or_404
from .forms import * 
from django.contrib.auth.decorators import login_required

# 배낭톡 main + post ##############################################################################

# 배낭톡 main
class MainPostListView(ListView):
    model = Baenangtalk
    template_name = 'bae_main.html'
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = Baenangtalk.objects.all()

        # URL에서 전달된 county_id, period_id, subject_id 가져오기
        county_id = self.kwargs.get('county_id')
        period_id = self.kwargs.get('period_id')
        subject_id = self.kwargs.get('subject_id')

        # 필터링 조건 추가
        if county_id:
            queryset = queryset.filter(county_id=county_id)
        if period_id:
            queryset = queryset.filter(period_id=period_id)
        if subject_id:
            queryset = queryset.filter(subject_id=subject_id)

        return queryset.order_by('-bae_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # county_id, period_id, subject_id에 해당하는 객체 가져오기
        county_id = self.kwargs.get('county_id')
        period_id = self.kwargs.get('period_id')
        subject_id = self.kwargs.get('subject_id')

        if county_id:
            context['county'] = County.objects.get(pk=county_id)
        if period_id:
            context['period'] = BaenangtalkPeriod.objects.get(pk=period_id)
        if subject_id:
            context['subject'] = BaenangtalkSubject.objects.get(pk=subject_id)

        return context
    

# 배낭톡 detail
class PostDetailView(DetailView):
    template_name = 'post/bae_detail.html'

    def get(self, request, pk):
        # pk에 해당하는 Baenangtalk 객체 가져오기
        baenangtalk = get_object_or_404(Baenangtalk, pk=pk)

        # 작성자 닉네임 가져오기 (가정: Baenangtalk 모델에 작성자 정보가 User 외래키로 연결되어 있다고 가정)
        nickname = baenangtalk.author.username  # User 모델에서 username을 닉네임으로 사용

        # 월 가져오기 
        period = baenangtalk.period.strftime('%m') 

        # 도시, 주제 가져오기
        county = baenangtalk.county.city_name
        subject = baenangtalk.subject.bae_sub_name

        # 템플릿에 전달할 컨텍스트 데이터 정의
        context = {
            'nickname': nickname,
            'period': period,
            'county': county,
            'subject': subject,
            'bae_title': baenangtalk.bae_title,
            'bae_content': baenangtalk.bae_content,
            'bae_date': baenangtalk.bae_date,
            'bae_like': baenangtalk.bae_like,
            'comments': baenangtalk.comments.all()  # 댓글 필드가 있는 경우 comments 필드 사용 (예시)
        }

        return render(request, self.template_name, context)
    

# 배낭톡 create
class PostCreateView(CreateView):
    template_name = 'post/bae_create.html'

    def get(self, request):
        form = BaenangtalkForm()  # 폼 인스턴스 생성
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = BaenangtalkForm(request.POST, request.FILES)  # POST 데이터와 파일 데이터를 받아 폼 인스턴스 생성

        if form.is_valid():
            # 폼이 유효하면 데이터 저장
            baenangtalk = form.save(commit=False)  # 데이터베이스에 바로 저장하지 않고 인스턴스 생성
            baenangtalk.author = request.user  # 현재 사용자를 작성자로 설정 
            baenangtalk.save()  # 데이터베이스에 저장

            # 게시글 작성 완료 후 리다이렉트
            return redirect('baenangtalk:bae_detail', pk=baenangtalk.pk)  # 작성된 게시글의 상세 페이지로 리다이렉트

        # 폼이 유효하지 않으면 다시 폼을 보여줌
        return render(request, self.template_name, {'form': form})


# 배낭톡 edit
class PostEditView(UpdateView):
    template_name = 'post/bae_edit.html' 

    def get(self, request, pk):
        baenangtalk = get_object_or_404(Baenangtalk, pk=pk)  # pk에 해당하는 Baenangtalk 객체 가져오기

        # 현재 사용자가 작성자인지 확인
        if baenangtalk.author != request.user:
            return redirect('baenangtalk_detail', pk=pk)

        # 폼 인스턴스 생성 및 기존 데이터로 초기화
        form = BaenangtalkForm(instance=baenangtalk)

        return render(request, self.template_name, {'form': form, 'baenangtalk': baenangtalk})

    def post(self, request, pk):
        baenangtalk = get_object_or_404(Baenangtalk, pk=pk)  # pk에 해당하는 Baenangtalk 객체 가져오기

        # 현재 사용자가 작성자인지 확인
        if baenangtalk.author != request.user:
            return redirect('bae_detail', pk=pk)

        form = BaenangtalkForm(request.POST, request.FILES, instance=baenangtalk)

        if form.is_valid():
            # 폼이 유효하면 데이터 저장
            baenangtalk = form.save()

            # 수정 완료 후 리다이렉트
            return redirect('bae_detail', pk=pk)

        # 폼이 유효하지 않으면 다시 폼을 보여줌
        return render(request, self.template_name, {'form': form, 'baenangtalk': baenangtalk})


# 배낭톡 delete
class PostDeleteView(DeleteView):
    def post(self, request, pk):
        baenangtalk = get_object_or_404(Baenangtalk, pk=pk)  # pk에 해당하는 Baenangtalk 객체 가져오기

        # 현재 사용자가 작성자인지 확인
        if baenangtalk.author == request.user:
            # 작성자일 경우 삭제
            baenangtalk.delete()

        # 삭제 후 리다이렉트할 URL 설정 
        return redirect('bae_main') 


# 배낭톡 좋아요 ##############################################################################


# 배낭톡 게시글 좋아요
@login_required
def bae_post_like(request, pk):
    if request.method == 'POST':
        post = get_object_or_404(Baenangtalk, pk=pk)

        if request.user.customer:  # 사용자 계정인 경우
            customer = Customer.objects.get(user=request.user)

            if customer not in post.liked_by.all():
                post.liked_by.add(customer)
                post.bae_like += 1
                post.save()

        return redirect('baenangtalk:bae_detail', pk=pk)
    return redirect('baenangtalk:bae_detail', pk=pk)



# 배낭톡 게시글 좋아요 취소
@login_required
def bae_post_unlike(request, pk):
    if request.method == 'POST':
        post = get_object_or_404(Baenangtalk, pk=pk)

        if request.user.customer:  # 사용자 계정인 경우
            customer = Customer.objects.get(user=request.user)

            if customer in post.bae_like_by.all():
                post.bae_like_by.remove(customer)
                post.bae_like -= 1
                post.save()

        return redirect('baenangtalk:bae_detail', pk=pk)
    return redirect('baenangtalk:bae_detail', pk=pk)


# 댓글 ##############################################################################

# 댓글 수정
def com_edit(request, comment_id):
    comment = get_object_or_404(BaenangtalkComment, id=comment_id)
    
    if request.method == 'POST':
        form = CommentEditForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('baenangtalk:bae_detail', pk=comment.baenangtalk.pk)  # 댓글이 수정된 후 게시글 상세페이지로 이동
    else:
        form = CommentEditForm(instance=comment)
    
    return render(request, 'comment/com_edit.html', {'form': form})



# 댓글 삭제
def com_delete(request, comment_id):  
    comment = get_object_or_404(BaenangtalkComment, id=comment_id)
    
    if request.method == 'POST':
        # 삭제
        comment.delete()
        return redirect('baenangtalk:bae_detail', pk=comment.baenangtalk.pk)  # 댓글이 삭제된 후 게시글 상세페이지로 이동



# 댓글 좋아요
@login_required
def com_like(request, comment_id):
    if request.method == 'POST':
        comment = get_object_or_404(BaenangtalkComment, id=comment_id)

        if request.user.customer:  # 사용자가 고객 계정인 경우
            customer = Customer.objects.get(user=request.user)

            if customer not in comment.bae_com_like_by.all():
                comment.bae_com_like_by.add(customer)
                comment.bae_com_like += 1
                comment.save()

        return redirect('baenangtalk:bae_detail', pk=comment.baenangtalk.pk)
    return redirect('baenangtalk:bae_detail', pk=comment.baenangtalk.pk)



# 댓글 좋아요 취소
@login_required
def com_unlike(request, comment_id):
    if request.method == 'POST':
        comment = get_object_or_404(BaenangtalkComment, id=comment_id)

        if request.user.customer:  # 사용자가 고객 계정인 경우
            customer = Customer.objects.get(user=request.user)
            
            if customer in comment.bae_com_like_by.all():
                comment.bae_com_like_by.remove(customer)
                comment.bae_com_like -= 1
                comment.save()

        return redirect('baenangtalk:bae_detail', pk=comment.baenangtalk.pk)
    return redirect('baenangtalk:bae_detail', pk=comment.baenangtalk.pk)