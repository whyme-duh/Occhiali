


setTimeout(()=>{
    var message = document.getElementById('alert');

    message.style.display= "none";  
}, 2000)

// order style

var angledown = document.getElementById('down');
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


