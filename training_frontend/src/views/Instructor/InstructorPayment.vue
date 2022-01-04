<template>
  <h1 class="pt-10 text-xl font-semibold">Instructor Payment</h1>
  <div class="px-28 py-10">
    <div class="flex items-center justify-center">
      <form @submit.prevent="addInstructor">
        <div class="space-y-5">
          <!-- <div v-for="inputField in inputFields" :key="inputField.id"> -->
          <div class="grid grid-rows-1 gap-2 place-items-start">
            <label for="inst_name" class="font-semibold ml-2"
              >Instructor*</label
            >
            <select
              name="inst_name"
              id="inst_name"
              v-model="inst_name"
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
              <!-- <option
                v-for="batch in tempBatchList"
                :value="batch"
                :key="batch.batch_id"
              >
                {{ batch.batch_id }}
              </option> -->
            </select>
          </div>

          <div class="grid grid-rows-1 gap-2 place-items-start">
            <label for="batch" class="font-semibold ml-2">Batch*</label>
            <select
              name="batch"
              id="batch"
              v-model="batchId"
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
              <!-- <option
                v-for="batch in tempBatchList"
                :value="batch"
                :key="batch.batch_id"
              >
                {{ batch.batch_id }}
              </option> -->
            </select>
          </div>

          <div class="grid grid-rows-1 gap-2 place-items-start">
            <label for="total_sale" class="font-semibold ml-2"
              >Total Sale</label
            >
            <input
              type="number"
              name="total_sale"
              required
              disabled
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
              placeholder="total sale"
              v-model="totalSale"
            />
          </div>

          <div class="grid grid-rows-1 gap-2 place-items-start">
            <label for="total_payable" class="font-semibold ml-2"
              >Total Payable</label
            >
            <input
              type="number"
              name="total_payable"
              required
              disabled
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
              placeholder="total payable"
              v-model="totalPayable"
            />
          </div>

          <div class="grid grid-rows-1 gap-2 place-items-start">
            <label for="total_paid" class="font-semibold ml-2"
              >Total Paid</label
            >
            <input
              type="number"
              name="total_paid"
              required
              disabled
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
              placeholder="total paid"
              v-model="totalPaid"
            />
          </div>

          <div class="grid grid-rows-1 gap-2 place-items-start">
            <label for="total_due" class="font-semibold ml-2">Total Due</label>
            <input
              type="number"
              name="total_due"
              required
              disabled
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
              placeholder="total due"
              v-model="totalDue"
            />
          </div>

          <div class="grid grid-rows-1 gap-2 place-items-start">
            <label for="paymentMethod" class="font-semibold ml-2"
              >Payment Method*</label
            >
            <select
              name="paymentMethod"
              id="paymentMethod"
              @change="toggleCheckDate"
              v-model="paymentMethod"
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
                v-for="payMethod in paymentMethodList"
                :value="payMethod.name"
                :key="payMethod.id"
              >
                {{ payMethod.name }}
              </option>
            </select>
          </div>

          <div class="grid grid-rows-1 gap-2 place-items-start">
            <label for="checkRefNo" class="font-semibold ml-2"
              >Cheque/Ref No*</label
            >
            <input
              type="text"
              name="checkRefNo"
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
              placeholder="check/ref no."
              v-model="checkRefNo"
            />
          </div>

          <div
            class="grid grid-rows-1 gap-2 place-items-start"
            v-if="showCheckDate"
          >
            <label for="checkDate" class="font-semibold ml-2"
              >Cheque Date*</label
            >
            <input
              type="date"
              name="checkDate"
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
              v-model="checkDate"
            />
          </div>

          <div class="grid grid-rows-1 gap-2 place-items-start">
            <label for="payment" class="font-semibold ml-2">Payment*</label>
            <input
              type="number"
              name="payment"
              required
              @keydown.enter.prevent=""
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
              placeholder="payment"
              v-model="payment"
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
            Pay
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
      inst_name: "",
      batchId: "",
      totalSale: "",
      totalPayable: "",
      totalPaid: "",
      totalDue: "",
      date: "",
      checkDate: "",
      paymentMethod: "",
      payment: "",
      paymentMethodList: [
        { id: 1, name: "bkash" },
        { id: 2, name: "nagad" },
        { id: 3, name: "cash" },
        { id: 4, name: "exim bank" },
        { id: 5, name: "dbbl" },
        { id: 6, name: "check" },
      ],
      showCheckDate: false,
      address: "",
      organization: "",
      designation: "",
      profit: "",
      showModal: false,
      message: "Instructor added",
    };
  },
  mounted() {
    this.$store.dispatch("getInstructorCount");
  },
  computed: {
    instructorCount: {
      get() {
        return this.$store.getters.instructorCount;
      },
    },
  },
  methods: {
    addInstructor() {
      //   if (this.name.length > 3) {
      //     let inst_id = this.name.substr(0, 3);
      //     inst_id = inst_id.toUpperCase();
      //     let num = (10000 + (this.instructorCount[0] + 1)).toString();
      //     inst_id = inst_id.concat(num.substr(1, 4));
      //     const data = {
      //       inst_id: inst_id,
      //       inst_name: this.name,
      //       inst_phone: this.phone,
      //       inst_email: this.email,
      //       inst_address: this.address,
      //       inst_organization: this.organization,
      //       inst_designation: this.designation,
      //       inst_profit: this.profit,
      //     };
      //     console.log(data);
      //     this.$store.dispatch("addInstructor", data);
      //     this.showModal = true;
      //   }
    },

    toggleModal() {
      //   this.showModal = false;
      //   window.location.reload();
    },

    toggleCheckDate() {
      if (this.paymentMethod == "check") {
        this.showCheckDate = true;
      } else {
        this.showCheckDate = false;
      }
    },
  },
};
</script>

