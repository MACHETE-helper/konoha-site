$('.menu-btn').on('click', function (e){
  e.preventDefault();
  $('.menu').toggleClass('menu_active');
  $('.content').toggleClass('content_active');
  $('.content').fadeIn('slow')
})

let btn = document.querySelector('.teacher_name_ana');
let mytxt = document.querySelector('.teachers_txt');
let dropcheck = true;

//btn.addEventListener('click', () => {
//  mytxt.classList.toggle('show');
//});

function showTextAna() {
  let textElement = document.getElementById('teachers_txt');
  textElement.classList.toggle('show');
}

function hideText() {
  let textElement = document.getElementById('teachers_txt');
  let computedStyle = window.getComputedStyle(textElement);
  let displayValue = computedStyle.getPropertyValue('display');
  console.log(displayValue);
  if (displayValue == 'block') {
    textElement.classList.toggle('hidetxt');
  }

}




