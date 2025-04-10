<template>
  <div class="min-h-screen bg-gray-50">
    <header-component />
    <div class="flex">
      <sidebar-component />
      <main class="flex-1 p-6">
        <slot></slot>
      </main>
    </div>
  </div>
</template>

<script>
import { defineComponent } from 'vue';
import HeaderComponent from './Header.vue';
import SidebarComponent from './Sidebar.vue';

export default defineComponent({
  name: 'LayoutComponent',
  components: {
    HeaderComponent,
    SidebarComponent
  }
});
</script> 