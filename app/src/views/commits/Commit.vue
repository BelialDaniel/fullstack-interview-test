<template>
  <div v-if="commitData">
    <div>
      <div>{{ commitData.author.name }}</div>
      <div>{{ commitData.author.email }}</div>
    </div>
    <div>
      <span>{{ commitData.key }}</span>
    </div>
    <div v-if="commitData && commitData.files">
      <div>Modified Files: {{ commitData.files.count }}</div>
      <div v-for="(item, index) in commitData.files.names" :key="index">
        <div>
          <div>{{ item.name }}</div>
          <div>{{ item.path }}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Options, Vue } from "vue-class-component";
import { getCommit } from "@/api/commits.api";
import Commit from "@/models/commit";

@Options({
  components: {},
})
export default class CommitView extends Vue {
  commitData: Commit | null = null;

  mounted() {
    this.getCommit();
  }

  async getCommit() {
    try {
      const commitHash: string = this.$route.params.hash as string;
      const response: any = await getCommit(commitHash);
      this.commitData = response.data;
    } catch (exception) {
      throw new Error(exception);
    }
  }
}
</script>
