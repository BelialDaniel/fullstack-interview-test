<template>
  <div v-if="commitData">
    <h1>{{ commitData.key }}</h1>
    <div class="card">
      <div class="card-content">
        <div class="media">
          <div class="media-content">
            <p class="title is-4">{{ commitData.author.name }}</p>
            <p class="subtitle is-6">{{ commitData.author.email }}</p>
          </div>
        </div>
        <div>
          <h5>Modified Files: {{ commitData.files.count }}</h5>
          <ul v-for="(item, index) in commitData.files.names" :key="index">
            <li>
              <div class="heading">{{ item.name }}</div>
              <div class="title is-7">{{ item.path }}</div>
            </li>
          </ul>
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
