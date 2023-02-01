from django.urls import path
from vegfoodapp import views

urlpatterns=[
    path('index4/',views.index4,name="index4"),
    path('contactpage/',views.contactpage,name="contactpage"),
    path('aboutpage/',views.aboutpage,name="aboutpage"),
    path('blogpage/', views.blogpage, name="blogpage"),
    path('product3/', views.product3, name="product3"),
    path('discategory/<itemcatg>',views.discategory,name="discategory"),
    path('prodetails/<int:dataid>',views.prodetails,name="prodetails"),
    path('logregpage/', views.logregpage, name="logregpage"),
    path('regdata/',views.regdata,name="regdata"),
    path('customerlogin/',views.customerlogin,name="customerlogin"),
    path('userlogout/',views.userlogout,name="userlogout"),
    path('cartpage/',views.cartpage,name="cartpage"),
    path('adcontactsave/',views.adcontactsave,name="adcontactsave")
]