<template>
  <layout-component>
    <router-view />
  </layout-component>
</template>

<script>
import { defineComponent } from 'vue';
import LayoutComponent from './components/layout/Layout.vue';

export default defineComponent({
  name: 'App',
  components: {
    LayoutComponent
  }
});
</script>

<style>
@import 'tailwindcss/base';
@import 'tailwindcss/components';
@import 'tailwindcss/utilities';

body {
  @apply bg-gray-50;
}
</style> 