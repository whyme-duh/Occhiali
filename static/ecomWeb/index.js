// var orderButton = document.getElementById('orderButton');
// var billingButton = document.getElementById('billingButton');
// var personalButton = document.getElementById('personalButton');
// var redeemButton = document.getElementById('redeemButton');


// var orderBody = document.getElementById('order');
// var piBody = document.getElementById('personal');
// var billingBody = document.getElementById('billing');
// var redeemBody = document.getElementById('redeem');

// orderButton.addEventListener('click', ()=>{
//     orderBody.style.display = 'block';
//     piBody.style.display = 'none';
//     billingBody.style.display = 'none';
//     redeemBody.style.display = 'none';
// });
// billingButton.addEventListener('click', ()=>{
//     orderBody.style.display = 'none';
//     piBody.style.display = 'none';
//     billingBody.style.display = 'block';
//     redeemBody.style.display = 'none';
// });
// personalButton.addEventListener('click', ()=>{
//     orderBody.style.display = 'none';
//     piBody.style.display = 'block';
//     billingBody.style.display = 'none';
//     redeemBody.style.display = 'none';
// });
// redeemButton.addEventListener('click', ()=>{
//     orderBody.style.display = 'none';
//     piBody.style.display = 'none';
//     billingBody.style.display = 'none';
//     redeemBody.style.display = 'block';
// });


setTimeout(()=>{
    const message = document.getElementById('alert');

    message.style.display= "none";  
}, 2000)

// order style

const angledown = document.getElementById('down');
angledown.addEventListener('click', ()=>{
    document.getElementById('product-detail').style.display = "block";
})

var addForm = document.getElementById('addForm');
var closeBtn = document.getElementById('close')

addForm.addEventListener('click' , ()=>{
    document.getElementById('form').style.display = 'block';
    document.getElementById('close').style.display = 'inline';
    document.getElementById('form').style.transition = '1s ease-in';
});

closeBtn.addEventListener('click' , ()=>{
    document.getElementById('form').style.display = 'none';
    document.getElementById('close').style.display = 'none';
});


