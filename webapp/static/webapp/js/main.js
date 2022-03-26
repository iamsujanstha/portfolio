// Get the container element
navbar = document.querySelector(".nav").querySelectorAll('.navbar-nav a');

navbar.forEach(element => {
  element.addEventListener('click',function(){
    navbar.forEach(nav=>nav.classList.remove('active'));
    this.classList.add('active');
  });   
    
});

