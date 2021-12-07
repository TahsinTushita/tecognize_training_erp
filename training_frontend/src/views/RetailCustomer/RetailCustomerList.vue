<template>
  <h1 class="pt-10 text-xl font-semibold">Retail Customer List</h1>

  <table class="m-10">
    <thead>
      <tr>
        <th class="w-1/5 px-4 py-4 text-center border-2">
          Retail Customer Name
        </th>
        <th class="w-1/5 px-4 py-4 text-center border-2">Phone</th>
        <th class="w-1/5 px-4 py-4 text-center border-2">email</th>
        <th class="w-1/5 px-4 py-4 text-center border-2">Address</th>
        <th class="w-1/5 px-4 py-4 text-center border-2">Organization</th>
        <th class="w-1/5 px-4 py-4 text-center border-2">Designation</th>
        <th class="w-1/5 px-4 py-4 text-center border-2">Total Fee</th>
        <th class="w-1/5 px-4 py-4 text-center border-2">Paid Fee</th>
        <th class="w-1/5 px-4 py-4 text-center border-2">Due Fee</th>
      </tr>
    </thead>
    <tbody v-if="retailCustomerList.length">
      <tr
        v-for="retailCustomer in retailCustomerList"
        :key="retailCustomer.cust_id"
        class="hover:bg-gray-100"
        @click="navigateToUserDetails(retailCustomer.cust_id)"
      >
        <td class="w-1/5 px-4 py-4 text-center border-2">
          {{ retailCustomer.cust_name }}
        </td>
        <td class="w-1/5 px-4 py-4 text-center border-2">
          {{ retailCustomer.cust_phone }}
        </td>
        <td class="w-1/5 px-4 py-4 text-center border-2">
          {{ retailCustomer.cust_email }}
        </td>
        <td class="w-1/5 px-4 py-4 text-center border-2">
          {{ retailCustomer.cust_address }}
        </td>
        <td class="w-1/5 px-4 py-4 text-center border-2">
          {{ retailCustomer.cust_organization }}
        </td>
        <td class="w-1/5 px-4 py-4 text-center border-2">
          {{ retailCustomer.cust_designation }}
        </td>
        <td class="w-1/5 px-4 py-4 text-center border-2">
          {{ retailCustomer.cust_total_fee }}
        </td>
        <td class="w-1/5 px-4 py-4 text-center border-2">
          {{ retailCustomer.cust_paid_fee }}
        </td>
        <td class="w-1/5 px-4 py-4 text-center border-2">
          {{ retailCustomer.cust_due_fee }}
        </td>
      </tr>
    </tbody>
  </table>
</template>

<script>
export default {
  mounted() {
    this.$store.dispatch("getRetailCustomerList");
  },
  computed: {
    retailCustomerList: {
      get() {
        return this.$store.getters.retailCustomerList;
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