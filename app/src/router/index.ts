import { createRouter, createWebHashHistory, RouteRecordRaw } from "vue-router"
import BranchView from "../views/branches/Branch.vue"
import BranchesView from "../views/branches/Branches.vue"
import CommitView from "../views/commits/Commit.vue"
import CommitsView from "../views/commits/Commits.vue"
import PullRequestView from "../views/pull_requests/PullRequest.vue"
import PullRequestsView from "../views/pull_requests/PullRequests.vue"
import CreatePullRequestView from "../views/pull_requests/CreatePullRequest.vue"

const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
    name: "Home",
    component: BranchesView,
  },
  {
    path: "/branches/:pk",
    name: "Branch",
    component: BranchView,
  },
  {
    path: "/commits",
    name: "Commits",
    component: CommitsView,
  },
  {
    path: "/commits/:hash",
    name: "Commit",
    component: CommitView,
  },
  {
    path: "/pull_requests/",
    name: "PullRequests",
    component: PullRequestsView,
  },
  {
    path: "/pull_requests/:id",
    name: "PullRequest",
    component: PullRequestView,
  },
  {
    path: "/pull_requests/create",
    name: "CreatePullRequest",
    component: CreatePullRequestView,
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
]

const router = createRouter({
  history: createWebHashHistory(),
  routes,
})

export default router
