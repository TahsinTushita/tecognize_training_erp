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
            class="bg-white rounded-md px-8 py-4 flex justify-center w-600 border-2 border-gray-200 hover:border-navlink hover:ring-0 focus:outline-none focus:border-navlink"
            placeholder="customer name"
            v-model="custName"
          />
        </div>
        <div class="grid grid-rows-1 gap-2 place-items-start">
          <label for="date" class="font-semibold ml-2">Date*</label>
          <input
            type="date"
            name="date"
            class="bg-white rounded-md px-8 py-4 flex justify-center w-600 border-2 border-gray-200 hover:border-navlink hover:ring-0 focus:outline-none focus:border-navlink"
            v-model="date"
          />
        </div>
        <div class="grid grid-rows-1 gap-2 place-items-start">
          <label for="courseName" class="font-semibold ml-2">Course*</label>
          <select
            name="courseName"
            id="courseName"
            v-model="course"
            @change="filterBatch"
            required
            class="bg-white rounded-md px-8 py-4 flex justify-center w-600 border-2 border-gray-200 hover:border-navlink hover:ring-0 focus:outline-none focus:border-navlink"
          >
            <option
              v-for="course in courseList"
              :value="course"
              :key="course.course_id"
            >
              {{ course.course_name }}
            </option>
          </select>
        </div>

        <div class="grid grid-rows-1 gap-2 place-items-start">
          <label for="batch" class="font-semibold ml-2">Batch*</label>
          <select
            name="batch"
            id="batch"
            v-model="batch"
            required
            class="bg-white rounded-md px-8 py-4 flex justify-center w-600 border-2 border-gray-200 hover:border-navlink hover:ring-0 focus:outline-none focus:border-navlink"
          >
            <option
              v-for="batch in batchesByCourse"
              :value="batch"
              :key="batch.batch_id"
            >
              {{ batch.batch_num }}
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
          completing the course of {{ course.course_name }}
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
          :src="require(`../../assets/images/${getSign}`)"
          alt="signature"
        />
      </div>
    </div>
  </div>
  <div class="flex items-center justify-center gap-20">
    <button
      class="px-4 py-2 rounded-md bg-green bg-green-200 hover:bg-green-300 my-10"
      @click="downloadCertificate"
    >
      Download pdf
    </button>
    <button
      class="px-4 py-2 rounded-md bg-green bg-green-200 hover:bg-green-300 my-10"
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
      batch: "",
      course: "",
      image: "shahedvai.png",
    };
  },

  methods: {
    downloadCertificate() {
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
          "_Certificate_of_" +
          this.course.course_name +
          "_" +
          this.batch.batch_num +
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
            "_Certificate_of_" +
            this.course.course_name +
            "_" +
            this.batch.batch_num +
            ".png"
        );
      });
    },

    filterBatch() {
      this.$store.dispatch("getBatchesByCourse", this.course.course_id);
    },
  },

  computed: {
    courseList: {
      get() {
        return this.$store.getters.courseList;
      },
    },

    batchesByCourse: {
      get() {
        return this.$store.getters.batchesByCourse;
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
      if (this.course.course_name == "System Design: Level 1") {
        this.courseNameShort = "Sys Design 1";
      } else if (this.course.course_name == "System Design: Level 2") {
        this.courseNameShort = "Sys Design 2";
      } else if (this.course.course_name == "Software Quality Assurance") {
        this.courseNameShort = "SQA";
      } else if (this.course.course_name == "Backend Development with Java") {
        this.courseNameShort = "Java";
      } else if (
        this.course.course_name == "Cracking the Coding Interview with Leetcode"
      ) {
        this.courseNameShort = "Leetcode";
      } else if (this.course.course_name == "Backend Engineering with Python") {
        this.courseNameShort = "Python";
      } else if (this.course.course_name == "Backend Engineering with Java") {
        this.courseNameShort = "Java";
      } else if (this.course.course_name == "Design Patterns with Python") {
        this.courseNameShort = "Design Patterns";
      } else if (this.course.course_name == "Linux Administration") {
        this.courseNameShort = "Linux Admin";
      } else if (this.course.course_name == "Python with Network Automation") {
        this.courseNameShort = "Python";
      } else if (this.course.course_name == "Leveraging Python") {
        this.courseNameShort = "Python";
      } else {
        this.courseNameShort = this.course.course_name;
      }
      return this.courseNameShort;
    },
    getSign() {
      if (this.course.course_name == "Backend Engineering with Python") {
        this.image = "sadmanaminvai.png";
      } else if (
        this.course.course_name == "Mongo DB" ||
        this.course.course_name == "DevOps" ||
        this.course.course_name ==
          "Cracking the Coding Interview with Leetcode" ||
        this.course.course_name == "System Design: Level 1" ||
        this.course.course_name == "System Design: Level 2"
      ) {
        this.image = "shajalvai.png";
      } else if (
        this.course.course_name == "QaOps" ||
        this.course.course_name == "Software Quality Assurance"
      ) {
        this.image = "imransign.png";
      } else if (this.course.course_name == "Backend Development with Java") {
        this.image = "ahsan.png";
      } else this.image = "shahedvai.png";
      return this.image;
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
