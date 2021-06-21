<template>
  <div v-if="pullRequest">
    <div>
      <div>
        <div>{{ pullRequest.title }}</div>
        <div>{{ pullRequest.status }}</div>
      </div>
      <div>
        <div>{{ pullRequest.author.name }}</div>
        <div>{{ pullRequest.author.email }}</div>
      </div>
      <div>
        <div>
          {{ pullRequest.description }}
        </div>
        <div>From Branch : {{ pullRequest.from_branch }}</div>
        <div>To Branch : {{ pullRequest.to_breanch }}</div>
      </div>
      <div v-if="pullRequest.status === 'open'">
        <button @click="mergePullRequest()">Merge</button>
        <button @click="closePullRequest()">Close</button>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Options, Vue } from "vue-class-component";
import { getPullRequest } from "@/api/pullRequests.api";
import PullRequest from "@/models/pullRequest";

@Options({
  components: {},
})
export default class PullRequestView extends Vue {
  pullRequest: PullRequest | null = null;

  mounted() {
    this.getPullRequestList();
  }

  async getPullRequestList() {
    try {
      const id: string = this.$route.params.id as string;
      const response: any = await getPullRequest(+id);
      this.pullRequest = response.data;
      console.log("Pull Request", this.pullRequest);
    } catch (exception) {
      throw new Error(exception);
    }
  }

  mergePullRequest() {
    console.log("Merge");
  }

  closePullRequest() {
    console.log("Close");
  }
}
</script>

<style scoped>
.title {
  display: flex;
}
</style>
