<template>
  <div>
    <div id="nav">
      <router-link to="/">Branches</router-link> |
      <router-link to="/commits">Commits</router-link> |
      <router-link to="/pull_requests">Pull requests</router-link>
    </div>
    <div id="main-layut">
      <slot />
    </div>
    <div>
      <slot name="footer" />
    </div>
  </div>
</template>
