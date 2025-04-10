<template>
  <div class="w-64 bg-white shadow-sm">
    <nav class="mt-5 px-2">
      <div class="space-y-1">
        <router-link
          v-for="item in navigation"
          :key="item.name"
          :to="item.href"
          :class="[
            'group flex items-center px-2 py-2 text-sm font-medium rounded-md',
            isActive(item.href)
              ? 'bg-gray-100 text-gray-900'
              : 'text-gray-600 hover:bg-gray-50 hover:text-gray-900'
          ]"
        >
          <component
            :is="item.icon"
            :class="[
              'mr-3 h-5 w-5',
              isActive(item.href)
                ? 'text-gray-500'
                : 'text-gray-400 group-hover:text-gray-500'
            ]"
          />
          {{ item.name }}
        </router-link>
      </div>
    </nav>
  </div>
</template>

<script>
import { defineComponent } from 'vue';
import { useRoute } from 'vue-router';
import { 
  Home, 
  Shirt, 
  Wand2, 
  ShoppingBag, 
  User, 
  Camera 
} from 'lucide-vue-next';

export default defineComponent({
  name: 'SidebarComponent',
  components: {
    Home, 
    Shirt, 
    Wand2, 
    ShoppingBag, 
    User, 
    Camera
  },
  setup() {
    const route = useRoute();
    
    const navigation = [
      { name: 'Dashboard', href: '/', icon: 'Home' },
      { name: 'My Wardrobe', href: '/wardrobe', icon: 'Shirt' },
      { name: 'AI Stylist', href: '/stylist', icon: 'Wand2' },
      { name: 'Virtual Try-On', href: '/try-on', icon: 'Camera' },
      { name: 'Shop', href: '/shop', icon: 'ShoppingBag' },
      { name: 'Profile', href: '/profile', icon: 'User' },
    ];

    const isActive = (path) => {
      return route.path === path;
    };

    return {
      navigation,
      isActive
    };
  }
});
</script> 