<template>
  <h1 class="pt-10 text-xl font-semibold">Corporate Customer List</h1>

  <table class="m-10">
    <thead>
      <tr>
        <th class="w-1/5 px-4 py-4 text-center border-2">
          Corporate Customer Name
        </th>
        <th class="w-1/5 px-4 py-4 text-center border-2">Phone</th>
        <th class="w-1/5 px-4 py-4 text-center border-2">email</th>
        <th class="w-1/5 px-4 py-4 text-center border-2">Address</th>
        <th class="w-1/5 px-4 py-4 text-center border-2">Total Fee</th>
        <th class="w-1/5 px-4 py-4 text-center border-2">Paid Fee</th>
        <th class="w-1/5 px-4 py-4 text-center border-2">Due Fee</th>
        <th class="w-1/5 px-4 py-4 text-center border-2">Units</th>
      </tr>
    </thead>
    <tbody v-if="corporateCustomerList.length">
      <tr
        v-for="corporateCustomer in corporateCustomerList"
        :key="corporateCustomer.corp_id"
        class="hover:bg-gray-100"
        @click="navigateToUserDetails(corporateCustomer.corp_id)"
      >
        <td class="w-1/5 px-4 py-4 text-center border-2">
          {{ corporateCustomer.corp_name }}
        </td>
        <td class="w-1/5 px-4 py-4 text-center border-2">
          {{ corporateCustomer.corp_phone }}
        </td>
        <td class="w-1/5 px-4 py-4 text-center border-2">
          {{ corporateCustomer.corp_email }}
        </td>
        <td class="w-1/5 px-4 py-4 text-center border-2">
          {{ corporateCustomer.corp_address }}
        </td>
        <td class="w-1/5 px-4 py-4 text-center border-2">
          {{ corporateCustomer.corp_total_fee }}
        </td>
        <td class="w-1/5 px-4 py-4 text-center border-2">
          {{ corporateCustomer.corp_paid_fee }}
        </td>
        <td class="w-1/5 px-4 py-4 text-center border-2">
          {{ corporateCustomer.corp_due_fee }}
        </td>
        <td class="w-1/5 px-4 py-4 text-center border-2">
          {{ corporateCustomer.corp_units }}
        </td>
      </tr>
    </tbody>
  </table>
</template>

<script>
export default {
  mounted() {
    this.$store.dispatch("getCorporateCustomerList");
  },
  computed: {
    corporateCustomerList: {
      get() {
        return this.$store.getters.corporateCustomerList;
      },
    },
  },

  methods: {
    // navigateToUserDetails(user_id) {
    //   this.$router.push({
    //     name: "UserDetails",
    //     params: { id: user_id },
    //   });
    // },
  },
};
</script>