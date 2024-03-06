// НАВЕДЕНИЕ НА КАРТИНКУ И НАДПИСЬ
const captions = document.querySelectorAll('.poster .caption-overlay');

captions.forEach((caption) => {
  const poster = caption.closest('a');
  const image = poster.querySelector('.image-item');

  let isHovered = false; // флаг для отслеживания, находится ли курсор над постером или над надписью

  const handleMouseOver = () => {
    isHovered = true;

    captions.forEach((c) => {
      const img = c.parentNode.querySelector('.image-item');
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
      c.parentNode.querySelector('.image-item').classList.remove('no-animation');
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







