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
        console.log('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa');
        const filteredData = data.filter(stock => {
            console.log('stock:', stock); // Log the entire stock object
            console.log('stock.Product:', stock.Product); // Log the Product property
    
            return stock.Product.Category_Fr.Namecategory  === category_name && stock.Product.Is_for_sale === true;
        });
        console.log("dats",filteredData)
        const container = $('.parent-listin'); // Target the specific container

        container.empty();
        for (let i = 0; i < filteredData.length; i++) {
            const productName = filteredData[i].Product.Product_Name;
            console.log(productName)
            const quantityValue = filteredData[i].Quantity;
            console.log(quantityValue)
            const price = filteredData[i].Selling_Amount;
            const img = filteredData[i].Product.Product_Image;

            console.log(price)
            

            let content = `
            <div class="listin card">
                <img src="${img}" alt="" class="img-product">
                <h6 id="categoryName">${productName}</h6>
                <p id="quantityDetails">Quantity: ${quantityValue}</p>
                <p id="sellingAmountDetails">Selling Amount: ${price}</p>
                </div>
            `;
            container.append(content);
        }
    }
});
