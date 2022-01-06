<template>
  <div class="flex items-center justify-center">
    <table class="m-10 w-full">
      <thead>
        <tr>
          <th class="px-4 py-4 text-center border-2">Instructor ID</th>
          <th class="px-4 py-4 text-center border-2">Batch</th>
          <th class="px-4 py-4 text-center border-2">Sale</th>
          <th class="px-4 py-4 text-center border-2">Payment received</th>
          <th class="px-4 py-4 text-center border-2">Payable</th>
          <th class="px-4 py-4 text-center border-2">Paid</th>
          <th class="px-4 py-4 text-center border-2">Due</th>
          <th class="px-4 py-4 text-center border-2">Date</th>
          <th class="px-4 py-4 text-center border-2">Payment Method</th>
          <th class="px-4 py-4 text-center border-2">Cheque/Ref No.</th>
          <th class="px-4 py-4 text-center border-2">Cheque Date</th>
        </tr>
      </thead>
      <tbody v-if="instructorFeeByBatch.length">
        <tr
          v-for="record in instructorFeeByBatch"
          :key="record.inst_id"
          class="hover:bg-gray-100"
        >
          <td class="px-4 py-4 text-center border-2">
            {{ record.inst_id }}
          </td>
          <td class="px-4 py-4 text-center border-2">
            {{ record.batch_id }}
          </td>
          <td class="px-4 py-4 text-center border-2">
            {{ record.total_sale }}
          </td>
          <td class="px-4 py-4 text-center border-2">
            {{ record.pay_received }}
          </td>
          <td class="px-4 py-4 text-center border-2">
            {{ record.total_payable }}
          </td>
          <td class="px-4 py-4 text-center border-2">
            {{ record.paid }}
          </td>
          <td class="px-4 py-4 text-center border-2">
            {{ record.due }}
          </td>
          <td class="px-4 py-4 text-center border-2">
            {{ record.date }}
          </td>
          <td class="px-4 py-4 text-center border-2">
            {{ record.pay_mode }}
          </td>
          <td class="px-4 py-4 text-center border-2">
            {{ record.check_no }}
          </td>
          <td class="px-4 py-4 text-center border-2">
            {{ record.check_date }}
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  props: ["batchid"],

  mounted() {
    this.$store.dispatch("getInstructorFeeByBatch", this.batchid);
  },

  computed: {
    instructorFeeByBatch: {
      get() {
        return this.$store.getters.instructorFeeByBatch;
      },
    },
  },
};
</script>