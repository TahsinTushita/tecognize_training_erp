<template>
  <h1 class="pt-10 text-xl font-semibold">Due</h1>
  <div class="flex items-center justify-center mb-20">
    <form @submit.prevent="false">
      <div class="space-y-5">
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
          >
            <option
              v-for="type in customerTypes"
              :key="type.id"
              :value="type.type"
            >
              {{ type.type }}
            </option>
          </select>
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
            >Check/Ref No*</label
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
          <label for="checkDate" class="font-semibold ml-2">Check Date*</label>
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
          <label for="phone" class="font-semibold ml-2">Phone Number* </label>
          <input
            type="tel"
            name="phone"
            required
            @change="filterCustomerAndBatch"
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
          <label for="name" class="font-semibold ml-2">Customer Name*</label>
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
            disabled
            placeholder="name"
            v-model="name"
          />
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
            @change="setFees"
          >
            <option
              v-for="(batch, index) in tempBatchList"
              :value="batch"
              :key="index"
            >
              {{ batch }}
            </option>
          </select>
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
            v-model="totalFee"
          />
        </div>
        <div class="grid grid-rows-1 gap-2 place-items-start">
          <label for="custTotalFee" class="font-semibold ml-2"
            >1st installment*</label
          >
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
            placeholder="1st installment"
            v-model="installment1"
          />
        </div>
        <div class="grid grid-rows-1 gap-2 place-items-start">
          <label for="custTotalFee" class="font-semibold ml-2"
            >2nd installment*</label
          >
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
            placeholder="2nd installment"
            v-model="installment2"
          />
        </div>
        <div class="grid grid-rows-1 gap-2 place-items-start">
          <label for="custTotalFee" class="font-semibold ml-2"
            >3rd installment*</label
          >
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
            placeholder="3rd installment"
            v-model="installment3"
          />
        </div>
        <div class="grid grid-rows-1 gap-2 place-items-start">
          <label for="custTotalFee" class="font-semibold ml-2"
            >4th installment*</label
          >
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
            placeholder="4th installment"
            v-model="installment4"
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
            v-model="getDue"
            disabled
          />
        </div>
      </div>
    </form>
  </div>
  <div class="flex items-center justify-center">
    <div ref="retailReceiptContent" class="space-y-5">
      <!-- Money Receipt -->
      <div class="w-1100 bg-receiptBg">
        <div class="px-10 pt-10">
          <div class="flex justify-between items-center mb-5">
            <h1
              class="
                border-b-8
                font-segoeUI
                text-2xl
                font-bold
                pb-3
                text-receiptTextColor
                border-receiptBorder
              "
            >
              Money Receipt
            </h1>
            <img
              src="../../assets/images/traininglogo.png"
              alt="logo"
              class="w-36 h-10"
            />
          </div>
          <div class="flex justify-between items-center justify-center mb-5">
            <h1
              class="
                font-segoeUI
                text-xl
                font-bold
                text-receiptTextColor
                flex
                gap-2
              "
            >
              SL NO:
              <p class="text-black font-medium">{{ saleid[0] + 1 }}</p>
            </h1>
            <div class="flex gap-2 items-center justify-center">
              <h1 class="font-segoeUI text-xl font-bold text-receiptTextColor">
                DATE:
              </h1>
              <div
                type="text"
                class="
                  w-40
                  px-4
                  py-2
                  bg-transparent
                  border-b-2 border-receiptInputBorder
                  flex
                  items-start
                "
              >
                {{ date }}
              </div>
            </div>
          </div>
          <div class="grid grid-rows-1 place-items-start w-full mb-14">
            <div class="flex w-full relative mb-12">
              <h1
                class="
                  font-poppins
                  text-lg
                  font-medium
                  text-receiptTextColor
                  left-0
                  absolute
                "
              >
                Received with Thanks From
              </h1>
              <div
                type="text"
                class="
                  px-4
                  h-10
                  py-1
                  bg-transparent
                  border-b-2 border-receiptInputBorder
                  w-9/12
                  right-0
                  absolute
                  flex
                  items-start
                "
              >
                {{ name }}
              </div>
            </div>
            <div class="flex item-start w-full">
              <h1
                class="font-poppins text-lg font-medium text-receiptTextColor"
              >
                Address
              </h1>
              <div
                type="text"
                class="
                  px-4
                  h-10
                  py-1
                  bg-transparent
                  border-b-2 border-receiptInputBorder
                  w-full
                  flex
                  items-start
                "
              >
                {{ address }}
              </div>
            </div>
            <div class="flex item-start w-full relative mb-12">
              <h1
                class="
                  font-poppins
                  text-lg
                  font-medium
                  text-receiptTextColor
                  left-0
                  absolute
                "
              >
                Payment Purpose
              </h1>
              <div
                type="text"
                class="
                  px-4
                  h-10
                  py-1
                  bg-transparent
                  border-b-2 border-receiptInputBorder
                  right-0
                  absolute
                  flex
                  items-start
                  w-10/12
                "
              >
                {{ batchId }}
              </div>
            </div>

            <div class="grid grid-cols-3 w-full gap-3 mb-12">
              <div class="flex relative">
                <h1
                  class="
                    font-poppins
                    text-lg
                    font-medium
                    text-receiptTextColor
                    left-0
                    absolute
                  "
                >
                  Payment Method
                </h1>

                <div
                  type="text"
                  class="
                    px-4
                    h-10
                    py-1
                    bg-transparent
                    border-b-2 border-receiptInputBorder
                    right-0
                    absolute
                    w-1/2
                    flex
                    items-start
                  "
                >
                  {{ paymentMethod }}
                </div>
              </div>
              <div class="flex relative">
                <h1
                  class="
                    font-poppins
                    text-lg
                    font-medium
                    text-receiptTextColor
                    left-0
                    absolute
                  "
                >
                  Check/Ref No.
                </h1>
                <div
                  type="text"
                  class="
                    px-4
                    h-10
                    py-1
                    bg-transparent
                    border-b-2 border-receiptInputBorder
                    right-0
                    absolute
                    w-2/3
                    flex
                    items-start
                  "
                >
                  {{ checkRefNo }}
                </div>
              </div>
              <div class="flex w-full relative">
                <h1
                  class="
                    font-poppins
                    text-lg
                    font-medium
                    text-receiptTextColor
                    left-0
                    absolute
                  "
                >
                  Check Date
                </h1>
                <div
                  class="
                    px-4
                    h-10
                    py-1
                    bg-transparent
                    border-b-2 border-receiptInputBorder
                    w-2/3
                    right-0
                    absolute
                    flex
                    items-start
                  "
                >
                  {{ checkDate }}
                </div>
              </div>
            </div>

            <div class="flex item-start w-full">
              <h1
                class="font-poppins text-lg font-medium text-receiptTextColor"
              >
                Amount
              </h1>

              <div
                type="text"
                class="
                  px-4
                  h-10
                  py-1
                  bg-transparent
                  border-b-2 border-receiptInputBorder
                  w-full
                  flex
                  items-start
                "
              >
                {{ totalFee }}
              </div>
            </div>

            <div class="flex w-full relative mb-12">
              <h1
                class="
                  font-poppins
                  text-lg
                  font-medium
                  text-receiptTextColor
                  left-0
                  absolute
                "
              >
                Amount in Word
              </h1>
              <div
                type="text"
                class="
                  px-4
                  h-10
                  py-1
                  bg-transparent
                  border-b-2 border-receiptInputBorder
                  w-10/12
                  right-0
                  absolute
                  flex
                  items-start
                "
              >
                {{ amountInWords }}
              </div>
            </div>
            <div class="grid grid-cols-2 w-full gap-2">
              <div class="flex relative">
                <label
                  class="
                    font-poppins
                    text-lg
                    font-medium
                    text-receiptTextColor
                    left-0
                    absolute
                  "
                >
                  Previous Receipt No.(If Any)
                </label>

                <div
                  type="text"
                  class="
                    px-4
                    h-10
                    py-1
                    bg-transparent
                    border-b-2 border-receiptInputBorder
                    right-0
                    absolute
                    w-1/2
                    flex
                    items-start
                    gap-2
                  "
                >
                  {{ prevReceipts }}
                  <!-- <div
                    v-for="(receipt, index) in previousReceipts"
                    :key="index"
                  >
                    {{ receipt }}
                  </div> -->
                </div>
              </div>
              <div class="flex relative">
                <label
                  class="
                    font-poppins
                    text-lg
                    font-medium
                    text-receiptTextColor
                    left-0
                    absolute
                  "
                >
                  Due Amount
                </label>
                <div
                  type="text"
                  class="
                    px-4
                    h-10
                    py-1
                    bg-transparent
                    border-b-2 border-receiptInputBorder
                    right-0
                    absolute
                    w-3/4
                    flex
                    items-start
                  "
                >
                  {{ dueFee }}
                </div>
              </div>
            </div>
          </div>
          <div class="flex justify-between mb-5">
            <div class="flex items-center gap-3">
              <p class="text-receiptBorder text-xs">
                {{ officeAddress }}
              </p>
              <p class="text-receiptBorder text-xs">|</p>

              <p class="text-receiptBorder text-xs">
                {{ officeEmail }}
              </p>
              <p class="text-receiptBorder text-xs">|</p>

              <p class="text-receiptBorder text-xs">
                {{ officePhone }}
              </p>
            </div>
            <div>
              <div class="flex justify-center">
                <img
                  src="../../assets/images/nihalvaiasign.png"
                  alt=""
                  class="w-20 h-10"
                />
              </div>
              <h1
                class="
                  border-t-2 border-receiptInputBorder
                  text-sm text-receiptTextColor
                  font-semibold
                "
              >
                Authorized Signature
              </h1>
            </div>
          </div>
        </div>
        <div class="grid grid-cols-2">
          <h1 class="border-t-8 border-receiptTextColor"></h1>
          <h1 class="border-t-8 border-receiptBorder"></h1>
        </div>
      </div>
      <!-- Money Receipt end -->
    </div>
  </div>
  <button
    class="px-4 py-2 bg-blue-200 rounded-md text-xl hover:bg-blue-300 my-10"
    @click="downloadReceipt"
  >
    Download receipt
  </button>
  <button
    class="bg-green-200 px-4 py-2 rounded-md hover:bg-green-300 m-20 text-xl"
    @click="clearDue"
  >
    Clear Due
  </button>
</template>

<script>
import moment from "moment";
import numberToWords from "number-to-words";
import jsPDF from "jspdf";
import html2canvas from "html2canvas";

export default {
  data() {
    return {
      customerTypes: [
        { id: 1, type: "Retail" },
        { id: 2, type: "Corporate" },
      ],
      customerType: "",
      date: "",
      officeAddress: "H# B-160,New DOHS Mohakhali,Dhaka-1206",
      officeEmail: "training@tecognize.com",
      officePhone: "+8801893466660",
      checkDate: "N/A",
      showCheckDate: false,
      paymentMethodList: [
        { id: 1, name: "bkash" },
        { id: 2, name: "nagad" },
        { id: 3, name: "cash" },
        { id: 4, name: "exim bank" },
        { id: 5, name: "dbbl" },
        { id: 6, name: "check" },
      ],
      paymentMethod: "",
      checkRefNo: "",
      phone: "",
      name: "",
      custid: "",
      batchId: "",
      totalFee: 0,
      regularFee: 0,
      installment1: 0,
      installment2: 0,
      installment3: 0,
      installment4: 0,
      dueFee: 0,
      instId: "",
      userId: "",
      address: "",
      batchList: [],
      amountInWords: "",
      previousReceipts: [],
      prevCustTotalFee: "",
      prevCustDueFee: "",
      prevCustPaidFee: "",
      prevDueFee: "",
      corpUnits: "",
      tempBatchList: [],
      tempRecords: [],
      prevReceipts: "",
    };
  },

  mounted() {
    this.$store.dispatch("getRetailCustomerList");
    this.$store.dispatch("getCorporateCustomerList");
    this.$store.dispatch("getSaleList");
    this.$store.dispatch("getSaleId");
    this.date = this.getDate();
  },

  methods: {
    getDate: function () {
      return moment(String(new Date().toLocaleDateString())).format(
        "YYYY-MM-DD"
      );
    },

    toggleCheckDate() {
      if (this.paymentMethod == "check") {
        this.showCheckDate = true;
      } else {
        this.showCheckDate = false;
      }
    },

    filterCustomerAndBatch() {
      if (this.customerType == this.customerTypes[0].type) {
        this.retailCustomerList.filter((customer) => {
          if (customer.cust_phone == this.phone) {
            this.name = customer.cust_name;
            this.custid = customer.cust_id;
            this.address = customer.cust_address;
            this.prevCustTotalFee = customer.cust_total_fee;
            this.prevCustPaidFee = customer.cust_paid_fee;
            this.prevCustDueFee = customer.cust_due_fee;
          }
        });

        this.tempBatchList = [];
        this.tempRecords = [];

        this.saleList.filter((record) => {
          if (record.cust_id == this.custid) {
            this.tempRecords.push(record);
            if (!this.tempBatchList.includes(record.batch_id)) {
              this.tempBatchList.push(record.batch_id);
            }
          }
        });
      } else {
        this.corporateCustomerList.filter((customer) => {
          if (customer.corp_phone == this.phone) {
            this.name = customer.corp_name;
            this.custid = customer.corp_id;
            this.address = customer.corp_address;
            this.prevCustTotalFee = customer.corp_total_fee;
            this.prevCustPaidFee = customer.corp_paid_fee;
            this.prevCustDueFee = customer.corp_due_fee;
            this.corpUnits = customer.corp_units;
          }
        });

        this.tempBatchList = [];
        this.tempRecords = [];

        this.saleList.filter((record) => {
          if (record.corp_id == this.custid) {
            this.tempRecords.push(record);
            if (!this.tempBatchList.includes(record.batch_id)) {
              this.tempBatchList.push(record.batch_id);
            }
          }
        });

        // let tempBatchList = [];
        // this.batchList = [];
        // this.saleList.filter((record) => {
        //   if (record.corp_id == this.custid) {
        //     if (!tempBatchList.includes(record)) {
        //       tempBatchList.push(record);
        //     }
        //   }

        //   tempBatchList.filter((batch) => {
        //     let due = 9007199254740991;
        //     this.saleList.filter((record) => {
        //       if (record.batch_id == batch.batch_id) {
        //         if (record.due_fee < due) {
        //           due = record.due_fee;
        //         }
        //       }
        //     });
        //     console.log(due);
        //     if (due != 0 && !this.batchList.includes(batch))
        //       this.batchList.push(batch);
        //   });
        // });

        // this.saleList.filter((record) => {
        //   if (record.corp_id == this.custid) {
        //     if (!this.batchList.includes(record)) {
        //       this.batchList.push(record);
        //     }
        //   }
        // });
      }
    },

    setFees() {
      this.previousReceipts = [];
      this.prevReceipts = "";
      this.tempRecords.filter((record) => {
        if (record.batch_id == this.batchId) {
          this.totalFee = record.sale_fee;
          this.installment1 = record.installment1;
          if (record.installment2 > 0) {
            this.installment2 = record.installment2;
          }
          if (record.installment3 > 0) {
            this.installment3 = record.installment3;
          }
          if (record.installment4 > 0) {
            this.installment4 = record.installment4;
          }
          this.regularFee = record.regular_fee;
          this.instId = record.inst_id;
          this.userId = record.user_id;
          this.previousReceipts.push(record.id);
          this.prevReceipts = this.prevReceipts + " " + String(record.id);
        }
      });

      this.prevDueFee =
        this.totalFee -
        (this.installment1 +
          this.installment2 +
          this.installment3 +
          this.installment4);

      this.amountInWords =
        numberToWords.toWords(this.totalFee).toUpperCase() + " TAKA";

      // this.totalFee = this.batchId.sale_fee;
      // this.installment1 = this.batchId.installment1;
      // this.installment2 = this.batchId.installment2;
      // this.installment3 = this.batchId.installment3;
      // this.installment4 = this.batchId.installment4;
      // this.regularFee = this.batchId.regular_fee;
      // this.dueFee = this.batchId.due_fee;
      // this.instId = this.batchId.inst_id;
      // this.userId = this.batchId.user_id;
      // this.prevDueFee = this.batchId.due_fee;
      // this.amountInWords =
      //   numberToWords.toWords(this.totalFee).toUpperCase() + " TAKA";
      // this.previousReceipts = [];
      // this.saleList.filter((record) => {
      //   if (record.batch_id == this.batchId.batch_id) {
      //     if (this.customerType == this.customerTypes[0].type) {
      //       if (record.cust_id == this.custid) {
      //         this.previousReceipts.push(record.id);
      //       }
      //     } else {
      //       if (record.corp_id == this.custid) {
      //         this.previousReceipts.push(record.id);
      //       }
      //     }
      //   }
      // });

      // this.totalFee = this.batchId.sale_fee;
      // this.installment1 = this.batchId.installment1;
      // this.installment2 = this.batchId.installment2;
      // this.installment3 = this.batchId.installment3;
      // this.installment4 = this.batchId.installment4;
      // this.regularFee = this.batchId.regular_fee;
      // this.dueFee = this.batchId.due_fee;
      // this.instId = this.batchId.inst_id;
      // this.userId = this.batchId.user_id;
      // this.prevDueFee = this.batchId.due_fee;
      // this.amountInWords =
      //   numberToWords.toWords(this.totalFee).toUpperCase() + " TAKA";
      // this.previousReceipts = [];
      // this.saleList.filter((record) => {
      //   if (record.batch_id == this.batchId.batch_id) {
      //     if (this.customerType == this.customerTypes[0].type) {
      //       if (record.cust_id == this.custid) {
      //         this.previousReceipts.push(record.id);
      //       }
      //     } else {
      //       if (record.corp_id == this.custid) {
      //         this.previousReceipts.push(record.id);
      //       }
      //     }
      //   }
      // });
    },

    downloadReceipt() {
      const doc = new jsPDF({
        orientation: "l",
        unit: "px",
        format: "a4",
        hotfixes: ["px_scaling"],
      });

      html2canvas(this.$refs.retailReceiptContent, {
        width: doc.internal.pageSize.getWidth(),
        height: doc.internal.pageSize.getHeight(),
      }).then((canvas) => {
        const img = canvas.toDataURL("image/png");

        doc.addImage(
          img,
          "PNG",
          0,
          0,
          doc.internal.pageSize.getWidth(),
          doc.internal.pageSize.getHeight()
        );
        let filename =
          this.name +
          "_" +
          this.batchId +
          "_" +
          new Date().toLocaleDateString() +
          "_" +
          new Date().toLocaleTimeString() +
          ".pdf";
        doc.save(filename);
      });
    },

    clearDue() {
      if (this.customerType == this.customerTypes[0].type) {
        const custData = {
          cust_id: this.custid,
          cust_total_fee: this.prevCustTotalFee,
          cust_paid_fee: this.prevCustPaidFee + (this.prevDueFee - this.dueFee),
          cust_due_fee: this.prevCustDueFee - (this.prevDueFee - this.dueFee),
        };

        this.$store.dispatch("updateRetailCustomerFees", custData);
        if (this.checkDate == "N/A") this.checkDate = this.date;

        const saleData = {
          id: this.saleid[0] + 1,
          batch_id: this.batchId,
          regular_fee: this.regularFee,
          sale_fee: this.totalFee,
          installment1: this.installment1,
          installment2: this.installment2,
          installment3: this.installment3,
          installment4: this.installment4,
          due_fee: this.dueFee,
          inst_id: this.instId,
          user_id: this.userId,
          cust_id: this.custid,
          corp_id: "",
          pay_method: this.paymentMethod,
          check_ref_no: this.checkRefNo,
          curr_date: this.date,
          check_date: this.checkDate,
          name: this.name,
          address: this.address,
          prev_receipts: this.prevReceipts,
        };
        this.$store.dispatch("addSaleRecord", saleData);
      } else {
        const corpData = {
          corp_id: this.custid,
          corp_total_fee: this.prevCustTotalFee,
          corp_paid_fee: this.prevCustPaidFee + (this.prevDueFee - this.dueFee),
          corp_due_fee: this.prevCustDueFee - (this.prevDueFee - this.dueFee),
          corp_units: this.corpUnits,
        };

        this.$store.dispatch("updateCorporateCustomerFees", corpData);
        if (this.checkDate == "N/A") this.checkDate = this.date;

        const saleData = {
          id: this.saleid[0] + 1,
          batch_id: this.batchId,
          regular_fee: this.regularFee,
          sale_fee: this.totalFee,
          installment1: this.installment1,
          installment2: this.installment2,
          installment3: this.installment3,
          installment4: this.installment4,
          due_fee: this.dueFee,
          inst_id: this.instId,
          user_id: this.userId,
          cust_id: "",
          corp_id: this.custid,
          pay_method: this.paymentMethod,
          check_ref_no: this.checkRefNo,
          curr_date: this.date,
          check_date: this.checkDate,
          name: this.name,
          address: this.address,
          prev_receipts: this.prevReceipts,
        };
        this.$store.dispatch("addSaleRecord", saleData);
      }
      window.location.reload();
    },
  },

  computed: {
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

    saleList: {
      get() {
        return this.$store.getters.saleList;
      },
    },

    saleid: {
      get() {
        return this.$store.getters.saleid;
      },
    },

    getDue() {
      if (this.totalFee) {
        this.dueFee =
          this.totalFee -
          (this.installment1 +
            this.installment2 +
            this.installment3 +
            this.installment4);
      } else {
        this.dueFee = 0;
      }
      return this.dueFee;
    },
  },
};
</script>