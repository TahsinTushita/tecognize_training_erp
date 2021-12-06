import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
import AddInstructor from "../views/Instructor/AddInstructor.vue";
import InstructorList from "../views/Instructor/InstructorList.vue";
import InstructorDetails from "../views/Instructor/InstructorDetails.vue";
import InstructorLedger from "../views/Instructor/InstructorLedger.vue";

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
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
