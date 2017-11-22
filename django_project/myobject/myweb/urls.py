
from django.conf.urls import url
# from django.contrib import admin
from . import views,viewsusers,viewsorders
#网站前台路由配置
urlpatterns = [
    url(r'^$',views.index,name="index"),#首页
    url(r'^list/(?P<pIndex>[0-9]*)$',views.list,name="list"),#列表页
    url(r'^detail/(?P<gid>[0-9]*)$',views.detail,name="detail"),#详情页

    #登录注册
    url(r'^login$',viewsusers.login,name='myweb_login'),#加载登录界面
    url(r'^alogin$',viewsusers.alogin,name='myweb_alogin'),#使用ajax验证用户是否存在
    url(r'^dologin$',viewsusers.dologin,name='myweb_dologin'),#执行登录操作
    url(r'^register$',viewsusers.register,name='myweb_register'),#加载注册界面
    url(r'^addregister$',viewsusers.addregister,name="myweb_addregister"),#添加用户
    url(r'^logout$',viewsusers.logout,name="myweb_logout"),#退出当前用户

    #购物车和订单处理问题
    url(r'^cart$',viewsorders.cart,name="myweb_cart"),#购物车显示
    url(r'^cartadd/(?P<gid>[0-9]*)$',viewsorders.cartadd,name="myweb_cartadd"),#向购物车中添加商品
    url(r'^cartdel/(?P<gid>[0-9]*)$',viewsorders.cartdel,name="myweb_cartdel"),#删除商品
    url(r'^cartclear$',viewsorders.cartclear,name="myweb_cartclear"),#清空购物车
    url(r'^cartchange$',viewsorders.cartchange,name="cartchange"),#更改购物车的数量

    #订单详情
    url(r'^order$',viewsorders.order,name="order"),#订单处理
    url(r'^add_orders$',viewsorders.add_orders,name="add_orders"), #添加订单表
    url(r'^confirmorder$',viewsorders.confirmorder,name="confirmorder"),#确认付款页面
    url(r'^myorder$',viewsorders.myorder,name='myorder'),#我的订单
    url(r'^await/(?P<oid>[0-9]*)$',viewsorders.await,name="await"),#待发货界面

    #个人中心
    url(r'^member$',viewsorders.member,name="member"),
    url(r'^editmember$',viewsorders.editmember,name="editmember"),#加载修改个人信息表单
    url(r'^updatemember$',viewsorders.updatemember,name="updatemember"),#修改个人信息
    url(r'^staorder/(?P<state>[0-9]*)/(?P<oid>[0-9]*)$',viewsorders.staorder,name = "staorder"),#修改订单状态
]
