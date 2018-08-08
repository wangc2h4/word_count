# from django.http import HttpResponse
from django.shortcuts import render
# render是递交传达一个网页给用户


def home(request):
    # request是用户发出的一个请求
    return render(request, 'home.html')
    # 获得发出的请求request后反馈

def count(request):
    # request是用户发出的一个请求
    user_text = request.GET['text']
    total_count = len(request.GET['text'])

    word_dict = {}
    for word in user_text:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1
    sorted_dict = \
        sorted(word_dict.items(),key=lambda w: w[1], reverse=True)
    # 回去查python lambda

    return render(request, 'count.html',
                  {'count': total_count, 'text': user_text,
                   'dict': word_dict, 'sorted': sorted_dict})
    # 获得发出的请求request后反馈

def about(request):
    return render(request,'about.html')