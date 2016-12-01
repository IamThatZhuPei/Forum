# coding: utf-8
from django.core.mail import send_mail

__author__ = '朱沛'


def send_activate_email(activate_url, to_email):
    # activate_email = '''点击<a href="%s">这里</a>激活''' % activate_url
    print(activate_url)

    send_mail(
        subject='[某网站]注册激活邮件',
        message='点击/打开链接：%s' % activate_url,
        html_message= "",
        from_email='zp2332@qq.com',
        recipient_list=[to_email],
        fail_silently=False
    )

