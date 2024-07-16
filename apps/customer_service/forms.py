from django import forms
from .models import Inquiry, InquiryImage,InquiryComment

class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ['category', 'email', 'phone_number', 'inquiry_title', 'inquiry_body']
        labels = {
            'category': '카테고리',
            'email': '이메일',
            'phone_number': '전화번호',
            'inquiry_title': '제목',
            'inquiry_body': '내용'
        }

class InquiryImageForm(forms.ModelForm):
    class Meta:
        model = InquiryImage
        fields = ['image']
        labels = {
            'image': '이미지'
        }


class CommentcreateForm(forms.ModelForm):
    class Meta:
        model = InquiryComment
        fields = ['body']
