import { createRouter, createWebHashHistory, RouteRecordRaw } from "vue-router";
import Home from "../views/Home.vue";
import BranchView from "../views/Branch.vue";
import Commits from "../views/Commits.vue";
import Commit from "../views/Commit.vue";
import PullRequests from "../views/PullRequests.vue";
import PullRequestView from "../views/PullRequest.vue";
import CreatePullRequest from "../views/CreatePullRequest.vue";

const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/branches/:pk",
    name: "Branch",
    component: BranchView,
  },
  {
    path: "/commits",
    name: "Commits",
    component: Commits,
  },
  {
    path: "/commits/:hash",
    name: "Commit",
    component: Commit,
  },
  {
    path: "/pull_requests/",
    name: "PullRequests",
    component: PullRequests,
  },
  {
    path: "/pull_requests/:id",
    name: "PullRequest",
    component: PullRequestView,
  },
  {
    path: "/pull_requests/create",
    name: "CreatePullRequest",
    component: CreatePullRequest,
  },
  // {
  //   path: "/about",
  //   name: "About",
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () =>
  //     import(/* webpackChunkName: "about" */ "../views/About.vue"),
  // },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
