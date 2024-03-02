const captions = document.querySelectorAll('.poster .caption-overlay');

captions.forEach((caption) => {
  const poster = caption.closest('a');
  const image = poster.querySelector('img');

  let isHovered = false; // флаг для отслеживания, находится ли курсор над постером или над надписью

  const handleMouseOver = () => {
    isHovered = true;

    captions.forEach((c) => {
      const img = c.parentNode.querySelector('img');
      if (img !== image) {
        img.classList.add('no-animation');
      }
    });

    image.classList.add('animate'); // Добавляем класс для анимации на картинку
    caption.style.opacity = '1';
  };

  const handleMouseOut = () => {
    isHovered = false;

    captions.forEach((c) => {
      c.parentNode.querySelector('img').classList.remove('no-animation');
      c.classList.remove('no-animation');
    });

    if (!isHovered) {
      image.classList.remove('no-animation');
      image.classList.remove('animate'); // Удаляем класс для анимации с картинки
      caption.style.opacity = '0';
    }
  };

  poster.addEventListener('mouseover', handleMouseOver);
  poster.addEventListener('mouseout', handleMouseOut);
  caption.addEventListener('mouseover', handleMouseOver);
  caption.addEventListener('mouseout', handleMouseOut);
});



const slider = document.querySelector('.slider');
const prevButton = document.querySelector('.prev-button');
const nextButton = document.querySelector('.next-button');

const slideWidth = slider.clientWidth / 4;
const slideMargin = -30;
let currentSlide = 0;

const updateSliderPosition = () => {
  const translateX = (slideWidth + slideMargin) * currentSlide * -1;
  slider.style.transform = `translateX(${translateX}px)`;
};

const showPrevSlide = () => {
  if (currentSlide > 0) {
    currentSlide--;
    updateSliderPosition();
  }
};

const showNextSlide = () => {
  const totalSlides = slider.children.length;
  if (currentSlide < totalSlides - 3) {
    currentSlide++;
    updateSliderPosition();
  }
};

prevButton.addEventListener('click', showPrevSlide);
nextButton.addEventListener('click', showNextSlide);




// Код получает ссылку на кнопку переключения темы и на элементы страницы, которые нужно изменить при переключении темы (например, тело страницы, заголовки и кнопки).
const themeToggle = document.getElementById('theme-toggle');
const body = document.body;
const content = document.querySelector('.content');
const third_header = document.querySelector('.third-header');



// Получаем текущую тему из localStorage
let currentTheme = localStorage.getItem('theme');

// Код проверяет, сохранена ли текущая тема в localStorage. Если да, то он устанавливает эту тему на странице.
if (currentTheme) {
  body.classList.add(currentTheme);
  content.classList.add(currentTheme);
  third_header.classList.add(currentTheme);
}


// Когда пользователь нажимает на кнопку переключения темы, код добавляет или удаляет класс "dark" у элементов страницы, которые нужно изменить при переключении темы.
themeToggle.addEventListener('click', () => {
  // Переключаем тему
  body.classList.toggle('dark');
  content.classList.toggle('dark');
  third_header.classList.toggle('dark');
  });


  // Код сохраняет текущую тему в localStorage, чтобы она была сохранена при перезагрузке страницы.
  currentTheme = body.classList.contains('dark') ? 'dark' : '';
  localStorage.setItem('theme', currentTheme);
});
