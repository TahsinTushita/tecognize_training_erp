import { createRouter, createWebHistory } from "vue-router";
// import Home from "../views/Home.vue";
import AddInstructor from "../views/Instructor/AddInstructor.vue";
import InstructorList from "../views/Instructor/InstructorList.vue";
import InstructorDetails from "../views/Instructor/InstructorDetails.vue";
import InstructorLedger from "../views/Instructor/InstructorLedger.vue";
import InstructorPayment from "../views/Instructor/InstructorPayment.vue";
import AddUser from "../views/User/AddUser.vue";
import UserList from "../views/User/UserList.vue";
import UserLedger from "../views/User/UserLedger.vue";
import UserDetails from "../views/User/UserDetails.vue";
import NotFound from "../views/NotFound.vue";
import CategoryList from "../views/Category/CategoryList.vue";
import AddCourse from "../views/Course/AddCourse.vue";
import CourseList from "../views/Course/CourseList.vue";
import CourseDetails from "../views/Course/CourseDetails.vue";
import AddBatch from "../views/BatchFolder/AddBatch.vue";
import BatchList from "../views/BatchFolder/BatchList.vue";
import BatchDetails from "../views/BatchFolder/BatchDetails.vue";
import AddRetailCustomer from "../views/RetailCustomer/AddRetailCustomer.vue";
import RetailCustomerList from "../views/RetailCustomer/RetailCustomerList.vue";
import RetailCustomerDetails from "../views/RetailCustomer/RetailCustomerDetails.vue";
import AddCorporateCustomer from "../views/CorporateCustomer/AddCorporateCustomer.vue";
import CorporateCustomerList from "../views/CorporateCustomer/CorporateCustomerList.vue";
import CorporateCustomerDetails from "../views/CorporateCustomer/CorporateCustomerDetails.vue";
import Sale from "../views/Sale/Sale.vue";
import SaleRecords from "../views/Sale/SaleRecords.vue";
import Due from "../views/Sale/Due.vue";
import InstructorBatchLedger from "../views/Instructor/InstructorBatchLedger.vue";

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
    path: "/instructor-payment",
    name: "InstructorPayment",
    component: InstructorPayment,
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
    path: "/add-batch",
    name: "AddBatch",
    component: AddBatch,
  },
  {
    path: "/batch-list",
    name: "BatchList",
    component: BatchList,
  },
  {
    path: "/batch-details/:id",
    name: "BatchDetails",
    component: BatchDetails,
  },
  {
    path: "/add-retail-customer",
    name: "AddRetailCustomer",
    component: AddRetailCustomer,
  },
  {
    path: "/retail-customer-list",
    name: "RetailCustomerList",
    component: RetailCustomerList,
  },
  {
    path: "/retail-customer-details/:id",
    name: "RetailCustomerDetails",
    component: RetailCustomerDetails,
  },
  {
    path: "/add-corporate-customer",
    name: "AddCorporateCustomer",
    component: AddCorporateCustomer,
  },
  {
    path: "/corporate-customer-list",
    name: "CorporateCustomerList",
    component: CorporateCustomerList,
  },
  {
    path: "/corporate-customer-detials/:id",
    name: "CorporateCustomerDetails",
    component: CorporateCustomerDetails,
  },
  {
    path: "/sale",
    name: "Sale",
    component: Sale,
  },
  {
    path: "/sale-list",
    name: "SaleRecords",
    component: SaleRecords,
  },
  {
    path: "/due",
    name: "Due",
    component: Due,
  },
  {
    path: "/instructor-batch-ledger/:id",
    name: "InstructorBatchLedger",
    component: InstructorBatchLedger,
    props: true,
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
