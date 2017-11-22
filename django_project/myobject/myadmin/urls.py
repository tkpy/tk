
from django.conf.urls import url
# from django.contrib import admin
from . import views,viewsgoods,viewsorders

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^$',views.index,name="myadmin_index"),#后台首页

    # 后台用户管理
    url(r'^users$', views.usersindex, name="myadmin_usersindex"),
    url(r'^usersadd$', views.usersadd, name="myadmin_usersadd"),
    url(r'^usersinsert$', views.usersinsert, name="myadmin_usersinsert"),
    url(r'^usersdel/(?P<uid>[0-9]+)$', views.usersdel, name="myadmin_usersdel"),
    url(r'^usersedit/(?P<uid>[0-9]+)$', views.usersedit, name="myadmin_usersedit"),
    url(r'^usersupdate/(?P<uid>[0-9]+)$', views.usersupdate, name="myadmin_usersupdate"),

    #后台管理员路由
    url(r'^login$',views.login,name="myadmin_login"),
    url(r'^dologin$',views.dologin,name="myadmin_dologin"),
    url(r'^logout$',views.logout,name="myadmin_logout"),
    url(r'^verify$',views.verify,name="myadmin_verify"),#验证码

    #商品类别
    url(r'^types/(?P<pIndex>[0-9]*)$', viewsgoods.typeindex, name="myadmin_typeindex"),
    url(r'^typesadd/(?P<tid>[0-9]+)$', viewsgoods.typeadd, name="myadmin_typeadd"),
    url(r'^typeinsert$', viewsgoods.typeinsert, name="myadmin_typeinsert"),
    url(r'^typedel/(?P<tid>[0-9]+)$', viewsgoods.typedel, name="myadmin_typedel"),
    url(r'^typeedit/(?P<tid>[0-9]+)$', viewsgoods.typeedit, name="myadmin_typeedit"),
    url(r'^typeupdate/(?P<tid>[0-9]+)$', viewsgoods.typeupdate, name="myadmin_typeupdate"),
    #商品信息管理
    url(r'^goods/(?P<pIndex>[0-9]*)$', viewsgoods.goodsindex, name="myadmin_goodsindex"),
    url(r'^goodsadd$', viewsgoods.goodsadd, name="myadmin_goodsadd"),
    url(r'^goodsinsert$', viewsgoods.goodsinsert, name="myadmin_goodsinsert"),
    url(r'^goodsdel/(?P<gid>[0-9]+)$', viewsgoods.goodsdel, name="myadmin_goodsdel"),
    url(r'^goodsedit/(?P<gid>[0-9]+)$', viewsgoods.goodsedit, name="myadmin_goodsedit"),
    url(r'^goodsupdate/(?P<gid>[0-9]+)$', viewsgoods.goodsupdate, name="myadmin_goodsupdate"),

    # 分页浏览信息
    url(r'^pageindex/(?P<obj>[a-zA-Z]*)/(?P<pathname>[a-zA-Z]*)/(?P<pIndex>[0-9]*)$',views.pageindex,name='pageindex'),#会员信息分页

    #后台订单管理
    url(r'^orders/(?P<pIndex>[0-9]*)$',viewsorders.orders,name='myadmin_orders'),
    url(r'^detail/(?P<oid>[0-9]*)$',viewsorders.detail,name = 'myadmin_detail'),#查看订单详情
    url(r'^editorder/(?P<oid>[0-9]*)$',viewsorders.editorder,name="myadmin_editorder"),#编辑页面
    url(r'^updateorder/(?P<oid>[0-9]*)$',viewsorders.updateorder,name="myadmin_updateorder"),#执行编辑

    #推荐商品
    url(r'^recommend/(?P<gid>[0-9]*)$',viewsgoods.recommend,name="myadmin_recommend"),
]
