<template>
  <h1 class="pt-10 text-2xl font-semibold">Add Course</h1>
  <div class="flex items-center justify-center mb-20">
    <form @submit.prevent="addCourse">
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
  <div class="flex items-center justify-center relative">
    <img src="../../assets/images/certificatebg.png" alt="logo" />
    <h1 class="absolute text-white text-9xl font-greatVibes mb-16">
      {{ custName }}
    </h1>
    <h1 class="absolute text-white text-4xl mt-24">
      has been awarded this certificate for successfully
    </h1>
    <h1 class="absolute text-white text-4xl mt-44">
      completing the course of {{ courseName }}
    </h1>
  </div>
</template>

<script>
export default {
  mounted() {
    this.$store.dispatch("getCourseList");
  },

  data() {
    return {
      custName: "",
      date: "",
      courseName: "",
      courseNameShort: "",
    };
  },

  computed: {
    courseList: {
      get() {
        return this.$store.getters.courseList;
      },
    },
  },
};
</script>