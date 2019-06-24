# -*- coding:utf-8 -*-
_author__ = 'cdtaogang'
__date__ = '2019/6/24 15:50'
import xadmin
from .models import EmailVerifyRecord, Banner
from xadmin import views
# from extra_apps import xadmin  错误的导入
# from extra_apps.xadmin import views  错误的导入


class BaseSetting(object):
    enable_themes = True  # 开启主题功能
    use_bootswatch = True


class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']  # 列表字段展示
    search_fields = ['code', 'email', 'send_type']  #  搜索框显示
    list_filter = ['code', 'email', 'send_type', 'send_time']  # 筛选字段


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']
#修改页面左上方的Django Xadmin以及页面底部的我的公司
class GlobalSettings(object):
    site_title = "灰灰后台管理系统"
    site_footer = "灰灰老师"
    menu_style = "accordion"#菜单收缩

xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
