from django.shortcuts import render, redirect
import random

from quiz.models import *


def get_ranking(request):
    tot = Question.objects.all().count()
    usuarios = [
        (
            u,
            UserAnswer.objects.filter(usuario=u, correta=True).count()
        )
        for u in UserModel.objects.all().order_by('username')
    ]
    user_atual = request.user if request.user.is_authenticated else None
    if user_atual:
        user_atual = (user_atual, UserAnswer.objects.filter(usuario=user_atual, correta=True).count())
    return tot, user_atual, list(sorted(usuarios, key=lambda x: x[1], reverse=True))


def questao(request):
    lista_not = [i.question.id for i in request.user.RespUser_set.all()]
    perguntas = [q for q in Question.objects.exclude(id__in=lista_not)]
    if len(perguntas) == 0:
        ranking = get_ranking(request)
        qtd_user = ranking[1][1]
        qtd_tot = ranking[0]
        return render(request, 'components/congrats.html', locals())

    pergunta = random.choice(perguntas)
    return render(request, 'components/question.html', locals())


def responder(request):
    resposta = Answer.objects.filter(id=int(request.GET.get('r', 0)))
    if resposta.count() > 0:
        resposta = resposta[0]
        ra = UserAnswer()
        ra.usuario = request.user
        ra.question = resposta.question
        ra.answer = resposta
        ra.correta = resposta.iscorrect
        ra.save()

    return redirect("/questao/")


def ranking_view(request):
    ranking = get_ranking(request)
    has_rank = UserAnswer.objects.all().count() > 0
    print(ranking)
    return render(request, 'components/ranking.html', locals())
