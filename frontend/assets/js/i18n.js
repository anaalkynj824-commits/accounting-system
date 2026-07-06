/**
 * i18n - Internationalization Module
 * Handles Arabic and English language switching
 */

const i18n = {
    currentLanguage: localStorage.getItem('language') || 'ar',
    
    /**
     * Initialize i18n system
     */
    init() {
        this.setLanguage(this.currentLanguage);
        this.attachEventListeners();
    },
    
    /**
     * Set the current language
     * @param {string} lang - Language code ('ar' or 'en')
     */
    setLanguage(lang) {
        if (lang !== 'ar' && lang !== 'en') {
            console.error('Invalid language code. Use "ar" or "en"');
            return;
        }
        
        this.currentLanguage = lang;
        localStorage.setItem('language', lang);
        
        // Update HTML element
        const htmlElement = document.documentElement;
        htmlElement.lang = lang;
        htmlElement.dir = lang === 'ar' ? 'rtl' : 'ltr';
        htmlElement.setAttribute('data-lang', lang);
        
        // Update all translatable elements
        this.updateContent(lang);
        
        // Update active language button
        this.updateLanguageButtons(lang);
        
        // Dispatch custom event
        window.dispatchEvent(new CustomEvent('languageChanged', { detail: { language: lang } }));
    },
    
    /**
     * Update all content to match language
     * @param {string} lang - Language code
     */
    updateContent(lang) {
        const elements = document.querySelectorAll('[data-ar][data-en]');
        
        elements.forEach(element => {
            if (lang === 'ar') {
                element.textContent = element.getAttribute('data-ar');
                if (element.tagName === 'INPUT') {
                    element.placeholder = element.getAttribute('data-ar');
                }
            } else {
                element.textContent = element.getAttribute('data-en');
                if (element.tagName === 'INPUT') {
                    element.placeholder = element.getAttribute('data-en');
                }
            }
        });
    },
    
    /**
     * Update language button states
     * @param {string} lang - Language code
     */
    updateLanguageButtons(lang) {
        const langButtons = document.querySelectorAll('.lang-btn');
        langButtons.forEach(btn => {
            const btnLang = btn.getAttribute('data-lang');
            if (btnLang === lang) {
                btn.classList.add('active');
            } else {
                btn.classList.remove('active');
            }
        });
    },
    
    /**
     * Get translated string by key
     * @param {string} key - Translation key
     * @returns {string} - Translated string or key if not found
     */
    t(key) {
        // This function allows programmatic access to translations
        // You can extend this with a translation object as needed
        const translations = {
            ar: {
                'dashboard': 'لوحة التحكم',
                'customers': 'العملاء',
                'suppliers': 'الموردين',
                'invoices': 'الفواتير',
                'expenses': 'المصروفات',
                'reports': 'التقارير',
                'ai': 'الذكاء الاصطناعي',
                'settings': 'الإعدادات',
                'logout': 'تسجيل الخروج',
                'total_revenue': 'إجمالي الإيرادات',
                'total_expenses': 'إجمالي المصروفات',
                'net_profit': 'صافي الربح',
                'total_customers': 'عدد العملاء'
            },
            en: {
                'dashboard': 'Dashboard',
                'customers': 'Customers',
                'suppliers': 'Suppliers',
                'invoices': 'Invoices',
                'expenses': 'Expenses',
                'reports': 'Reports',
                'ai': 'AI Assistant',
                'settings': 'Settings',
                'logout': 'Logout',
                'total_revenue': 'Total Revenue',
                'total_expenses': 'Total Expenses',
                'net_profit': 'Net Profit',
                'total_customers': 'Total Customers'
            }
        };
        
        return translations[this.currentLanguage][key] || key;
    },
    
    /**
     * Attach event listeners for language switching
     */
    attachEventListeners() {
        const langButtons = document.querySelectorAll('.lang-btn');
        langButtons.forEach(btn => {
            btn.addEventListener('click', (e) => {
                e.preventDefault();
                const lang = btn.getAttribute('data-lang');
                this.setLanguage(lang);
            });
        });
    },
    
    /**
     * Get current language
     * @returns {string} - Current language code
     */
    getLanguage() {
        return this.currentLanguage;
    },
    
    /**
     * Check if current language is Arabic
     * @returns {boolean}
     */
    isArabic() {
        return this.currentLanguage === 'ar';
    },
    
    /**
     * Check if current language is English
     * @returns {boolean}
     */
    isEnglish() {
        return this.currentLanguage === 'en';
    }
};

// Initialize i18n when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
        i18n.init();
    });
} else {
    i18n.init();
}

// Export for use in other modules
if (typeof module !== 'undefined' && module.exports) {
    module.exports = i18n;
}