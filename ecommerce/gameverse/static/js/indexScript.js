var typed = new Typed(".auto_type",{
    strings:["GAMING ACCESSORIES","PLAY STATIONS","VIDEO GAMES","GIFT CARDS","PC ACCESSORIES"],
    typeSpeed:90,
    backSpeed:80,
    loop:true
})
let list = document.querySelector('.mover .mover_container');
let items = document.querySelectorAll('.mover .mover_container .slider');
let dots = document.querySelectorAll('.mover .dots li');
let prev = document.getElementById('prev');
let next = document.getElementById('next');

let active = 0;
let lenghtItems = items.length - 1;
next.onclick = function(){
    if (active + 1 >lenghtItems){
        active = 0;
    }
    else{
        active = active + 1;

    }
    reloadSlider();
}
prev.onclick = function(){
    if (active - 1 < 0){
        active = lenghtItems;
    }
    else{
        active = active - 1;

    }
    reloadSlider();
}
let refreshSlider = setInterval(()=>{next.click()},4000);
function reloadSlider(){
    let checkLeft = items[active].offsetLeft;
    list.style.left = -checkLeft + 'px';

    let lastActiveDot = document.querySelector('.mover .dots li.active');
    lastActiveDot.classList.remove('active');
    dots[active].classList.add('active');
    clearInterval(refreshSlider);
    refreshSlider = setInterval(()=>{next.click()},3000);

    
}
dots.forEach((li,key)=>{
    li.addEventListener('click',function(){
        active = key;
        reloadSlider()
    })
})