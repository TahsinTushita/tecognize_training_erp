<template>
  <h1 class="pt-10 text-xl font-semibold">Instructor Ledger</h1>
  <table class="m-10">
    <thead>
      <tr>
        <th class="w-1/12 px-4 py-4 text-center border-2">ID</th>
        <th class="w-1/5 px-4 py-4 text-center border-2">Instructor Name</th>
        <th class="w-1/5 px-4 py-4 text-center border-2">Phone</th>
        <th class="w-1/12 px-4 py-4 text-center border-2">Profit</th>
        <th class="w-1/5 px-4 py-4 text-center border-2">Sale</th>
        <th class="w-1/5 px-4 py-4 text-center border-2">Payable</th>
        <th class="w-1/5 px-4 py-4 text-center border-2">Paid</th>
        <th class="w-1/5 px-4 py-4 text-center border-2">Due</th>
      </tr>
    </thead>
    <tbody v-if="instructorLedger.length">
      <tr
        v-for="record in instructorLedger"
        :key="record.inst_id"
        class="hover:bg-gray-100"
        @click="navigateToInstructorBatchLedger(record.inst_id)"
      >
        <td class="w-1/12 px-4 py-4 text-center border-2">
          {{ record.inst_id }}
        </td>
        <td class="w-1/5 px-4 py-4 text-center border-2">
          {{ record.inst_name }}
        </td>
        <td class="w-1/5 px-4 py-4 text-center border-2">
          {{ record.inst_phone }}
        </td>
        <td class="w-1/12 px-4 py-4 text-center border-2">
          {{ record.inst_profit }}
        </td>
        <td class="w-1/5 px-4 py-4 text-center border-2">{{ record.sale }}</td>
        <td class="w-1/5 px-4 py-4 text-center border-2">
          {{ record.inst_payable }}
        </td>
        <td class="w-1/5 px-4 py-4 text-center border-2">
          {{ record.inst_paid }}
        </td>
        <td class="w-1/5 px-4 py-4 text-center border-2">
          {{ record.inst_due }}
        </td>
      </tr>
    </tbody>
  </table>
</template>

<script>
export default {
  mounted() {
    this.$store.dispatch("getInstructorLedger");
  },

  methods: {
    navigateToInstructorBatchLedger(inst_id) {
      // console.log();
      this.$router.push({
        name: "InstructorBatchLedger",
        params: { id: inst_id },
      });
    },
  },

  computed: {
    instructorLedger: {
      get() {
        return this.$store.getters.instructorLedger;
      },
    },
  },
};
</script>