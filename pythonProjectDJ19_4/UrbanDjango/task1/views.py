from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UserRegister
from .models import *




def index(request):
    title = 'Мой сайт'
    text = 'Главная страница'
    context ={
        'title' : title,
        'text' : text,
    }
    return render(request, 'fourth_task/index.html', context)

def games(request):
    title = 'Мой сайт'
    text = 'Игры'
    list = ['Mario warriors', 'Deus Ex', 'Fallout 3']
    game_dict = {'games': ["Atomic Heart", "Cyberpunk 2077", "PayDay 77"]}
    games = Game.objects.all()
    context = {
        'title': title,
        'text': text,
        'list': list,
        'game_dict': game_dict,
        'games': games,
    }
    return render(request, 'fourth_task/games.html', context)

def cart(request):
    title = 'Мой сайт'
    text = 'Корзина'
    context = {
        'title': title,
        'text': text,
    }
    return render(request, 'fourth_task/cart.html', context)

def platform(request):
    title = 'Мой сайт'
    text = 'Операционные системы'
    os_dictionary ={"Windows 10":"В ней реализована совместимость со всеми актуальными играми и приложениями." ,
                    "Ubuntu":"Операционная система совместима с широким спектром игр, особенно благодаря интеграции со Steam. Также поддерживает другие игровые платформы, например Lutris и GameHub." ,
                    "IOS":"При активации режима iOS мгновенно перераспределяет ресурсы устройства, отдавая приоритет игровому приложению. Это означает, что процессор и графический чип работают на максимальной мощности именно для игры, в то время как фоновые процессы других приложений минимизируются или вовсе приостанавливаются." ,
                    "Android":"Возможность регулировать производительность. На Android игрово режим позволяет пользователю разрешить смартфону либо задействовать ресурсы по максимуму для наибольшей производительности, либо жёстко экономить их (тем самым сохраняя заряд аккумулятора)." ,
                    }
    context = {
        'title': title,
        'text': text,
        'os_dictionary': os_dictionary,
    }
    return render(request, 'fourth_task/platform.html', context)


def index2(request):
    return render(request, 'fifth_task/index2.html')


def sign_up_by_django(request):
    if request.method == "POST":
        form = UserRegister(request.POST)
        info = {'form':form}
        if form.is_valid():
            users = Buyer.objects.all()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if username not in users and password == repeat_password and age >= '18':
                Buyer.objects.create(name=username, age=age, balance=0)
                return HttpResponse(f'Приветствуем, {username}!')

            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
                print(f'Error: {info["error"]}')
                return HttpResponse(info['error'])

            elif age < '18':
                info['error'] = 'Вы должны быть старше 18'
                print(f'Error: {info["error"]}')
                return HttpResponse(info['error'])

            elif username in users:
                info['error'] = 'Пользователь уже существует'
                print(f'Error: {info["error"]}')
                return HttpResponse(info['error'])

    else:
        form = UserRegister()
        info = {'form': form}
    return render(request, 'fifth_task/registration_page.html', context=info)

# def sign_up_by_html(request):  - не используем легко обходиться со стороны клиента
#
#     if request.method == "POST":
#         form = UserRegister(request.POST)
#         info = {'form':form}
#         if form.is_valid():
#             buyers = Buyer.objects.all()
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             repeat_password = form.cleaned_data['repeat_password']
#             age = form.cleaned_data['age']
#
#             if username not in buyers and password == repeat_password and age >= '18':
#                 Buyer.objects.create(name=username, age=age, balance=0)
#                 return HttpResponse(f'Приветствуем, {username}!')
#
#             elif password != repeat_password:
#                 info['error'] = 'Пароли не совпадают'
#                 print(f'Error: {info["error"]}')
#                 return HttpResponse(info['error'])
#
#             elif age < '18':
#                 info['error'] = 'Вы должны быть старше 18'
#                 print(f'Error: {info["error"]}')
#                 return HttpResponse(info['error'])
#
#             elif username in buyers:
#                 info['error'] = 'Пользователь уже существует'
#                 print(f'Error: {info["error"]}')
#                 return HttpResponse(info['error'])
#
#     else:
#         form = UserRegister()
#         info = {'form': form}
#     return render(request, 'fifth_task/registration_page.html', context=info)
