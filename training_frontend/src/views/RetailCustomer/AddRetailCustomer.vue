<template>
  <h1 class="pt-10 text-xl font-semibold">Add Retail Customer</h1>
  <div class="px-28 py-10">
    <div class="flex items-center justify-center">
      <form @submit.prevent="AddRetailCustomer">
        <div class="space-y-5">
          <div class="grid grid-rows-1 gap-2 place-items-start">
            <label for="name" class="font-semibold ml-2"
              >Retail Customer Name*</label
            >
            <input
              type="text"
              name="name"
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
              v-model="name"
            />
          </div>

          <div class="grid grid-rows-1 gap-2 place-items-start">
            <label for="email" class="font-semibold ml-2">Email*</label>
            <input
              type="email"
              name="email"
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
              v-model="email"
            />
          </div>

          <div class="grid grid-rows-1 gap-2 place-items-start">
            <label for="phone" class="font-semibold ml-2">Phone number*</label>
            <input
              type="tel"
              name="phone"
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
              v-model="phone"
            />
          </div>

          <div class="grid grid-rows-1 gap-2 place-items-start">
            <label for="address" class="font-semibold ml-2">Address*</label>
            <input
              type="text"
              name="address"
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
              v-model="address"
            />
          </div>

          <div class="grid grid-rows-1 gap-2 place-items-start">
            <label for="organization" class="font-semibold ml-2"
              >Organization*</label
            >
            <input
              type="text"
              name="organization"
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
              v-model="organization"
            />
          </div>

          <div class="grid grid-rows-1 gap-2 place-items-start">
            <label for="designation" class="font-semibold ml-2"
              >Designation*</label
            >
            <input
              type="text"
              name="designation"
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
              v-model="designation"
            />
          </div>

          <div class="grid grid-rows-1 gap-2 place-items-start">
            <label for="totalFee" class="font-semibold ml-2">Total Fee*</label>
            <input
              type="number"
              name="totalFee"
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
              placeholder="total fee"
              v-model="totalFee"
            />
          </div>

          <div class="grid grid-rows-1 gap-2 place-items-start">
            <label for="paidFee" class="font-semibold ml-2">Paid Fee*</label>
            <input
              type="number"
              name="paidFee"
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
              placeholder="paid fee"
              v-model="paidFee"
            />
          </div>

          <div class="grid grid-rows-1 gap-2 place-items-start">
            <label for="dueFee" class="font-semibold ml-2">Due Fee*</label>
            <input
              type="number"
              name="dueFee"
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
              placeholder="due fee"
              v-model="dueFee"
            />
          </div>

          <!-- </div> -->
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
            Add Retail Customer
          </button>
        </div>
      </form>
    </div>
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
      name: "",
      email: "",
      phone: "",
      address: "",
      organization: "",
      designation: "",
      totalFee: 0,
      paidFee: 0,
      dueFee: 0,
      showModal: false,
      message: "Retail customer added",
    };
  },
  mounted() {
    this.$store.dispatch("getRetailCustomerCount");
  },
  computed: {
    retailCustomerCount: {
      get() {
        return this.$store.getters.retailCustomerCount;
      },
    },
  },
  methods: {
    AddRetailCustomer() {
      if (this.name.length >= 3) {
        let cust_id = new Date().getFullYear();
        cust_id = cust_id.toString();
        cust_id = (
          parseInt(cust_id.substr(2, 4)) * 10000 +
          this.retailCustomerCount[0] +
          1
        ).toString();

        const data = {
          cust_id: cust_id,
          cust_name: this.name,
          cust_phone: this.phone,
          cust_email: this.email,
          cust_address: this.address,
          cust_organization: this.organization,
          cust_designation: this.designation,
          cust_total_fee: this.totalFee,
          cust_paid_fee: this.paidFee,
          cust_due_fee: this.dueFee,
        };

        console.log(data);
        this.$store.dispatch("addRetailCustomer", data);
        this.showModal = true;
      }
    },

    toggleModal() {
      this.showModal = false;
      window.location.reload();
    },
  },
};
</script>

