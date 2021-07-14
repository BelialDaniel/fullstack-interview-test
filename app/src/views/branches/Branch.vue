<template>
  <div v-if="branch">
    <div class="pb-1">
      <h1 class="">{{ branch.name }}</h1>
      <button class="button small is-outlined mb-2">
        <router-link to="/pull_requests/create">
          Create Pull Rrequest
        </router-link>
      </button>
    </div>
    <div>
      <div class="card mb-1" v-for="commit in branch.commits" :key="commit.key">
        <div class="card-content">
          <div class="media">
            <div class="media-content">
              <p class="title is-4">{{ commit.author.name }}</p>
              <p class="subtitle is-6">{{ commit.author.email }}</p>
              <p class="subtitle is-6">{{ commit.key }}</p>
            </div>
          </div>
          <p>
            {{ commit.message }}
          </p>
          <time> {{ commit.created_on }}</time>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Options, Vue } from "vue-class-component"
import { getBranch } from "@/api/branches.api"
import Branch from "@/models/branch"

@Options({
  components: {},
})
export default class BranchView extends Vue {
  branch: Branch | null = null

  mounted() {
    this.getBranch()
  }

  async getBranch() {
    try {
      const branchName: string = this.$route.params.pk as string
      const response: any = await getBranch(branchName)
      this.branch = response.data
    } catch (exception) {
      throw new Error(exception)
    }
  }

  onClick() {
    console.log("Clicked xD")
  }
}
</script>

<style scoped>
.title {
  display: flex;
}
</style>
