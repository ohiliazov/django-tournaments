const defaultTheme = require("tailwindcss/defaultTheme");

module.exports = {
  content: [
    "./templates/**/*.html",
    "./templates/**/*.svg",
    "./accounts/templates/**/*.html",
    "./tournaments/templates/**/*.html",
  ],
  theme: {
    extend: {
      fontFamily: {
        sans: ["Inter var", ...defaultTheme.fontFamily.sans],
      },
    },
  },
  plugins: [],
};
