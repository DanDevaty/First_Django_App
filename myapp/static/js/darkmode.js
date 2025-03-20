console.log("Darkmode JS je načten!");

document.addEventListener("DOMContentLoaded", function () {
    const toggleTheme = document.getElementById("toggleTheme");
    const themeIcon = document.getElementById("themeIcon");

    if (!toggleTheme || !themeIcon) {
        console.error("Chyba: Nelze najít tlačítko nebo ikonu!");
        return;
    }

    // Získáme téma z localStorage nebo podle systému
    let currentTheme = localStorage.getItem("theme") || (window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");

    // Aplikujeme téma
    document.documentElement.setAttribute("data-bs-theme", currentTheme);
    themeIcon.className = currentTheme === "dark" ? "bi bi-sun-fill" : "bi bi-moon-fill";

    // Přepnutí na kliknutí
    toggleTheme.addEventListener("click", () => {
        currentTheme = currentTheme === "dark" ? "light" : "dark";
        document.documentElement.setAttribute("data-bs-theme", currentTheme);
        localStorage.setItem("theme", currentTheme);
        themeIcon.className = currentTheme === "dark" ? "bi bi-sun-fill" : "bi bi-moon-fill";
    });
});
