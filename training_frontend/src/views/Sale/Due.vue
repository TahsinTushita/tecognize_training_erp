<template>
  <h1 class="pt-10 text-xl font-semibold">Due</h1>
  <div class="flex items-center justify-center mb-20">
    <form @submit.prevent="false">
      <div class="space-y-5">
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
            >Cheque/Ref No.*</label
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
          <label for="checkDate" class="font-semibold ml-2">Cheque Date*</label>
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
            @change="filterCustomer"
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
            v-model="customer.cust_name"
          />
        </div>
        <div class="grid grid-rows-1 gap-2 place-items-start">
          <label for="batch" class="font-semibold ml-2">Batch*</label>
          <select
            name="batch"
            id="batch"
            v-model="record"
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
            <!-- <option
              v-for="(batch, index) in tempBatchList"
              :value="batch"
              :key="index"
            >
              {{ batch }}
            </option> -->

            <option
              v-for="record in saleCustomerBatchList"
              :value="record"
              :key="record.id"
            >
              {{ record.course_name }} {{ record.batch_num }}
            </option>
          </select>
        </div>

        <div class="grid grid-rows-1 gap-2 place-items-start">
          <label for="paymentMethod" class="font-semibold ml-2"
            >Installment Number*</label
          >
          <select
            name="paymentMethod"
            id="paymentMethod"
            v-model="installment"
            required
            @change="enableInstallmentField"
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
              v-for="(number, index) in installmentNumber"
              :value="number"
              :key="index"
            >
              {{ number }}
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
            :disabled="installment2Disabled"
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
            :disabled="installment3Disabled"
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
            :disabled="installment4Disabled"
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
              <p class="text-black font-medium">{{ slNo }}</p>
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
                {{ customer.cust_name }}
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
                {{ customer.cust_address }}
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
                {{ record.course_name }} ({{ record.batch_num }})
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
                  Cheque/Ref No.
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
                    w-7/12
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
                  Cheque Date
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

            <div class="flex relative mb-12 w-full">
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
                Total Amount
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
                {{ totalFee }}
              </div>
            </div>

            <div class="flex relative mb-12 w-full">
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
                Paid Amount
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
                {{ getPaidAmount }}
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
                {{ getAmountInWords }}
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
        { id: 6, name: "cheque" },
      ],
      paymentMethod: "",
      checkRefNo: "",
      phone: "",
      name: "",
      custid: "",
      batchId: "",
      totalFee: 0,
      regularFee: 0,
      installment: "",
      installment1: 0,
      installment2: 0,
      installment3: 0,
      installment4: 0,
      installment2Disabled: true,
      installment3Disabled: true,
      installment4Disabled: true,
      dueFee: 0,
      instId: "",
      instProfit: "",
      userId: "",
      address: "",
      batchList: [],
      amountInWords: "",
      previousReceipts: [],
      prevCustTotalFee: "",
      prevCustDueFee: "",
      prevCustPaidFee: "",
      prevDueFee: "",
      custUnits: "",
      tempBatchList: [],
      tempRecords: [],
      prevReceipts: "",
      installmentNumber: ["2nd", "3rd", "4th"],
      mrNo1: "",
      mrNo2: "",
      mrNo3: "",
      mrNo4: "",
      slNo: "",
      date2: null,
      date3: null,
      date4: null,
      checkDate2: null,
      checkDate3: null,
      checkDate4: null,
      payMode2: null,
      payMode3: null,
      payMode4: null,
      id: "",
      checkRefNo2: null,
      checkRefNo3: null,
      checkRefNo4: null,
      paidFee: 0,
      record: "",
    };
  },

  mounted() {
    let var1 = "None";
    // this.$store.dispatch("getRetailCustomerList");
    // this.$store.dispatch("getSaleList");
    this.$store.dispatch("getSaleId");
    this.$store.dispatch("getInstructorTotal", var1);
    this.date = this.getDate();
  },

  methods: {
    getDate: function () {
      return moment(String(new Date().toLocaleDateString())).format(
        "YYYY-MM-DD"
      );
    },

    toggleCheckDate() {
      if (this.paymentMethod == "cheque") {
        this.showCheckDate = true;
      } else {
        this.showCheckDate = false;
      }
    },

    async filterCustomer() {
      // this.retailCustomerList.filter((customer) => {
      //   if (customer.cust_phone == this.phone) {
      // this.name = customer.cust_name;
      // this.custid = customer.cust_id;
      // this.address = customer.cust_address;
      // this.prevCustTotalFee = customer.cust_total_fee;
      // this.prevCustPaidFee = customer.cust_paid_fee;
      // this.prevCustDueFee = customer.cust_due_fee;
      // this.custUnits = customer.cust_units;
      //   }
      // });

      // this.tempBatchList = [];
      // this.tempRecords = [];

      // this.saleList.filter((record) => {
      //   if (record.cust_id == this.custid) {
      //     this.tempRecords.push(record);
      //     if (!this.tempBatchList.includes(record.batch_num)) {
      //       this.tempBatchList.push(record.batch_num);
      //     }
      //   }
      // });

      await this.$store.dispatch("getCustomerByPhone", this.phone);
      this.$store.dispatch("getSaleCustomerBatchList", this.customer.cust_id);

      // this.name = retailCustomer.cust_name;

      this.setCustomerInfo();
    },

    setCustomerInfo() {
      this.name = this.customer.cust_name;
      this.custid = this.customer.cust_id;
      this.address = this.customer.cust_address;
      this.prevCustTotalFee = this.customer.cust_total_fee;
      this.prevCustPaidFee = this.customer.cust_paid_fee;
      this.prevCustDueFee = this.customer.cust_due_fee;
      this.custUnits = this.customer.cust_units;
    },

    setFees() {
      this.previousReceipts = [];
      this.prevReceipts = "";
      this.saleCustomerBatchList.filter((record) => {
        if (record.batch_id == this.record.batch_id) {
          this.id = record.id;
          this.totalFee = record.batch_fee;
          this.installment1 = record.installment1;

          this.installment2 = record.installment2;

          this.installment3 = record.installment3;
          this.installment4 = record.installment4;
          this.regularFee = record.regular_fee;
          this.instId = record.inst_id;
          this.instProfit = record.inst_profit;
          this.userId = record.user_id;
          this.prevReceipts = this.prevReceipts + String(record.mr_no1);
          this.mrNo1 = record.mr_no1;
          this.mrNo2 = record.mr_no2;
          this.mrNo3 = record.mr_no3;
          this.mrNo4 = record.mr_no4;
          this.date2 = record.date2;
          this.date3 = record.date3;
          this.date4 = record.date4;
          this.checkDate2 = record.check_date2;
          this.checkDate3 = record.check_date3;
          this.checkDate4 = record.check_date4;
          this.payMode2 = record.pay_mode2;
          this.payMode3 = record.pay_mode3;
          this.payMode4 = record.pay_mode4;
          this.checkRefNo2 = record.check_ref_no2;
          this.checkRefNo3 = record.check_ref_no3;
          this.checkRefNo4 = record.check_ref_no4;
          this.$store.dispatch("getInstructorTotal", record.inst_id);
        }
      });

      this.prevDueFee =
        this.totalFee -
        (this.installment1 +
          this.installment2 +
          this.installment3 +
          this.installment4);

      // this.amountInWords =
      //   numberToWords.toWords(this.totalFee).toUpperCase() + " TAKA";
    },

    enableInstallmentField() {
      if (this.installment == "2nd") {
        this.installment2Disabled = false;
        this.slNo = this.mrNo2;
      } else if (this.installment == "3rd") {
        this.installment3Disabled = false;
        this.prevReceipts = this.prevReceipts + "," + this.mrNo2;
        this.slNo = this.mrNo3;
      } else if (this.installment == "4th") {
        this.installment4Disabled = false;
        this.prevReceipts =
          this.prevReceipts + "," + this.mrNo2 + "," + this.mrNo3;
        this.slNo = this.mrNo4;
      }
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
          this.customer.cust_name +
          "_E_money_receipt_of_" +
          this.record.course_name +
          "_" +
          this.record.batch_num +
          ".pdf";
        doc.save(filename);
      });
    },

    clearDue() {
      if (this.checkDate == "N/A") this.checkDate = null;

      if (this.installment == "2nd") {
        this.date2 = this.date;
        this.checkDate2 = this.checkDate;
        this.checkRefNo2 = this.checkRefNo;
        this.payMode2 = this.paymentMethod;
      } else if (this.installment == "3rd") {
        this.date3 = this.date;
        this.checkDate3 = this.checkDate;
        this.checkRefNo3 = this.checkRefNo;
        this.payMode3 = this.paymentMethod;
      } else if (this.installment == "4th") {
        this.date4 = this.date;
        this.checkDate4 = this.checkDate;
        this.checkRefNo4 = this.checkRefNo;
        this.payMode4 = this.paymentMethod;
      }

      const custData = {
        cust_total_fee: this.prevCustTotalFee,
        cust_paid_fee: this.prevCustPaidFee + (this.prevDueFee - this.dueFee),
        cust_due_fee: this.prevCustDueFee - (this.prevDueFee - this.dueFee),
        cust_units: this.custUnits,
        cust_id: this.custid,
      };

      this.$store.dispatch("updateCustomerFees", custData);

      const saleData = {
        installment2: this.installment2,
        date2: this.date2,
        check_date2: this.checkDate2,
        check_ref_no2: this.checkRefNo2,
        pay_mode2: this.payMode2,
        installment3: this.installment3,
        date3: this.date3,
        check_date3: this.checkDate3,
        check_ref_no3: this.checkRefNo3,
        pay_mode3: this.payMode3,
        installment4: this.installment4,
        date4: this.date4,
        check_date4: this.checkDate4,
        check_ref_no4: this.checkRefNo4,
        pay_mode4: this.payMode4,
        paid:
          this.installment1 +
          this.installment2 +
          this.installment3 +
          this.installment4,
        due:
          this.totalFee -
          (this.installment1 +
            this.installment2 +
            this.installment3 +
            this.installment4),
        id: this.id,
      };
      const instData = {
        inst_payable:
          this.instructorTotal.inst_payable +
          ((this.prevDueFee - this.dueFee) * this.instProfit) / 100,
        inst_paid: this.instructorTotal.inst_paid,
        inst_due:
          this.instructorTotal.inst_due +
          ((this.prevDueFee - this.dueFee) * this.instProfit) / 100,
        inst_id: this.instId,
      };
      this.$store.dispatch("updateSaleRecord", saleData);
      this.$store.dispatch("updateInstructorFee", instData);

      window.location.reload();
    },
  },

  computed: {
    // retailCustomerList: {
    //   get() {
    //     return this.$store.getters.retailCustomerList;
    //   },
    // },

    customer: {
      get() {
        return this.$store.getters.customer;
      },
    },

    saleCustomerBatchList: {
      get() {
        return this.$store.getters.saleCustomerBatchList;
      },
    },

    // saleList: {
    //   get() {
    //     return this.$store.getters.saleList;
    //   },
    // },

    saleid: {
      get() {
        return this.$store.getters.saleid;
      },
    },

    receipt4: {
      get() {
        return this.$store.getters.receipt4;
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

    getPaidAmount() {
      if (this.installment == "2nd") {
        this.paidFee = this.installment2;
      } else if (this.installment == "3rd") {
        this.paidFee = this.installment3;
      } else if (this.installment == "4th") {
        this.paidFee = this.installment4;
      } else {
        this.paidFee = 0;
      }
      return this.paidFee;
    },

    getAmountInWords() {
      // if (this.installment == "2nd") {
      //   this.amountInWords =
      //     numberToWords.toWords(this.installment2).toUpperCase() + " TAKA";
      // } else if (this.installment == "3rd") {
      //   this.amountInWords =
      //     numberToWords.toWords(this.installment3).toUpperCase() + " TAKA";
      // } else if (this.installment == "4th") {
      //   this.amountInWords =
      //     numberToWords.toWords(this.installment4).toUpperCase() + " TAKA";
      // } else {
      //   this.amountInWords = "";
      // }
      this.amountInWords =
        numberToWords.toWords(this.paidFee).toUpperCase() + " TAKA";

      return this.amountInWords;
    },

    instructorTotal: {
      get() {
        return this.$store.getters.instructorTotal;
      },
    },
  },
};
</script>