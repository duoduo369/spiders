# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect
from weibo import APIClient
from models import User
import config

APP_KEY = config.APP_KEY
APP_SECRET = config.APP_SECRET
CALLBACK_URL = config.CALLBACK_URL


def authorize(request):
    """
    跳转到验证页面
    """
    client = APIClient(
        app_key=APP_KEY,
        app_secret=APP_SECRET,
        redirect_uri=CALLBACK_URL
    )
    auth_url = client.get_authorize_url()
    return HttpResponseRedirect(auth_url)


def callback(request):
    """
    用户授权后的回调
    """
    code = request.GET.get(u'code')
    client = APIClient(
        app_key=APP_KEY,
        app_secret=APP_SECRET,
        redirect_uri=CALLBACK_URL
    )
    res = client.request_access_token(code)
    access_token = res['access_token']
    expires_in = res['expires_in']
    request.session['access_token'] = access_token
    request.session['expires_in'] = expires_in
    client.set_access_token(access_token, expires_in)
    uid = client.get.account__get_uid()['uid']
    user = client.users.show.get(uid=uid)
    username = str(uid)+'@weibo'
    email = str(uid) + '@weibo.com'
    print '====================='
    print 'success login'
    print access_token
    print expires_in
    print uid, username, email
    print user
