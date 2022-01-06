<template>
  <h1 class="pt-10 text-xl font-semibold">Instructor Ledger</h1>
  <table class="m-10">
    <thead>
      <tr>
        <th class="w-1/12 px-4 py-4 text-center border-2">ID</th>
        <th class="w-1/5 px-4 py-4 text-center border-2">Instructor Name</th>
        <th class="w-1/5 px-4 py-4 text-center border-2">Phone</th>
        <th class="w-1/12 px-4 py-4 text-center border-2">Profit</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td class="w-1/12 px-4 py-4 text-center border-2">
          {{ instructor.inst_id }}
        </td>
        <td class="w-1/5 px-4 py-4 text-center border-2">
          {{ instructor.inst_name }}
        </td>
        <td class="w-1/5 px-4 py-4 text-center border-2">
          {{ instructor.inst_phone }}
        </td>
        <td class="w-1/12 px-4 py-4 text-center border-2">
          {{ instructor.inst_profit }}
        </td>
      </tr>
    </tbody>
  </table>
  <table class="m-10">
    <thead>
      <tr>
        <th class="w-2/5 px-4 py-4 text-center border-2">Batch</th>
        <th class="px-4 py-4 text-center border-2">Sale</th>
        <th class="px-4 py-4 text-center border-2">Payable</th>
        <th class="px-4 py-4 text-center border-2">Paid</th>
        <th class="px-4 py-4 text-center border-2">Due</th>
      </tr>
    </thead>
    <tbody v-if="ledgerPaidDue.length">
      <tr
        v-for="record in ledgerPaidDue"
        :key="record.batch_id"
        class="hover:bg-gray-100"
        @click="navigateToInstructorLedgerDetails(record.batch_id)"
      >
        <td class="w-1/12 px-4 py-4 text-center border-2">
          {{ record.batch_id }}
        </td>
        <td class="w-1/5 px-4 py-4 text-center border-2">
          {{ record.sale }}
        </td>
        <td class="w-1/5 px-4 py-4 text-center border-2">
          {{ record.payable }}
        </td>
        <td class="w-1/12 px-4 py-4 text-center border-2">
          {{ record.paid }}
        </td>
        <td class="w-1/5 px-4 py-4 text-center border-2">{{ record.due }}</td>
      </tr>
    </tbody>
  </table>
</template>

<script>
export default {
  props: ["id"],

  mounted() {
    this.$store.dispatch("getInstructor", this.id);
    this.$store.dispatch("getLedgerPaidDue", this.id);
  },

  methods: {
    navigateToInstructorLedgerDetails(batchId) {
      // console.log();
      this.$router.push({
        name: "InstructorLedgerDetails",
        params: { batchid: batchId },
      });
    },
  },

  computed: {
    instructor: {
      get() {
        return this.$store.getters.instructor;
      },
    },
    ledgerPaidDue: {
      get() {
        return this.$store.getters.ledgerPaidDue;
      },
    },
  },
};
</script>