import { createStore } from "vuex";
import axios from "axios";

axios.defaults.baseURL = "http://localhost:8080";

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
  },
  actions: {
    getInstructorList({ commit }) {
      axios("/api/instructors").then((res) => {
        commit("SET_INSTRUCTOR_LIST", res.data);
        console.log(res.data);
      }),
        (error) => {
          console.log(error);
        };
    },

    getInstructorCount({ commit }) {
      axios("/api/instructors-count").then((res) => {
        commit("SET_INSTRUCTOR_COUNT", res.data);
        console.log(res.data);
      }),
        (error) => {
          console.log(error);
        };
    },

    addInstructor({ commit }, data) {
      axios.post("/api/instructors", data).then((res) => {
        console.log(res.data);
      }),
        (error) => {
          console.log(error);
        };
    },

    getInstructor({ commit }, inst_id) {
      axios("/api/instructors/" + inst_id).then((res) => {
        commit("SET_INSTRUCTOR", res.data);
        console.log(res.data);
      }),
        (error) => {
          console.log(error);
        };
    },

    getUserList({ commit }) {
      axios("/api/users").then((res) => {
        commit("SET_USER_LIST", res.data);
        console.log(res.data);
      }),
        (error) => {
          console.log(error);
        };
    },

    addUser({ commit }, data) {
      axios.post("/api/users", data).then((res) => {
        console.log(res.data);
      }),
        (error) => {
          console.log(error);
        };
    },

    getUser({ commit }, user_id) {
      axios("/api/users/" + user_id).then((res) => {
        commit("SET_USER", res.data);
        console.log(res.data);
      }),
        (error) => {
          console.log(error);
        };
    },

    getUserCount({ commit }) {
      axios("/api/users-count").then((res) => {
        commit("SET_USER_COUNT", res.data);
        console.log(res.data);
      }),
        (error) => {
          console.log(error);
        };
    },

    getCategoryList({ commit }) {
      axios("/api/categories").then((res) => {
        commit("SET_CATEGORY_LIST", res.data);
        console.log(res.data);
      }),
        (error) => {
          console.log(error);
        };
    },

    addCategory({ commit }, data) {
      axios.post("/api/categories", data).then((res) => {
        console.log(res.data);
      }),
        (error) => {
          console.log(error);
        };
    },

    addCourse({ commit }, data) {
      axios.post("/api/courses", data).then((res) => {
        console.log(res.data);
      }),
        (error) => {
          console.log(error);
        };
    },

    getCourseList({ commit }) {
      axios("/api/courses").then((res) => {
        commit("SET_COURSE_LIST", res.data);
        console.log(res.data);
      }),
        (error) => {
          console.log(error);
        };
    },

    getCourseCount({ commit }) {
      axios("/api/courses-count").then((res) => {
        commit("SET_COURSE_COUNT", res.data);
        console.log(res.data);
      }),
        (error) => {
          console.log(error);
        };
    },

    addRetailCustomer({ commit }, data) {
      axios.post("/api/retail-customers", data).then((res) => {
        console.log(res.data);
      }),
        (error) => {
          console.log(error);
        };
    },

    getRetailCustomerCount({ commit }) {
      axios("/api/retail-customers-count").then((res) => {
        commit("SET_RETAIL_CUSTOMER_COUNT", res.data);
        console.log(res.data);
      }),
        (error) => {
          console.log(error);
        };
    },

    getRetailCustomer({ commit }, cust_id) {
      axios("/api/retail-customers/" + cust_id).then((res) => {
        commit("SET_RETAIL_CUSTOMER", res.data);
        console.log(res.data);
      }),
        (error) => {
          console.log(error);
        };
    },

    getRetailCustomerList({ commit }) {
      axios("/api/retail-customers").then((res) => {
        commit("SET_RETAIL_CUSTOMER_LIST", res.data);
        console.log(res.data);
      }),
        (error) => {
          console.log(error);
        };
    },

    addCorporateCustomer({ commit }, data) {
      axios.post("/api/corporate-customers", data).then((res) => {
        console.log(res.data);
      }),
        (error) => {
          console.log(error);
        };
    },

    getCorporateCustomerCount({ commit }) {
      axios("/api/corporate-customers-count").then((res) => {
        commit("SET_CORPORATE_CUSTOMER_COUNT", res.data);
        console.log(res.data);
      }),
        (error) => {
          console.log(error);
        };
    },

    getCorporateCustomer({ commit }, cust_id) {
      axios("/api/corporate-customers/" + cust_id).then((res) => {
        commit("SET_CORPORATE_CUSTOMER", res.data);
        console.log(res.data);
      }),
        (error) => {
          console.log(error);
        };
    },

    getCorporateCustomerList({ commit }) {
      axios("/api/corporate-customers").then((res) => {
        commit("SET_CORPORATE_CUSTOMER_LIST", res.data);
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
  },
  modules: {},
});
