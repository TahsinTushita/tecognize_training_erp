<template>
  <h1 class="pt-10 text-xl font-semibold">Course List</h1>
  <div class="flex justify-center">
    <table class="m-10">
      <thead>
        <tr>
          <th class="w-1/5 px-4 py-4 text-center border-2">Course Name</th>
          <th class="w-1/5 px-4 py-4 text-center border-2">Regular Price</th>
          <th class="w-1/5 px-4 py-4 text-center border-2">Category</th>
        </tr>
      </thead>
      <tbody v-if="courseList.length">
        <tr
          v-for="course in courseList"
          :key="course.course_id"
          class="hover:bg-gray-100"
        >
          <td class="w-1/5 px-4 py-4 text-center border-2">
            {{ course.course_name }}
          </td>
          <td class="w-1/5 px-4 py-4 text-center border-2">
            {{ course.regular_price }}
          </td>
          <td class="w-1/5 px-4 py-4 text-center border-2">
            {{ course.cat_name }}
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  mounted() {
    this.$store.dispatch("getCourseList");
  },
  computed: {
    courseList: {
      get() {
        return this.$store.getters.courseList;
      },
    },
  },

  // methods: {
  //   navigateToInstructorDetails(inst_id) {
  //     console.log(inst_id);
  //     this.$router.push({
  //       name: "InstructorDetails",
  //       params: { id: inst_id },
  //     });
  //   },
  // },
};
</script>