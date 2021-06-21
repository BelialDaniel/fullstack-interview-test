<template>
  <div>
    <form @submit.prevent>
      <h1>Author</h1>
      <div>
        <label for="name">Name</label>
        <input type="text" v-model.trim="pullRequest.author.name" id="name" />
      </div>
      <div>
        <label for="last_name">Last name</label>
        <input
          type="text"
          v-model.trim="pullRequest.author.last_name"
          id="last_name"
        />
      </div>
      <div>
        <label for="email">Email</label>
        <input
          type="text"
          v-model.trim="pullRequest.author.email"
          placeholder="mail@email.com"
          id="email"
        />
      </div>
      <h1>Pull request</h1>
      <div>
        <label for="title">Title</label>
        <input type="text" v-model.trim="pullRequest.title" id="title" />
      </div>
      <div>
        <div>
          <label for="description">Description</label>
        </div>
        <textarea
          type="text"
          v-model.trim="pullRequest.description"
          id="description"
        />
      </div>
      <div>
        From Branch
        <select v-model.trim="pullRequest.from_branch">
          <option
            v-for="branch in branches"
            :value="branch.name"
            :key="branch.name"
          >
            {{ branch.name }}
          </option>
        </select>
      </div>
      <div>
        To Branch
        <select v-model.trim="pullRequest.to_breanch">
          <option
            v-for="branch in branches"
            :value="branch.name"
            :key="branch.name"
          >
            {{ branch.name }}
          </option>
        </select>
      </div>
      <button class="button" @click="submitPullRequest">
        Create pull request
      </button>
    </form>
  </div>
</template>

<script lang="ts">
import { Options, Vue } from "vue-class-component";
import { createPullRequest } from "@/api/pullRequests.api";
import { getBranches } from "@/api/branches.api";
import BranchList from "@/models/branchList";
import PullRequest from "@/models/pullRequest";

@Options({
  components: {},
})
export default class CreatePullRequestView extends Vue {
  branches: Array<BranchList> = [];
  pullRequest: PullRequest = {
    author: {
      name: "",
      last_name: "",
      email: "",
    },
    title: "",
    description: "",
    status: "open",
    from_branch: "",
    to_breanch: "",
  };

  mounted() {
    this.init();
  }

  async init() {
    try {
      const response: any = await getBranches();
      this.branches = response.data;
    } catch (exception) {
      throw new Error(exception);
    }
  }

  async submitPullRequest() {
    const from_branch: string = this.pullRequest.from_branch;
    const to_branch: string = this.pullRequest.to_breanch;

    if (!from_branch || !to_branch) {
      alert("Missing Branches for Merge request");
    }

    try {
      await createPullRequest(this.pullRequest);
      this.$router.push("/pull_requests");
    } catch (exception) {
      alert(exception.errors);
    }
  }
}
</script>
