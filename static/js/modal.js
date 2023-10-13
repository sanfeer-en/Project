// modal search div....................



$(document).ready(function () {
    $('#searchInput').on('input', function () {
        const searchText = $(this).val().toLowerCase();
        console.log(searchText);

        // Make an AJAX request with product_name to fetch stock data.
        $.ajax({
            url: '/api/category/?search=' + searchText,
            type: 'GET',
            dataType: 'json',
            success: function (data) {
                // Display the products in the modal.
                displayModalProducts(data, searchText);
                console.log(data)
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
                    <ul>
                        <li id="categoryName">${productName}</li>
                        <li id="sellingAmountDetails">Rs: ${price}</li>
                        <li id="quantityDetails">Quantity: ${quantityValue}</li>
                    </ul>
                `;

                resultContainerDiv.append(content);
            }
        }
    }

    // Listen for input changes in the search input field
    $('#searchInput').on('input', function () {
        const searchText = $(this).val().toLowerCase();
        displayModalProducts(data, searchText);
    });

    // When the user clicks on a search result, call the displayModalProducts() function.
  
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
