from django.conf import settings
from django.contrib.auth import logout, login, authenticate, get_user_model
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import translate_url
from django.utils import translation

# Create your views here.
from django.utils.translation import check_for_language, LANGUAGE_SESSION_KEY


def traducao(request):
    response = HttpResponse(status=204)
    lang_code = request.GET.get('language')
    check_for_language(lang_code)
    next_trans = translate_url('/', lang_code)
    if next_trans != next:
        response = HttpResponseRedirect(next_trans)
    if hasattr(request, 'session'):
        request.session[LANGUAGE_SESSION_KEY] = lang_code
    response.set_cookie(
        settings.LANGUAGE_COOKIE_NAME, lang_code,
        max_age=settings.LANGUAGE_COOKIE_AGE,
        path=settings.LANGUAGE_COOKIE_PATH,
        domain=settings.LANGUAGE_COOKIE_DOMAIN,
    )
    lang = translation.get_language_from_request(request)
    translation.activate(lang)
    request.LANGUAGE_CODE = lang
    return response

def sair(request):
    logout(request)
    return redirect('/')

def is_logged(request):
    module = request.GET.get("module", "nosso jogo")
    qmodal = request.GET.get('qmodal', '')
    if request.user.is_authenticated:
        return render(request, 'components/authenticated.html', locals())
    return render(request, 'components/login.html', locals())

def  mylogin(request):
    login_input = request.POST.get('inputLogin', '')
    password_input = request.POST.get('inputSenha', '')
    if login_input == '' or password_input == '':
        return HttpResponse('#nodata')
    user = authenticate(username=login_input, password=password_input)
    if not user:
        return HttpResponse('#erroruser')
    login(request, user)
    return HttpResponse("#ok")

def insert_user(request):
    login_input = request.POST.get('inputLogin', '')
    password_input = request.POST.get('inputSenha', '')
    if login_input == '' or password_input == '':
        return HttpResponse('#nodata')
    UserModel = get_user_model()
    user = UserModel.objects.filter(username=login_input)
    print(user)
    if user.count() > 0:
        return HttpResponse('#erroruser')
    user = UserModel.objects.create_user(login_input, 'test@sistema.com', password_input)
    user.set_password(password_input)
    user.save()
    user = authenticate(username=login_input, password=password_input)
    login(request, user)
    return HttpResponse("#ok")
