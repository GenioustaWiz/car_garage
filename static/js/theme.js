const toggleButton = document.getElementById('toggle-theme');
const themeIcon = document.getElementById('theme-icon');
const body = document.body;

toggleButton.addEventListener('click', () => {
    const currentTheme = body.getAttribute('data-theme');
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    body.setAttribute('data-theme', newTheme);
    updateThemeIcon(newTheme);
    saveThemeToLocalStorage(newTheme); // Save the theme preference
});

// Check for user's preferred color scheme
const preferredColorScheme = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
const savedTheme = getThemeFromLocalStorage();

if (savedTheme) {
    body.setAttribute('data-theme', savedTheme);
    updateThemeIcon(savedTheme);
} else {
    body.setAttribute('data-theme', preferredColorScheme);
    updateThemeIcon(preferredColorScheme);
}

function updateThemeIcon(theme) {
    themeIcon.innerHTML = theme === 'dark' ? '🌞' : '🌙' ;
}

function saveThemeToLocalStorage(theme) {
    localStorage.setItem('selected-theme', theme);
    // or use "sessionStorage" for data is cleared when the browser session ends
}

function getThemeFromLocalStorage() {
    return localStorage.getItem('selected-theme');
}
