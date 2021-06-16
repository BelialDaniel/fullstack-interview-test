<template>
  <div v-if="branch">
    <div>
      <div>{{ branch.name }}</div>
      <div>
        <button>
          <router-link to="/pull_requests/create">Creatr PR</router-link>
        </button>
      </div>
    </div>
    <div v-for="commit in branch.commits" :key="commit.key">
      <div>
        <div>
          <span>{{ commit.author.name }}</span>
          <span>{{ commit.author.email }}</span>
        </div>
        <span>{{ commit.created_on }}</span>
      </div>
      <div>
        <span>{{ commit.key }}</span>
      </div>
      <div>{{ commit.message }}</div>
    </div>
  </div>
</template>

<script lang="ts">
import { Options, Vue } from "vue-class-component";
import { getBranch } from "@/api/branches.api";
import Branch from "@/models/branch";

@Options({
  components: {},
})
export default class BranchView extends Vue {
  branch: Branch | null = null;

  mounted() {
    this.getBranch();
  }

  async getBranch() {
    try {
      const branchName: string = this.$route.params.pk as string;
      const response: any = await getBranch(branchName);
      this.branch = response.data;
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
