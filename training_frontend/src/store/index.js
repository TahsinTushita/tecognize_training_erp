import { createStore } from "vuex";
import axios from "axios";

axios.defaults.baseURL = "http://localhost:8080";

export default createStore({
  state: {
    instructorList: [],
    instructorCount: "",
    userList: [],
    userCount: "",
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

    getUserCount({ commit }) {
      axios("/api/users-count").then((res) => {
        commit("SET_USER_COUNT", res.data);
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
  },
  modules: {},
});
