<template>
  <h1 class="pt-10 text-2xl font-semibold">Generate certificate</h1>
  <div class="flex items-center justify-center mb-10">
    <form @submit.prevent="">
      <div class="space-y-5">
        <div class="grid grid-rows-1 gap-2 place-items-start">
          <label for="custName" class="font-semibold ml-2"
            >Customer Name*</label
          >
          <input
            type="text"
            name="custName"
            required
            class="
              bg-white
              rounded-md
              px-8
              py-4
              flex
              justify-center
              w-600
              border-2 border-gray-200
              hover:border-navlink hover:ring-0
              focus:outline-none focus:border-navlink
            "
            placeholder="customer name"
            v-model="custName"
          />
        </div>
        <div class="grid grid-rows-1 gap-2 place-items-start">
          <label for="date" class="font-semibold ml-2">Date*</label>
          <input
            type="date"
            name="date"
            class="
              bg-white
              rounded-md
              px-8
              py-4
              flex
              justify-center
              w-600
              border-2 border-gray-200
              hover:border-navlink hover:ring-0
              focus:outline-none focus:border-navlink
            "
            v-model="date"
          />
        </div>
        <div class="grid grid-rows-1 gap-2 place-items-start">
          <label for="courseName" class="font-semibold ml-2">Course*</label>
          <select
            name="courseName"
            id="courseName"
            v-model="courseName"
            required
            class="
              bg-white
              rounded-md
              px-8
              py-4
              flex
              justify-center
              w-600
              border-2 border-gray-200
              hover:border-navlink hover:ring-0
              focus:outline-none focus:border-navlink
            "
          >
            <option
              v-for="course in courseList"
              :value="course.course_name"
              :key="course.course_id"
            >
              {{ course.course_name }}
            </option>
          </select>
        </div>
      </div>
    </form>
  </div>

  <div class="flex justify-center">
    <div ref="receiptContent">
      <div class="flex items-center justify-center relative w-1120 h-830">
        <img
          src="../../assets/images/certificatebg1.png"
          alt="logo"
          class="w-1120 h-830"
        />
        <h1 class="absolute text-white text-8xl font-greatVibes mb-48">
          {{ custName }}
        </h1>
        <h1 class="absolute text-white text-3xl mt-16">
          has been awarded this certificate for successfully
        </h1>
        <h1 class="absolute text-white text-3xl mt-36">
          completing the course of {{ courseName }}
        </h1>
        <h1 class="absolute text-white text-2xl left-20 bottom-24">
          {{ getCertDate }}
        </h1>
        <img
          class="absolute w-96 h-96 -bottom-5"
          src="../../assets/images/3.png"
          alt="signature"
        />
        <h1 class="absolute text-certificateColor1 text-sm bottom-48 font-bold">
          {{ courseNameShort }}
        </h1>
        <h1
          class="absolute text-certificateColor1 text-2xl bottom-36 font-bold"
        >
          {{ getYear }}
        </h1>
        <img
          class="absolute right-20 bottom-24 w-24 h-24"
          src="../../assets/images/shajalvai.png"
          alt="signature"
        />
      </div>
    </div>
  </div>
  <div class="flex items-center justify-center gap-20">
    <button
      class="
        px-4
        py-2
        rounded-md
        bg-green bg-green-200
        hover:bg-green-300
        my-10
      "
      @click="downloadReceipt"
    >
      Download pdf
    </button>
    <button
      class="
        px-4
        py-2
        rounded-md
        bg-green bg-green-200
        hover:bg-green-300
        my-10
      "
      @click="downloadImage"
    >
      Download image
    </button>
  </div>
</template>

<script>
import jsPDF from "jspdf";
import html2canvas from "html2canvas";

export default {
  mounted() {
    this.$store.dispatch("getCourseList");
  },

  data() {
    return {
      custName: "",
      date: "",
      certDate: "",
      courseName: "",
      courseNameShort: "",
      month: "",
      day: "",
      year: "",
    };
  },

  methods: {
    downloadReceipt() {
      const doc = new jsPDF({
        orientation: "l",
        unit: "px",
        format: "a4",
        hotfixes: ["px_scaling"],
      });

      html2canvas(this.$refs.receiptContent, {
        width: doc.internal.pageSize.getWidth(),
        height: doc.internal.pageSize.getHeight(),
      }).then((canvas) => {
        const img = canvas.toDataURL("image/png");
        doc.addImage(
          img,
          "PNG",
          0,
          0,
          doc.internal.pageSize.getWidth(),
          doc.internal.pageSize.getHeight()
        );
        let filename =
          this.custName +
          "_" +
          this.courseNameShort +
          "_" +
          new Date().toLocaleDateString() +
          "_" +
          new Date().toLocaleTimeString() +
          ".pdf";
        doc.save(filename);
      });
    },

    saveImage(data, filename = "untitled.png") {
      var a = document.createElement("a");
      a.href = data;
      a.download = filename;
      document.body.appendChild(a);
      a.click();
    },

    downloadImage() {
      const doc = new jsPDF({
        orientation: "l",
        unit: "px",
        format: "a4",
        hotfixes: ["px_scaling"],
      });
      html2canvas(this.$refs.receiptContent, {
        width: doc.internal.pageSize.getWidth(),
        height: doc.internal.pageSize.getHeight(),
      }).then((canvas) => {
        const img = canvas.toDataURL("image/png");
        this.saveImage(
          img,
          this.custName +
            "_" +
            this.courseNameShort +
            "_" +
            new Date().toLocaleDateString() +
            "_" +
            new Date().toLocaleTimeString() +
            ".png"
        );
      });
    },
  },

  computed: {
    courseList: {
      get() {
        return this.$store.getters.courseList;
      },
    },

    getCertDate() {
      if (this.date) {
        let d = new Date(this.date);
        let year = d.getFullYear();
        let month = d.toLocaleString("en-us", { month: "long" });
        let day = d.getDate();
        this.certDate =
          month.toUpperCase() + " " + day.toString() + " - " + year.toString();
      } else {
        this.certDate = "";
      }
      return this.certDate;
    },

    courseNameShort() {
      if (this.courseName == "System Design Level 1") {
        this.courseNameShort = "Sys Design 1";
      } else if (this.courseName == "System Design Level 2") {
        this.courseNameShort = "Sys Design 2";
      } else if (
        this.courseName == "Cracking the Coding Interview with Leetcode"
      ) {
        this.courseNameShort = "Leetcode";
      } else if (this.courseName == "Backend Engineering with Python") {
        this.courseNameShort = "Python";
      } else if (this.courseName == "Backend Engineering with Java") {
        this.courseNameShort = "Java";
      } else if (this.courseName == "Design Patterns with Python") {
        this.courseNameShort = "Design Patterns";
      } else if (this.courseName == "Linux Administration") {
        this.courseNameShort = "Linux Admin";
      } else if (this.courseName == "Python with Network Automation") {
        this.courseNameShort = "Python";
      } else if (this.courseName == "Leveraging Python") {
        this.courseNameShort = "Python";
      } else {
        this.courseNameShort = this.courseName;
      }
      return this.courseNameShort;
    },
    getYear() {
      if (this.date) {
        let d = new Date(this.date);
        this.year = d.getFullYear();
      } else {
        this.year = "";
      }
      return this.year;
    },
  },
};
</script>