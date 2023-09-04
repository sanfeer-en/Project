from django.shortcuts import render , redirect ,HttpResponse
from django.http import JsonResponse
from .models import *
from django.shortcuts import get_object_or_404

# Create your views here.

def index(request):
    return render(request, 'base.html')
def unit(request):
    if request.method == 'POST':
        unitname = request.POST.get('UnitName')
        unitvalue = request.POST.get('UnitValue')
        unit=Unit(UnitName=unitname,UnitValue=unitvalue)
        unit.save()
        return redirect("/unitable")
        
    return render(request, 'unit/form_unit.html')
# def unitable(request):
#     return render(request, 'unit/table_unit.html')
def unitable(request):
    userinput = Unit.objects.all()
    return render(request,'unit/table_unit.html',{"userdata":userinput})
def unitdelete(request,unitid):
    userinput = Unit.objects.get(id=unitid)
    userinput.delete()
    return redirect("/unitable")
def unitedit(request,id):
    userinput = Unit.objects.get(id=id)
    return render(request,'unit/unit_edit.html',{"userdata":userinput})
def unitupdate(request,id):
    userinput = Unit.objects.get(id=id)
    if request.method == 'POST':
        userinput.UnitName = request.POST['UnitName']
        userinput.UnitValue = request.POST['UnitValue']
        userinput.save()
        return redirect ("/unitable")


def Add_category(request):
    if request.method == 'POST':
        categoryName = request.POST.get('CategoryName')
        imgCategory=request.FILES.get('CategoryImage', None)
        category=Category(Imagecategory=imgCategory,Namecategory=categoryName)
        category.save()
        return redirect('/category_table')
    return render(request,'category/category_form.html')
def Category_table(request):
    categorytable =Category.objects.all()
    return render(request,'category/table_category.html',{'categorytable':categorytable})
def Category_delete(request,ctgryid):
    category_data=Category.objects.get(id=ctgryid)
    category_data.delete()
    return redirect('/category_table')
def Category_edit(request,ctgryid):
    category_data=Category.objects.get(id=ctgryid)
    return render(request,'category/category_edit.html',{"categorytable":category_data})
def Category_update(request,ctgryid):
    category_data = Category.objects.get(id=ctgryid)
    
    if request.method == 'POST':
        category_data.Namecategory = request.POST['CategoryName']
        try:
            if request.FILES['CategoryImage']:
                category_data.Imagecategory = request.FILES['CategoryImage']
        except:
            pass
       
        category_data.save()
        return redirect('/category_table')
    
    
def add_tax(request):
    if request.method == 'POST':
        taxname = request.POST.get('TaxName')
        taxvalue = request.POST.get('TaxValue')
        tax=Tax(Taxname=taxname,Taxpercentage=taxvalue)
        tax.save()
        return redirect ('/tax_table')
    return render(request, 'Tax/form_tax.html') 
def tax_table(request):
    Tax_data = Tax.objects.all()
    return render(request,'Tax/tax_table.html',{'taxdata':Tax_data})
def tax_delete(request,taxid):
    tax_data=Tax.objects.get(id=taxid)
    tax_data.delete()
    return redirect('/tax_table')
def tax_edit(request,taxid):
    tax_data=Tax.objects.get(id=taxid)
    return render(request,'Tax/edit_tax.html',{"taxdata":tax_data})
def tax_update(request,taxid):
    tax_data = Tax.objects.get(id=taxid)
    if request.method == 'POST':
        tax_data.Taxname = request.POST['TaxName']
        tax_data.Taxpercentage = request.POST['TaxValue']
        tax_data.save()
        return redirect ('/tax_table')



def attribute_add(request):
    product_Value =Product.objects.all()
    if request.method == 'POST':
        attributename = request.POST.get('attributeName')
        
    
        product_Id = request.POST.get('ProductValue')
        products =Product.objects.get(id=product_Id)

        quantities = request.POST.get('QuantityValue') 
        prices = request.POST.get('PriceValue') 

        add_on_Id = request.POST.get('AddOnValue')
        add_on =Product.objects.get(id=add_on_Id)

        add_on_Quantity_Id = request.POST.get('AdQuantityValue')
        add_on_quantity =Product.objects.get(id=add_on_Quantity_Id)

        extra_Id = request.POST.get('ExtraValue')
        extra_Value =Product.objects.get(id=extra_Id)

      
        extra_Quantity = request.POST.get('ExtraQunatitytValue')

        attributedata=attributecategory(attributeName=attributename,product =products,quantity =quantities,price=prices ,add_On=add_on,add_on_quantity=add_on_quantity,
                                        extra=extra_Value,extra_quantity=extra_Quantity)
        attributedata.save()
        return redirect ('/attribute_table')
    context = {
           'product_Data': product_Value,
    }
    return render(request, 'attributecategory/attribute_form.html',context)
def attribute_table(request):
    attribute_data = attributecategory.objects.all()
    return render(request,'attributecategory/table_attribute.html',{'attribute_Data':attribute_data})
def attributecategory_delete(request,atrictgry):
    attribute_data=attributecategory.objects.get(id=atrictgry)
    attribute_data.delete()
    return redirect('/attribute_table') 

def attributecategory_edit(request,atrictgry):
    attribute_data=attributecategory.objects.get(id=atrictgry)
    product_Fr =Product.objects.all()
    add_On =Product.objects.all()
    context = {
           'attribute_Data': attribute_data,
           'product_Data' :product_Fr,
           'addOn_data': add_On,
           
    } 
    return render(request,'attributecategory/edit_attribute.html',context)
   
def attribute_update(request,atrictgry):
    attribute_data = attributecategory.objects.get(id=atrictgry)
    if request.method == 'POST':
        attribute_data.attributeName = request.POST['attributeName']
        
        product_id =request.POST['ProductValue']
        attribute_data.product =Product.objects.get(id=product_id)

        attribute_data.quantity = request.POST['QuantityValue']

        ad_On_id =request.POST['AddOnValue']
        attribute_data.add_On =Product.objects.get(id=ad_On_id)

        attribute_data.price = request.POST['PriceValue']

        ad_On_quan_id =request.POST['AdQuantityValue']
        attribute_data.add_on_quantity =Product.objects.get(id=ad_On_quan_id)

        extra_id =request.POST['AdQuantityValue']
        attribute_data.extra =Product.objects.get(id=extra_id)

        attribute_data.extra_quantity = request.POST['ExtraQunatitytValue']

        attribute_data.save()
        return redirect ('/attribute_table')


def product(request):
    category =Category.objects.all()
    unit = Unit.objects.all()
  
    taxs = Tax.objects.all()
    
    if request.method == 'POST':
        product_Name = request.POST.get('ProductName')
        Category_id =request.POST.get('CategoryValue')
        Categories =Category.objects.get(id=Category_id)
        unit_Id = request.POST.get('UnitValue')
        unities =Unit.objects.get(id=unit_Id)

       
       
        tax_Id = request.POST.get('TaxValue')
        taxes =Tax.objects.get(id=tax_Id)
        is_or_Sale = request.POST.get('for_Sale') == 'True'
        img_Product=request.FILES.get('ProductImage')

        all_Product=Product.objects.create(Product_Name=product_Name,Category_Fr=Categories,Unit_Fr=unities,Tax_Fr =taxes ,Is_for_sale =is_or_Sale,Product_Image=img_Product)
        
        all_Product.save()
        return redirect ('/product_tble')
    return render(request, 'product/product.html', {'category_data':category , 'Unit_Data' :unit , 'Tax_Data': taxs })

def Product_Table(request):
    product_Data =Product.objects.all()
    return render(request,'product/table_product.html',{'Product_Data':product_Data}) 
def Product_Delete(request,id):
    product_Data =Product.objects.get(id=id)
    product_Data.delete()
    return redirect('/product_tble')
def Product_edit(request,id):
    product_Data=Product.objects.get(id=id)
    Category_fori = Category.objects.all()
    Unit_Fori =Unit.objects.all()
    
    tax_for=Tax.objects.all()
    return render(request, 'product/edit_product.html',{"product_data":product_Data , 'for_category':Category_fori , 'for_unit':Unit_Fori  , 'fr_tax':tax_for })

def Product_Update(request,id):
    product_Data=Product.objects.get(id=id)
    if request.method == 'POST':
        product_Data.Product_Name = request.POST['ProductName']
        Category_id =request.POST['CategoryValue']
        product_Data.Category_Fr =Category.objects.get(id=Category_id)
        Unit_id =request.POST['UnitValue']
        product_Data.Unit_Fr =Unit.objects.get(id=Unit_id)
        Tax_id =request.POST['TaxValue']
        product_Data.Tax_Fr =Tax.objects.get(id=Tax_id)
        product_Data.Is_for_sale = request.POST.get('for_Sale') == 'on'
        try:
            if request.FILES['ProductImage']:

                product_Data.Product_Image = request.FILES['ProductImage']
        except:
            pass
        
        product_Data.save()
        return redirect('/product_tble')
    


def company_Inform(request):
    if request.method == 'POST':
        Compni_name = request.POST.get('CmpName')
        Compani_adrss= request.POST.get('CmpAddrs')
        Gst_Numbr=request.POST.get('gstNumb')
        country_Code=request.POST.get('countryCode')
        manufactur_Code=request.POST.get('manufacturCode')
        compnyinfo=CompanyInformation(Company_Name=Compni_name,Company_Address=Compani_adrss,GST_Number=Gst_Numbr,Country_Code=country_Code,Manufacturing_code=manufactur_Code)
        compnyinfo.save()
        return redirect('/company_tble')
    return render(request, 'company_Info/company_form.html') 

def Company_Table(request):
    compnay_Data = CompanyInformation.objects.all()
    return render(request, 'company_Info/company_table.html',{'Compnay_Data':compnay_Data}) 
def Company_Delete(request,id):
    company_Data =CompanyInformation.objects.get(id=id)
    company_Data.delete()
    return redirect('/company_tble')
def company_edit(request,id):
    company_data=CompanyInformation.objects.get(id=id)
    return render(request,'company_Info/company_edit.html',{"company_Data":company_data})
def company_Update(request,id):
    company_Data = CompanyInformation.objects.get(id=id)
    if request.method == 'POST':
        company_Data.Company_Name = request.POST['CmpName']
        company_Data.Company_Address = request.POST['CmpAddrs']
        company_Data.GST_Number = request.POST['gstNumb']
        company_Data.Country_Code = request.POST['countryCode']
        company_Data.Manufacturing_code = request.POST['manufacturCode']
        company_Data.save()
        return redirect ("/company_tble")
    


def ad_stock(request):
    product_Value =Product.objects.all()
    units_Data= Unit.objects.all()
    code_data =CompanyInformation.objects.first()
    if request.method == 'POST':
        vendor_Bill = request.POST.get('vendorBill')

        product_Id = request.POST.get('ProductValue')
        products =Product.objects.get(id=product_Id)

        uni_Id = request.POST.get('UnitData')
        units =Unit.objects.get(id=uni_Id)

        quantities = request.POST.get('QuantityValue')
        purchasing_Amnt = request.POST.get('PurchaseValue')
        selling_Amnt = request.POST.get('SellingValue')
        manfctre_Date=request.POST.get('DateValue')
        expireDate=request.POST.get('DateWorth')
        stock_Data=Stock(Vendor_Bill_No=vendor_Bill ,Product =products ,Units=units ,Quantity=quantities,Purchasing_Amount=purchasing_Amnt,
                         Selling_Amount=selling_Amnt ,Manufacture_Date= manfctre_Date,Expire_Date=expireDate)
        
        stock_Data.save()
        return redirect('/table_stock')
    context = {
        'product_Data': product_Value,
        'unities_Data': units_Data,
        'country_code': code_data.Country_Code,
        'manufacture_code': code_data.Manufacturing_code
    }
    return render(request, 'stock/ad_stock.html',context) 

def stock_Table(request):
    stock_Data =Stock.objects.all()
    return render(request,'stock/table_stock.html',{'Stock_Data':stock_Data}) 
def stock_Delete(request,id):
    stock_Data =Stock.objects.get(id=id)
    stock_Data.delete()
    return redirect('/table_stock')
def stock_edit(request,id):
    stock_Data=Stock.objects.get(id=id)
    product_For =Product.objects.all()
    Unit_For =Unit.objects.all()
    return render(request, 'stock/edit_stock.html',{"Stock_Data":stock_Data ,'fr_Prdct':product_For,'fo_unit':Unit_For})
def stock_Update(request,id):
    stock_Data=Stock.objects.get(id=id)
    if request.method == 'POST':
        stock_Data.Vendor_Bill_No=request.POST['vendorBill']

        product_id =request.POST['ProductValue']
        stock_Data.Product =Product.objects.get(id=product_id)

        unit_id =request.POST['UnitData']
        stock_Data.Units =Unit.objects.get(id=unit_id)

        stock_Data.Quantity=request.POST['QuantityValue']
        stock_Data.Purchasing_Amount=request.POST['PurchaseValue']
        stock_Data.Selling_Amount=request.POST['SellingValue']
        stock_Data.Manufacture_Date=request.POST['DateValue']
        stock_Data.Expire_Date=request.POST['DateWorth']


        stock_Data.save()
        return redirect('/table_stock')
    

def ad_Production(request):
   
    product_Data = Product.objects.filter(Is_for_sale=True)
    RawMaterial_data = Stock.objects.filter(Product__Is_for_sale=False)

    if request.method == 'POST':
        productFr_Id = request.POST.get('product')
        
        products = Product.objects.get(id=productFr_Id)
        

        raw_materials = request.POST.getlist('raw_materials[]')
       

        measurements = request.POST.getlist('raw_materials_measurement[]')
        

        production = Production.objects.create(Product_fr=products)

        for i in range(len(raw_materials)):
            raw_material_id = raw_materials[i]
            try:
                raw_material_ = Stock.objects.get(id=raw_material_id)
            except Stock.DoesNotExist:
                error_message = f"The selected raw material does not exist in the stocks."
                return render(request, 'productions/ad_production.html', {'error_message': error_message, 'Product_Data': product_Data, 'RawMaterial_Data': RawMaterial_data})

            measurement = measurements[i]

            if float(measurement) > raw_material_.Quantity:
                error_message = f"The Measurement for raw Material '{raw_material_.Product}' exceeds the available stock quantity."
                return render(request, 'productions/ad_production.html', {'error_message': error_message, 'Product_Data': product_Data, 'RawMaterial_Data': RawMaterial_data})

            ProductionRawMaterial.objects.create(production=production, Raw_Material=raw_material_, Measurement=measurement)

        return redirect('/table_production')  # Redirect after processing the form

    return render(request, 'productions/ad_production.html', {'Product_Data': product_Data, 'RawMaterial_Data': RawMaterial_data})

def production_Table(request):
    production_Data =Production.objects.all()
    return render(request, 'productions/production_table.html', {'Production_Data':production_Data})
def production_Delete(request,id):
    production_Data =Production.objects.get(id=id)
    production_Data.delete()
    return redirect('/table_production')

def edit_production(request, id):
    production = Production.objects.get(id=id)
    raw_materials = ProductionRawMaterial.objects.filter(production=production)
    product_for_sale = Product.objects.filter(Is_for_sale=True)
    raw_materials_for_production = Stock.objects.filter(Product__Is_for_sale=False)

    if request.method == 'POST':
        product_id = request.POST.get('product')
        try:
            selected_product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            error_message = f"The selected product does not exist."
            return render(request, 'productions/ad_production.html', {'error_message': error_message, 'Product_Data': product_for_sale, 'RawMaterial_Data': raw_materials_for_production})

        production.Product_fr = selected_product
        production.save()

        raw_materials_list = request.POST.getlist('raw_materials[]')
        measurements_list = request.POST.getlist('raw_materials_measurement[]')

        production.productionrawmaterial_set.all().delete()

        for i in range(len(raw_materials_list)):
            raw_material_id = raw_materials_list[i]
            if not raw_material_id:
                continue
            try:
                raw_material_ = Stock.objects.get(id=raw_material_id)
            except Stock.DoesNotExist:
                error_message = f"The selected raw material does not exist in the stocks."
                return render(request, 'productions/ad_production.html', {'error_message': error_message, 'Product_Data': product_for_sale, 'RawMaterial_Data': raw_materials_for_production})

            measurement = measurements_list[i]

            if float(measurement) > raw_material_.Quantity:
                error_message = f"The Measurement for raw Material '{raw_material_.Product.Product_Name}' exceeds the available stock quantity."
                return render(request, 'productions/ad_production.html', {'error_message': error_message, 'Product_Data': product_for_sale, 'RawMaterial_Data': raw_materials_for_production})

            ProductionRawMaterial.objects.create(production=production, Raw_Material=raw_material_, Measurement=measurement)

        return redirect('/table_production')

    context = {
        'production': production,
        'raw_materials': raw_materials,
        'Product_Data': product_for_sale,
        'RawMaterial_Data': raw_materials_for_production,
    }
    return render(request, 'productions/production_edit.html', context)

def biling_Form(request):
    categories = Category.objects.all()
    return render(request, 'billing/billing.html', {'categories': categories})






    
    



