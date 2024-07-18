from django.db import models
# from django.contrib.auth.models import Group, User, Permission
# from django.utils.translation import gettext_lazy as _
# from ? import pc_gen


# class OrganizationGroup(Group):  # Admin create
#     CHOICE_LIST = [('operator', 'Конечный пользователь'), ('service', 'Обслуживающая организация'),
#                    ('manager', 'Представитель производителя'), ]
#     group_name = models.CharField(max_length=128, choices=CHOICE_LIST, null=False, blank=False, verbose_name=_("Group name"))
#     # name = models.CharField(max_length=128, unique=True, verbose_name=_("Group name"))
#     # need cross table.. Work to Admin...
#     # group_permissions = models.ManyToManyField(Permission, null=False, blank=False, verbose_name=_("Group permissions"))
#
#
# class TheUser(User):
#     # Основные (\venv\Lib\site-packages\django\contrib\auth\models.py)
#     # password, last_login (Дата и время последней активности в веб-приложении), username(unique),
#     # email, is_staff (может заходить в панель администратора), is_active (доступ пользователя
#     # на сайт в целом), date_joined (дата и время регистрации пользователя)
#     organization_group = models.ForeignKey(to='OrganizationGroup', null=False, blank=False,
#                                            on_delete=models.PROTECT, verbose_name=_('Organization group'), )
#     # personal_code = pc_gen(name=username, group=organization_group, date=date_joined, type="card")
#     personal_code = models.CharField(max_length=24, null=False, blank=False, default='0000-0000-0000-0000',
#                                      unique=True, verbose_name=_('Personal code'), )
#     # last_viewed_url = models.URLField(null=True, blank=True, verbose_name=_('Last viewed page'), )
#
#     # # Уведомления на ...
#     # m_mailing = models.BooleanField(default=False, verbose_name=_('Mailing'))  # отправка на e-mail
#     # t_mailing = models.BooleanField(default=False, verbose_name=_('Phone notifications'))  # отправка на телефон
#     #  def email_user(self, subject, message, from_email=None, **kwargs):
#     #         """Send an email to this user."""
#     #         send_mail(subject, message, from_email, [self.email], **kwargs)
#
#     REQUIRED_FIELDS = ["email", "username", "organization_group", "personal_code"]
#
#     def __str__(self):
#         return f'<{self.username}>'  # ({self.email})>'
