from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy
from .models import BaseModel, Category
from .forms import  ContactForm
from django.core.mail import send_mail
import datetime

def CategoryFunc(request, category):
    category = Category.objects.get(name=category)
    publish_list = BaseModel.objects.published().filter(category=category)
    return render(request, 'category.html', { 'category':category, 'publish_list':publish_list})

def BlogFunc(request):
    publish_list = BaseModel.objects.published()
    return render(request, 'top.html',  {'publish_list':publish_list})

def listFunc(request):
    publish_list = BaseModel.objects.published()
    return render(request, 'list.html',  {'publish_list':publish_list})

def DetailFunc(request, pk):
    object = get_object_or_404(BaseModel, pk=pk)
    return render(request, 'detail.html', {'object':object})

# お問い合わせ
class ContactView(FormView):
    
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('content')
 
    def get_form(self, form_class=None):
        # contact.hmltで、データを送信した場合
        if 'name' in self.request.POST:
            form_data = self.request.POST
  
        # お問い合わせフォーム確認画面から「戻る」リンクを押した場合や初回の入力欄表示は以下の表示。
        # セッションにユーザーデータがあれば、それをフォームに束縛
        else:
            form_data = self.request.session.get('form_data', None)
  
        return self.form_class(form_data)
  
    def form_valid(self, form):
        # 入力した値を、セッションに保存
        self.request.session['form_data'] = self.request.POST
        return super().form_valid(form)
 
 
# お問い合わせフォーム確認ページ
class ContentView(TemplateView):
    template_name = 'content.html'
  
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form_data = self.request.session.get('form_data', None)
        context['form'] = ContactForm(form_data)
        return context
 
 
# お問い合わせ送信
class SendEmailView(FormView):
 
    form_class = ContactForm
    success_url = reverse_lazy('success')
  
    def get_form(self, form_class=None):
        # セッションに入れたユーザーデータ取り出し
        form_data = self.request.session.pop('form_data', None)
 
        #メール送信
        subject = form_data['name']
        message = form_data['message']
        from_email = form_data['email']
        # to = [settings.EMAIL_HOST_USER]
        # send_mail(subject, message, from_email, to)
 
        return self.form_class(form_data)

def SuccessFunc(request):
    return render(request, 'success.html')
