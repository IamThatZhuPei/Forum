# coding: utf-8
from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from .forms import UserForm
import uuid
import datetime
from django.utils import timezone
from .aboutMail import send_activate_email
from .models import ActivateCode


def user_register(request):
    if request.method == "GET":
        return render(request, "user_register.html", {"data": ""})
    else:
        form = UserForm(request.POST)

        if form.is_valid():
            user_info = form.save(commit=False)
            user = User.objects.create_user(user_info.username, user_info.email, user_info.password)
            user.is_active = False
            user.save()

            # 生成激活码并存储
            active_code = str(uuid.uuid4()).replace("-", "")
            expiration_time = timezone.now()
            delta = datetime.timedelta(days=1)
            expiration_time = expiration_time + delta
            userActivateCode = ActivateCode(user=user, activate_code=active_code, expiration_time=expiration_time)
            userActivateCode.save()


            # 生成激活链接并发送到用户邮箱
            active_url = "https//%s/user/activate/%s" % (request.get_host(), active_code)
            send_activate_email(active_url, user.email)

            return render(request, "user_reg_suc.html", {"form": form})
        else:
            return render(request, "user_register.html", {"form": form})


def activate(request, code):
    if request.method == "GET":
        try:
            userAcCode = ActivateCode.objects.get(activate_code=code)
            user = userAcCode.user
            now = timezone.now()
            print(now, userAcCode.expiration_time)
            if user.is_active:
                message = "此用户已经激活"
            elif now > userAcCode.expiration_time:
                message = "激活时间已失效，请重新注册"
            else:
                user.is_active = True
                user.save()
                message = "激活成功"
        except ObjectDoesNotExist:
            print("用户激活失败")
            message = "抱歉，激活失败"

        return render(request, "register_back.html", {"message": message})
    else:
        return render(request, "register_back.html")


