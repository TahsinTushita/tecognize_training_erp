<template>
  <h1 class="pt-10 text-xl font-semibold">Sale</h1>
  <div class="flex items-center justify-center mb-20">
    <div>
      <form @submit.prevent="false">
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
              v-model="batch"
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
                :value="batch"
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
              v-model="user"
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
                :value="user"
                :key="user.user_id"
              >
                {{ user.user_name }}
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
            <label for="course" class="font-semibold ml-2"
              >Customer Type*</label
            >
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
          <div class="space-y-5">
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
              <label for="custAddress" class="font-semibold ml-2"
                >Address*</label
              >
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

            <div
              class="grid grid-rows-1 gap-2 place-items-start"
              v-if="retailCustomer"
            >
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

            <div
              class="grid grid-rows-1 gap-2 place-items-start"
              v-if="retailCustomer"
            >
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
              <label for="batchFee" class="font-semibold ml-2"
                >Batch Fee*</label
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
                placeholder="batch fee"
                v-model="batchFee"
              />
            </div>

            <div
              class="grid grid-rows-1 gap-2 place-items-start"
              v-if="corporateCustomer"
            >
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
                v-model="custUnits"
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
              <label for="custTotalFee" class="font-semibold ml-2"
                >Total*</label
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
                placeholder="total"
                v-model="getCustTotal"
              />
            </div>

            <div class="grid grid-rows-1 gap-2 place-items-start">
              <label for="custPaidFee" class="font-semibold ml-2">Paid*</label>
              <input
                type="number"
                name="custPaidFee"
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
                v-model="getCustDue"
              />
            </div>
          </div>
          <!-- Retail Customer Form end -->
        </div>
      </form>
    </div>
  </div>

  <div class="flex justify-center">
    <div>
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
                <p class="text-black font-medium">{{ this.receipt4 + 1 }}</p>
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
                  {{ custName }}
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
                  {{ custAddress }}
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
                  {{ batch.batch_id }}
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
                    aria-placeholder="N/A"
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
                  {{ custTotalFee }}
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
                  {{ custPaidFee }}
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
                  {{ custAmountInWords }}
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
                    "
                  >
                    N/A
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
                    {{ custDueFee }}
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
      <button
        class="px-4 py-2 bg-blue-200 rounded-md text-xl hover:bg-blue-300 mt-10"
        @click="downloadRetailReceipt"
      >
        Download receipt
      </button>
    </div>
  </div>

  <button
    class="bg-green-200 px-4 py-2 rounded-md hover:bg-green-300 m-20 text-xl"
    @click="addSaleRecord"
  >
    Sale
  </button>

  <div v-if="showModal">
    <Modal :header="header" :text="text" @close="toggleModal">
      <h3>{{ message }}</h3>
    </Modal>
  </div>
</template>

<script>
import Modal from "../../components/Modal.vue";
import jsPDF from "jspdf";
import html2canvas from "html2canvas";
import moment from "moment";
import numberToWords from "number-to-words";

export default {
  components: { Modal },
  data() {
    return {
      customerType: "",
      message: "Record added successfully",
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
      custPaidFee: 0,
      custDueFee: "",
      custUnits: 1,
      courseId: "",
      batchId: "",
      batch: "",
      regularFee: "",
      batchFee: "",
      discountFee: 0,
      selectBatch: true,
      tempBatchList: [],
      newCustomer: true,
      user: "",
      instId: "",
      prevCustTotalFee: "",
      prevCustPaidFee: "",
      prevCustDueFee: "",
      prevCustUnits: "",
      notPrinted: true,
      retailReceipt: false,
      corporateReceipt: false,
      courseName: "",
      userName: "",
      date: "",
      officeAddress: "H# B-160,New DOHS Mohakhali,Dhaka-1206",
      officeEmail: "training@tecognize.com",
      officePhone: "+8801893466660",
      custAmountInWords: "",
      corpAmountInWords: "",
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
      checkDate: "N/A",
      showCheckDate: false,
      prevReceipts: "N/A",
    };
  },
  mounted() {
    this.$store.dispatch("getCourseList");
    this.$store.dispatch("getBatchList");
    this.$store.dispatch("getRetailCustomerList");
    this.$store.dispatch("getUserList");
    this.$store.dispatch("getRetailCustomerCount");
    this.$store.dispatch("getSaleId");
    this.date = this.getDate();
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
        if (course == batch.batch_id.substr(0, 3) && batch.admit_closed == 0) {
          this.tempBatchList.push(batch);
        }
      });

      this.courseList.filter((course) => {
        if (course.course_id == this.courseId) {
          this.regularFee = course.regular_price;
          this.courseName = course.course_name;
        }
      });
      console.log(course);
      // this.selectBatch = false;
    },

    setBatchFee() {
      this.batchFee = this.batch.batch_fee;
      this.instId = this.batch.inst_id;
      this.inst_profit = this.batch.inst_profit;
    },

    filterRetailCustomer() {
      this.retailCustomerList.filter((customer) => {
        if (this.custPhone == customer.cust_phone) {
          this.newCustomer = false;
          this.custId = customer.cust_id;
          this.custName = customer.cust_name;
          this.custEmail = customer.cust_email;
          this.custAddress = customer.cust_address;
          this.custOrganization = customer.cust_organization;
          this.custDesignation = customer.cust_designation;
          this.prevCustTotalFee = customer.cust_total_fee;
          this.prevCustPaidFee = customer.cust_paid_fee;
          this.prevCustDueFee = customer.cust_due_fee;
          this.prevCustUnits = customer.cust_units;
        }
      });
    },

    filterCorporateCustomer() {
      this.corporateCustomerList.filter((customer) => {
        if (this.corpPhone == customer.corp_phone) {
          this.newCustomer = false;
          this.corpId = customer.corp_id;
          this.corpName = customer.corp_name;
          this.corpEmail = customer.corp_email;
          this.corpAddress = customer.corp_address;
          this.prevCorpTotalFee = customer.corp_total_fee;
          this.prevCorpPaidFee = customer.corp_paid_fee;
          this.prevCorpDueFee = customer.corp_due_fee;
          this.prevCorpUnits = customer.corp_units;
        }
      });
    },

    toggleCheckDate() {
      if (this.paymentMethod == "check") {
        this.showCheckDate = true;
      } else {
        this.showCheckDate = false;
      }
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

    async addSaleRecord() {
      if (this.checkDate == "N/A") this.checkDate = null;

      if (this.newCustomer == true) {
        if (this.custName.length >= 3) {
          let cust_id = new Date().getFullYear();
          cust_id = cust_id.toString();
          cust_id = (
            parseInt(cust_id.substr(2, 4)) * 10000 +
            this.retailCustomerCount[0] +
            1
          ).toString();

          if (this.customerType == "corporate") {
            cust_id = cust_id + "C";
          }

          const custData = {
            cust_id: cust_id,
            cust_name: this.custName,
            cust_phone: this.custPhone,
            cust_email: this.custEmail,
            cust_address: this.custAddress,
            cust_organization: this.custOrganization,
            cust_designation: this.custDesignation,
            cust_total_fee: this.custTotalFee,
            cust_paid_fee: this.custPaidFee,
            cust_due_fee: this.custDueFee,
            cust_units: this.custUnits,
          };

          await this.$store.dispatch("addRetailCustomer", custData);
          const saleData = {
            id: this.receipt4 + 1,
            cust_id: cust_id,
            batch_id: this.batch.batch_id,
            regular_fee: this.regularFee,
            batch_fee: this.custTotalFee,
            installment1: this.custPaidFee,
            mr_no1: this.receipt4 + 1,
            date1: this.date,
            check_date1: this.checkDate,
            check_ref_no1: this.checkRefNo,
            pay_mode1: this.paymentMethod,
            installment2: 0,
            mr_no2: this.receipt4 + 2,
            date2: null,
            check_date2: null,
            check_ref_no2: null,
            pay_mode2: null,
            installment3: 0,
            mr_no3: this.receipt4 + 3,
            date3: null,
            check_date3: null,
            check_ref_no3: null,
            pay_mode3: null,
            installment4: 0,
            mr_no4: this.receipt4 + 4,
            date4: null,
            check_date4: null,
            check_ref_no4: null,
            pay_mode4: null,
            paid: this.custPaidFee,
            due: this.custDueFee,
            inst_id: this.instId,
            inst_profit: this.inst_profit,
            user_id: this.user.user_id,
            user_profit: this.user.user_profit,
            remarks: "",
          };
          await this.$store.dispatch("addSaleRecord", saleData);
        }
      } else {
        if (this.customerType == "corporate") {
          this.custUnits = this.custUnits + this.prevCustUnits;
        }
        const custData = {
          cust_total_fee: this.custTotalFee + this.prevCustTotalFee,
          cust_paid_fee: this.custPaidFee + this.prevCustPaidFee,
          cust_due_fee: this.custDueFee + this.prevCustDueFee,
          cust_units: this.custUnits,
          cust_id: this.custId,
        };

        this.$store.dispatch("updateCustomerFees", custData);
        const saleData = {
          id: this.receipt4 + 1,
          cust_id: this.custId,
          batch_id: this.batch.batch_id,
          regular_fee: this.regularFee,
          batch_fee: this.custTotalFee,
          installment1: this.custPaidFee,
          mr_no1: this.receipt4 + 1,
          date1: this.date,
          check_date1: this.checkDate,
          check_ref_no1: this.checkRefNo,
          pay_mode1: this.paymentMethod,
          installment2: 0,
          mr_no2: this.receipt4 + 2,
          date2: null,
          check_date2: null,
          check_ref_no2: null,
          pay_mode2: null,
          installment3: 0,
          mr_no3: this.receipt4 + 3,
          date3: null,
          check_date3: null,
          check_ref_no3: null,
          pay_mode3: null,
          installment4: 0,
          mr_no4: this.receipt4 + 4,
          date4: null,
          check_date4: null,
          check_ref_no4: null,
          pay_mode4: null,
          paid: this.custPaidFee,
          due: this.custDueFee,
          inst_id: this.instId,
          inst_profit: this.inst_profit,
          user_id: this.user.user_id,
          user_profit: this.user.user_profit,
          remarks: "",
        };
        await this.$store.dispatch("addSaleRecord", saleData);
      }

      this.showModal = true;
    },

    enableSaleButton() {
      this.notPrinted = false;
    },

    toggleModal() {
      this.showModal = !this.showModal;
      window.location.reload();
    },

    setUserName() {
      if (this.userId) {
        this.userList.filter((user) => {
          if (user.user_id == this.userId) {
            this.userName = user.user_name;
          }
        });

        return this.userName;
      }
    },

    downloadRetailReceipt() {
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
          this.custName +
          "_" +
          this.courseName +
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

    downloadCorporateReceipt() {
      const doc = new jsPDF({
        orientation: "l",
        unit: "px",
        format: "a4",
        hotfixes: ["px_scaling"],
      });

      html2canvas(this.$refs.corporateReceiptContent, {
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
          this.corpName +
          "_" +
          this.courseName +
          "_" +
          this.batchId +
          "_" +
          new Date().toLocaleDateString() +
          "_" +
          new Date().toLocaleTimeString() +
          ".pdf";
        doc.save(filename);
        this.moneyReceipt = doc;
      });
    },
    getDate: function () {
      return moment(String(new Date().toLocaleDateString())).format(
        "YYYY-MM-DD"
      );
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

    corporateCustomerCount: {
      get() {
        return this.$store.getters.corporateCustomerCount;
      },
    },

    retailCustomerCount: {
      get() {
        return this.$store.getters.retailCustomerCount;
      },
    },

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

    getCorpTotal() {
      if (this.batchFee && this.corpUnits && this.discountFee) {
        this.corpTotalFee = this.batchFee * this.corpUnits - this.discountFee;
        this.corpAmountInWords =
          numberToWords.toWords(this.corpTotalFee).toUpperCase() + " TAKA";
      } else if (this.batchFee && this.corpUnits) {
        this.corpTotalFee = this.batchFee * this.corpUnits;
        this.corpAmountInWords =
          numberToWords.toWords(this.corpTotalFee).toUpperCase() + " TAKA";
      }
      return this.corpTotalFee;

      // return !!this.batchFee && !!this.corpUnits && !!this.discountFee
      //   ? this.batchFee * this.corpUnits - this.discountFee
      //   : 0;
    },

    getCorpDue() {
      if (this.corpTotalFee && this.corpPaidFee) {
        this.corpDueFee = this.corpTotalFee - this.corpPaidFee;
      } else if (this.corpTotalFee) {
        this.corpDueFee = this.corpTotalFee;
      }
      return this.corpDueFee;

      // return !!this.corpTotalFee && !!this.corpPaidFee
      //   ? this.corpTotalFee - this.corpPaidFee
      //   : 0;
    },

    getCustTotal() {
      if (this.batchFee && this.discountFee) {
        this.custTotalFee = this.batchFee * this.custUnits - this.discountFee;
        // this.custAmountInWords =
        //   numberToWords.toWords(this.custTotalFee).toUpperCase() + " TAKA";
      } else if (this.batchFee) {
        this.custTotalFee = this.batchFee * this.custUnits;
        this.custAmountInWords =
          numberToWords.toWords(this.custTotalFee).toUpperCase() + " TAKA";
      }
      return this.custTotalFee;
    },

    getCustDue() {
      if (this.custTotalFee && this.custPaidFee) {
        this.custDueFee = this.custTotalFee - this.custPaidFee;
        this.custAmountInWords =
          numberToWords.toWords(this.custPaidFee).toUpperCase() + " TAKA";
      } else if (this.custTotalFee) {
        this.custDueFee = this.custTotalFee;
        this.custAmountInWords = "";
      }
      return this.custDueFee;
    },
  },
};
</script>