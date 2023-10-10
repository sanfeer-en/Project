$(document).ready(function () {
    $('.category-item').on('click', function () {
        const category_name = $(this).data('category-name');
        console.log(category_name);
        $.ajax({
            url: '/api/category',
            type: 'GET',
            dataType: 'json',
            success: function (data) {
                displayCategoryProducts(data, category_name, $(this));
                console.log(data);
            },
            error: function (error) {
                alert('error');
            }
        });
    });



    function displayCategoryProducts(data, category_name, clickedElement) {
        // console.log('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa');
        const filteredData = data.filter(stock => {
            // console.log('stock:', stock); // Log the entire stock object
            // console.log('stock.Product:', stock.Product); // Log the Product property
    
            return stock.Product.Category_Fr.Namecategory  === category_name && stock.Product.Is_for_sale === true;
        });
        // console.log("dats",filteredData)
        const container = $('.parent-listin'); // Target the specific container

        container.empty();
        for (let i = 0; i < filteredData.length; i++) {
            const productName = filteredData[i].Product.Product_Name;
            // console.log(productName)
            const quantityValue = filteredData[i].Quantity;
            // console.log(quantityValue)
            const price = filteredData[i].Selling_Amount;
            const img = filteredData[i].Product.Product_Image;

            // console.log(price)
            

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
});


$(document).ready(function () {
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
});

// modal search div....................
$(document).ready(function () {
    $('.searchdiv').on('click', function () {
        const product_name = $(this).data('product-name');
        console.log(product_name);

        // Make an AJAX request with product_name to fetch stock data
        $.ajax({
            url: '/api/category/?search=' + product_name,
            type: 'GET',
            dataType: 'json',
            success: function (data) {
                // Handle the success response here
                console.log(data);
                
                // You can update the UI with the fetched stock data here
                // For example, update the content of the #productSearchResults div
                const productSearchResults = $('#productSearchResults');
                productSearchResults.empty(); // Clear previous results

                // Iterate through the data and append results to the div
                $.each(data, function (index, stockItem) {
                    const resultItem = $('<div class="result-item">');
                    resultItem.append('<p class="product-name">Product: ' + stockItem.Product + '</p>');
                    resultItem.append('<p class="quantity">Quantity: ' + stockItem.Quantity + '</p>');
                    resultItem.append('<p class="selling-amount">Selling Amount: ' + stockItem.Selling_Amount + '</p>');

                    productSearchResults.append(resultItem);
                });
            },
            error: function (error) {
                alert('error');
            }
        });
    });
});



// ... (the rest of your JavaScript code)

const searchDiv = document.getElementById('searchdiv');
const modal = document.getElementById('modal');
const closeModal = document.getElementById('closeModal');

searchDiv.addEventListener('click', () => {
    modal.style.display = 'block';
});

closeModal.addEventListener('click', () => {
    modal.style.display = 'none';
});

// Close the modal when clicking outside of it
modal.addEventListener('click', (event) => {
    if (event.target === modal) {
        modal.style.display = 'none';
    }
});

// Prevent modal from showing on page load
window.addEventListener('load', () => {
    modal.style.display = 'none';
});


