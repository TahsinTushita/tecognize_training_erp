<template>
  <div id="nav">
    <div class="grid grid-cols-12 p-6 bg-gray-200">
      <div class="col-span-4"></div>
      <div class="col-span-4">
        <div class="grid grid-cols-4 place-items-center">
          <!-- <DropDown animation="slide-in-up" color="green"></DropDown> -->
          <router-link :to="{ name: 'AddInstructor' }" class="text-lg">
            Add Instructor
          </router-link>

          <router-link :to="{ name: 'InstructorList' }" class="text-lg"
            >Instructor List</router-link
          >
          <router-link :to="{ name: 'InstructorLedger' }" class="text-lg">
            Instructor Ledger
          </router-link>
        </div>
      </div>
      <div class="col-span-4"></div>
    </div>
  </div>
  <router-view />
</template>

<script>
import DropDown from "./DropDown.vue";

export default {
  components: { DropDown },
};
</script>