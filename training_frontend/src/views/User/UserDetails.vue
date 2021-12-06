<template>
  <h1 class="pt-10 text-2xl font-semibold">User Details</h1>
  <div class="grid grid-rows-1 gap-2 px-28 pt-10">
    <div class="flex gap-5 items-baseline">
      <h1 class="font-semibold text-xl">User Name:</h1>
      <p class="text-lg">{{ user.name }}</p>
    </div>
    <div class="flex gap-5 items-baseline">
      <h1 class="font-semibold text-xl">Email:</h1>
      <p class="text-lg">{{ user.email }}</p>
    </div>
    <div class="flex gap-5 items-baseline">
      <h1 class="font-semibold text-xl">Phone:</h1>
      <p class="text-lg">{{ user.phone }}</p>
    </div>
    <div class="flex gap-5 items-baseline">
      <h1 class="font-semibold text-xl">Address:</h1>
      <p class="text-lg">{{ user.address }}</p>
    </div>
    <div class="flex gap-5 items-baseline">
      <h1 class="font-semibold text-xl">Designation:</h1>
      <p class="text-lg">{{ user.designation }}</p>
    </div>
    <div class="flex gap-5 items-baseline">
      <h1 class="font-semibold text-xl">Profit Margin:</h1>
      <p class="text-lg">{{ user.profit }}</p>
    </div>
  </div>
  <button
    class="mt-10 px-4 py-2 rounded-md bg-green-300 text-lg hover:bg-green-400"
  >
    Update
  </button>
</template>

<script>
export default {
  props: ["id"],
  mounted() {
    this.$store.dispatch("getUser", this.id);
  },
  computed: {
    user: {
      get() {
        return this.$store.getters.user;
      },
    },
  },
};
</script>