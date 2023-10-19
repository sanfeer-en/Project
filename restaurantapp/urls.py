from django.urls import path
from .views import  *
from .apis import *


urlpatterns = [
    
    path("home", index,name='home'),
    path('unit', unit, name="unit"),
    path('unitable',unitable , name="unitabel"),
    path('unitdelete/<int:unitid>/',unitdelete,name='delete'),
    path("unitedit/<int:id>", unitedit , name="unitedit"),
    path("update/<int:id>", unitupdate , name="update"),

    path("add_category" ,Add_category,name="add_category" ),
    path('category_table',Category_table , name="category_tabel"),
    path('category_delete/<int:ctgryid>/',Category_delete,name='category_delete'),
    path('category_edit/<int:ctgryid>/',Category_edit,name='category_edit'),
    path('category_update/<int:ctgryid>/',Category_update,name='category_update'),

    path("add_tax" ,add_tax,name="add_tax" ),
    path('tax_table',tax_table , name="taxtabel"),
    path('tax_delete/<int:taxid>/',tax_delete,name='taxdelete'),
    path("tax_edit/<int:taxid>", tax_edit , name="taxedit"),
    path('tax_update/<int:taxid>/',tax_update,name='tax_update'),

    path("attribute_add" ,attribute_add,name="addattribute" ),
    path('attribute_table',attribute_table , name="attribute_table"),
    path('attributecategory_delete/<int:atrictgry>/',attributecategory_delete,name='attributecategory_delete'),
    path("attributecategory_edit/<int:atrictgry>", attributecategory_edit , name="attributecategory_edit"),
    path('attribute_update/<int:atrictgry>/',attribute_update,name='attribute_update'),

 

    path('prodct_nam',product ,name='generate'),
    path('product_tble',Product_Table , name="product_Table"),
    path('product_delte/<int:id>/',Product_Delete,name="product_Delete"),
    path('product_edit/<int:id>/',Product_edit,name='product_edit'),
    path('product_Update/<int:id>/',Product_Update,name='product_Update'),

    path('company_info',company_Inform , name='cmpnyinfo'),
    path('company_tble',Company_Table , name="cmpny_Table"),
    path('compny_delte/<int:id>/',Company_Delete, name='compnydelete'),
    path('company_edit/<int:id>/',company_edit,name='company_edit'),
    path('cpmpany_Update/<int:id>/',company_Update,name='compani_Update'),

    path('ad_stock',ad_stock ,name='adStck'),
    path('table_stock',stock_Table ,name='table_stock'),
    path('stck_delte/<int:id>/',stock_Delete, name='stckdelete'),
    path('stock_edit/<int:id>/',stock_edit,name='stock_edit'),
    path('stock_Update/<int:id>/',stock_Update,name='stock_Update'),

    path('ad_production_product',ad_Production_product ,name='ad_productions_Prdct'),
    
    path('ad_production',ad_Production ,name='adPrdct'),
    path('table_production',production_Table ,name='table_production'),
    path('prdction_delte/<int:id>/',production_Delete, name='productiondelete'),
    path('producton_edit/<int:id>/', edit_production,name='productionedit'),
    


    path('bills', billing_Form, name='billing'),
    path('api/category/',CategoryProductApi.as_view(),),
    path('api/attribute/',AttributeCategoryViewSet,),
    # path('api/category/',category_product_api, name='category_product_api'),
    # path('api/category/',category_product_api, name='category_product_api'),
  

   
]
