<template>
  <h1 class="pt-10 text-xl font-semibold">Sale</h1>
  <div class="flex items-center justify-center mb-20">
    <form @submit="addBatch">
      <div class="space-y-5">
        <div class="grid grid-rows-1 gap-2 place-items-start">
          <label for="course" class="font-semibold ml-2">Course*</label>
          <select
            name="course"
            id="course"
            v-model="courseId"
            required
            @change="filterBatch"
            class="
              bg-white
              rounded-md
              px-8
              py-4
              flex
              justify-center
              w-600
              border-2 border-gray-200
              hover:border-navlink hover:ring-0
              focus:outline-none focus:border-navlink
            "
          >
            <option
              v-for="course in courseList"
              :value="course.course_id"
              :key="course.course_id"
            >
              {{ course.course_name }}
            </option>
          </select>
        </div>

        <div class="grid grid-rows-1 gap-2 place-items-start">
          <label for="batch" class="font-semibold ml-2">Batch*</label>
          <select
            name="batch"
            id="batch"
            v-model="batchId"
            required
            @change="setBatchFee"
            class="
              bg-white
              rounded-md
              px-8
              py-4
              flex
              justify-center
              w-600
              border-2 border-gray-200
              hover:border-navlink hover:ring-0
              focus:outline-none focus:border-navlink
            "
          >
            <option
              v-for="batch in tempBatchList"
              :value="batch.batch_id"
              :key="batch.batch_id"
            >
              {{ batch.batch_id }}
            </option>
          </select>
        </div>

        <div class="grid grid-rows-1 gap-2 place-items-start">
          <label for="user" class="font-semibold ml-2">User*</label>
          <select
            name="user"
            id="user"
            v-model="userId"
            required
            class="
              bg-white
              rounded-md
              px-8
              py-4
              flex
              justify-center
              w-600
              border-2 border-gray-200
              hover:border-navlink hover:ring-0
              focus:outline-none focus:border-navlink
            "
          >
            <option
              v-for="user in userList"
              :value="user.user_id"
              :key="user.user_id"
            >
              {{ user.user_name }}
            </option>
          </select>
        </div>

        <div class="grid grid-rows-1 gap-2 place-items-start">
          <label for="course" class="font-semibold ml-2">Customer Type*</label>
          <select
            name="course"
            id="course"
            v-model="customerType"
            required
            class="
              bg-white
              rounded-md
              px-8
              py-4
              flex
              justify-center
              w-600
              border-2 border-gray-200
              hover:border-navlink hover:ring-0
              focus:outline-none focus:border-navlink
            "
            @change="toggleCustomer"
          >
            <option value="retail">Retail</option>
            <option value="corporate">Corporate</option>
          </select>
        </div>

        <!-- Retail Customer Form -->
        <div class="space-y-5" v-if="retailCustomer">
          <div class="grid grid-rows-1 gap-2 place-items-start">
            <label for="custPhone" class="font-semibold ml-2"
              >Phone Number*
            </label>
            <input
              type="tel"
              name="custPhone"
              required
              @change="filterRetailCustomer"
              class="
                bg-white
                rounded-md
                px-8
                py-4
                flex
                justify-center
                w-600
                border-2 border-gray-200
                hover:border-navlink hover:ring-0
                focus:outline-none focus:border-navlink
              "
              placeholder="phone number"
              v-model="custPhone"
            />
          </div>

          <div class="grid grid-rows-1 gap-2 place-items-start">
            <label for="custName" class="font-semibold ml-2"
              >Customer Name*</label
            >
            <input
              type="text"
              name="custName"
              required
              class="
                bg-white
                rounded-md
                px-8
                py-4
                flex
                justify-center
                w-600
                border-2 border-gray-200
                hover:border-navlink hover:ring-0
                focus:outline-none focus:border-navlink
              "
              placeholder="name"
              v-model="custName"
            />
          </div>

          <div class="grid grid-rows-1 gap-2 place-items-start">
            <label for="custEmail" class="font-semibold ml-2">Email*</label>
            <input
              type="email"
              name="custEmail"
              required
              class="
                bg-white
                rounded-md
                px-8
                py-4
                flex
                justify-center
                w-600
                border-2 border-gray-200
                hover:border-navlink hover:ring-0
                focus:outline-none focus:border-navlink
              "
              placeholder="email"
              v-model="custEmail"
            />
          </div>

          <div class="grid grid-rows-1 gap-2 place-items-start">
            <label for="custAddress" class="font-semibold ml-2">Address*</label>
            <input
              type="text"
              name="custAddress"
              required
              class="
                bg-white
                rounded-md
                px-8
                py-4
                flex
                justify-center
                w-600
                border-2 border-gray-200
                hover:border-navlink hover:ring-0
                focus:outline-none focus:border-navlink
              "
              placeholder="address"
              v-model="custAddress"
            />
          </div>

          <div class="grid grid-rows-1 gap-2 place-items-start">
            <label for="custOrganization" class="font-semibold ml-2"
              >Organization*</label
            >
            <input
              type="text"
              name="custOrganization"
              required
              class="
                bg-white
                rounded-md
                px-8
                py-4
                flex
                justify-center
                w-600
                border-2 border-gray-200
                hover:border-navlink hover:ring-0
                focus:outline-none focus:border-navlink
              "
              placeholder="organization"
              v-model="custOrganization"
            />
          </div>

          <div class="grid grid-rows-1 gap-2 place-items-start">
            <label for="custDesignation" class="font-semibold ml-2"
              >Designation*</label
            >
            <input
              type="tel"
              name="custDesignation"
              required
              class="
                bg-white
                rounded-md
                px-8
                py-4
                flex
                justify-center
                w-600
                border-2 border-gray-200
                hover:border-navlink hover:ring-0
                focus:outline-none focus:border-navlink
              "
              placeholder="designation"
              v-model="custDesignation"
            />
          </div>

          <div class="grid grid-rows-1 gap-2 place-items-start">
            <label for="regularFee" class="font-semibold ml-2"
              >Regular Fee*</label
            >
            <input
              type="number"
              name="regularFee"
              required
              class="
                bg-white
                rounded-md
                px-8
                py-4
                flex
                justify-center
                w-600
                border-2 border-gray-200
                hover:border-navlink hover:ring-0
                focus:outline-none focus:border-navlink
              "
              placeholder="regular fee"
              v-model="regularFee"
            />
          </div>

          <div class="grid grid-rows-1 gap-2 place-items-start">
            <label for="batchFee" class="font-semibold ml-2">Batch Fee*</label>
            <input
              type="number"
              name="batchFee"
              required
              class="
                bg-white
                rounded-md
                px-8
                py-4
                flex
                justify-center
                w-600
                border-2 border-gray-200
                hover:border-navlink hover:ring-0
                focus:outline-none focus:border-navlink
              "
              placeholder="batch fee"
              v-model="batchFee"
            />
          </div>

          <div class="grid grid-rows-1 gap-2 place-items-start">
            <label for="discountFee" class="font-semibold ml-2"
              >Discount*</label
            >
            <input
              type="number"
              name="discountFee"
              required
              @change="setCustTotal"
              class="
                bg-white
                rounded-md
                px-8
                py-4
                flex
                justify-center
                w-600
                border-2 border-gray-200
                hover:border-navlink hover:ring-0
                focus:outline-none focus:border-navlink
              "
              placeholder="discount"
              v-model="discountFee"
            />
          </div>

          <div class="grid grid-rows-1 gap-2 place-items-start">
            <label for="custTotalFee" class="font-semibold ml-2">Total*</label>
            <input
              type="number"
              name="custTotalFee"
              required
              class="
                bg-white
                rounded-md
                px-8
                py-4
                flex
                justify-center
                w-600
                border-2 border-gray-200
                hover:border-navlink hover:ring-0
                focus:outline-none focus:border-navlink
              "
              disabled
              placeholder="total"
              v-model="custTotalFee"
            />
          </div>

          <div class="grid grid-rows-1 gap-2 place-items-start">
            <label for="custPaidFee" class="font-semibold ml-2">Paid*</label>
            <input
              type="number"
              name="custPaidFee"
              required
              @change="setCustDue"
              class="
                bg-white
                rounded-md
                px-8
                py-4
                flex
                justify-center
                w-600
                border-2 border-gray-200
                hover:border-navlink hover:ring-0
                focus:outline-none focus:border-navlink
              "
              placeholder="paid"
              v-model="custPaidFee"
            />
          </div>

          <div class="grid grid-rows-1 gap-2 place-items-start">
            <label for="custDueFee" class="font-semibold ml-2">Due*</label>
            <input
              type="number"
              name="custDueFee"
              required
              class="
                bg-white
                rounded-md
                px-8
                py-4
                flex
                justify-center
                w-600
                border-2 border-gray-200
                hover:border-navlink hover:ring-0
                focus:outline-none focus:border-navlink
              "
              placeholder="due"
              v-model="custDueFee"
            />
          </div>

          <button
            class="
              bg-navlink
              rounded-md
              text-white text-xl
              px-8
              py-2
              w-500
              mt-10
              border-2 border-navlink
              shadow-xl
              hover:text-navlink hover:bg-transparent
              transition
              duration-300
            "
            type="submit"
          >
            Sale
          </button>
        </div>
        <!-- Retail Customer Form end -->

        <!-- Corporate Customer Form -->
        <div class="space-y-5" v-if="corporateCustomer">
          <div class="grid grid-rows-1 gap-2 place-items-start">
            <label for="corpPhone" class="font-semibold ml-2"
              >Phone Number*</label
            >
            <input
              type="tel"
              name="corpPhone"
              required
              @change="filterCorporateCustomer"
              class="
                bg-white
                rounded-md
                px-8
                py-4
                flex
                justify-center
                w-600
                border-2 border-gray-200
                hover:border-navlink hover:ring-0
                focus:outline-none focus:border-navlink
              "
              placeholder="phone number"
              v-model="corpPhone"
            />
          </div>

          <div class="grid grid-rows-1 gap-2 place-items-start">
            <label for="corpName" class="font-semibold ml-2"
              >Organization*</label
            >
            <input
              type="text"
              name="corpName"
              required
              class="
                bg-white
                rounded-md
                px-8
                py-4
                flex
                justify-center
                w-600
                border-2 border-gray-200
                hover:border-navlink hover:ring-0
                focus:outline-none focus:border-navlink
              "
              placeholder="organization"
              v-model="corpName"
            />
          </div>

          <div class="grid grid-rows-1 gap-2 place-items-start">
            <label for="corpEmail" class="font-semibold ml-2">Email*</label>
            <input
              type="email"
              name="corpEmail"
              required
              class="
                bg-white
                rounded-md
                px-8
                py-4
                flex
                justify-center
                w-600
                border-2 border-gray-200
                hover:border-navlink hover:ring-0
                focus:outline-none focus:border-navlink
              "
              placeholder="email"
              v-model="corpEmail"
            />
          </div>

          <div class="grid grid-rows-1 gap-2 place-items-start">
            <label for="corpAddress" class="font-semibold ml-2">Address*</label>
            <input
              type="text"
              name="corpAddress"
              required
              class="
                bg-white
                rounded-md
                px-8
                py-4
                flex
                justify-center
                w-600
                border-2 border-gray-200
                hover:border-navlink hover:ring-0
                focus:outline-none focus:border-navlink
              "
              placeholder="address"
              v-model="corpAddress"
            />
          </div>

          <div class="grid grid-rows-1 gap-2 place-items-start">
            <label for="regularFee" class="font-semibold ml-2"
              >Regular Fee*</label
            >
            <input
              type="number"
              name="regularFee"
              required
              class="
                bg-white
                rounded-md
                px-8
                py-4
                flex
                justify-center
                w-600
                border-2 border-gray-200
                hover:border-navlink hover:ring-0
                focus:outline-none focus:border-navlink
              "
              placeholder="regular fee"
              v-model="regularFee"
            />
          </div>

          <div class="grid grid-rows-1 gap-2 place-items-start">
            <label for="batchFee" class="font-semibold ml-2">Batch Fee*</label>
            <input
              type="number"
              name="batchFee"
              required
              class="
                bg-white
                rounded-md
                px-8
                py-4
                flex
                justify-center
                w-600
                border-2 border-gray-200
                hover:border-navlink hover:ring-0
                focus:outline-none focus:border-navlink
              "
              placeholder="batch fee"
              v-model="batchFee"
            />
          </div>

          <div class="grid grid-rows-1 gap-2 place-items-start">
            <label for="corpUnits" class="font-semibold ml-2">Units*</label>
            <input
              type="number"
              name="corpUnits"
              required
              class="
                bg-white
                rounded-md
                px-8
                py-4
                flex
                justify-center
                w-600
                border-2 border-gray-200
                hover:border-navlink hover:ring-0
                focus:outline-none focus:border-navlink
              "
              placeholder="units"
              v-model="corpUnits"
            />
          </div>

          <div class="grid grid-rows-1 gap-2 place-items-start">
            <label for="discountFee" class="font-semibold ml-2"
              >Discount*</label
            >
            <input
              type="number"
              name="discountFee"
              required
              @change="setCorpTotal"
              class="
                bg-white
                rounded-md
                px-8
                py-4
                flex
                justify-center
                w-600
                border-2 border-gray-200
                hover:border-navlink hover:ring-0
                focus:outline-none focus:border-navlink
              "
              placeholder="discount"
              v-model="discountFee"
            />
          </div>

          <div class="grid grid-rows-1 gap-2 place-items-start">
            <label for="corpTotalFee" class="font-semibold ml-2">Total*</label>
            <input
              type="number"
              name="corpTotalFee"
              required
              class="
                bg-white
                rounded-md
                px-8
                py-4
                flex
                justify-center
                w-600
                border-2 border-gray-200
                hover:border-navlink hover:ring-0
                focus:outline-none focus:border-navlink
              "
              disabled
              placeholder="total"
              v-model="corpTotalFee"
            />
          </div>

          <div class="grid grid-rows-1 gap-2 place-items-start">
            <label for="corpPaidFee" class="font-semibold ml-2">Paid*</label>
            <input
              type="number"
              name="corpPaidFee"
              required
              @keydown.enter.prevent="setCorpDue"
              class="
                bg-white
                rounded-md
                px-8
                py-4
                flex
                justify-center
                w-600
                border-2 border-gray-200
                hover:border-navlink hover:ring-0
                focus:outline-none focus:border-navlink
              "
              placeholder="paid"
              v-model="corpPaidFee"
            />
          </div>

          <div class="grid grid-rows-1 gap-2 place-items-start">
            <label for="corpDueFee" class="font-semibold ml-2">Due*</label>
            <input
              type="number"
              name="corpDueFee"
              required
              class="
                bg-white
                rounded-md
                px-8
                py-4
                flex
                justify-center
                w-600
                border-2 border-gray-200
                hover:border-navlink hover:ring-0
                focus:outline-none focus:border-navlink
              "
              placeholder="due"
              v-model="corpDueFee"
            />
          </div>

          <button
            class="
              bg-navlink
              rounded-md
              text-white text-xl
              px-8
              py-2
              w-500
              mt-10
              border-2 border-navlink
              shadow-xl
              hover:text-navlink hover:bg-transparent
              transition
              duration-300
            "
            type="submit"
          >
            Sale
          </button>
        </div>
        <!-- Corporate Customer Form end -->
      </div>
    </form>
  </div>

  <div v-if="showModal">
    <Modal :header="header" :text="text" @close="toggleModal">
      <h3>{{ message }}</h3>
    </Modal>
  </div>
</template>

<script>
import Modal from "../../components/Modal.vue";

export default {
  components: { Modal },
  data() {
    return {
      customerType: "",
      message: "Customer added",
      showModal: false,
      retailCustomer: false,
      corporateCustomer: false,
      custId: "",
      custName: "",
      custEmail: "",
      custPhone: "",
      custAddress: "",
      custOrganization: "",
      custDesignation: "",
      custTotalFee: "",
      custPaidFee: "",
      custDueFee: "",
      corpId: "",
      corpName: "",
      corpEmail: "",
      corpPhone: "",
      corpAddress: "",
      corpTotalFee: "",
      corpPaidFee: "",
      corpDueFee: "",
      corpUnits: "",
      courseId: "",
      batchId: "",
      regularFee: "",
      batchFee: "",
      discountFee: "",
      selectBatch: true,
      tempBatchList: [],
      newCustomer: true,
      userId: "",
    };
  },
  mounted() {
    this.$store.dispatch("getCourseList");
    this.$store.dispatch("getBatchList");
    this.$store.dispatch("getRetailCustomerList");
    this.$store.dispatch("getCorporateCustomerList");
    this.$store.dispatch("getUserList");
  },
  methods: {
    toggleModal() {
      this.showModal = !this.showModal;
    },

    toggleCustomer() {
      if (this.customerType == "retail") {
        this.corporateCustomer = false;
        this.retailCustomer = true;
      } else if (this.customerType == "corporate") {
        this.retailCustomer = false;
        this.corporateCustomer = true;
      }
    },

    filterBatch() {
      let course = this.courseId.substr(0, 3);
      this.tempBatchList.length = 0;
      this.batchList.filter((batch) => {
        if (course == batch.batch_id.substr(0, 3)) {
          this.tempBatchList.push(batch);
        }
      });

      this.courseList.filter((course) => {
        if (course.course_id == this.courseId) {
          this.regularFee = course.regular_price;
        }
      });
      console.log(course);
      // this.selectBatch = false;
    },

    setBatchFee() {
      this.tempBatchList.filter((batch) => {
        if (batch.batch_id == this.batchId) {
          this.batchFee = batch.batch_fee;
        }
      });
    },

    filterRetailCustomer() {
      this.retailCustomerList.filter((customer) => {
        if (this.custPhone == customer.cust_phone) {
          this.newCustomer = false;
          this.custName = customer.cust_name;
          this.custEmail = customer.cust_email;
          this.custAddress = customer.cust_address;
          this.custOrganization = customer.cust_organization;
          this.custDesignation = customer.cust_designation;
        }
      });
    },

    filterCorporateCustomer() {
      this.corporateCustomerList.filter((customer) => {
        if (this.corpPhone == customer.corp_phone) {
          this.newCustomer = false;
          this.corpName = customer.corp_name;
          this.corpEmail = customer.corp_email;
          this.corpAddress = customer.corp_address;
        }
      });
    },

    setCustTotal() {
      this.custTotalFee = this.batchFee - this.discountFee;
    },

    setCorpTotal() {
      this.corpTotalFee = this.batchFee * this.corpUnits - this.discountFee;
    },

    setCustDue() {
      this.custDueFee = this.custTotalFee - this.custPaidFee;
    },

    setCorpDue() {
      this.corpDueFee = this.corpTotalFee - this.corpPaidFee;
    },
  },
  computed: {
    courseList: {
      get() {
        return this.$store.getters.courseList;
      },
    },

    // batchesByCourse: {
    //   get() {
    //     return this.$store.getters.batchesByCourse;
    //   },
    // },

    batchList: {
      get() {
        return this.$store.getters.batchList;
      },
    },

    retailCustomerList: {
      get() {
        return this.$store.getters.retailCustomerList;
      },
    },

    corporateCustomerList: {
      get() {
        return this.$store.getters.corporateCustomerList;
      },
    },

    userList: {
      get() {
        return this.$store.getters.userList;
      },
    },
  },
};
</script>