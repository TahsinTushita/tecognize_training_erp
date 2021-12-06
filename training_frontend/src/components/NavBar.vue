<template>
  <div id="nav">
    <div class="grid grid-cols-12 p-6 bg-gray-200">
      <div class="col-span-3"></div>
      <div class="col-span-5">
        <div class="grid grid-cols-4 place-items-center">
          <!-- <DropDown animation="slide-in-up" color="green"></DropDown> -->
          <div class="relative space-y-6 w-full">
            <a href="#" class="text-lg" @click="toggleInstructorOptions"
              >Instructor</a
            >
            <div
              class="
                absolute
                left-0
                top-full
                shadow-md
                py-3
                grid grid-rows-1
                gap-2
                bg-gray-200
                w-full
              "
              v-if="showInstructorOptions"
            >
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
          <div class="relative space-y-6 w-full">
            <a href="#" class="text-lg" @click="toggleUserOptions">User</a>
            <div
              class="
                absolute
                left-0
                top-full
                shadow-md
                py-3
                grid grid-rows-1
                gap-2
                bg-gray-200
                w-full
              "
              v-if="showUserOptions"
            >
              <router-link :to="{ name: 'AddUser' }" class="text-lg">
                Add User
              </router-link>

              <router-link :to="{ name: 'UserList' }" class="text-lg"
                >User List</router-link
              >
              <router-link :to="{ name: 'UserLedger' }" class="text-lg">
                User Ledger
              </router-link>
            </div>
          </div>
          <div class="relative space-y-6 w-full">
            <a href="#" class="text-lg" @click="toggleCourseOptions">Course</a>
            <div
              class="
                absolute
                left-0
                top-full
                shadow-md
                py-3
                grid grid-rows-1
                gap-2
                bg-gray-200
                w-full
              "
              v-if="showCourseOptions"
            >
              <router-link :to="{ name: 'AddCategory' }" class="text-lg">
                Add Category
              </router-link>

              <router-link :to="{ name: 'CategoryList' }" class="text-lg"
                >Category List</router-link
              >
            </div>
          </div>
          <div class="relative">
            <a href="#" class="text-lg">Customer</a>
          </div>
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
  data() {
    return {
      showInstructorOptions: false,
      showUserOptions: false,
      showCourseOptions: false,
      showCustomerOptions: false,
    };
  },
  methods: {
    toggleInstructorOptions() {
      this.showInstructorOptions = !this.showInstructorOptions;
    },

    toggleUserOptions() {
      this.showUserOptions = !this.showUserOptions;
    },

    toggleCourseOptions() {
      this.showCourseOptions = !this.showCourseOptions;
    },

    toggleCustomerOptions() {
      this.showCustomerOptions = !this.showCustomerOptions;
    },
  },
};
</script>