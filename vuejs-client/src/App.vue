<template>
  <v-app>
    <v-main>
      <RemoteControl/>
    </v-main>
  </v-app>
</template>

<script>
import RemoteControl from './components/RemoteControl';

export default {
  name: 'App',

  components: {
    RemoteControl,
  },

  data: () => ({
  }),
};
</script>
