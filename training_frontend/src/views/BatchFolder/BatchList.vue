<template>
  <h1 class="pt-10 text-2xl font-semibold">Batch List</h1>
  <div class="flex justify-center">
    <table class="m-10">
      <thead>
        <tr>
          <th class="w-1/5 px-4 py-4 text-center border-2">Batch id</th>
          <th class="w-1/5 px-4 py-4 text-center border-2">Course</th>
          <th class="w-1/5 px-4 py-4 text-center border-2">Instructor</th>
          <th class="w-1/5 px-4 py-4 text-center border-2">Batch Fee</th>
          <th class="w-1/5 px-4 py-4 text-center border-2" colspan="4">
            Admission Closed
          </th>
        </tr>
      </thead>
      <tbody v-if="batchListTable.length">
        <tr
          v-for="batch in batchListTable"
          :key="batch.batch_id"
          class="hover:bg-gray-100"
        >
          <td class="w-1/5 px-4 py-4 text-center border-2">
            {{ batch.batch_id }}
          </td>
          <td class="w-1/5 px-4 py-4 text-center border-2">
            {{ batch.course_name }}
          </td>
          <td class="w-1/5 px-4 py-4 text-center border-2">
            {{ batch.inst_name }}
          </td>
          <td class="w-1/5 px-4 py-4 text-center border-2">
            {{ batch.batch_fee }}
          </td>
          <td class="w-1/5 px-4 py-4 text-center border-2" colspan="4">
            {{ batch.admit_closed }}
            <button
              class="px-4 py-2 bg-green-200 hover:bg-green-300 rounded-md"
              @click="changeBatchAdmissionStatus(batch.batch_id)"
            >
              Change
            </button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  mounted() {
    this.$store.dispatch("getBatchListTable");
  },
  computed: {
    batchListTable: {
      get() {
        return this.$store.getters.batchListTable;
      },
    },
  },

  methods: {
    changeBatchAdmissionStatus(batch_id) {
      this.$store.dispatch("changeBatchAdmissionStatus", batch_id);
      window.location.reload();
    },
  },
};
</script>