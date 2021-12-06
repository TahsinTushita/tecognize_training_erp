<template>
  <h1 class="pt-10 text-2xl font-semibold">Instructor Details</h1>
  <div class="grid grid-rows-1 gap-2 px-28 pt-10">
    <div class="flex gap-5 items-baseline">
      <h1 class="font-semibold text-xl">Instructor Name:</h1>
      <p class="text-lg">{{ instructor.name }}</p>
    </div>
    <div class="flex gap-5 items-baseline">
      <h1 class="font-semibold text-xl">Email:</h1>
      <p class="text-lg">{{ instructor.email }}</p>
    </div>
    <div class="flex gap-5 items-baseline">
      <h1 class="font-semibold text-xl">Phone:</h1>
      <p class="text-lg">{{ instructor.phone }}</p>
    </div>
    <div class="flex gap-5 items-baseline">
      <h1 class="font-semibold text-xl">Address:</h1>
      <p class="text-lg">{{ instructor.address }}</p>
    </div>
    <div class="flex gap-5 items-baseline">
      <h1 class="font-semibold text-xl">Organization:</h1>
      <p class="text-lg">{{ instructor.organization }}</p>
    </div>
    <div class="flex gap-5 items-baseline">
      <h1 class="font-semibold text-xl">Designation:</h1>
      <p class="text-lg">{{ instructor.designation }}</p>
    </div>
    <div class="flex gap-5 items-baseline">
      <h1 class="font-semibold text-xl">Profit Margin:</h1>
      <p class="text-lg">{{ instructor.profit }}</p>
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
    this.$store.dispatch("getInstructor", this.id);
  },
  computed: {
    instructor: {
      get() {
        return this.$store.getters.instructor;
      },
    },
  },
};
</script>