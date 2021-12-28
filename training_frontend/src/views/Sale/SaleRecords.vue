<template>
  <h1 class="pt-10 text-xl font-semibold">Sale Records</h1>
  <div>
    <div class="flex justify-center">
      <!-- Money receipt -->
      <div ref="receiptContent">
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
                <h1
                  class="font-segoeUI text-xl font-bold text-receiptTextColor"
                >
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
                  {{ paymentPurpose }}
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
                  {{ amount }}
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
                    <!-- <div v-for="(receipt, index) in previousReceipts" :key="index">
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
                    {{ due }}
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
      </div>
      <!-- Money receipt end-->
    </div>
    <button
      class="
        px-4
        py-2
        rounded-md
        bg-green bg-green-200
        hover:bg-green-300
        my-10
      "
      @click="downloadReceipt"
    >
      Download receipt
    </button>
  </div>
  <div class="flex items-start">
    <div class="grid grid-rows-1 gap-2 place-items-start m-10">
      <label for="batchId" class="font-semibold ml-2">Batch*</label>
      <select
        name="batchId"
        id="batchId"
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
        @change="filterByBatch"
      >
        <option value="None">None</option>
        <option
          v-for="batch in batchIds"
          :value="batch.batch_id"
          :key="batch.batch_id"
        >
          {{ batch.batch_id }}
        </option>
      </select>
    </div>
    <table class="m-10">
      <title>Instructor</title>
      <thead>
        <th class="px-4 py-4 text-center border-2">ID</th>
        <th class="px-4 py-4 text-center border-2">Name</th>
        <th class="px-4 py-4 text-center border-2">Percentage</th>
        <th class="px-4 py-4 text-center border-2">Fee</th>
      </thead>
      <tbody v-if="instructorPercentages.length">
        <tr
          v-for="instructor in instructorPercentages"
          :key="instructor.inst_id"
          class="hover:bg-gray-100"
        >
          <td class="px-4 py-4 text-center border-2">
            {{ instructor.inst_id }}
          </td>
          <td class="px-4 py-4 text-center border-2">
            {{ instructor.inst_name }}
          </td>
          <td class="px-4 py-4 text-center border-2">
            {{ instructor.inst_profit }}
          </td>
          <td class="px-4 py-4 text-center border-2">
            {{ instructor.inst_fee }}
          </td>
        </tr>
      </tbody>
    </table>
  </div>
  <table class="m-10">
    <thead>
      <tr>
        <th class="px-4 py-4 text-center border-2">Serial</th>
        <th class="px-4 py-4 text-center border-2">Participants ID</th>
        <th class="px-4 py-4 text-center border-2">Name</th>
        <th class="px-4 py-4 text-center border-2">Email</th>
        <th class="px-4 py-4 text-center border-2">Phone</th>
        <th class="px-4 py-4 text-center border-2">Address</th>
        <th class="px-4 py-4 text-center border-2">Organization</th>
        <th class="px-4 py-4 text-center border-2">Designation</th>
        <th class="px-4 py-4 text-center border-2">Registered Course</th>
        <th class="px-4 py-4 text-center border-2">Batch Fee</th>
        <th class="px-4 py-4 text-center border-2">1st Installment</th>
        <th class="px-4 py-4 text-center border-2">MR No.</th>
        <th class="px-4 py-4 text-center border-2">Date</th>
        <th class="px-4 py-4 text-center border-2">Payment Method</th>
        <th class="px-4 py-4 text-center border-2">2nd Installment</th>
        <th class="px-4 py-4 text-center border-2">MR No.</th>
        <th class="px-4 py-4 text-center border-2">Date</th>
        <th class="px-4 py-4 text-center border-2">Pay Mode</th>
        <th class="px-4 py-4 text-center border-2">3rd Installment</th>
        <th class="px-4 py-4 text-center border-2">MR No.</th>
        <th class="px-4 py-4 text-center border-2">Date</th>
        <th class="px-4 py-4 text-center border-2">Pay Mode</th>
        <th class="px-4 py-4 text-center border-2">4th Installment</th>
        <th class="px-4 py-4 text-center border-2">MR No.</th>
        <th class="px-4 py-4 text-center border-2">Date</th>
        <th class="px-4 py-4 text-center border-2">Pay Mode</th>
        <th class="px-4 py-4 text-center border-2">Total Paid</th>
        <th class="px-4 py-4 text-center border-2">Total Due</th>
        <th class="px-4 py-4 text-center border-2">User ID</th>
        <th class="px-4 py-4 text-center border-2">Remarks</th>
      </tr>
    </thead>
    <tbody v-if="saleCustomerList.length">
      <tr
        v-for="record in saleCustomerList"
        :key="record.id"
        class="hover:bg-gray-100"
      >
        <td class="px-4 py-4 text-center border-2">
          {{ record.id }}
        </td>
        <td class="px-4 py-4 text-center border-2">
          {{ record.cust_id }}
        </td>
        <td class="px-4 py-4 text-center border-2">
          {{ record.cust_name }}
        </td>
        <td class="px-4 py-4 text-sm text-center border-2">
          {{ record.cust_email }}
        </td>
        <td class="px-4 py-4 text-sm text-center border-2">
          {{ record.cust_phone }}
        </td>
        <td class="px-4 py-4 text-sm text-center border-2">
          {{ record.cust_address }}
        </td>
        <td class="px-4 py-4 text-sm text-center border-2">
          {{ record.cust_organization }}
        </td>
        <td class="px-4 py-4 text-sm text-center border-2">
          {{ record.cust_designation }}
        </td>
        <td class="px-4 py-4 text-sm text-center border-2">
          {{ record.batch_id }}
        </td>
        <td class="px-4 py-4 text-sm text-center border-2">
          {{ record.batch_fee }}
        </td>
        <td class="px-4 py-4 text-sm text-center border-2">
          {{ record.installment1 }}
        </td>
        <td class="px-4 py-4 text-sm text-center border-2">
          {{ record.mr_no1 }}
          <button
            class="p-2 bg-green bg-green-200 hover:bg-green-300 rounded-md mt-1"
            :name="mr1"
            @click="setData($event, record)"
          >
            Show receipt
          </button>
        </td>
        <td class="px-4 py-4 text-sm text-center border-2">
          {{ record.date1 }}
        </td>
        <td class="px-4 py-4 text-sm text-center border-2">
          {{ record.pay_mode1 }}
        </td>
        <td class="px-4 py-4 text-sm text-center border-2">
          {{ record.installment2 }}
        </td>
        <td class="px-4 py-4 text-sm text-center border-2">
          {{ record.mr_no2 }}
          <button
            class="p-2 bg-green bg-green-200 hover:bg-green-300 rounded-md mt-1"
            :name="mr2"
            @click="setData($event, record)"
          >
            Show receipt
          </button>
        </td>
        <td class="px-4 py-4 text-sm text-center border-2">
          {{ record.date2 }}
        </td>
        <td class="px-4 py-4 text-sm text-center border-2">
          {{ record.pay_mode2 }}
        </td>
        <td class="px-4 py-4 text-sm text-center border-2">
          {{ record.installment3 }}
        </td>
        <td class="px-4 py-4 text-sm text-center border-2">
          {{ record.mr_no3 }}
          <button
            class="p-2 bg-green bg-green-200 hover:bg-green-300 rounded-md mt-1"
            :name="mr3"
            @click="setData($event, record)"
          >
            Show receipt
          </button>
        </td>
        <td class="px-4 py-4 text-sm text-center border-2">
          {{ record.date3 }}
        </td>
        <td class="px-4 py-4 text-sm text-center border-2">
          {{ record.pay_mode3 }}
        </td>
        <td class="px-4 py-4 text-sm text-center border-2">
          {{ record.installment4 }}
        </td>
        <td class="px-4 py-4 text-sm text-center border-2">
          {{ record.mr_no4 }}
          <button
            class="p-2 bg-green bg-green-200 hover:bg-green-300 rounded-md mt-1"
            :name="mr4"
            @click="setData($event, record)"
          >
            Show receipt
          </button>
        </td>
        <td class="px-4 py-4 text-sm text-center border-2">
          {{ record.date4 }}
        </td>
        <td class="px-4 py-4 text-sm text-center border-2">
          {{ record.pay_mode4 }}
        </td>
        <td class="px-4 py-4 text-sm text-center border-2">
          {{ record.paid }}
        </td>
        <td class="px-4 py-4 text-sm text-center border-2">
          {{ record.due }}
        </td>
        <td class="px-4 py-4 text-sm text-center border-2">
          {{ record.user_id }}
        </td>
        <td class="px-4 py-4 text-sm text-center border-2">
          {{ record.remarks }}
        </td>
      </tr>
    </tbody>
  </table>
</template>

<script>
import numberToWords from "number-to-words";
import jsPDF from "jspdf";
import html2canvas from "html2canvas";

export default {
  data() {
    return {
      slNo: "",
      date: "",
      name: "",
      address: "",
      paymentPurpose: "",
      paymentMethod: "",
      checkRefNo: "",
      checkDate: "",
      amount: "",
      amountInWords: "",
      previousReceipts: [],
      due: "",
      officeAddress: "H# B-160,New DOHS Mohakhali,Dhaka-1206",
      officeEmail: "training@tecognize.com",
      officePhone: "+8801893466660",
      prevReceipts: "",
      mr1: "mr1",
      mr2: "mr2",
      mr3: "mr3",
      mr4: "mr4",
      batchId: "",
    };
  },

  mounted() {
    let batchId = "None";
    this.$store.dispatch("getSaleCustomerList", batchId);
    this.$store.dispatch("getInstructorPercentages", batchId);
    this.$store.dispatch("getBatchIds");
  },

  methods: {
    setData(event, record) {
      this.name = record.cust_name;
      this.address = record.cust_address;
      this.paymentPurpose = record.batch_id;
      this.amount = record.batch_fee;
      this.amountInWords =
        numberToWords.toWords(this.amount).toUpperCase() + " TAKA";

      if (event.target.name == this.mr1) {
        this.slNo = record.mr_no1;
        this.date = record.date1;
        this.paymentMethod = record.pay_mode1;
        this.checkRefNo = record.check_ref_no1;
        if (record.check_date1 == null) {
          this.checkDate = "N/A";
        } else {
          this.checkDate = record.check_date1;
        }
        this.prevReceipts = "N/A";
        this.due = record.batch_fee - record.installment1;
      } else if (event.target.name == this.mr2) {
        this.slNo = record.mr_no2;
        this.date = record.date2;
        this.paymentMethod = record.pay_mode2;
        this.checkRefNo = record.check_ref_no2;
        if (record.check_date2 == null) {
          this.checkDate = "N/A";
        } else {
          this.checkDate = record.check_date2;
        }
        this.prevReceipts = String(record.mr_no1);
        this.due =
          record.batch_fee - (record.installment1 + record.installment2);
      } else if (event.target.name == this.mr3) {
        this.slNo = record.mr_no3;
        this.date = record.date3;
        this.paymentMethod = record.pay_mode3;
        this.checkRefNo = record.check_ref_no3;
        if (record.check_date3 == null) {
          this.checkDate = "N/A";
        } else {
          this.checkDate = record.check_date3;
        }
        this.prevReceipts = String(record.mr_no1) + "," + String(record.mr_no2);
        this.due =
          record.batch_fee -
          (record.installment1 + record.installment2 + record.installment3);
      } else if (event.target.name == this.mr4) {
        this.slNo = record.mr_no4;
        this.date = record.date4;
        this.paymentMethod = record.pay_mode4;
        this.checkRefNo = record.check_ref_no4;
        if (record.check_date4 == null) {
          this.checkDate = "N/A";
        } else {
          this.checkDate = record.check_date4;
        }
        this.prevReceipts =
          String(record.mr_no1) +
          "," +
          String(record.mr_no2) +
          "," +
          String(record.mr_no3);
        this.due =
          record.batch_fee -
          (record.installment1 +
            record.installment2 +
            record.installment3 +
            record.installment4);
      }
    },

    filterByBatch() {
      this.$store.dispatch("getSaleCustomerList", this.batchId);
      this.$store.dispatch("getInstructorPercentages", this.batchId);
    },

    downloadReceipt() {
      const doc = new jsPDF({
        orientation: "l",
        unit: "px",
        format: "a4",
        hotfixes: ["px_scaling"],
      });

      html2canvas(this.$refs.receiptContent, {
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
          this.paymentPurpose +
          "_" +
          new Date().toLocaleDateString() +
          "_" +
          new Date().toLocaleTimeString() +
          ".pdf";
        doc.save(filename);
      });
    },
  },

  computed: {
    saleCustomerList: {
      get() {
        return this.$store.getters.saleCustomerList;
      },
    },

    batchIds: {
      get() {
        return this.$store.getters.batchIds;
      },
    },

    instructorPercentages: {
      get() {
        return this.$store.getters.instructorPercentages;
      },
    },
  },
};
</script>