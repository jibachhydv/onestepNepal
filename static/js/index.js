/*
const threeBars = document.querySelector(".three-bars");
const barFirst = document.querySelector(".bar-1");
const barSecond = document.querySelector(".bar-2");
const barThird = document.querySelector(".bar-3");

threeBars.addEventListener("click",()=>{
    barFirst.classList.toggle("cross-bar-1");
    barSecond.classList.toggle("cross-bar-2");
    barThird.classList.toggle("cross-bar-3");
})
*/






const threeBars = document.querySelector(".three-bars");
const navigation = document.querySelector(".navigation");

function myFunction() {
    threeBars.classList.toggle("change");
    navigation.classList.toggle("navigation-toggle");
  }

const ripplesButton =   document.querySelector(".button");
if(ripplesButton !== null){

ripplesButton.addEventListener("click",function(e){
    let x = e.clientX - e.target.offsetLeft;
    let y = e.clientY - e.target.offsetTop;
    let ripples = document.createElement("span");
    ripples.classList.add("ripple");
    this.appendChild(ripples);
    ripples.style.left = `${x}px`; 
    ripples.style.top = `${y}px`;

    setTimeout(() => { 
        ripples.remove(); 
    }, 300); 
})
}
