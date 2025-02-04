from django.urls import path
from shop.views import (HomePageTemplateView, ShopPageTemplateView, SingleProductTemplateView, WishListView,
                        LoginRegisterPageTemplateView, CheckOutPageTemplateView, SingleProductTabStyleLeftTemplateView,
                        SingleProductTabStyleTopTemplateView,
                        SingleProductGroupTemplateView, SingleProductAffinityTemplateView,
                        SingleProductNormalTemplateView,
                        Shop3PageTemplateView, Shop4PageTemplateView, ShopRightSidebarPageTemplateView,
                        ShopListPageTemplateView, ShopListLeftSidebarPageTemplateView,
                        ShopListRightSidebarPageTemplateView,
                        SingleProductGalleryLeftTemplateView, SingleProductCarouselTemplateView,
                        SingleProductGalleryRightTemplateView, SingleProductSaleTemplateView,
                        SingleProductTabStyleRightTemplateView,ShoppingCardTemplateView,CompareTemplateView,
                        )
from shop.views.about_us import AboutUsTemplateView
from shop.views.accessories import AccessoriesTemplateView
from shop.views.contact import ContactTemplateView
from shop.views.smartwatch import SmartwatchTemplateView

urlpatterns = [
    path('', HomePageTemplateView.as_view(), name='home'),
    path('shop/',ShopPageTemplateView.as_view(), name='shop'),
    path('shop3/',Shop3PageTemplateView.as_view(), name='shop3'),
    path('shop4/',Shop4PageTemplateView.as_view(), name='shop4'),
    path('shop/right-sidebar/', ShopRightSidebarPageTemplateView.as_view(), name='shopRightSidebar'),
    path('shop/shop-list/', ShopListPageTemplateView.as_view(), name='shopList'),
    path('shop/shopping-card/', ShoppingCardTemplateView.as_view(), name='shoppingCard'),
    path('compare/', CompareTemplateView.as_view(), name='compare'),
    path('shop/shop-list-left-sidebar/', ShopListLeftSidebarPageTemplateView.as_view(), name='shopListLeftSidebar'),
    path('shop/shop-list-right-sidebar/', ShopListRightSidebarPageTemplateView.as_view(), name='shopListRightSidebar'),
    path('shop/single-product-gallery-left/', SingleProductGalleryLeftTemplateView.as_view(), name='single-product-gallery-left'),
    path('shop/single-product-gallery-right/', SingleProductGalleryRightTemplateView.as_view(), name='single-product-gallery-right'),
    path('shop/single-product-carousel/', SingleProductCarouselTemplateView.as_view(), name='single-product-carousel'),
    path('single/product_sale/',SingleProductSaleTemplateView.as_view(), name='single_product_sale'),
    path('shop/single-product/',SingleProductTemplateView.as_view(), name='single-product'),
    path('shop/single-product-left/',SingleProductTabStyleLeftTemplateView.as_view(), name='single-product_left'),
    path('shop/single-product-top/',SingleProductTabStyleTopTemplateView.as_view(), name='single-product_top'),
    path('shop/single-product-right/',SingleProductTabStyleRightTemplateView.as_view(), name='single-product_right'),
    path('shop/single-product-group/',SingleProductGroupTemplateView.as_view(), name='single_product_group'),
    path('shop/single-product-normal/', SingleProductNormalTemplateView.as_view(), name='single_product_normal'),
    path('shop/single-product-affiliation/',SingleProductAffinityTemplateView.as_view(), name='single_product_affiliation'),
    path('shop/single-product/detail/',ShopPageTemplateView.as_view(), name='shop_single_product_detail'),
    path('wishlist/', WishListView.as_view(), name='wishlist'),
    path('login-register/',LoginRegisterPageTemplateView.as_view(), name='login_register'),
    path('checkout/',CheckOutPageTemplateView.as_view(), name='checkout'),
    path('about_us/', AboutUsTemplateView.as_view(), name='about_us'),
    path('contact/', ContactTemplateView.as_view(), name='contact'),
    path('smartwatch/', SmartwatchTemplateView.as_view(), name='smartwatch'),
    path('accessories/', AccessoriesTemplateView.as_view(), name='accessories'),
]
