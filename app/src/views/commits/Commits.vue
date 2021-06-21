<template>
  <div>
    <h1>Commits</h1>
    <div class="card mb-1" v-for="commit in commits" :key="commit.key">
      <div class="card-content">
        <router-link :to="`/commits/${commit.key}`">
          <div class="media">
            <div class="media-content">
              <p class="title is-4">{{ commit.author.name }}</p>
              <p class="subtitle is-6">{{ commit.author.email }}</p>
            </div>
          </div>
          <div>
            <span>{{ commit.key }}</span>
          </div>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Options, Vue } from "vue-class-component";
import { getCommits } from "@/api/commits.api";
import Commit from "@/models/commit";

@Options({
  components: {},
})
export default class CommitsView extends Vue {
  commits: Array<Commit> = [];

  mounted() {
    this.getCommits();
  }

  async getCommits() {
    try {
      const response: any = await getCommits();
      this.commits = response.data;
    } catch (exception) {
      throw new Error(exception);
    }
  }
}
</script>
