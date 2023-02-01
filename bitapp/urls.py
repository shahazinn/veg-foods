from django.urls import path
from bitapp import views

urlpatterns=[
    path('index3/',views.index3,name="index3"),
    path('adminpage/',views.adminpage,name="adminpage"),
    path('savedata/', views.savedata, name="savedata"),
    path('adminpage2/',views.adminpage2,name="adminpage2"),
    path('editpage/<int:dataid>/',views.editpage,name="editpage"),
    path('updatedata/<int:dataid>/',views.updatedata,name="updatedata"),
    path('deletedata/<int:dataid>/',views.deletedata,name="deletedata"),
    path('categorypage/',views.categorypage,name="categorypage"),
    path('savedataa/', views.savedataa, name="savedataa"),
    path('cate/',views.cate,name="cate"),
    path('editpage2/<int:dataid>/',views.editpage2,name="editpage2"),
    path('updatedataa/<int:dataid>/',views.updatedataa,name="updatedataa"),
    path('deletedataa/<int:dataid>/',views.deletedataa,name="deletedataa"),
    path('productpage/',views.productpage,name="productpage"),
    path('savedata3/',views.savedata3,name="savedata3"),
    path('product2/',views.product2,name="product2"),
    path('editp/<int:dataid>/',views.editp,name="editp"),
    path('updatedatap/<int:dataid>/',views.updatedatap,name="updatedatap"),
    path('deletedatta/<int:dataid>/',views.deletedatta,name="deletedatta"),
    path('loginpage/',views.loginpage,name="loginpage"),
    path('adminlogin/',views.adminlogin,name="adminlogin"),
    path('adminlogout/',views.adminlogout,name="adminlogout"),
    path('contact/',views.contact,name="contact"),



]


