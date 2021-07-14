<template>
  <div v-if="pullRequest">
    <div class="is-flex">
      <h1>{{ pullRequest.title }}</h1>
      <span
        class="tag ml-2"
        :class="[pullRequest.status === 'open' ? 'is-success' : 'is-danger']"
      >
        {{ pullRequest.status }}
      </span>
    </div>
    <div class="card">
      <div class="card-content">
        <div class="media is-flex is-flex-direction-column">
          <div class="media-cotent mb-1">
            <p class="title is-5">
              {{ pullRequest.author.name }} {{ pullRequest.author.last_name }}
            </p>
            <p class="subtitle is-7">{{ pullRequest.author.email }}</p>
          </div>
          <div class="is-flex">
            <span class="tag is-primary mr-2">
              {{ pullRequest.from_branch }}
            </span>
            <span class="tag is-info">{{ pullRequest.to_branch }}</span>
          </div>
        </div>
        <div class="content">
          <p>
            {{ pullRequest.description }}
          </p>
        </div>
      </div>
      <footer class="card-footer" v-if="pullRequest.status === 'open'">
        <a class="card-footer-item" @click="mergePullRequest()"> Merge </a>
        <a class="card-footer-item" @click="closePullRequest()"> Close </a>
      </footer>
    </div>
  </div>
</template>

<script lang="ts">
import { Options, Vue } from "vue-class-component"
import { getPullRequest, merge, close } from "@/api/pullRequests.api"
import PullRequest from "@/models/pullRequest"

@Options({
  components: {},
})
export default class PullRequestView extends Vue {
  pullRequest: PullRequest | null = null

  mounted(): void {
    this.getPullRequestList()
  }

  async getPullRequestList(): Promise<void> {
    try {
      const id: string = this.$route.params.id as string
      const response: any = await getPullRequest(+id)
      this.pullRequest = response.data
      console.log("Pull Request", this.pullRequest)
    } catch (exception) {
      throw new Error(exception)
    }
  }

  async mergePullRequest(): Promise<void> {
    try {
      if (!this.pullRequest) {
        return
      }

      await merge(this.pullRequest.id)
      this.$router.push("pull_requests")
    } catch (exception) {
      throw new Error(exception)
    }
  }

  async closePullRequest(): Promise<void> {
    try {
      if (!this.pullRequest) {
        return
      }

      await close(this.pullRequest.id)
      this.$router.push("pull_requests")
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
