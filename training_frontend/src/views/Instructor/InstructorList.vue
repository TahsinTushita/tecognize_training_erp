<template>
  <table class="m-10">
    <thead>
      <tr>
        <th class="w-1/5 px-4 py-4 text-center border-2">Name</th>
        <th class="w-1/5 px-4 py-4 text-center border-2">Phone</th>
        <th class="w-1/5 px-4 py-4 text-center border-2">email</th>
        <th class="w-1/5 px-4 py-4 text-center border-2">Address</th>
        <th class="w-1/5 px-4 py-4 text-center border-2">Organization</th>
        <th class="w-1/5 px-4 py-4 text-center border-2">Designation</th>
        <th class="w-1/5 px-4 py-4 text-center border-2">Profit</th>
      </tr>
    </thead>
    <tbody v-if="instructorList.length">
      <tr v-for="instructor in instructorList" :key="instructor.inst_id">
        <td class="w-1/5 px-4 py-4 text-center border-2">
          {{ instructor.name }}
        </td>
        <td class="w-1/5 px-4 py-4 text-center border-2">
          {{ instructor.phone }}
        </td>
        <td class="w-1/5 px-4 py-4 text-center border-2">
          {{ instructor.email }}
        </td>
        <td class="w-1/5 px-4 py-4 text-center border-2">
          {{ instructor.address }}
        </td>
        <td class="w-1/5 px-4 py-4 text-center border-2">
          {{ instructor.organization }}
        </td>
        <td class="w-1/5 px-4 py-4 text-center border-2">
          {{ instructor.designation }}
        </td>
        <td class="w-1/5 px-4 py-4 text-center border-2">
          {{ instructor.profit }}
        </td>
      </tr>
    </tbody>
  </table>
</template>

<script>
export default {
  mounted() {
    this.$store.dispatch("getInstructorList");
  },
  computed: {
    instructorList: {
      get() {
        return this.$store.getters.instructorList;
      },
    },
  },
};
</script>