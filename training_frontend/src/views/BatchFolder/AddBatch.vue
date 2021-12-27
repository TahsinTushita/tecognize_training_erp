<template>
  <h1 class="pt-10 text-2xl font-semibold">Add Batch</h1>
  <div class="flex items-center justify-center">
    <form @submit.prevent="addBatch">
      <div class="space-y-5">
        <div class="grid grid-rows-1 gap-2 place-items-start">
          <label for="course" class="font-semibold ml-2">Course*</label>
          <select
            name="course"
            id="course"
            v-model="course_id"
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
            @change="generateBatchId"
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
          <label for="batch" class="font-semibold ml-2">Batch id*</label>
          <input
            type="text"
            name="batch"
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
            placeholder="batch id"
            v-model="batch_id"
          />
        </div>

        <div class="grid grid-rows-1 gap-2 place-items-start">
          <label for="instructor" class="font-semibold ml-2">Instructor*</label>
          <select
            name="instructor"
            id="instructor"
            v-model="instructor"
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
              v-for="instructor in instructorList"
              :value="instructor"
              :key="instructor.inst_id"
            >
              {{ instructor.inst_name }}
            </option>
          </select>
        </div>

        <div class="grid grid-rows-1 gap-2 place-items-start">
          <label for="batchFee" class="font-semibold ml-2">Batch Fee*</label>
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
            v-model="batch_fee"
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
          type="submit"
        >
          Add Batch
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
      course_id: "",
      instructor: "",
      batch_id: "",
      batch_fee: 0,
      admit_closed: false,
      message: "Batch added",
      showModal: false,
      inst_profit: "",
    };
  },
  mounted() {
    this.$store.dispatch("getCourseList");
    this.$store.dispatch("getInstructorList");
    this.$store.dispatch("getBatchList");
  },
  methods: {
    addBatch() {
      const data = {
        batch_id: this.batch_id,
        batch_fee: this.batch_fee,
        inst_id: this.instructor.inst_id,
        admit_closed: this.admit_closed,
        course_id: this.course_id,
        inst_profit: this.instructor.inst_profit,
      };

      this.$store.dispatch("addBatch", data);
      this.showModal = true;
    },

    generateBatchId() {
      let num = new Date().getFullYear();
      num = num.toString();
      num = parseInt(num.substr(2, 4)) * 100 + 1;
      this.batchList.filter((batch) => {
        if (batch.course_id == this.course_id) {
          if (parseInt(batch.batch_id.substr(3, 7)) >= num)
            num = parseInt(batch.batch_id.substr(3, 7)) + 1;
          console.log(num);
        }
      });
      let batch_id = this.course_id.substr(0, 3).concat(num.toString());
      console.log(batch_id);
      this.batch_id = batch_id;
    },

    // async generateBatchId2() {
    //   await this.$store
    //     .dispatch("getBatchesByCourse", this.course_id)
    //     .then(() => {
    //       console.log(this.$store.state.batchesByCourse);
    //       // if (this.$store.state.batchesByCourse.length) {
    //       //   this.batchesByCourse.filter((batch) => {
    //       //     console.log(batch.batch_id);
    //       //   });
    //       // }
    //     });
    // },

    toggleModal() {
      this.showModal = !this.showModal;
      window.location.reload();
    },
  },
  computed: {
    courseList: {
      get() {
        return this.$store.getters.courseList;
      },
    },

    instructorList: {
      get() {
        return this.$store.getters.instructorList;
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
  },
};
</script>