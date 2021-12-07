<template>
  <h1 class="pt-10 text-xl font-semibold">Add Instructor</h1>
  <div class="h-screen px-28 py-10">
    <div class="flex items-center justify-center">
      <form @submit="addInstructor">
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
            <label for="profit" class="font-semibold ml-2"
              >Profit margin*</label
            >
            <input
              type="number"
              name="profit"
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
              placeholder="profit margin"
              v-model="profit"
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
            Add Instructor
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
      if (this.name.length > 3) {
        let inst_id = this.name.substr(0, 3);
        inst_id = inst_id.toUpperCase();
        inst_id = inst_id.concat((this.instructorCount[0] + 1).toString());

        const data = {
          inst_id: inst_id,
          inst_name: this.name,
          inst_phone: this.phone,
          inst_email: this.email,
          inst_address: this.address,
          inst_organization: this.organization,
          inst_designation: this.designation,
          inst_profit: this.profit,
        };

        console.log(data);
        this.$store.dispatch("addInstructor", data);
        this.showModal = true;
      }
    },

    toggleModal() {
      this.showModal = false;
    },
  },
};
</script>

