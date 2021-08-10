const togglebox = document.querySelector('.navbar-tooglebox');
const rightMenu = document.querySelector('.nav-item-right-container');
const leftMenu = document.querySelector('.nav-item-left-container');
const mainSlogan = document.querySelector('.main-slogan');
togglebox.addEventListener('click', ()=>{
    leftMenu.classList.toggle('active');
    rightMenu.classList.toggle('active');
    mainSlogan.classList.toggle('active');
});