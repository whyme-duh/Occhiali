var orderButton = document.getElementById('orderButton');
var billingButton = document.getElementById('billingButton');
var personalButton = document.getElementById('personalButton');
var redeemButton = document.getElementById('redeemButton');


var orderBody = document.getElementById('order');
var piBody = document.getElementById('personal');
var billingBody = document.getElementById('billing');
var redeemBody = document.getElementById('redeem');

orderButton.addEventListener('click', ()=>{
    orderBody.style.display = 'block';
    piBody.style.display = 'none';
    billingBody.style.display = 'none';
    redeemBody.style.display = 'none';
});
billingButton.addEventListener('click', ()=>{
    orderBody.style.display = 'none';
    piBody.style.display = 'none';
    billingBody.style.display = 'block';
    redeemBody.style.display = 'none';
});
personalButton.addEventListener('click', ()=>{
    orderBody.style.display = 'none';
    piBody.style.display = 'block';
    billingBody.style.display = 'none';
    redeemBody.style.display = 'none';
});
redeemButton.addEventListener('click', ()=>{
    orderBody.style.display = 'none';
    piBody.style.display = 'none';
    billingBody.style.display = 'none';
    redeemBody.style.display = 'block';
});


// function openTab(evt, tabName){
// 	var i, tabContent, tabLinks;
// 	tabContent = document.getElementsByClassName('content');
//     console.log(tabContent[0]);
// 	for(i = 0 ;i< tabContent.length; i++){
// 		tabContent[i].style.display="none";
// 	}
// 	// tabLinks = document.getElementsByClassName('nav');
// 	// for(i=0;i<tabLinks.length ;  i++){
// 	// 	tabLinks[i].className = tabLinks[i].className.replace("active", "");
// 	// }
// 	document.getElementById('tabName').style.display = "block";
// }