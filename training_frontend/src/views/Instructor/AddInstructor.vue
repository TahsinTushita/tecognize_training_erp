<template>
  <div class="h-screen px-28 py-10">
    <div class="flex items-center justify-center">
      <div class="space-y-5">
        <!-- <div v-for="inputField in inputFields" :key="inputField.id"> -->
        <div class="grid grid-rows-1 gap-2 place-items-start">
          <label for="name" class="font-semibold ml-2">Name*</label>
          <input
            type="text"
            name="name"
            required
            class="
              bg-white
              rounded-md
              font-poppins
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
              font-poppins
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
              font-poppins
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
              font-poppins
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
              font-poppins
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
              font-poppins
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
          />
        </div>

        <div class="grid grid-rows-1 gap-2 place-items-start">
          <label for="profit" class="font-semibold ml-2">Profit margin*</label>
          <input
            type="number"
            name="profit"
            required
            class="
              bg-white
              rounded-md
              font-poppins
              px-8
              py-4
              flex
              justify-center
              w-600
              border-2 border-gray-200
              hover:border-navlink hover:ring-0
              focus:outline-none focus:border-navlink
            "
            placeholder="profit margin"
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
        >
          Add Instructor
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      name: "",
      email: "",
      phoene: "",
      address: "",
      organization: "",
      designation: "",
      profit: "",
    };
  },
  methods: {},
};
</script>

