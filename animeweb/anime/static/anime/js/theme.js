const themeToggle = document.getElementById('theme-toggle');
const body = document.body;
const content = document.querySelector('.content');
const third_header = document.querySelector('.third-header');

// Получаем текущую тему из localStorage
let currentTheme = localStorage.getItem('theme');

// Если тема сохранена в localStorage, устанавливаем ее
if (currentTheme) {
  body.classList.add(currentTheme);
  content.classList.add(currentTheme);
  third_header.classList.add(currentTheme);
}

themeToggle.addEventListener('click', () => {
  // Переключаем тему
  body.classList.toggle('dark');
  content.classList.toggle('dark');
  third_header.classList.toggle('dark');
  });

  // Сохраняем текущую тему в localStorage
  currentTheme = body.classList.contains('dark') ? 'dark' : '';
  localStorage.setItem('theme', currentTheme);
});