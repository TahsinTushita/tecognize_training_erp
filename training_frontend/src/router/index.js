import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
import AddInstructor from "../views/Instructor/AddInstructor.vue";
import InstructorList from "../views/Instructor/InstructorList.vue";
import InstructorDetails from "../views/Instructor/InstructorDetails.vue";
import InstructorLedger from "../views/Instructor/InstructorLedger.vue";
import AddUser from "../views/User/AddUser.vue";
import UserList from "../views/User/UserList.vue";
import UserLedger from "../views/User/UserLedger.vue";
import UserDetails from "../views/User/UserDetails.vue";

const routes = [
  // {
  //   path: "/",
  //   name: "Home",
  //   component: Home,
  // },
  {
    path: "/add-instructor",
    name: "AddInstructor",
    component: AddInstructor,
  },
  {
    path: "/instructor-list",
    name: "InstructorList",
    component: InstructorList,
  },
  {
    path: "/instructor-details/:id",
    name: "InstructorDetails",
    component: InstructorDetails,
  },
  {
    path: "/instructor-ledger",
    name: "InstructorLedger",
    component: InstructorLedger,
  },
  {
    path: "/add-user",
    name: "AddUser",
    component: AddUser,
  },
  {
    path: "/user-list",
    name: "UserList",
    component: UserList,
  },
  {
    path: "/user-ledger",
    name: "UserLedger",
    component: UserLedger,
  },
  {
    path: "/user-details/:id",
    name: "UserDetails",
    component: UserDetails,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
