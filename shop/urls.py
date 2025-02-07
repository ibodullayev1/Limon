from django.urls import path

from shop.views.error import custom_404_view, custom_500_view

from shop.views import (HomePageTemplateView, ShopPageTemplateView, SingleProductTemplateView, WishListView,
                        CheckOutPageTemplateView, SingleProductTabStyleLeftTemplateView,
                        SingleProductTabStyleTopTemplateView,
                        SingleProductGroupTemplateView, SingleProductAffinityTemplateView,
                        SingleProductNormalTemplateView,
                        Shop3PageTemplateView, Shop4PageTemplateView, ShopRightSidebarPageTemplateView,
                        ShopListPageTemplateView, ShopListLeftSidebarPageTemplateView,
                        ShopListRightSidebarPageTemplateView,
                        SingleProductGalleryLeftTemplateView, SingleProductCarouselTemplateView,
                        SingleProductGalleryRightTemplateView, SingleProductSaleTemplateView,
                        SingleProductTabStyleRightTemplateView, ShoppingCardTemplateView, CompareTemplateView,
                        LoginView, LogoutView, edit_profile,
                        BlogPageTemplateView, Blog3PageView, Blog4PageView,
                        Blog5PageView, Blog6PageView, Blog7PageView,
                        Blog8PageView, Blog9PageView, BlogListTemplateView,
                        BlogVideoView, BlogAudiView, BlogGalaryView, signup_view,forgot_password_view,OPTView
                        )
from shop.views.page_log_reg import ContactView,\
    AboutView, FaqView, ErrorView

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
    path('shop/single-product-gallery-left/', SingleProductGalleryLeftTemplateView.as_view(),
         name='single-product-gallery-left'),
    path('shop/single-product-gallery-right/', SingleProductGalleryRightTemplateView.as_view(),
         name='single-product-gallery-right'),
    path('shop/single-product-carousel/', SingleProductCarouselTemplateView.as_view(), name='single-product-carousel'),
    path('single/product_sale/', SingleProductSaleTemplateView.as_view(), name='single_product_sale'),
    path('shop/single-product/', SingleProductTemplateView.as_view(), name='single-product'),
    path('shop/single-product-left/', SingleProductTabStyleLeftTemplateView.as_view(), name='single-product_left'),
    path('shop/single-product-top/', SingleProductTabStyleTopTemplateView.as_view(), name='single-product_top'),
    path('shop/single-product-right/', SingleProductTabStyleRightTemplateView.as_view(), name='single-product_right'),
    path('shop/single-product-group/', SingleProductGroupTemplateView.as_view(), name='single_product_group'),
    path('shop/single-product-normal/', SingleProductNormalTemplateView.as_view(), name='single_product_normal'),
    path('shop/single-product-affiliation/', SingleProductAffinityTemplateView.as_view(),
         name='single_product_affiliation'),
    path('shop/single-product/detail/', SingleProductNormalTemplateView.as_view(), name='shop_single_product_detail'),
    path('wishlist/', WishListView.as_view(), name='wishlist'),
    path('register/', signup_view, name='register'),
    path('forgot-password/', forgot_password_view, name='forgot_password'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('checkout/', CheckOutPageTemplateView.as_view(), name='checkout'),
    path('otp/',OPTView,name='otp'),
    path('myprofile/', edit_profile, name='myprofile'),
]

# 404 xatolik uchun sozlash
handler404 = custom_404_view
handler500 = custom_500_view