$(document).ready(function () {
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



    function displayCategoryProducts(data, category_name, clickedElement) {
        const filteredData = data.filter(stock => {

    
            return stock.Product.Category_Fr.Namecategory  === category_name && stock.Product.Is_for_sale === true;
        });
        console.log(filteredData)
        const container = $('.parent-listin'); // Target the specific container

        container.empty();
        for (let i = 0; i < filteredData.length; i++) {
            const productName = filteredData[i].Product.Product_Name;
           
            const quantityValue = filteredData[i].Quantity;
          
            const price = filteredData[i].Selling_Amount;
            const img = filteredData[i].Product.Product_Image;

            

            let content = `
            <div class="listin card text-center">
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
            // ...
        
            // Function to display modal products based on the search input
            function displayModalProducts(data, searchText) {
                const resultContainerDiv = $('.result-container');
                resultContainerDiv.empty();
        
                for (let i = 0; i < data.length; i++) {
                    const productName = data[i].Product.Product_Name;
                    const quantityValue = data[i].Quantity;
                    const price = data[i].Selling_Amount;
        
                    if (productName.toLowerCase().includes(searchText) && data[i].Product.Is_for_sale) {
                        let content = `
                        <div class="w-100 "  data-product_name="${productName}">
                            <ul>
                                <li id="categoryName">${productName}</li>
                                <li id="sellingAmountDetails">Rs: ${price}</li>
                                <li id="quantityDetails">Quantity:  ${quantityValue}</li>
                            </ul>
                            </div>
                        `;
        
                        resultContainerDiv.append(content);
                    }
                }
                $('.result-container div').on('click', function() {
                    const product_name = $(this).data('product_name');
                
                    $.ajax({
                        url: '/api/attribute/',
                        type: 'GET',
                        dataType: 'json',
                        success: function(data) {
                            const filteredData = data.filter(attributCategory => {
                                return attributCategory.product.Product_Name === product_name;
                            });
                
                            if (filteredData.length > 0) {
                                displayVariantDiv(filteredData);
                            } else {
                                alert('No data found for the selected product.');
                            }
                        },
                        error: function(error) {
                            alert('Error: ' + error);
                        }
                    });
                });
                
                function displayVariantDiv(filteredData) {
                    const modal = $("#modalVariens");
                    const modalBody = modal.find('.modal-body');
                    modalBody.empty();
                
                    // Assuming filteredData contains only one item (you can loop if there can be multiple)
                    const item = filteredData[0];
                    // console.log(item);
                    // Extract relevant information from the item
                    const productImg= item.product.Product_Image;
                    console.log(productImg)
                    const attributeName = item.attributeName;
                    console.log(attributeName)
                    const addOn = item.add_On.Product_Name;
                    console.log(addOn)
                    const addOnQuantity = item.add_on_quantity;
                    console.log(addOnQuantity)
                    const extra = item.extra.Product_Name;
                    console.log(extra)
                    const extraQuantity = item.extra_quantity;
                    console.log(extraQuantity)
                    const price = item.price;
                    console.log(price)
                
                    // Create HTML elements with the extracted information
                    const card = $('<div class="card w-50"></div>');
                    card.append(`<img src="${productImg}" alt="" class="product_Image">`);
                    card.append(`<p>attributeName: ${attributeName}</p>`);
                    card.append(`<p>Add On: ${addOn}<span> add_on_quantity: ${addOnQuantity}</span></p>`);
                    card.append(`<p>Extra: ${extra}<span> extra_quantity: ${extraQuantity}</span></p>`);
                    card.append(`<p>Price: ${price}</p>`);
                    
                
                    // Append the card to the modal body
                    modalBody.append(card);
                
                    // Show the modal
                    modal.modal('show');
                    
                }
            }
            $('.result-container').on('click', function() {
                $('#modalSearch').hide();
            });
            $('.close').on('click', function() {
                $('#modalSearch').show();
            });
            
        
       
          
       
          













});






