<template>
  <div class="card">
    <div v-for="branch in branchList" :key="branch.pk">
      <router-link :to="`/branches/${branch.name}`">
        <div>
          <span>Name:</span>
          <span>{{ branch.name }}</span>
        </div>
      </router-link>
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
