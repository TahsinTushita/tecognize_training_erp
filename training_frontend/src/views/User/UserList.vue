<template>
  <h1 class="pt-10 text-xl font-semibold">User List</h1>
  <table class="m-10">
    <thead>
      <tr>
        <th class="w-1/5 px-4 py-4 text-center border-2">User Name</th>
        <th class="w-1/5 px-4 py-4 text-center border-2">email</th>
        <th class="w-1/5 px-4 py-4 text-center border-2">Phone</th>
        <th class="w-1/5 px-4 py-4 text-center border-2">Address</th>
        <th class="w-1/5 px-4 py-4 text-center border-2">Designation</th>
        <th class="w-1/5 px-4 py-4 text-center border-2">Profit</th>
      </tr>
    </thead>
    <tbody v-if="userList.length">
      <tr
        v-for="user in userList"
        :key="user.user_id"
        class="hover:bg-gray-100"
        @click="navigateToUserDetails(user.user_id)"
      >
        <td class="w-1/5 px-4 py-4 text-center border-2">
          {{ user.user_name }}
        </td>
        <td class="w-1/5 px-4 py-4 text-center border-2">
          {{ user.user_email }}
        </td>
        <td class="w-1/5 px-4 py-4 text-center border-2">
          {{ user.user_phone }}
        </td>
        <td class="w-1/5 px-4 py-4 text-center border-2">
          {{ user.user_address }}
        </td>
        <td class="w-1/5 px-4 py-4 text-center border-2">
          {{ user.user_designation }}
        </td>
        <td class="w-1/5 px-4 py-4 text-center border-2">
          {{ user.user_profit }}
        </td>
      </tr>
    </tbody>
  </table>
</template>

<script>
export default {
  mounted() {
    this.$store.dispatch("getUserList");
  },
  computed: {
    userList: {
      get() {
        return this.$store.getters.userList;
      },
    },
  },

  methods: {
    navigateToUserDetails(user_id) {
      this.$router.push({
        name: "UserDetails",
        params: { id: user_id },
      });
    },
  },
};
</script>