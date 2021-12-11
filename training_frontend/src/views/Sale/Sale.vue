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
              @change="setUserName"
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
              @click="generateSalesReceipt"
            >
              show receipt
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
              <label for="corpAddress" class="font-semibold ml-2"
                >Address*</label
              >
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
              <label for="corpTotalFee" class="font-semibold ml-2"
                >Total*</label
              >
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
                v-model="getCorpTotal"
              />
            </div>

            <div class="grid grid-rows-1 gap-2 place-items-start">
              <label for="corpPaidFee" class="font-semibold ml-2">Paid*</label>
              <input
                type="number"
                name="corpPaidFee"
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
                v-model="getCorpDue"
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
              @click="generateSalesReceipt"
            >
              show receipt
            </button>
          </div>
          <!-- Corporate Customer Form end -->
        </div>
      </form>
    </div>
  </div>

  <div class="flex justify-center">
    <div v-if="retailReceipt">
      <div ref="retailReceiptContent" class="space-y-5">
        <h1 class="text-xl">Retail Customer Receipt</h1>

        <table>
          <tbody>
            <tr class="border-2 border-b-0">
              <td class="w-2/5 px-4 py-4 text-center">Customer Name:</td>
              <td class="w-2/5 px-4 py-4 text-center">
                {{ custName }}
              </td>
            </tr>
            <tr class="border-2 border-t-0 border-b-0">
              <td class="w-2/5 px-4 py-4 text-center">Course:</td>
              <td class="w-2/5 px-4 py-4 text-center">
                {{ courseName }}
              </td>
            </tr>
            <tr class="border-2 border-t-0 border-b-0">
              <td class="w-2/5 px-4 py-4 text-center">Batch:</td>
              <td class="w-2/5 px-4 py-4 text-center">
                {{ batchId }}
              </td>
            </tr>

            <tr class="border-2 border-t-0 border-b-0">
              <td class="w-2/5 px-4 py-4 text-center">Reference:</td>
              <td class="w-2/5 px-4 py-4 text-center">
                {{ userName }}
              </td>
            </tr>

            <tr class="border-2 border-t-0 border-b-0">
              <td class="w-2/5 px-4 py-4 text-center">Phone number:</td>
              <td class="w-2/5 px-4 py-4 text-center">
                {{ custPhone }}
              </td>
            </tr>

            <tr class="border-2 border-t-0 border-b-0">
              <td class="w-2/5 px-4 py-4 text-center">email:</td>
              <td class="w-2/5 px-4 py-4 text-center">
                {{ custEmail }}
              </td>
            </tr>

            <tr class="border-2 border-t-0 border-b-0">
              <td class="w-2/5 px-4 py-4 text-center">Address:</td>
              <td class="w-2/5 px-4 py-4 text-center">
                {{ custAddress }}
              </td>
            </tr>

            <tr class="border-2 border-t-0 border-b-0">
              <td class="w-2/5 px-4 py-4 text-center">Organization:</td>
              <td class="w-2/5 px-4 py-4 text-center">
                {{ custOrganization }}
              </td>
            </tr>

            <tr class="border-2 border-t-0 border-b-0">
              <td class="w-2/5 px-4 py-4 text-center">Designation:</td>
              <td class="w-2/5 px-4 py-4 text-center">
                {{ custDesignation }}
              </td>
            </tr>

            <tr class="border-2 border-t-0 border-b-0">
              <td class="w-2/5 px-4 py-4 text-center">Regular fee:</td>
              <td class="w-2/5 px-4 py-4 text-center">
                {{ regularFee }}
              </td>
            </tr>

            <tr class="border-2 border-t-0 border-b-0">
              <td class="w-2/5 px-4 py-4 text-center">Batch fee:</td>
              <td class="w-2/5 px-4 py-4 text-center">
                {{ batchFee }}
              </td>
            </tr>

            <tr class="border-2 border-t-0 border-b-0">
              <td class="w-2/5 px-4 py-4 text-center">Discount:</td>
              <td class="w-2/5 px-4 py-4 text-center">
                {{ discountFee }}
              </td>
            </tr>

            <tr class="border-2 border-t-0 border-b-0">
              <td class="w-2/5 px-4 py-4 text-center">Total:</td>
              <td class="w-2/5 px-4 py-4 text-center">
                {{ custTotalFee }}
              </td>
            </tr>

            <tr class="border-2 border-t-0 border-b-0">
              <td class="w-2/5 px-4 py-4 text-center">Paid:</td>
              <td class="w-2/5 px-4 py-4 text-center">
                {{ custPaidFee }}
              </td>
            </tr>

            <tr class="border-2 border-t-0">
              <td class="w-2/5 px-4 py-4 text-center">Due:</td>
              <td class="w-2/5 px-4 py-4 text-center">
                {{ custDueFee }}
              </td>
            </tr>
          </tbody>
        </table>
        <h1>{{ fulldatetime }}</h1>
      </div>
      <button
        class="px-4 py-2 bg-blue-200 rounded-md text-xl hover:bg-blue-300 mt-10"
        @click="downloadRetailReceipt"
      >
        Download receipt
      </button>
    </div>

    <div v-if="corporateReceipt">
      <div ref="corporateReceiptContent" class="space-y-5">
        <h1 class="text-xl">Corporate Customer Receipt</h1>

        <table>
          <tbody>
            <tr class="border-2 border-b-0">
              <td class="w-2/5 px-4 py-4 text-center">Organization:</td>
              <td class="w-2/5 px-4 py-4 text-center">
                {{ corpName }}
              </td>
            </tr>
            <tr class="border-2 border-t-0 border-b-0">
              <td class="w-2/5 px-4 py-4 text-center">Course:</td>
              <td class="w-2/5 px-4 py-4 text-center">
                {{ courseName }}
              </td>
            </tr>
            <tr class="border-2 border-t-0 border-b-0">
              <td class="w-2/5 px-4 py-4 text-center">Batch:</td>
              <td class="w-2/5 px-4 py-4 text-center">
                {{ batchId }}
              </td>
            </tr>

            <tr class="border-2 border-t-0 border-b-0">
              <td class="w-2/5 px-4 py-4 text-center">Reference:</td>
              <td class="w-2/5 px-4 py-4 text-center">
                {{ userName }}
              </td>
            </tr>

            <tr class="border-2 border-t-0 border-b-0">
              <td class="w-2/5 px-4 py-4 text-center">Phone number:</td>
              <td class="w-2/5 px-4 py-4 text-center">
                {{ corpPhone }}
              </td>
            </tr>

            <tr class="border-2 border-t-0 border-b-0">
              <td class="w-2/5 px-4 py-4 text-center">email:</td>
              <td class="w-2/5 px-4 py-4 text-center">
                {{ corpEmail }}
              </td>
            </tr>

            <tr class="border-2 border-t-0 border-b-0">
              <td class="w-2/5 px-4 py-4 text-center">Address:</td>
              <td class="w-2/5 px-4 py-4 text-center">
                {{ corpAddress }}
              </td>
            </tr>

            <tr class="border-2 border-t-0 border-b-0">
              <td class="w-2/5 px-4 py-4 text-center">Regular fee:</td>
              <td class="w-2/5 px-4 py-4 text-center">
                {{ regularFee }}
              </td>
            </tr>

            <tr class="border-2 border-t-0 border-b-0">
              <td class="w-2/5 px-4 py-4 text-center">Batch fee:</td>
              <td class="w-2/5 px-4 py-4 text-center">
                {{ batchFee }}
              </td>
            </tr>

            <tr class="border-2 border-t-0 border-b-0">
              <td class="w-2/5 px-4 py-4 text-center">Units:</td>
              <td class="w-2/5 px-4 py-4 text-center">
                {{ corpUnits }}
              </td>
            </tr>

            <tr class="border-2 border-t-0 border-b-0">
              <td class="w-2/5 px-4 py-4 text-center">Discount:</td>
              <td class="w-2/5 px-4 py-4 text-center">
                {{ discountFee }}
              </td>
            </tr>

            <tr class="border-2 border-t-0 border-b-0">
              <td class="w-2/5 px-4 py-4 text-center">Total:</td>
              <td class="w-2/5 px-4 py-4 text-center">
                {{ corpTotalFee }}
              </td>
            </tr>

            <tr class="border-2 border-t-0 border-b-0">
              <td class="w-2/5 px-4 py-4 text-center">Paid:</td>
              <td class="w-2/5 px-4 py-4 text-center">
                {{ corpPaidFee }}
              </td>
            </tr>

            <tr class="border-2 border-t-0 border-b-0">
              <td class="w-2/5 px-4 py-4 text-center">Paid:</td>
              <td class="w-2/5 px-4 py-4 text-center">
                {{ corpPaidFee }}
              </td>
            </tr>

            <tr class="border-2 border-t-0">
              <td class="w-2/5 px-4 py-4 text-center">Due:</td>
              <td class="w-2/5 px-4 py-4 text-center">
                {{ corpDueFee }}
              </td>
            </tr>
          </tbody>
        </table>
        <h1>{{ fulldatetime }}</h1>
      </div>

      <button
        class="px-4 py-2 bg-blue-200 rounded-md text-xl hover:bg-blue-300 mt-10"
        @click="downloadCorporateReceipt"
      >
        Download receipt
      </button>
    </div>
  </div>

  <button
    class="bg-green-200 px-4 py-2 rounded-md hover:bg-green-300 m-20 text-xl"
    @click="addSaleRecord"
    :disabled="notPrinted"
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
      corpId: "",
      corpName: "",
      corpEmail: "",
      corpPhone: "",
      corpAddress: "",
      corpTotalFee: "",
      corpPaidFee: 0,
      corpDueFee: "",
      corpUnits: "",
      courseId: "",
      batchId: "",
      regularFee: "",
      batchFee: "",
      discountFee: 0,
      selectBatch: true,
      tempBatchList: [],
      newCustomer: true,
      userId: "",
      instId: "",
      prevCustTotalFee: "",
      prevCustPaidFee: "",
      prevCustDueFee: "",
      prevCorpTotalFee: "",
      prevCorpPaidFee: "",
      prevCorpDueFee: "",
      prevCorpUnits: "",
      notPrinted: true,
      retailReceipt: false,
      corporateReceipt: false,
      courseName: "",
      userName: "",
      fulldatetime: "",
    };
  },
  mounted() {
    this.$store.dispatch("getCourseList");
    this.$store.dispatch("getBatchList");
    this.$store.dispatch("getRetailCustomerList");
    this.$store.dispatch("getCorporateCustomerList");
    this.$store.dispatch("getUserList");
    this.$store.dispatch("getCorporateCustomerCount");
    this.$store.dispatch("getRetailCustomerCount");
    this.fulldatetime = this.printFullDate();
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
      this.tempBatchList.filter((batch) => {
        if (batch.batch_id == this.batchId) {
          this.batchFee = batch.batch_fee;
          this.instId = batch.inst_id;
        }
      });
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

    addSaleRecord() {
      if (this.customerType == "retail") {
        if (this.newCustomer == true) {
          if (this.custName.length >= 3) {
            let cust_id = new Date().getFullYear();
            cust_id = cust_id.toString();
            cust_id = (
              parseInt(cust_id.substr(2, 4)) * 10000 +
              this.retailCustomerCount[0] +
              1
            ).toString();

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
            };

            this.$store.dispatch("addRetailCustomer", custData).then(() => {
              const saleData = {
                regular_fee: this.regularFee,
                sale_fee: this.custTotalFee,
                paid_fee: this.custPaidFee,
                due_fee: this.custDueFee,
                batch_id: this.batchId,
                corp_id: this.corpId,
                cust_id: cust_id,
                inst_id: this.instId,
                user_id: this.userId,
              };
              this.$store.dispatch("addSaleRecord", saleData);
            });
          }
        } else {
          const custData = {
            cust_id: this.custId,
            cust_total_fee: this.custTotalFee + this.prevCustTotalFee,
            cust_paid_fee: this.custPaidFee + this.prevCustPaidFee,
            cust_due_fee: this.custDueFee + this.prevCustDueFee,
          };

          this.$store.dispatch("updateRetailCustomerFees", custData);
          const saleData = {
            regular_fee: this.regularFee,
            sale_fee: this.custTotalFee,
            paid_fee: this.custPaidFee,
            due_fee: this.custDueFee,
            batch_id: this.batchId,
            corp_id: this.corpId,
            cust_id: this.custId,
            inst_id: this.instId,
            user_id: this.userId,
          };
          this.$store.dispatch("addSaleRecord", saleData);
        }
      }
      if (this.customerType == "corporate") {
        if (this.newCustomer == true) {
          if (this.corpName.length >= 3) {
            let corp_id = this.corpName.substr(0, 3);
            corp_id = corp_id.toUpperCase();
            let num = (10000 + (this.corporateCustomerCount[0] + 1)).toString();
            corp_id = corp_id.concat(num.substr(1, 4));

            const corpData = {
              corp_id: corp_id,
              corp_name: this.corpName,
              corp_phone: this.corpPhone,
              corp_email: this.corpEmail,
              corp_address: this.corpAddress,
              corp_total_fee: this.corpTotalFee,
              corp_paid_fee: this.corpPaidFee,
              corp_due_fee: this.corpDueFee,
              corp_units: this.corpUnits,
            };

            this.$store.dispatch("addCorporateCustomer", corpData).then(() => {
              const saleData = {
                regular_fee: this.regularFee,
                sale_fee: this.corpTotalFee,
                paid_fee: this.corpPaidFee,
                due_fee: this.corpDueFee,
                batch_id: this.batchId,
                corp_id: corp_id,
                cust_id: this.custId,
                inst_id: this.instId,
                user_id: this.userId,
              };
              this.$store.dispatch("addSaleRecord", saleData);
            });
            // this.showModal = true;
          }
        } else {
          const corpData = {
            corp_id: this.corpId,
            corp_total_fee: this.corpTotalFee + this.prevCorpTotalFee,
            corp_paid_fee: this.corpPaidFee + this.prevCorpPaidFee,
            corp_due_fee: this.corpDueFee + this.prevCorpDueFee,
            corp_units: this.corpUnits + this.prevCorpUnits,
          };

          this.$store.dispatch("updateCorporateCustomerFees", corpData);

          const saleData = {
            regular_fee: this.regularFee,
            sale_fee: this.corpTotalFee,
            paid_fee: this.corpPaidFee,
            due_fee: this.corpDueFee,
            batch_id: this.batchId,
            corp_id: this.corpId,
            cust_id: this.custId,
            inst_id: this.instId,
            user_id: this.userId,
          };
          this.$store.dispatch("addSaleRecord", saleData);
        }
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

    generateSalesReceipt() {
      if (this.customerType == "retail") {
        this.corporateReceipt = false;
        this.retailReceipt = true;
      } else {
        this.retailReceipt = false;
        this.corporateReceipt = true;
      }

      this.notPrinted = false;
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
        orientation: "p",
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
          140,
          10,
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
        orientation: "p",
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
          140,
          10,
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
      });
    },
    printFullDate: function () {
      return new Date();
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

    getCorpTotal() {
      if (this.batchFee && this.corpUnits && this.discountFee) {
        this.corpTotalFee = this.batchFee * this.corpUnits - this.discountFee;
      } else if (this.batchFee && this.corpUnits) {
        this.corpTotalFee = this.batchFee * this.corpUnits;
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
        this.custTotalFee = this.batchFee - this.discountFee;
      } else if (this.batchFee) {
        this.custTotalFee = this.batchFee;
      }
      return this.custTotalFee;
    },

    getCustDue() {
      if (this.custTotalFee && this.custPaidFee) {
        this.custDueFee = this.custTotalFee - this.custPaidFee;
      } else if (this.custTotalFee) {
        this.custDueFee = this.custTotalFee;
      }
      return this.custDueFee;
    },
  },
};
</script>