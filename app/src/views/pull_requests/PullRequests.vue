<template>
  <div>
    <h1>Pull Requests</h1>
    <div class="card" v-for="(pullRequest, index) in pullRequests" :key="index">
      <router-link :to="`/pull_requests/${pullRequest.id}`">
        <div class="card-content">
          <div class="is-flex mb-1">
            <p class="title is-1 is-marginless">{{ pullRequest.title }}</p>
            <span
              class="tag ml-1"
              :class="[
                pullRequest.status === 'open' ? 'is-success' : 'is-danger',
              ]"
            >
              {{ pullRequest.status }}
            </span>
          </div>
          <div class="media">
            <div class="media-content">
              <p class="title is-4">
                {{ pullRequest.author.name }}
              </p>
              <p class="subtitle is-6">{{ pullRequest.author.email }}</p>
            </div>
          </div>
        </div>
      </router-link>
    </div>
  </div>
</template>

<script lang="ts">
import { Options, Vue } from "vue-class-component"
import { getPullRequests } from "@/api/pullRequests.api"
import PullRequest from "@/models/pullRequest"

@Options({
  components: {},
})
export default class PullRequestsView extends Vue {
  pullRequests: Array<PullRequest> = []

  mounted() {
    this.getPullRequestList()
  }

  async getPullRequestList() {
    try {
      const response: any = await getPullRequests()
      this.pullRequests = response.data
    } catch (exception) {
      throw new Error(exception)
    }
  }
}
</script>

<style scoped>
.title {
  display: flex;
}
</style>
