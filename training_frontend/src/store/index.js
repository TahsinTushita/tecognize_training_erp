import { createStore } from "vuex";
import axios from "axios";

axios.defaults.baseURL = "http://localhost:8080";

export default createStore({
  state: {
    instructorList: [],
  },
  mutations: {
    SET_INSTRUCTOR_LIST(state, instructorList) {
      state.instructorList = instructorList;
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
  },
  getters: {
    instructorList: (state) => {
      return state.instructorList;
    },
  },
  modules: {},
});
