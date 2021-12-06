module.exports = {
  purge: ["./public/**/*.html", "./src/**/*.vue"],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      colors: {
        navlink: "#42b983",
      },
      width: {
        500: "500px",
        600: "600px",
        400: "400px",
      },
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
};
