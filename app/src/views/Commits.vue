<template>
  <div>
    <div v-for="commit in commits" :key="commit.key">
      <router-link :to="`/commits/${commit.key}`">
        <div>
          <span>{{ commit.author.name }}</span>
          <span>{{ commit.author.email }}</span>
        </div>
        <div>
          <span>{{ commit.key }}</span>
        </div>
      </router-link>
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
export default class Commits extends Vue {
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
