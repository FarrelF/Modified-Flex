const toggleSwitch = document.querySelector('.switch input[type="checkbox"]');

if (localStorage.getItem('theme') === 'theme-dark') {
    toggleSwitch.checked = true; // If the theme has in Dark Mode, the toggle will be checked.
} else {
    toggleSwitch.checked = false; // Else, the toggle will be unchecked.
}

// function to set a given theme/color-scheme
function setTheme(themeName) {
    localStorage.setItem('theme', themeName);
    document.documentElement.className = themeName;
}
// function to toggle between light and dark theme
function toggleTheme() {
    if (localStorage.getItem('theme') === 'theme-dark') {
        setTheme('theme-light');
    } else {
        setTheme('theme-dark');
    }
}
// Immediately invoked function to set the theme on initial load
(function () {
   if (localStorage.getItem('theme') === 'theme-dark') {
      setTheme('theme-dark');
   } else {
      setTheme('theme-light');
   }
})();
