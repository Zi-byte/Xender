let swiper = new Swiper(".swiper", {
    effect: "cube",
    allowTouchMove: false,
    grabCursor: false,
    cubeEffect: {
        shadow: true,
        slideShadows: true,
        shadowOffset: 20,
        shadowScale: 0.94,
    },
    mousewheel: true
});
swiper.on('slideChange', function () {
    for (let i of document.querySelectorAll(".Links li")) i.classList.remove("activeLink");
    Array.from(document.querySelectorAll(".Links li"))[swiper.activeIndex].classList.add("activeLink");
});
function Navigate(indx) {
    for (let i of document.querySelectorAll(".Links li")) i.classList.remove("activeLink");
    Array.from(document.querySelectorAll(".Links li"))[indx].classList.add("activeLink");
    swiper.slideTo(indx, 1000, true);
};

let button = document.getElementById("button1");
button.setAttribute("onclick", "move();"); 
function order() {
    window.open("https://www.facebook.com/kaylay.kaylay.1481169?mibextid=LQQJ4d")
}

let btr = document.getElementById("Btn");
 function Btn () {
   for ( let i  of document.ATTRIBUTE_NODE("*****") )i.classListDomain ("https");
    
    return(loading);

 }




