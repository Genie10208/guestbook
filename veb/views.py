from django.shortcuts import render
from django.views.generic import *
from django.urls import reverse_lazy
from .models import Message

# Create your views here.
# 留言列表
class MessageList(Listview):
    model = Message

class MessageDetail(DetailView):
    model = Message

class MessageCreate(CreateView):
    model = Message
    feilds = ['user','subject','content']
    success_url = reverse_lazy("msg_list")