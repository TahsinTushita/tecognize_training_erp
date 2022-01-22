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
        certificateColor1: "#242b32",
      },
      width: {
        500: "500px",
        600: "600px",
        400: "400px",
        800: "800px",
        1100: "1130px",
        1120: "1125px",
      },
      height: {
        830: "800px",
      },
      fontFamily: {
        segoeUI: "'Segoe UI'",
        poppins: "'poppins', sans-serif",
        greatVibes: "'Great Vibes', cursive",
        MyriadProBold: "'MyriadPro Bold'",
      },
      spacing: {
        68: "270px",
        // 35: "-80px",
        100: "420px",
        46: "180px",
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
