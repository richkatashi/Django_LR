// Код получает ссылку на кнопку переключения темы и на элементы страницы, которые нужно изменить при переключении темы (например, тело страницы, заголовки и кнопки).
const themeToggle = document.getElementById('theme-toggle');
const body = document.body;
const content = document.querySelector('.content');
const footer = document.querySelector('footer');
const information = document.querySelector('.information');
const container_wrapper = document.querySelector('.container-wrapper');

// Получаем текущую тему из localStorage
let currentTheme = localStorage.getItem('theme');

// Код проверяет, сохранена ли текущая тема в localStorage. Если да, то он устанавливает эту тему на странице.
if (currentTheme) {
  body.classList.add(currentTheme);
  content.classList.add(currentTheme);
  footer.classList.add(currentTheme);
  information.classList.add(currentTheme);
  container_wrapper.classList.add(currentTheme);
}

// Когда пользователь нажимает на кнопку переключения темы, код добавляет или удаляет класс "dark" у элементов страницы, которые нужно изменить при переключении темы.
themeToggle.addEventListener('click', () => {
  // Переключаем тему
  body.classList.toggle('dark');
  content.classList.toggle('dark');
  footer.classList.toggle('dark');
  information.classList.toggle('dark');
  container_wrapper.classList.toggle('dark');

  // Код сохраняет текущую тему в localStorage, чтобы она была сохранена при перезагрузке страницы.
  currentTheme = body.classList.contains('dark') ? 'dark' : '';
  localStorage.setItem('theme', currentTheme);
});