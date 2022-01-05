import { createStore } from "vuex";
import axios from "axios";

// axios.defaults.baseURL = "http://18.140.55.67/backend/api/";
axios.defaults.baseURL = "http://localhost:8080/backend/api/";

export default createStore({
  state: {
    instructorList: [],
    instructorCount: "",
    userList: [],
    userCount: "",
    instructor: "",
    user: "",
    categoryList: [],
    category: "",
    categoryCount: "",
    courseList: [],
    course: "",
    courseCount: "",
    batchList: [],
    batch: "",
    batchCount: "",
    retailCustomerList: [],
    retailCustomerCount: "",
    retailCustomer: "",
    corporateCustomerList: [],
    corporateCustomerCount: "",
    corporateCustomer: "",
    batchesByCourse: [],
    batchListTable: [],
    saleList: [],
    saleCount: "",
    saleRecord: "",
    saleid: "",
    receipt4: "",
    saleCustomerList: [],
    batchIds: [],
    instructorPercentages: [],
    userPercentages: [],
    instructorTotal: "",
  },
  mutations: {
    SET_INSTRUCTOR_LIST(state, instructorList) {
      state.instructorList = instructorList;
    },

    SET_INSTRUCTOR_COUNT(state, instructorCount) {
      state.instructorCount = instructorCount;
    },

    SET_USER_LIST(state, userList) {
      state.userList = userList;
    },

    SET_USER_COUNT(state, userCount) {
      state.userCount = userCount;
    },

    SET_INSTRUCTOR(state, instructor) {
      state.instructor = instructor;
    },

    SET_USER(state, user) {
      state.user = user;
    },

    SET_CATEGORY_LIST(state, categoryList) {
      state.categoryList = categoryList;
    },

    SET_CATEGORY(state, category) {
      state.category = category;
    },

    SET_CATEGORY_COUNT(state, categoryCount) {
      state.categoryCount = categoryCount;
    },

    SET_COURSE_LIST(state, courseList) {
      state.courseList = courseList;
    },

    SET_COURSE(state, course) {
      state.course = course;
    },

    SET_COURSE_COUNT(state, courseCount) {
      state.courseCount = courseCount;
    },

    SET_BATCH_LIST(state, batchList) {
      state.batchList = batchList;
    },

    SET_BATCH(state, batch) {
      state.batch = batch;
    },

    SET_BATCH_COUNT(state, batchCount) {
      state.batchCount = batchCount;
    },

    SET_RETAIL_CUSTOMER_LIST(state, retailCustomerList) {
      state.retailCustomerList = retailCustomerList;
    },

    SET_RETAIL_CUSTOMER_COUNT(state, retailCustomerCount) {
      state.retailCustomerCount = retailCustomerCount;
    },

    SET_RETAIL_CUSTOMER(state, retailCustomer) {
      state.retailCustomer = retailCustomer;
    },

    SET_CORPORATE_CUSTOMER_LIST(state, corporateCustomerList) {
      state.corporateCustomerList = corporateCustomerList;
    },

    SET_CORPORATE_CUSTOMER_COUNT(state, corporateCustomerCount) {
      state.corporateCustomerCount = corporateCustomerCount;
    },

    SET_CORPORATE_CUSTOMER(state, corporateCustomer) {
      state.corporateCustomer = corporateCustomer;
    },

    SET_BACTHES_BY_COURSE(state, batchesByCourse) {
      state.batchesByCourse = batchesByCourse;
    },

    SET_BATCH_LIST_TABLE(state, batchListTable) {
      state.batchListTable = batchListTable;
    },

    SET_SALE_LIST(state, saleList) {
      state.saleList = saleList;
    },

    SET_SALE_COUNT(state, saleCount) {
      state.saleCount = saleCount;
    },

    SET_SALE_RECORD(state, saleRecord) {
      state.saleRecord = saleRecord;
    },

    SET_SALE_ID(state, saleid) {
      state.saleid = saleid;
    },

    SET_RECEIPT4(state, receipt4) {
      state.receipt4 = receipt4;
    },

    SET_SALE_CUSTOMER_LIST(state, saleCustomerList) {
      state.saleCustomerList = saleCustomerList;
    },

    SET_BATCH_IDS(state, batchIds) {
      state.batchIds = batchIds;
    },

    SET_INSTRUCTOR_PERCENTAGES(state, instructorPercentages) {
      state.instructorPercentages = instructorPercentages;
    },

    SET_USER_PERCENTAGES(state, userPercentages) {
      state.userPercentages = userPercentages;
    },

    SET_INSTRUCTOR_TOTAL(state, instructorTotal) {
      state.instructorTotal = instructorTotal;
    },
  },
  actions: {
    getInstructorList({ commit }) {
      axios("instructors").then((res) => {
        commit("SET_INSTRUCTOR_LIST", res.data);
        console.log(res.data);
      }),
        (error) => {
          console.log(error);
        };
    },

    getInstructorCount({ commit }) {
      axios("instructors-count").then((res) => {
        commit("SET_INSTRUCTOR_COUNT", res.data);
        console.log(res.data);
      }),
        (error) => {
          console.log(error);
        };
    },

    addInstructor({ commit }, data) {
      axios.post("instructors", data).then((res) => {
        console.log(res.data);
      }),
        (error) => {
          console.log(error);
        };
    },

    getInstructor({ commit }, inst_id) {
      axios("instructors/" + inst_id).then((res) => {
        commit("SET_INSTRUCTOR", res.data);
        console.log(res.data);
      }),
        (error) => {
          console.log(error);
        };
    },

    getUserList({ commit }) {
      axios("users").then((res) => {
        commit("SET_USER_LIST", res.data);
        console.log(res.data);
      }),
        (error) => {
          console.log(error);
        };
    },

    addUser({ commit }, data) {
      axios.post("users", data).then((res) => {
        console.log(res.data);
      }),
        (error) => {
          console.log(error);
        };
    },

    getUser({ commit }, user_id) {
      axios("users/" + user_id).then((res) => {
        commit("SET_USER", res.data);
        console.log(res.data);
      }),
        (error) => {
          console.log(error);
        };
    },

    getUserCount({ commit }) {
      axios("users-count").then((res) => {
        commit("SET_USER_COUNT", res.data);
        console.log(res.data);
      }),
        (error) => {
          console.log(error);
        };
    },

    getCategoryList({ commit }) {
      axios("categories").then((res) => {
        commit("SET_CATEGORY_LIST", res.data);
        console.log(res.data);
      }),
        (error) => {
          console.log(error);
        };
    },

    addCategory({ commit }, data) {
      axios.post("categories", data).then((res) => {
        console.log(res.data);
      }),
        (error) => {
          console.log(error);
        };
    },

    addCourse({ commit }, data) {
      axios.post("courses", data).then((res) => {
        console.log(res.data);
      }),
        (error) => {
          console.log(error);
        };
    },

    getCourseList({ commit }) {
      axios("courses").then((res) => {
        commit("SET_COURSE_LIST", res.data);
        console.log(res.data);
      }),
        (error) => {
          console.log(error);
        };
    },

    getCourseCount({ commit }) {
      axios("courses-count").then((res) => {
        commit("SET_COURSE_COUNT", res.data);
        console.log(res.data);
      }),
        (error) => {
          console.log(error);
        };
    },

    async addRetailCustomer({ commit }, data) {
      await axios.post("customers", data).then((res) => {
        console.log(res.data);
      }),
        (error) => {
          console.log(error);
        };
    },

    getRetailCustomerCount({ commit }) {
      axios("customers-count").then((res) => {
        commit("SET_RETAIL_CUSTOMER_COUNT", res.data);
        console.log(res.data);
      }),
        (error) => {
          console.log(error);
        };
    },

    getRetailCustomer({ commit }, cust_id) {
      axios("customers/" + cust_id).then((res) => {
        commit("SET_RETAIL_CUSTOMER", res.data);
        console.log(res.data);
      }),
        (error) => {
          console.log(error);
        };
    },

    getRetailCustomerList({ commit }) {
      axios("customers").then((res) => {
        commit("SET_RETAIL_CUSTOMER_LIST", res.data);
        console.log(res.data);
      }),
        (error) => {
          console.log(error);
        };
    },

    async addCorporateCustomer({ commit }, data) {
      await axios.post("corporate-customers", data).then((res) => {
        console.log(res.data);
      }),
        (error) => {
          console.log(error);
        };
    },

    getCorporateCustomerCount({ commit }) {
      axios("corporate-customers-count").then((res) => {
        commit("SET_CORPORATE_CUSTOMER_COUNT", res.data);
        console.log(res.data);
      }),
        (error) => {
          console.log(error);
        };
    },

    getCorporateCustomer({ commit }, cust_id) {
      axios("corporate-customers/" + cust_id).then((res) => {
        commit("SET_CORPORATE_CUSTOMER", res.data);
        console.log(res.data);
      }),
        (error) => {
          console.log(error);
        };
    },

    getCorporateCustomerList({ commit }) {
      axios("corporate-customers").then((res) => {
        commit("SET_CORPORATE_CUSTOMER_LIST", res.data);
        console.log(res.data);
      }),
        (error) => {
          console.log(error);
        };
    },

    getBatchCount({ commit }) {
      axios("batches-count").then((res) => {
        commit("SET_BATCH_COUNT", res.data);
        console.log(res.data);
      }),
        (error) => {
          console.log(error);
        };
    },

    getBatchList({ commit }) {
      axios("batches").then((res) => {
        commit("SET_BATCH_LIST", res.data);
        console.log(res.data);
      }),
        (error) => {
          console.log(error);
        };
    },

    getBatchIds({ commit }) {
      axios("batch-ids").then((res) => {
        commit("SET_BATCH_IDS", res.data);
        console.log(res.data);
      }),
        (error) => {
          console.log(error);
        };
    },

    getBatch({ commit }, batch_id) {
      axios("batches/" + batch_id).then((res) => {
        commit("SET_BATCH", res.data);
        console.log(res.data);
      }),
        (error) => {
          console.log(error);
        };
    },

    addBatch({ commit }, data) {
      axios.post("batches", data).then((res) => {
        console.log(res.data);
      }),
        (error) => {
          console.log(error);
        };
    },

    getBatchesByCourse({ commit }, course_id) {
      axios("batches-by-course?course_id=" + course_id).then((res) => {
        commit("SET_BACTHES_BY_COURSE", res.data);
        console.log(res.data);
      }),
        (error) => {
          console.log(error);
        };
    },

    getBatchListTable({ commit }) {
      axios("batch-list").then((res) => {
        commit("SET_BATCH_LIST_TABLE", res.data);
        console.log(res.data);
      }),
        (error) => {
          console.log(error);
        };
    },

    changeBatchAdmissionStatus({ commit }, batch_id) {
      axios.put("batch-admission/" + batch_id).then((res) => {
        console.log(res.data);
      }),
        (error) => {
          console.log(error);
        };
    },

    getSaleList({ commit }) {
      axios("sale-list").then((res) => {
        commit("SET_SALE_LIST", res.data);
        console.log(res.data);
      }),
        (error) => {
          console.log(error);
        };
    },

    getSaleCount({ commit }) {
      axios("sales-count").then((res) => {
        commit("SET_SALE_COUNT", res.data);
        console.log(res.data);
      }),
        (error) => {
          console.log(error);
        };
    },

    async addSaleRecord({ commit }, data) {
      await axios.post("sales", data).then((res) => {
        console.log(res.data);
      }),
        (error) => {
          console.log(error);
        };
    },

    getSaleId({ commit }) {
      axios("sale-id").then((res) => {
        console.log(res.data);
        if (res.data == null) {
          commit("SET_SALE_ID", 0);
          commit("SET_RECEIPT4", 0);
        } else {
          commit("SET_SALE_ID", res.data[0]);
          commit("SET_RECEIPT4", res.data[22]);
        }
      }),
        (error) => {
          console.log(error);
        };
    },

    updateCustomerFees({ commit }, data) {
      axios.put("customer-fee-update", data).then((res) => {
        console.log(res.data);
      }),
        (error) => {
          console.log(error);
        };
    },

    updateCorporateCustomerFees({ commit }, data) {
      axios.put("corporate-fee-update", data).then((res) => {
        console.log(res.data);
      }),
        (error) => {
          console.log(error);
        };
    },

    getReceipts({ commit }) {
      axios("receipts").then((res) => {
        commit("SET_RECEIPTS", res.data);
        console.log(res.data);
      }),
        (error) => {
          console.log(error);
        };
    },

    updateSaleRecord({ commit }, data) {
      axios.put("sale-update", data).then((res) => {
        console.log(res.data);
      }),
        (error) => {
          console.log(error);
        };
    },

    getSaleCustomerList({ commit }, batchId) {
      axios("sale-customer-list/" + batchId).then((res) => {
        console.log(res.data);
        commit("SET_SALE_CUSTOMER_LIST", res.data);
      }),
        (error) => {
          console.log(error);
        };
    },

    getInstructorPercentages({ commit }, batchId) {
      axios("instructor-percentage/" + batchId).then((res) => {
        console.log(res.data);
        commit("SET_INSTRUCTOR_PERCENTAGES", res.data);
      }),
        (error) => {
          console.log(error);
        };
    },

    getUserPercentages({ commit }, batchId) {
      axios("user-percentage/" + batchId).then((res) => {
        console.log(res.data);
        commit("SET_USER_PERCENTAGES", res.data);
      }),
        (error) => {
          console.log(error);
        };
    },

    getInstructorTotal({ commit }, instId) {
      if (instId == "None") {
        this.state.instructorTotal = [];
      } else {
        axios("instructor-total/" + instId).then((res) => {
          console.log(res.data);
          commit("SET_INSTRUCTOR_TOTAL", res.data[0]);
        }),
          (error) => {
            console.log(error);
          };
      }
    },

    updateInstructorFee({ commit }, data) {
      axios.put("instructor-fee-update", data).then((res) => {
        console.log(res.data);
      }),
        (error) => {
          console.log(error);
        };
    },
  },
  getters: {
    instructorList: (state) => {
      return state.instructorList;
    },

    instructorCount: (state) => {
      return state.instructorCount;
    },

    userList: (state) => {
      return state.userList;
    },

    userCount: (state) => {
      return state.userCount;
    },

    instructor: (state) => {
      return state.instructor;
    },

    user: (state) => {
      return state.user;
    },

    categoryList: (state) => {
      return state.categoryList;
    },

    courseList: (state) => {
      return state.courseList;
    },

    courseCount: (state) => {
      return state.courseCount;
    },

    retailCustomerList: (state) => {
      return state.retailCustomerList;
    },

    retailCustomerCount: (state) => {
      return state.retailCustomerCount;
    },

    retailCustomer: (state) => {
      return state.retailCustomer;
    },

    corporateCustomerList: (state) => {
      return state.corporateCustomerList;
    },

    corporateCustomerCount: (state) => {
      return state.corporateCustomerCount;
    },

    corporateCustomer: (state) => {
      return state.corporateCustomer;
    },

    batchCount: (state) => {
      return state.batchCount;
    },

    batchList: (state) => {
      return state.batchList;
    },

    batch: (state) => {
      return state.batch;
    },

    batchesByCourse: (state) => {
      return state.batchesByCourse;
    },

    batchListTable: (state) => {
      return state.batchListTable;
    },

    saleList: (state) => {
      return state.saleList;
    },

    saleCount: (state) => {
      return state.saleCount;
    },

    saleid: (state) => {
      return state.saleid;
    },
    receipt4: (state) => {
      return state.receipt4;
    },

    saleCustomerList: (state) => {
      return state.saleCustomerList;
    },

    batchIds: (state) => {
      return state.batchIds;
    },

    instructorPercentages: (state) => {
      return state.instructorPercentages;
    },

    userPercentages: (state) => {
      return state.userPercentages;
    },
    instructorTotal: (state) => {
      return state.instructorTotal;
    },
  },
  modules: {},
});

export const strict = false;
