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
                                <li id="quantityDetails">Quantity: ${quantityValue}</li>
                            </ul>
                            </div>
                        `;
        
                        resultContainerDiv.append(content);
                    }
                }
                $('.result-container div').on('click', function(){
        
                    const product_name = $(this).data('product_name');
                    console.log('rootsysadadadad')
                    $.ajax({
                      url: '/api/attribute/',
                      type: 'GET',
                      dataType: 'json',
                      data:{
                          product_name: product_name,
          
                      },
                      success: function(data) {
                          console.log(data);
          
                      },
                      error: function(error) {
                          alert(error);
                      }
          
                    });
                 }) 
            }
        
            
        
       
          
       
          





























});






