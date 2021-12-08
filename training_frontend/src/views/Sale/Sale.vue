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
            v-model="course_id"
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
            @change="generateBatchId"
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
          <label for="course" class="font-semibold ml-2">Batch*</label>
          <select
            name="course"
            id="course"
            v-model="course_id"
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
            @change="generateBatchId"
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
            <label for="due" class="font-semibold ml-2">Phone Number*</label>
            <input
              type="tel"
              name="due"
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
              placeholder="phone number"
              v-model="due"
            />
          </div>

          <div class="grid grid-rows-1 gap-2 place-items-start">
            <label for="due" class="font-semibold ml-2">Customer Name*</label>
            <input
              type="text"
              name="due"
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
              v-model="due"
            />
          </div>

          <div class="grid grid-rows-1 gap-2 place-items-start">
            <label for="due" class="font-semibold ml-2">Email*</label>
            <input
              type="email"
              name="due"
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
              v-model="due"
            />
          </div>

          <div class="grid grid-rows-1 gap-2 place-items-start">
            <label for="due" class="font-semibold ml-2">Address*</label>
            <input
              type="text"
              name="due"
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
              v-model="due"
            />
          </div>

          <div class="grid grid-rows-1 gap-2 place-items-start">
            <label for="due" class="font-semibold ml-2">Organization*</label>
            <input
              type="tel"
              name="due"
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
              v-model="due"
            />
          </div>

          <div class="grid grid-rows-1 gap-2 place-items-start">
            <label for="due" class="font-semibold ml-2">Designation*</label>
            <input
              type="tel"
              name="due"
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
              v-model="due"
            />
          </div>

          <div class="grid grid-rows-1 gap-2 place-items-start">
            <label for="batchFee" class="font-semibold ml-2"
              >Regular Fee*</label
            >
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
              placeholder="regular fee"
              v-model="regular_fee"
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
              v-model="batch_fee"
            />
          </div>

          <div class="grid grid-rows-1 gap-2 place-items-start">
            <label for="batchFee" class="font-semibold ml-2">Discount*</label>
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
              placeholder="discount"
              v-model="discount"
            />
          </div>

          <div class="grid grid-rows-1 gap-2 place-items-start">
            <label for="batchFee" class="font-semibold ml-2">Total*</label>
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
              disabled
              placeholder="total"
              v-model="total"
            />
          </div>

          <div class="grid grid-rows-1 gap-2 place-items-start">
            <label for="batchFee" class="font-semibold ml-2">Paid*</label>
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
              placeholder="paid"
              v-model="paid"
            />
          </div>

          <div class="grid grid-rows-1 gap-2 place-items-start">
            <label for="due" class="font-semibold ml-2">Due*</label>
            <input
              type="number"
              name="due"
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
              v-model="due"
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
            <label for="due" class="font-semibold ml-2">Phone Number*</label>
            <input
              type="tel"
              name="due"
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
              placeholder="phone number"
              v-model="due"
            />
          </div>

          <div class="grid grid-rows-1 gap-2 place-items-start">
            <label for="due" class="font-semibold ml-2">Organization*</label>
            <input
              type="text"
              name="due"
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
              v-model="due"
            />
          </div>

          <div class="grid grid-rows-1 gap-2 place-items-start">
            <label for="due" class="font-semibold ml-2">Email*</label>
            <input
              type="email"
              name="due"
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
              v-model="due"
            />
          </div>

          <div class="grid grid-rows-1 gap-2 place-items-start">
            <label for="due" class="font-semibold ml-2">Address*</label>
            <input
              type="text"
              name="due"
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
              v-model="due"
            />
          </div>

          <div class="grid grid-rows-1 gap-2 place-items-start">
            <label for="batchFee" class="font-semibold ml-2"
              >Regular Fee*</label
            >
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
              placeholder="regular fee"
              v-model="regular_fee"
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
              v-model="batch_fee"
            />
          </div>

          <div class="grid grid-rows-1 gap-2 place-items-start">
            <label for="batchFee" class="font-semibold ml-2">Units*</label>
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
              placeholder="units"
              v-model="discount"
            />
          </div>

          <div class="grid grid-rows-1 gap-2 place-items-start">
            <label for="batchFee" class="font-semibold ml-2">Discount*</label>
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
              placeholder="discount"
              v-model="discount"
            />
          </div>

          <div class="grid grid-rows-1 gap-2 place-items-start">
            <label for="batchFee" class="font-semibold ml-2">Total*</label>
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
              disabled
              placeholder="total"
              v-model="total"
            />
          </div>

          <div class="grid grid-rows-1 gap-2 place-items-start">
            <label for="batchFee" class="font-semibold ml-2">Paid*</label>
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
              placeholder="paid"
              v-model="paid"
            />
          </div>

          <div class="grid grid-rows-1 gap-2 place-items-start">
            <label for="due" class="font-semibold ml-2">Due*</label>
            <input
              type="number"
              name="due"
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
              v-model="due"
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
      custTotalFee: 0,
      custPaidFee: 0,
      custDueFee: 0,
      corpId: "",
      corpName: "",
      corpEmail: "",
      corpPhone: "",
      corpAddress: "",
      corpTotalFee: 0,
      corpPaidFee: 0,
      corpDueFee: 0,
      corpUnits: 0,
    };
  },
  mounted() {
    this.$store.dispatch("getCourseList");
    this.$store.dispatch("getInstructorList");
    this.$store.dispatch("getBatchList");
  },
  methods: {
    addBatch() {
      const data = {
        batch_id: this.batch_id,
        batch_fee: this.batch_fee,
        admit_closed: this.admit_closed,
        course_id: this.course_id,
        inst_id: this.inst_id,
      };

      //   this.$store.dispatch("addBatch", data);
      this.showModal = true;
    },

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
  },
  computed: {
    courseList: {
      get() {
        return this.$store.getters.courseList;
      },
    },

    instructorList: {
      get() {
        return this.$store.getters.instructorList;
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
  },
};
</script>