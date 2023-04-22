<template>
  <div id="app">
    <div v-for="user in users" :key="user.id">
      {{ user.name }}
    </div>
  </div>
</template>

<script>
import api from "@/services/api";

export default {
  name: "App",
  data() {
    return {
      users: [],
    };
  },
  async created() {
    const response = await api.getUsers();
    this.users = response.data;
  },
};
</script>
