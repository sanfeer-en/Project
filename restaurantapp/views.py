from django.shortcuts import render , redirect
from .models import *

# Create your views here.

def index(request):
    return render(request, 'base.html')
def unit(request):
    if request.method == 'POST':
        unitname = request.POST.get('UnitName')
        unitvalue = request.POST.get('UnitValue')
        unit=Unit(UnitName=unitname,UnitValue=unitvalue)
        unit.save()
    return render(request, 'unit/form_unit.html')
# def unitable(request):
#     return render(request, 'unit/table_unit.html')
def unitable(request):
    userinput = Unit.objects.all()
    return render(request,'unit/table_unit.html',{"userdata":userinput})
def unitdelete(rquest,unitid):
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
        category_data.Imagecategory = request.POST['CategoryImage']
        category_data.save()
        return redirect ('/category_table')
    
    
def add_tax(request):
    if request.method == 'POST':
        taxname = request.POST.get('TaxName')
        taxvalue = request.POST.get('TaxValue')
        tax=Tax(Taxname=taxname,Taxpercentage=taxvalue)
        tax.save()
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
    if request.method == 'POST':
        attributename = request.POST.get('attributeName')
        attributedata=attributecategory(attributeName=attributename)
        attributedata.save()
    return render(request, 'attributecategory/attribute_form.html')
def attribute_table(request):
    attribute_data = attributecategory.objects.all()
    return render(request,'attributecategory/table_attribute.html',{'attribute_Data':attribute_data})
def attributecategory_delete(request,atrictgry):
    attribute_data=attributecategory.objects.get(id=atrictgry)
    attribute_data.delete()
    return redirect('/attribute_table') 
def attributecategory_edit(request,atrictgry):
    attribute_data=attributecategory.objects.get(id=atrictgry)
    return render(request,'attributecategory/edit_attribute.html',{"attribute_Data":attribute_data})
def attribute_update(request,atrictgry):
    attribute_data = attributecategory.objects.get(id=atrictgry)
    if request.method == 'POST':
        attribute_data.attributeName = request.POST['attributeName']
        attribute_data.save()
        return redirect ('/attribute_table')





