from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
import requests
# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import InquiryForm,CommentcreateForm
from .models import InquiryImage,Inquiry,InquiryComment
class Customer_Service():
    pass



def customer_service(request):
    return render(request, 'customer_service/customer_service.html')


class InquiryListView(ListView):
    pass


from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from .forms import InquiryForm, InquiryImageForm

class InquiryCreateView(View):
    template_name = 'customer_service/inquiry_create.html'

    def get(self, request):
        form = InquiryForm()  # 폼 인스턴스 생성
        imageform = InquiryImageForm()
        return render(request, self.template_name, {'form': form, 'imageform': imageform})

    def post(self, request):
        form = InquiryForm(request.POST, request.FILES)  # POST 데이터와 파일 데이터를 받아 폼 인스턴스 생성
        imageform = InquiryImageForm(request.POST, request.FILES)

        if form.is_valid():
            # 폼이 유효하면 데이터 저장
            inquiry = form.save(commit=False)  # 데이터베이스에 바로 저장하지 않고 인스턴스 생성
            inquiry.user = request.user  # 현재 사용자를 작성자로 설정 
            inquiry.created_by = request.user  # 현재 사용자를 작성자로 설정
            inquiry.save()  # 데이터베이스에 저장

            # 이미지 저장
            images = request.FILES.getlist('image')
            for image in images:
                InquiryImage.objects.create(inquiry=inquiry, image=image)

            # 게시글 작성 완료 후 리다이렉트
            return HttpResponse("ㅎㅇ")  


        return render(request, self.template_name, {'form': form, 'imageform': imageform})
    
class InquiryListView(ListView):
    template_name = 'customer_service/customer_service.html'
    context_object_name = 'inquirys'
    model = Inquiry

    def get_queryset(self):
        return Inquiry.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    

    
class InquiryDetailView(DetailView):
    template_name = 'customer_service/inquiry_detail.html'
    model = Inquiry
    context_object_name = 'inquiry'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        inquiry = self.get_object()
        context['profile'] = inquiry.created_by.profile
        context['inquiry_image'] = InquiryImage.objects.filter(inquiry=inquiry).first()
        context['comments'] = InquiryComment.objects.filter(post=inquiry)
        context['form'] = CommentcreateForm()
        return context
    

    def post(self, request, *args, **kwargs):
        inquiry = self.get_object()
        form = CommentcreateForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = inquiry
            comment.created_by = request.user  # 현재 로그인한 사용자 설정
            comment.save()
            inquiry.answer_status = "True"
            inquiry.save()
            return redirect('customer_service:post_detail', pk=inquiry.pk)
        context = self.get_context_data()
        context['form'] = form
        return render(request, self.template_name, context)