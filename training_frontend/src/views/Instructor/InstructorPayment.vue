<template>
  <h1 class="pt-10 text-xl font-semibold">Instructor Payment</h1>
  <div class="px-28 py-10">
    <div class="flex items-center justify-center">
      <form @submit.prevent="addInstructorFee">
        <div class="space-y-5">
          <!-- <div v-for="inputField in inputFields" :key="inputField.id"> -->
          <div class="grid grid-rows-1 gap-2 place-items-start">
            <label for="instructor" class="font-semibold ml-2"
              >Instructor*</label
            >
            <select
              name="instructor"
              id="instructor"
              v-model="instructor"
              required
              @change="getBatches"
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
                v-for="instructor in instructorList"
                :value="instructor"
                :key="instructor.inst_id"
              >
                {{ instructor.inst_name }}
              </option>
            </select>
          </div>

          <div class="grid grid-rows-1 gap-2 place-items-start">
            <label for="batch" class="font-semibold ml-2">Batch*</label>
            <select
              name="batch"
              id="batch"
              v-model="batchId"
              @change="getTotalFees"
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
                v-for="batch in batchesByInstructor"
                :value="batch.batch_id"
                :key="batch.batch_id"
              >
                {{ batch.batch_id }}
              </option>
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
              v-model="saleTotalPayable.total_sale"
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
              v-model="saleTotalPayable.inst_payable"
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
              v-model="instructorPaidDue.paid"
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
              v-model="instructorPaidDue.due"
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
import moment from "moment";

export default {
  components: { Modal },
  data() {
    return {
      instId: "",
      batchId: "",
      totalSale: "",
      totalPayable: "",
      totalPaid: "",
      totalDue: "",
      date: "",
      checkDate: null,
      paymentMethod: "",
      payment: "",
      paymentMethodList: [
        { id: 1, name: "bkash" },
        { id: 2, name: "nagad" },
        { id: 3, name: "cash" },
        { id: 4, name: "exim bank" },
        { id: 5, name: "dbbl" },
        { id: 6, name: "cheque" },
      ],
      showCheckDate: false,
      address: "",
      organization: "",
      designation: "",
      profit: "",
      showModal: false,
      message: "Record added",
      checkRefNo: "",
      instructor: "",
    };
  },
  mounted() {
    this.$store.dispatch("getInstructorList");
    this.date = this.getDate();
  },
  computed: {
    instructorList: {
      get() {
        return this.$store.getters.instructorList;
      },
    },

    batchesByInstructor: {
      get() {
        return this.$store.getters.batchesByInstructor;
      },
    },

    saleTotalPayable: {
      get() {
        return this.$store.getters.saleTotalPayable;
      },
    },

    instructorPaidDue: {
      get() {
        return this.$store.getters.instructorPaidDue;
      },
    },
  },
  methods: {
    getBatches() {
      this.$store.dispatch("getBatchesByInstructor", this.instructor.inst_id);
    },

    getTotalFees() {
      this.$store.dispatch("getSaleTotalPayable", this.batchId);
      this.$store.dispatch("getInstructorPaidDue", this.batchId);
    },

    addInstructorFee() {
      let due = 0;
      if (this.instructorPaidDue.due == null) {
        due = this.saleTotalPayable.inst_payable - this.payment;
      } else {
        due = this.instructorPaidDue.due - this.payment;
      }

      const data = {
        inst_id: this.instructor.inst_id,
        batch_id: this.batchId,
        total_sale: this.saleTotalPayable.total_sale,
        pay_received: this.saleTotalPayable.pay_received,
        total_payable: this.saleTotalPayable.inst_payable,
        paid: this.payment,
        due: due,
        date: this.date,
        pay_mode: this.paymentMethod,
        check_date: this.checkDate,
        check_no: this.checkRefNo,
      };

      const instData = {
        inst_payable: this.instructor.inst_payable,
        inst_paid: this.instructor.inst_paid + this.payment,
        inst_due: this.instructor.inst_due - this.payment,
        inst_id: this.instructor.inst_id,
      };
      this.$store.dispatch("updateInstructorFee", instData);
      this.$store.dispatch("addInstructorFeeRecord", data);
      this.showModal = true;
    },

    getDate: function () {
      return moment(String(new Date().toLocaleDateString())).format(
        "YYYY-MM-DD"
      );
    },

    toggleModal() {
      this.showModal = false;
      window.location.reload();
    },

    toggleCheckDate() {
      if (this.paymentMethod == "cheque") {
        this.showCheckDate = true;
      } else {
        this.showCheckDate = false;
      }
    },
  },
};
</script>

