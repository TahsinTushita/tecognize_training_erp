import { createRouter, createWebHistory } from "vue-router";
// import Home from "../views/Home.vue";
import AddInstructor from "../views/Instructor/AddInstructor.vue";
import InstructorList from "../views/Instructor/InstructorList.vue";
import InstructorDetails from "../views/Instructor/InstructorDetails.vue";
import InstructorLedger from "../views/Instructor/InstructorLedger.vue";
import AddUser from "../views/User/AddUser.vue";
import UserList from "../views/User/UserList.vue";
import UserLedger from "../views/User/UserLedger.vue";
import UserDetails from "../views/User/UserDetails.vue";
import NotFound from "../views/NotFound.vue";
import CategoryList from "../views/Category/CategoryList.vue";
import AddCourse from "../views/Course/AddCourse.vue";
import CourseList from "../views/Course/CourseList.vue";
import CourseDetails from "../views/Course/CourseDetails.vue";

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
    props: true,
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
    props: true,
  },
  {
    path: "/category-list",
    name: "CategoryList",
    component: CategoryList,
  },
  {
    path: "/add-course",
    name: "AddCourse",
    component: AddCourse,
  },
  {
    path: "/course-list",
    name: "CourseList",
    component: CourseList,
  },
  {
    path: "/course-details/:id",
    name: "CourseDetails",
    component: CourseDetails,
  },
  {
    path: "/:catchAll(.*)",
    name: "NotFound",
    component: NotFound,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
