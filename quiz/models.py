from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from base.models import Country, Region

LEVEL_CHOICE = (
    (1, _('Easy')),
    (5, _('Medium')),
    (9, _('Hard')),
)

QUESTION_TYPE_CHOICE = (
    (1, _("Pergunta e Resposta")),
    (2, _("Clicar na imagem")),
)


class Category(models.Model):
    class Meta:
        db_table = 'category'
        verbose_name = _('categoria')
        verbose_name_plural = _('categorias')

    def __str__(self):
        return self.category_name

    def __unicode__(self):
        return self.category_name

    category_name = models.CharField(_('Nome da Categoria'), max_length=50)
    imagem = models.FileField(_('Imagem'), null=True, blank=True)


class Question(models.Model):
    class Meta:
        db_table = 'question'
        verbose_name = _('pergunta')

    def __str__(self):
        return self.text

    def __unicode__(self):
        return self.text

    text = models.TextField(_("Questão"))
    level = models.IntegerField(_("Nível"), default=1, choices=LEVEL_CHOICE)
    question_type = models.IntegerField(_("Tipo de Questão"), default=1, choices=QUESTION_TYPE_CHOICE)
    category = models.ForeignKey(Category, verbose_name=_('Categoria'), on_delete=None)
    country = models.ForeignKey(Country, verbose_name=_('País'), null=True, blank=True, on_delete=None)
    region = models.ForeignKey(Region, verbose_name=_('Região'), null=True, blank=True, on_delete=None)
    explanation = models.TextField(_('Explicação'), null=True, blank=True)
    image = models.ImageField(_('Imagem'), null=True, blank=True, upload_to='foto')


class Answer(models.Model):
    class Meta:
        db_table = 'answer'
        verbose_name = _('resposta')

    def __str__(self):
        return self.text_answer

    def __unicode__(self):
        return self.text_answer

    question = models.ForeignKey(Question, verbose_name=_('Pergunta'), on_delete=None, related_name='Resposta_set')
    text_answer = models.TextField('Resposta')
    iscorrect = models.BooleanField(default=False, verbose_name=_('É correta?'))


UserModel = get_user_model()


class UserAnswer(models.Model):
    class Meta:
        db_table = 'useranswer'
        verbose_name = _('resposta do usuário')
        verbose_name_plural = _('respostas dos usuários')

    def __str__(self):
        return self.question.text + ('Certa' if self.correta else 'Errada')

    def __unicode__(self):
        return self.question.text + ('Certa' if self.correta else 'Errada')

    usuario = models.ForeignKey(UserModel, verbose_name=_('Usuário'), on_delete=None, related_name='RespUser_set')
    question = models.ForeignKey(Question, verbose_name=_('Pergunta'), on_delete=None)
    answer = models.ForeignKey(Answer, verbose_name=_('Resposta'), on_delete=None)
    correta = models.BooleanField(_('Está correta?'), default=False)
