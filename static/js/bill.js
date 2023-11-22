
$(document).ready(function () {
    
    let billDetails = {
        holdingId:0,
        waiter: '',
        billing_staff : '',
        kot:false,
        bill_status:'None',
        selectedProducts: [],
        subTotal: 0,
        totalAmount: 0,
        discount: {
          type: '',
          value: 0,
          discountedPrice: 0
        },
        order: {
          type: '',
          deliveryAddress: ''
        },
        customer: {
          customer_id:'',
          customer_name:'',
        },
        comment: {
          text: '',
          showOnBill: false
        },
        referenceCode: '',
        payment_method: '',
        table:{
          table_on:0,
          table_status:'',
        }
      };
   


    $('.category-item').on('click', function () {
        const category_name = $(this).data('category-name');
       
        $.ajax({
            url: '/api/category',
            type: 'GET',
            dataType: 'json',
            success: function (data) {
                displayCategoryProducts(data, category_name, $(this));
            },
            error: function (error) {
                alert('error');
            }
        });
    });

    
    function displayCategoryProducts(data, category_name) {
        const filteredData = data.filter(stock => {
        
    
            return stock.Product.Category_Fr.Namecategory  === category_name && stock.Product.Is_for_sale === true;
        });
    
        const container = $('.parent-listin'); // Target the specific container

        container.empty();
        for (let i = 0; i < filteredData.length; i++) {
            const productName = filteredData[i].Product.Product_Name;
           
            const quantityValue = filteredData[i].Quantity;
          
            const price = filteredData[i].Selling_Amount;
            const img = filteredData[i].Product.Product_Image;

            

            let content = `
            <div class="listin card text-center "  data-product-name="${productName}" >
                <img src="${img}" alt="" class="img-product">
                <span id="categoryName">${productName}</span>
                <span id="sellingAmountDetails">Rs: ${price}</span>
                <span id="quantityDetails">Quantity: ${quantityValue}</span>
                
                </div>
            `;
            container.append(content);
        }
    
 
    
       
    }




    // Initial view state
    let isGridView = true;
    
    // Function to toggle between grid view and list view
    function toggleView() {
        isGridView = !isGridView;
    
        if (isGridView) {
            // Show the image in grid view
            $('.img-product').show();
            $('.listin').removeClass('list-view'); // Remove the list view class
        } else {
            // Hide the image in list view
            $('.img-product').hide();
            $('.listin').addClass('list-view'); // Add the list view class to adjust the height
        }
    }
    
    // Bind click events to the view buttons
    $('.btn-grid-view').on('click', function () {
        if (!isGridView) {
            toggleView();
            $(this).addClass('active');
            $('.btn-list-view').removeClass('active');
        }
    });
    
    $('.btn-list-view').on('click', function () {
        if (isGridView) {
            toggleView();
            $(this).addClass('active');
            $('.btn-grid-view').removeClass('active');
        }
    });



    $(document).on('click', '.listin', function () {

        const productName = $(this).data('product-name');

      
            // Check if the clicked .listin product is in filteredData
            $.ajax({
                url: '/api/attribute/',
                type: 'GET',
                dataType: 'json',
                success: function (data) {
                    filteredData = data.filter(attributCategory => {
                        return attributCategory.product.Product_Name === productName;
                    });
        
                    if (filteredData.length > 0) {
                        displayVariantDiv(filteredData, $('#modalVariens'));
                    } else {
                        alert('No data found for the selected product.');
                    }
                },
                error: function (error) {
                    alert('Error: ' + error);
                }
            });
        });

   
  
 
    $('#searchInput').on('input', function () {
        const searchText = $(this).val().toLowerCase();
           
        // Make an AJAX request with product_name to fetch stock data.
        $.ajax({
            url: '/api/category/',
            type: 'GET',
            dataType: 'json',
            success: function (data) {
                
                // Display the products in the modal.
                displayModalProducts(data, searchText);
                
            },
            error: function (error) {
                alert('error');
            }
        });
    });
    
    // Function to display modal products based on the search input
    function displayModalProducts(data, searchText) {
        const resultContainerDiv = $('.result-container');
        resultContainerDiv.empty();
    
        for (let i = 0; i < data.length; i++) {
            const productName = data[i].Product.Product_Name;
            const quantityValue = data[i].Quantity;
            const price = data[i].Selling_Amount;
        
            const productID = data[i].Product.id ;
          
        
            if (productName.toLowerCase().includes(searchText) && data[i].Product.Is_for_sale) {
                let content = `
                <div class="w-100 listingProducts text-center" data-product_name="${productName}">
                  
                        <li id="categoryName" class="productValue" data-product_name="${productName}">${productName}</li>
                        <li id="sellingAmountDetails" class="priceValue" data-price="${price}">Rs: ${price}</li>
                        <li id="quantityDetails" class="quantityValue" data-quantity="${quantityValue}">Quantity: ${quantityValue}</li>
                    
                    <input type="text" hidden class="productId" value="${productID}">
                </div>
            `;
                resultContainerDiv.append(content);
            }
        }

        
    
    
        $('.result-container div').on('click', function () {
            const product_name = $(this).data('product_name');
      
        
            $.ajax({
                url: '/api/attribute/',
                type: 'GET',
                dataType: 'json',
                success: function (data) {
                    filteredData = data.filter(attributCategory => {
                        return attributCategory.product.Product_Name === product_name;
                    });
        
                    if (filteredData.length > 0) {
                        displayVariantDiv(filteredData, $('#modalVariens'));
                    } else {
                        directBill()
                        $('.variantbody').modal('hide');
                        
                    }
                },
                error: function (error) {
                    alert('Error: ' + error);
                }
            });
        });
        
        // Attach a click event for .listin elements within the document
        
    }



    function displayVariantDiv(filteredData, modal) {
        const modalBody = modal.find(".variantbody");
        modalBody.empty();

        for (const item of filteredData) {
            // Extract relevant information from the item
            const productImg = item.product.Product_Image;
            const attributeName = item.attributeName;
            const addOn = item.add_On.Product_Name;
            const addOnQuantity = item.add_on_quantity;
            const extra = item.extra.Product_Name;
            const extraQuantity = item.extra_quantity;
            const price = item.price;
       
            const product_names = item.product.Product_Name;

            const attribute_id = item.id;
            // console.log(attribute_id);
            

            const product_id = item.product.id;


            // console.log(product_id);
            

            // Create HTML elements with the extracted information
            const card = $('<div class="col card cardVariants gy-5"></div>');
            card.append(`<img src="${productImg}" alt="" class="product_Image w-100">`);
            card.append(`<small class="font-weight-bold attrubuteClass" id="attributId" data-attribute_name="${attributeName}" >Attribute:${attributeName}</small>`);
            card.append(`<small class="font-weight-bold addOnclass" data-adon="${addOn}" >Add On: ${addOn}</small>`);
            card.append(`<small class="font-weight-bold addQuantity"  data-adquantity="${addOnQuantity}" >Add On Quantity: ${addOnQuantity}</small>`);
            card.append(`<small class="font-weight-bold ExtQTy" data-extraqty="${extraQuantity}" >Extra Quantity: ${extraQuantity}</small>`);
            card.append(`<small class="font-weight-bold Extra"  data-extra="${extra}"   >Extra: ${extra}</small>`);
            card.append(`<span class="font-weight-bold Prices" data-price="${price}"   >Price: ${price}</span>`);

            card.append(`<input type="text" hidden class="productnameid" value="${product_names}">`);
            card.append(`<input type="text" hidden class="productid" value="${product_id}">`);
            card.append(`<input type="text" hidden class="attributeid" value="${attribute_id}">`);

            // Append the card to the modal body
            modalBody.append(card);
        }

        // Open the modal
        modal.modal("show");
        
        //doubt to clear:------

        $(document).on('click', '.cardVariants', function() {
            // Call your VariantBill function or perform other actions with the clicked element
            VariantBill(this);
        });
        
       
    }


    function VariantBill(clickedElement) {
        // console.log('Clicked Element:', clickedElement);
    
        const attribute_Name = $(clickedElement).find('#attributId').data('attribute_name');
       
        
        const ad_On = $(clickedElement).find('.addOnclass').data('adon');
        // console.log('Add On:', ad_On);
        
        const aad_Quantity = $(clickedElement).find('.addQuantity').data('adquantity');
        // console.log('Add On Quantity:', aad_Quantity);
        
        const extraa = $(clickedElement).find('.Extra').data('extra');
        // console.log('Extra:', extraa);
        
        const pricess = $(clickedElement).find('.Prices').data('price');
        // console.log('Price:', pricess);
        
        const Extra_Quantity = $(clickedElement).find('.ExtQTy').data('extraqty');

         const product_Nameses = $('.productnameid').val();
        // console.log('Extra Quantity:', Extra_Quantity);

        const product_Ide = $('.productid').val();
        // console.log('Extra Quantity:', Extra_Quantity);

        const attributes_Ide = $('.attributeid').val();
    
        // Call the updateBill function with the extracted data
        updatedBill(pricess, attribute_Name, ad_On, extraa,product_Nameses,product_Ide,attributes_Ide);
    
        // Your logic here
    }
    
    function updatedBill(pricess, attribute_Name, ad_On, extraa,product_Nameses,product_Ide,attributes_Ide) {
        let product = {
            id: product_Ide,  // Set to null or any appropriate value
            p_name: product_Nameses,  // Set to null or any appropriate value
            attributeId: attributes_Ide,
            quantity: 1,
            price: pricess,
            total: pricess,
            delete: false,
            attr_name: attribute_Name,
            deleted_from: "None",
            attr_add: ad_On,
            attr_extra: extraa,
            add_on_deleted_from: "None",
            extra_deleted_from: "None",
            old_quantity: 0,
            product_status: 'None',
            product_type: 'None',
        };
      
        // Push the product into the selectedProducts array in billDetails
        billDetails.selectedProducts.push(product);

        displaySelectedProducts(billDetails.selectedProducts)
        // Log the product to the console
        console.log(product);
    }



    function displaySelectedProducts(product) {
    
        let tableBody = $("#productTableBody");
      

      
        for (let i = 0; i < product.length; i++) {
          
          console.log(`product: ${product[i].p_name}`);
          html = `
          <tr class="tablerow">
          <td class="border-right  border-bottom tableTd">${product[i].p_name}
             <br> <span>price:${product[1].price}
             </span>
          </td>
          <td class="border-right   border-bottom "><input  class="border-0 text-center" type="number" value='${product[i].quantity}'></td>
          <td class="border-right text-center   border-bottom ">Rs.${product[i].total}</td>
        </tr>
          `
          ;
          tableBody.append(html)
        }
      }
      
      // Call the function to initially display the selected products
      






    $('#barcodeNumber').on('change', function () {
        const product_code = $(this).val();
    
        // Extract the last 5 digits
        const last5Digits = product_code.slice(-5);
        
    
        // Check if the last5Digits exist in the Stock table
        $.ajax({
            url: '/api/category',
            type: 'GET',
            dataType: 'json',
            success: function (stockData) {
                
                if (stockData.length > 0) {
                    // Product exists in the Stock table
                    
    
                    // Call the displayprocode function with the filtered data
                    const filteredData = displayprocode(stockData, last5Digits);
                   
                    const product_names =filteredData.Product.Product_Name
                    barcodeAtttribute(product_names)

                } else {
                    // Product does not exist in the Stock table
                    console.log('Product does not exist in Stock');
                }
            },
            error: function (error) {
                alert('Error: ' + error);
            }
        });
   
    
    function displayprocode(stockData, last5Digits) {
        const filteredData = stockData.find(stock => {
            return stock.Product.Product_code === last5Digits && stock.Product.Is_for_sale === true;
        });
        return filteredData;
    }
    
    
    
        // Check if the product exists in the attributecategory table
        function barcodeAtttribute (product_Name){
            const product_name = product_Name
            $.ajax({
                url: '/api/attribute/',
                type: 'GET',
                dataType: 'json',
                success: function(data) {
                    filteredData = data.filter(attributCategory => {
                        return attributCategory.product.Product_Name === product_name;
                    });
        
                    if (filteredData.length > 0) {
                        displayVariantDiv(filteredData, $('#modalVariens'));
                    } else {
                        alert('No data found for the selected product.');
                    }
                },
                error: function (error) {
                    alert('Error: ' + error);
                }
            });
        }
    });


   
    function directBill() {
        const productName = $('.listingProducts').find('.productValue').data('product_name');
        
    
        // Retrieve the product ID from the hidden input
        const productIdElement = $('.productId').val();
       
    
       
        const price = $('.listingProducts').find('.priceValue').data('price');
       
    
        const quantityValue = $('.listingProducts').find('.quantityValue').data('quantity');
        // 
    
        
        updateBill(productName,productIdElement,price,quantityValue) 
    };

    function updateBill(productName,productIdElement,price,quantityValue,) {
      let product = { id: productIdElement,
        p_name: productName,
        attributeId: null,
        quantity: 1,
        price: price,
        total: price,
        delete: false,
        attr_name:"None",
        deleted_from :"None",
        attr_add:"None",
        attr_extra: "None",
        add_on_deleted_from :"None",
        extra_deleted_from :"None",
        old_quantity : 0,
        product_status:'None',
        product_type:'None',

    }
    billDetails.selectedProducts.push(product)

    displaySelectedProducts(billDetails.selectedProducts);
console.log(product);
}



        

}); 



    
 


