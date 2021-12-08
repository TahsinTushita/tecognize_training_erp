<template>
  <h1 class="pt-10 text-2xl font-semibold">Add Course</h1>
  <div class="flex items-center justify-center">
    <form @submit.prevent="addCourse">
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
            v-model="courseName"
          />
        </div>
        <div class="grid grid-rows-1 gap-2 place-items-start">
          <label for="name" class="font-semibold ml-2">Regular Price*</label>
          <input
            type="number"
            name="regularPrice"
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
            placeholder="regular price"
            v-model="regularPrice"
          />
        </div>
        <div class="grid grid-rows-1 gap-2 place-items-start">
          <label for="name" class="font-semibold ml-2">Category*</label>
          <select
            name="category"
            id="category"
            v-model="cat_id"
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
              v-for="category in categoryList"
              :value="category.cat_id"
              :key="category.cat_id"
            >
              {{ category.cat_name }}
            </option>
          </select>
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
          type="submit"
        >
          Add Course
        </button>
      </div>
    </form>
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
      courseName: "",
      regularPrice: 0,
      cat_id: "",
      message: "Course added",
      showModal: false,
    };
  },
  mounted() {
    this.$store.dispatch("getCategoryList");
    this.$store.dispatch("getCourseCount");
  },
  methods: {
    addCourse() {
      if (this.courseName.length >= 3) {
        let course_id = this.courseName.substr(0, 3);
        course_id = course_id.toUpperCase();
        let num = (10000 + (this.courseCount[0] + 1)).toString();
        course_id = course_id.concat(num.substr(1, 4));

        const data = {
          course_id: course_id,
          course_name: this.courseName,
          regular_price: this.regularPrice,
          cat_id: this.cat_id,
        };

        this.$store.dispatch("addCourse", data);
        this.showModal = true;
      }
    },

    toggleModal() {
      this.showModal = !this.showModal;
      window.location.reload();
    },
  },
  computed: {
    categoryList: {
      get() {
        return this.$store.getters.categoryList;
      },
    },

    courseCount: {
      get() {
        return this.$store.getters.courseCount;
      },
    },
  },
};
</script>