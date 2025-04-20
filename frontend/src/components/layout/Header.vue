<template>
  <header class="bg-white shadow-sm">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between h-16">
        <div class="flex">
          <div class="flex-shrink-0 flex items-center">
            <router-link to="/" class="text-xl font-bold text-gray-900">
              AI智能衣橱
            </router-link>
          </div>
        </div>
        <div class="flex items-center">
          <user-avatar />
        </div>
      </div>
    </div>
  </header>
</template>

<script>
import { defineComponent } from 'vue';
import UserAvatar from '../common/UserAvatar.vue';

export default defineComponent({
  name: 'HeaderComponent',
  components: {
    UserAvatar
  }
});
</script> 