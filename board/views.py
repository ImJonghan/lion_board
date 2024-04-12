from typing import Any
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import Item
from django.urls import reverse_lazy
# Create your views here.

class ItemLV(ListView):
    model = Item
    # ListView는 기본 세팅
    # - template : 앱이름/모델명(소문자)_list.html
    # - context : object_list
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['name'] = 'Tiger'
        return context

class ItemDV(DetailView):
    model = Item
    # DetailView는 기본 세팅
    # - template : 앱이름/모델명(소문자)_detail.html
    # - context : object
    # pk를 통해서 대상 데이터를 가져옵니다!!
    # url에서 pk를 가져오는 내용이 정의되어 있어야 합니다!!

class ItemCV(CreateView):
    model = Item
    success_url = reverse_lazy('spring:index') 
    fields = ['title', 'content']
    # - template : 앱이름/모델명(소문자)_form.html

class ItemDeleteView(DeleteView):
    model = Item
    success_url = reverse_lazy('spring:index')     
    # 지울건지 확인 : 앱이름/모델명(소문자)_confirm_delete.html

def itemLV(request):
    # 모델에서 데이터들 가져오고
    object = Item.objects.all()
    name = "Lion"
    # context에 담고
    context = {
        'object_list': object, 
        'name':name
    }
    # 템플릿에 결합해서
    # 페이지 반환
    return render(request=request, template_name='board/item_list.html', context=context)

def test(request):
    return HttpResponse("요청 잘 받았어")

def test1(request, pk):
    return HttpResponse(f"test1 pk: {pk} 이야")

