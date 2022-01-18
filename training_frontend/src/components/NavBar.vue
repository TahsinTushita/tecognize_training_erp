<template>
  <div id="nav">
    <div class="grid grid-cols-12 p-6 bg-gray-200">
      <div class="col-span-2"></div>
      <div class="col-span-8">
        <div class="grid grid-cols-5 place-items-center">
          <!-- <DropDown animation="slide-in-up" color="green"></DropDown> -->
          <!-- Instructor -->
          <div class="relative space-y-6 w-full group">
            <a href="#" class="text-lg" @click="toggleInstructorOptions"
              >Instructor</a
            >
            <div
              class="
                absolute
                left-0
                top-full
                shadow-md
                py-4
                grid grid-rows-1
                gap-2
                bg-gray-200
                w-full
                space-y-2
              "
              v-if="showInstructorOptions"
            >
              <!-- <div
              class="
                absolute
                top-full
                shadow-md
                py-4
                grid grid-rows-1
                gap-2
                bg-gray-200
                w-full
                space-y-2
                hidden
                group-hover:block
              "
            > -->
              <router-link :to="{ name: 'AddInstructor' }" class="text-lg">
                Add Instructor
              </router-link>

              <router-link :to="{ name: 'InstructorList' }" class="text-lg"
                >Instructor List</router-link
              >
              <router-link :to="{ name: 'InstructorLedger' }" class="text-lg">
                Instructor Ledger
              </router-link>
              <router-link :to="{ name: 'InstructorPayment' }" class="text-lg">
                Instructor Payment
              </router-link>
            </div>
          </div>
          <!-- Instructor end -->

          <!-- User -->
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
          <!-- User end -->

          <!-- Course -->
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
              <router-link :to="{ name: 'CategoryList' }" class="text-lg"
                >Category List</router-link
              >
              <router-link :to="{ name: 'AddCourse' }" class="text-lg"
                >Add Course</router-link
              >
              <router-link :to="{ name: 'CourseList' }" class="text-lg"
                >Course List</router-link
              >
              <router-link :to="{ name: 'AddBatch' }" class="text-lg"
                >Add Batch</router-link
              >
              <router-link :to="{ name: 'BatchList' }" class="text-lg"
                >Batch List</router-link
              >
              <router-link :to="{ name: 'Certificate' }" class="text-lg"
                >Generate Certificate</router-link
              >
            </div>
          </div>
          <!-- Course end -->

          <!-- Customer -->
          <div class="relative space-y-6 w-full">
            <a href="#" class="text-lg" @click="toggleCustomerOptions"
              >Customer</a
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
              v-if="showCustomerOptions"
            >
              <!-- <router-link :to="{ name: 'AddRetailCustomer' }" class="text-lg"
                >Add Retail Customer
              </router-link> -->
              <router-link :to="{ name: 'RetailCustomerList' }" class="text-lg"
                >Customer List
              </router-link>
              <!-- <router-link
                :to="{ name: 'AddCorporateCustomer' }"
                class="text-lg"
                >Add Corporate Customer
              </router-link>
              <router-link
                :to="{ name: 'CorporateCustomerList' }"
                class="text-lg"
                >Corporate Customer List
              </router-link> -->
            </div>
          </div>
          <!-- Customer end -->

          <!-- Sale -->
          <div class="relative space-y-6 w-full">
            <a href="#" class="text-lg" @click="toggleSaleOptions">Sale</a>
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
              v-if="showSaleOptions"
            >
              <router-link :to="{ name: 'Sale' }" class="text-lg">
                Sale
              </router-link>
              <router-link :to="{ name: 'Due' }" class="text-lg"
                >Due
              </router-link>
              <router-link :to="{ name: 'SaleRecords' }" class="text-lg"
                >Sale Records
              </router-link>
            </div>
          </div>
          <!-- Sale end -->
        </div>
      </div>
      <div class="col-span-2"></div>
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
      showSaleOptions: false,
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

    toggleSaleOptions() {
      this.showSaleOptions = !this.showSaleOptions;
    },
  },
};
</script>