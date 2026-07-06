/**
 * Theme Manager - Dark Mode & Light Mode System
 * Handles theme switching and persistence
 */

const ThemeManager = {
    currentTheme: localStorage.getItem('theme') || 'light',
    LIGHT_THEME: 'light',
    DARK_THEME: 'dark',
    
    /**
     * Initialize theme system
     */
    init() {
        this.setTheme(this.currentTheme);
        this.attachEventListeners();
        this.detectSystemPreference();
    },
    
    /**
     * Set the current theme
     * @param {string} theme - Theme name ('light' or 'dark')
     */
    setTheme(theme) {
        if (theme !== this.LIGHT_THEME && theme !== this.DARK_THEME) {
            console.error('Invalid theme. Use "light" or "dark"');
            return;
        }
        
        this.currentTheme = theme;
        localStorage.setItem('theme', theme);
        
        // Set data-theme attribute on HTML element
        document.documentElement.setAttribute('data-theme', theme);
        
        // Update toggle button appearance
        this.updateThemeButton(theme);
        
        // Dispatch custom event
        window.dispatchEvent(new CustomEvent('themeChanged', { 
            detail: { theme: theme } 
        }));
        
        console.log(`Theme changed to: ${theme}`);
    },
    
    /**
     * Toggle between light and dark theme
     */
    toggleTheme() {
        const newTheme = this.currentTheme === this.LIGHT_THEME 
            ? this.DARK_THEME 
            : this.LIGHT_THEME;
        this.setTheme(newTheme);
    },
    
    /**
     * Get current theme
     * @returns {string} - Current theme name
     */
    getTheme() {
        return this.currentTheme;
    },
    
    /**
     * Check if dark mode is active
     * @returns {boolean}
     */
    isDarkMode() {
        return this.currentTheme === this.DARK_THEME;
    },
    
    /**
     * Check if light mode is active
     * @returns {boolean}
     */
    isLightMode() {
        return this.currentTheme === this.LIGHT_THEME;
    },
    
    /**
     * Update theme button appearance
     * @param {string} theme - Current theme
     */
    updateThemeButton(theme) {
        const button = document.querySelector('.theme-toggle-btn');
        if (!button) return;
        
        if (theme === this.DARK_THEME) {
            button.textContent = '☀️'; // Sun icon for switching to light
            button.title = 'Switch to Light Mode';
        } else {
            button.textContent = '🌙'; // Moon icon for switching to dark
            button.title = 'Switch to Dark Mode';
        }
    },
    
    /**
     * Detect system preference and apply if no saved preference
     */
    detectSystemPreference() {
        const savedTheme = localStorage.getItem('theme');
        if (savedTheme) return; // Use saved preference if exists
        
        const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
        const preferredTheme = prefersDark ? this.DARK_THEME : this.LIGHT_THEME;
        this.setTheme(preferredTheme);
        
        // Listen for system theme changes
        window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
            const newTheme = e.matches ? this.DARK_THEME : this.LIGHT_THEME;
            this.setTheme(newTheme);
        });
    },
    
    /**
     * Attach event listeners for theme switching
     */
    attachEventListeners() {
        const themeButton = document.querySelector('.theme-toggle-btn');
        if (themeButton) {
            themeButton.addEventListener('click', () => {
                this.toggleTheme();
            });
        }
    },
    
    /**
     * Apply theme to external elements (charts, etc.)
     * @param {HTMLElement} element - Element to style
     */
    applyThemeToElement(element) {
        if (!element) return;
        
        const isDark = this.isDarkMode();
        if (isDark) {
            element.classList.add('dark-theme');
            element.classList.remove('light-theme');
        } else {
            element.classList.add('light-theme');
            element.classList.remove('dark-theme');
        }
    },
    
    /**
     * Get theme-specific colors
     * @returns {Object} - Color palette for current theme
     */
    getColors() {
        const isDark = this.isDarkMode();
        return {
            background: isDark ? '#1a1a1a' : '#f5f5f5',
            card: isDark ? '#2a2a2a' : '#ffffff',
            text: isDark ? '#e0e0e0' : '#333',
            border: isDark ? '#333' : '#ddd',
            primary: '#4CAF50',
            secondary: '#2196F3',
            danger: '#f44336',
            warning: '#ff9800',
            success: '#4CAF50'
        };
    },
    
    /**
     * Get chart.js config for current theme
     * @returns {Object} - Chart.js theme configuration
     */
    getChartConfig() {
        const colors = this.getColors();
        return {
            backgroundColor: colors.card,
            textColor: colors.text,
            gridColor: colors.border,
            borderColor: colors.text
        };
    }
};

// Initialize theme manager when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
        ThemeManager.init();
    });
} else {
    ThemeManager.init();
}

// Export for use in other modules
if (typeof module !== 'undefined' && module.exports) {
    module.exports = ThemeManager;
}