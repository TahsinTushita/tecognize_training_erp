<template>
  <h1 class="pt-10 text-xl font-semibold">Instructor List</h1>
  <table class="m-10">
    <thead>
      <tr>
        <th class="w-1/5 px-4 py-4 text-center border-2">Instructor Name</th>
        <th class="w-1/5 px-4 py-4 text-center border-2">email</th>
        <th class="w-1/5 px-4 py-4 text-center border-2">Phone</th>
        <th class="w-1/5 px-4 py-4 text-center border-2">Address</th>
        <th class="w-1/5 px-4 py-4 text-center border-2">Organization</th>
        <th class="w-1/5 px-4 py-4 text-center border-2">Designation</th>
        <th class="w-1/5 px-4 py-4 text-center border-2">Profit</th>
      </tr>
    </thead>
    <tbody v-if="instructorList.length">
      <tr
        v-for="instructor in instructorList"
        :key="instructor.inst_id"
        class="hover:bg-gray-100"
        @click="navigateToInstructorDetails(instructor.inst_id)"
      >
        <td class="w-1/5 px-4 py-4 text-center border-2">
          {{ instructor.inst_name }}
        </td>
        <td class="w-1/5 px-4 py-4 text-center border-2">
          {{ instructor.inst_email }}
        </td>
        <td class="w-1/5 px-4 py-4 text-center border-2">
          {{ instructor.inst_phone }}
        </td>
        <td class="w-1/5 px-4 py-4 text-center border-2">
          {{ instructor.inst_address }}
        </td>
        <td class="w-1/5 px-4 py-4 text-center border-2">
          {{ instructor.inst_organization }}
        </td>
        <td class="w-1/5 px-4 py-4 text-center border-2">
          {{ instructor.inst_designation }}
        </td>
        <td class="w-1/5 px-4 py-4 text-center border-2">
          {{ instructor.inst_profit }}
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