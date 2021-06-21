<template>
  <div>
    <h1>Branches</h1>
    <div class="card mb-1" v-for="branch in branchList" :key="branch.pk">
      <div class="card-content">
        <router-link :to="`/branches/${branch.name}`">
          <span>{{ branch.name }}</span>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Options, Vue } from "vue-class-component";
import { getBranches } from "@/api/branches.api";
import BranchList from "@/models/branchList";

@Options({
  components: {},
})
export default class BranchesView extends Vue {
  branchList: Array<BranchList> = [];

  mounted() {
    this.getBranchList();
  }

  async getBranchList() {
    try {
      const response: any = await getBranches();
      this.branchList = response.data;
    } catch (exception) {
      throw new Error(exception);
    }
  }
}
</script>

<style>
.card-branch {
}
</style>
