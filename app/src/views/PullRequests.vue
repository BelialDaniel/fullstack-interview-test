<template>
  <div>
    <div v-for="(pullRequest, index) in pullRequests" :key="index">
      <router-link :to="`/pull_requests/${pullRequest.id}`">
        <div>
          <div>{{ pullRequest.title }}</div>
          <div>{{ pullRequest.status }}</div>
        </div>
        <div>
          <div>{{ pullRequest.author.name }}</div>
          <div>{{ pullRequest.author.email }}</div>
        </div>
      </router-link>
    </div>
  </div>
</template>

<script lang="ts">
import { Options, Vue } from "vue-class-component";
import { getPullRequests } from "@/api/pullRequests.api";
import PullRequest from "@/models/pullRequest";

@Options({
  components: {},
})
export default class PullRequests extends Vue {
  pullRequests: Array<PullRequest> = [];

  mounted() {
    this.getPullRequestList();
  }

  async getPullRequestList() {
    try {
      const response: any = await getPullRequests();
      this.pullRequests = response.data;
    } catch (exception) {
      throw new Error(exception);
    }
  }
}
</script>

<style scoped>
.title {
  display: flex;
}
</style>
