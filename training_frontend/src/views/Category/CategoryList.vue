<template>
  <div class="flex justify-center w-full gap-24 mt-20">
    <!-- form -->
    <form @submit="addCategory">
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
            v-model="categoryName"
          />
        </div>
        <button
          class="
            bg-navlink
            rounded-md
            text-white text-xl
            px-8
            py-2
            w-54
            mt-10
            border-2 border-navlink
            shadow-xl
            hover:text-navlink hover:bg-transparent
            transition
            duration-300
          "
          type="submit"
        >
          Add Category
        </button>
      </div>
    </form>

    <!-- form end -->

    <!-- table -->
    <div class="grid grid-rows-1 place-items-center gap-2">
      <h1 class="text-xl font-semibold">Category List</h1>
      <table>
        <thead>
          <tr>
            <th class="w-1/5 px-4 py-4 text-center border-2">Category id</th>
            <th class="w-1/5 px-4 py-4 text-center border-2">Name</th>
          </tr>
        </thead>
        <tbody v-if="categoryList.length">
          <tr
            v-for="category in categoryList"
            :key="category.cat_id"
            class="hover:bg-gray-100"
          >
            <td class="w-1/5 px-4 py-4 text-center border-2">
              {{ category.cat_id }}
            </td>
            <td class="w-1/5 px-4 py-4 text-center border-2">
              {{ category.cat_name }}
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <!-- table end -->
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
      categoryName: "",
      message: "",
      showModal: false,
    };
  },
  mounted() {
    this.$store.dispatch("getCategoryList");
  },
  computed: {
    categoryList: {
      get() {
        return this.$store.getters.categoryList;
      },
    },
  },

  methods: {
    addCategory() {
      if (this.categoryName.length > 3) {
        let hasCategory = this.categoryList.filter((category) => {
          if (category.name == this.categoryName) {
            return category.name;
          }
        });

        if (!hasCategory.length) {
          let cat_id = this.categoryName.substr(0, 3);
          cat_id = cat_id.toUpperCase();
          cat_id = cat_id.concat((this.categoryList.length + 1).toString());

          const data = {
            cat_id: cat_id,
            cat_name: this.categoryName,
          };
          console.log(data);
          this.$store.dispatch("addCategory", data);
          this.message = "Category added";
          this.showModal = true;
        } else {
          this.message = "Category already exists";
          this.showModal = true;
        }
      }
    },

    toggleModal() {
      this.showModal = !this.showModal;
    },
  },
};
</script>