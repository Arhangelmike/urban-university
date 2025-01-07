from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


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
    context = {
        'title': title,
        'text': text,
        'list': list,
        'game_dict': game_dict,
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


# Классами сделаные
# class games(TemplateView):
#     template_name = 'games.html'
#
# class cart(TemplateView):
#     template_name = 'cart.html'
#
# class platform(TemplateView):
#     template_name = 'platform.html'
