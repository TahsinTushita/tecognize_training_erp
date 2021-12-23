<template>
  <h1 class="pt-10 text-xl font-semibold">Sale Records</h1>
  <table class="m-10">
    <thead>
      <tr>
        <th class="px-4 py-4 text-center border-2">ID</th>
        <th class="px-4 py-4 text-center border-2">Customer Name</th>
        <th class="px-4 py-4 text-center border-2">Previous Receipts</th>
        <th class="px-4 py-4 text-center border-2">Regular Fee</th>
        <th class="px-4 py-4 text-center border-2">Sale Fee</th>
        <th class="px-4 py-4 text-center border-2">Installment 1</th>
        <th class="px-4 py-4 text-center border-2">Installment 2</th>
        <th class="px-4 py-4 text-center border-2">Installment 3</th>
        <th class="px-4 py-4 text-center border-2">Installment 4</th>
        <th class="px-4 py-4 text-center border-2">Due Fee</th>
        <th class="px-4 py-4 text-center border-2">Payment Method</th>
        <th class="px-4 py-4 text-center border-2">Check/Ref No.</th>
        <th class="px-4 py-4 text-center border-2">Date</th>
        <th class="px-4 py-4 text-center border-2">Check Date</th>
        <th class="px-4 py-4 text-center border-2">Batch</th>
        <th class="px-4 py-4 text-center border-2">Corporate ID</th>
        <th class="px-4 py-4 text-center border-2">Customer ID</th>
        <th class="px-4 py-4 text-center border-2">Instructor ID</th>
        <th class="px-4 py-4 text-center border-2">User ID</th>
        <th class="px-4 py-4 text-center border-2">Receipt</th>
      </tr>
    </thead>
    <tbody v-if="saleList.length">
      <tr v-for="record in saleList" :key="record.id" class="hover:bg-gray-100">
        <td class="px-4 py-4 text-center border-2">
          {{ record.id }}
        </td>
        <td class="px-4 py-4 text-center border-2">
          {{ record.name }}
        </td>
        <td class="px-4 py-4 text-center border-2">
          {{ record.prev_receipts }}
        </td>
        <td class="px-4 py-4 text-sm text-center border-2">
          {{ record.regular_fee }}
        </td>
        <td class="px-4 py-4 text-sm text-center border-2">
          {{ record.sale_fee }}
        </td>
        <td class="px-4 py-4 text-sm text-center border-2">
          {{ record.installment1 }}
        </td>
        <td class="px-4 py-4 text-sm text-center border-2">
          {{ record.installment2 }}
        </td>
        <td class="px-4 py-4 text-sm text-center border-2">
          {{ record.installment3 }}
        </td>
        <td class="px-4 py-4 text-sm text-center border-2">
          {{ record.installment4 }}
        </td>
        <td class="px-4 py-4 text-sm text-center border-2">
          {{ record.due_fee }}
        </td>
        <td class="px-4 py-4 text-sm text-center border-2">
          {{ record.pay_method }}
        </td>
        <td class="px-4 py-4 text-sm text-center border-2">
          {{ record.check_ref_no }}
        </td>
        <td class="px-4 py-4 text-sm text-center border-2">
          {{ record.curr_date }}
        </td>
        <td class="px-4 py-4 text-sm text-center border-2">
          {{ record.check_date }}
        </td>
        <td class="px-4 py-4 text-sm text-center border-2">
          {{ record.batch_id }}
        </td>
        <td class="px-4 py-4 text-sm text-center border-2">
          {{ record.corp_id }}
        </td>
        <td class="px-4 py-4 text-sm text-center border-2">
          {{ record.cust_id }}
        </td>
        <td class="px-4 py-4 text-sm text-center border-2">
          {{ record.inst_id }}
        </td>
        <td class="px-4 py-4 text-sm text-center border-2">
          {{ record.user_id }}
        </td>
        <td class="text-sm px-2 border-2">
          <button
            class="py-2 bg-green bg-green-200 hover:bg-green-300"
            @click="setReceiptData(record)"
          >
            Download receipt
          </button>
        </td>
      </tr>
    </tbody>
  </table>

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
            <h1 class="font-poppins text-lg font-medium text-receiptTextColor">
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
            <h1 class="font-poppins text-lg font-medium text-receiptTextColor">
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
    };
  },

  mounted() {
    this.$store.dispatch("getSaleList");
    this.$store.dispatch("getRetailCustomerList");
    this.$store.dispatch("getCorporateCustomerList");
  },

  methods: {
    async setReceiptData(record) {
      await this.setData(record);

      this.downloadReceipt();
    },

    setData(record) {
      this.slNo = record.id;
      this.date = record.curr_date;
      if (record.curr_date == record.check_date) {
        this.checkDate = "N/A";
      } else {
        this.checkDate = record.check_date;
      }
      if (record.cust_id != null) {
        this.retailCustomerList.filter((customer) => {
          if (record.cust_id == customer.cust_id) {
            this.name = customer.cust_name;
            this.address = customer.cust_address;
          }
        });
      } else {
        this.corporateCustomerList.filter((customer) => {
          if (record.corp_id == customer.corp_id) {
            this.name = customer.corp_id;
            this.address = customer.corp_address;
          }
        });
      }

      this.paymentPurpose = record.batch_id;
      this.paymentMethod = record.pay_method;
      this.checkRefNo = record.check_ref_no;
      this.amount = record.sale_fee;
      this.amountInWords =
        numberToWords.toWords(this.amount).toUpperCase() + " TAKA";
      this.due = record.due_fee;
      this.prevReceipts = record.prev_receipts;
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
    saleList: {
      get() {
        return this.$store.getters.saleList;
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
  },
};
</script>