<template>
  <div>
    <nav class="navbar is-dark">
      <div class="navbar-end mr-3">
        <router-link class="navbar-item" to="/">Branches</router-link>
        <router-link class="navbar-item" to="/commits">Commits</router-link>
        <router-link class="navbar-item" to="/pull_requests">
          Pull requests
        </router-link>
      </div>
    </nav>
    <div id="main-layut" class="main content">
      <slot />
    </div>
    <div>
      <slot name="footer" />
    </div>
  </div>
</template>

<style>
.main {
  margin: 2rem;
}
</style>
