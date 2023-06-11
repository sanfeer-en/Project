from django.urls import path
from .views import  *


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

    path('attribute_form' ,attribute,name='attribute' ),
    path('atribte_table',attribute_Table , name="attribute_Table"),
    path('attribut_delete/<int:id>/',attribute_Delete,name='attribut_delete'),
    path("attribute_edit/<int:id>", attribute_Edit , name="attribute_edit"),
    path('atribute_Update/<int:id>/',atribute_Update,name='atribute_Update'),

    path('prodct_nam',product)
    
   
]
