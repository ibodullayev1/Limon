from django.urls import path

from shop.views import (AboutUsTemplateView, Blog3PageView, Blog4PageView,
                        Blog5PageView, Blog6PageView, Blog7PageView,
                        Blog8PageView, Blog9PageView, BlogAudiView,
                        BlogGalaryView, BlogListTemplateView,
                        BlogPageTemplateView, BlogVideoView,
                        CheckOutPageTemplateView, CompareTemplateView,
                        ContactTemplateView, HomePageTemplateView, LoginView,
                        LogoutView, OPTView, Shop3PageTemplateView,
                        Shop4PageTemplateView,
                        ShopListLeftSidebarPageTemplateView,
                        ShopListPageTemplateView,
                        ShopListRightSidebarPageTemplateView,
                        ShopPageTemplateView, ShoppingCardTemplateView,
                        ShopRightSidebarPageTemplateView,
                        SingleProductNormalDetailView,
                        SingleProductSaleTemplateView,
                        WishListView, edit_profile,
                        forgot_password_view, signup_view)
from shop.views.error import custom_404_view, custom_500_view
from shop.views.page_log_reg import AboutView, ContactView, ErrorView, FaqView
from shop.views.product import product_detail
from shop.views.search import search_products
from shop.views.wishlist import add_wishlist, remove_from_wishlist

app_name = 'shop'

urlpatterns = [
    path('', HomePageTemplateView.as_view(), name='home'),
    path('blog1/', BlogListTemplateView.as_view(), name='blog1'),
    path('blog2/', BlogPageTemplateView.as_view(), name='blog2'),
    path('blog3/', Blog3PageView.as_view(), name='blog3'),
    path('blog4/', Blog4PageView.as_view(), name='blog4'),
    path('blog5/', Blog5PageView.as_view(), name='blog5'),
    path('blog6/', Blog6PageView.as_view(), name='blog6'),
    path('blog7/', Blog7PageView.as_view(), name='blog7'),
    path('blog8/', Blog8PageView.as_view(), name='blog8'),
    path('blog9/', Blog9PageView.as_view(), name='blog9'),
    path('blog10/', BlogAudiView.as_view(), name='blog10'),
    path('blog11/', BlogVideoView.as_view(), name='blog11'),
    path('blog12/', BlogGalaryView.as_view(), name='blog12'),
    path('page1', LoginView.as_view(), name='page1'),
    path('page6', ContactView.as_view(), name='page6'),
    path('page7', AboutView.as_view(), name='page7'),
    path('page8', FaqView.as_view(), name='page8'),
    path('page9', ErrorView.as_view(), name='page9'),
    path('shop/', ShopPageTemplateView.as_view(), name='shop'),
    path('shop3/', Shop3PageTemplateView.as_view(), name='shop3'),
    path('shop4/', Shop4PageTemplateView.as_view(), name='shop4'),
    path('shop/right-sidebar/', ShopRightSidebarPageTemplateView.as_view(), name='shopRightSidebar'),
    path('shop/shop-list/', ShopListPageTemplateView.as_view(), name='shopList'),
    path('shop/shopping-card/', ShoppingCardTemplateView.as_view(), name='shoppingCard'),
    path('compare/', CompareTemplateView.as_view(), name='compare'),
    path('shop/shop-list-left-sidebar/', ShopListLeftSidebarPageTemplateView.as_view(), name='shopListLeftSidebar'),
    path('shop/shop-list-right-sidebar/', ShopListRightSidebarPageTemplateView.as_view(), name='shopListRightSidebar'),
    path('single/product_sale/', SingleProductSaleTemplateView.as_view(), name='single_product_sale'),
    path('shop/product/detail/<int:pk>/', SingleProductNormalDetailView.as_view(), name='product_detail'),
    path('wishlist/', WishListView.as_view(), name='wishlist'),
    path('checkout/', CheckOutPageTemplateView.as_view(), name='checkout'),
    path('about-us', AboutUsTemplateView.as_view(), name='about_us'),
    path('about-us', ContactTemplateView.as_view(), name='contact'),
    path('wishlist/add/', add_wishlist, name='add_wishlist'),
    path('wishlist/remove/', remove_from_wishlist, name='remove_wishlist'),
    path('register/', signup_view, name='register'),
    path('forgot-password/', forgot_password_view, name='forgot_password'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('checkout/', CheckOutPageTemplateView.as_view(), name='checkout'),
    path('myprofile/', edit_profile, name='myprofile'),
    path('search/', search_products, name='search'),
    path('product/<int:pk>/', product_detail, name='product_detail'),
    path('forgot-password/', forgot_password_view, name='forgot_password'),
    path('otp/', OPTView, name='otp'),

]

# 404 xatolik uchun sozlash
handler404 = custom_404_view
handler500 = custom_500_view
