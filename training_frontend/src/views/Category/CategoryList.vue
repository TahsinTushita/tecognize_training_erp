<template>
  <h1 class="pt-10 text-xl font-semibold">Category List</h1>
  <div class="flex justify-center w-full">
    <table class="m-10">
      <thead>
        <tr>
          <th class="w-1/5 px-4 py-4 text-center border-2">Category id</th>
          <th class="w-1/5 px-4 py-4 text-center border-2">Name</th>
        </tr>
      </thead>
      <tbody v-if="categoryList.length">
        <tr
          v-for="category in categoryList"
          :key="category.cat_id"
          class="hover:bg-gray-100"
        >
          <td class="w-1/5 px-4 py-4 text-center border-2">
            {{ category.cat_id }}
          </td>
          <td class="w-1/5 px-4 py-4 text-center border-2">
            {{ category.name }}
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  mounted() {
    this.$store.dispatch("getCategoryList");
  },
  computed: {
    categoryList: {
      get() {
        return this.$store.getters.categoryList;
      },
    },
  },

  methods: {
    navigateToInstructorDetails(inst_id) {
      console.log(inst_id);
      this.$router.push({
        name: "InstructorDetails",
        params: { id: inst_id },
      });
    },
  },
};
</script>