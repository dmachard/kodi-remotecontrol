<template>
  <v-app>
    <v-content>
      <RemoteControl/>
    </v-content>
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
