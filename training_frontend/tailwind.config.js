module.exports = {
  purge: ["./public/**/*.html", "./src/**/*.vue"],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      colors: {
        navlink: "#42b983",
        receiptBg: "#FFFBEF",
        receiptTextColor: "#004D80",
        receiptBorder: "#1B9DC9",
        receiptInputBorder: "#707070",
      },
      width: {
        500: "500px",
        600: "600px",
        400: "400px",
        800: "800px",
        1100: "1130px",
      },
      fontFamily: {
        segoeUI: "'Segoe UI'",
        poppins: "'poppins', sans-serif",
      },
      spacing: {
        68: "270px",
        // 35: "-80px",
        100: "420px",
      },
    },
  },
  variants: {
    extend: {
      display: ["group-hover"],
    },
  },
  plugins: [],
};
