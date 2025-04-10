<template>
  <div class="relative">
    <div 
      class="avatar cursor-pointer"
      @click="isOpen = !isOpen"
      ref="avatarRef"
    >
      <img src="/avatars/default.png" alt="User" />
      <div v-if="!hasImage" class="avatar-fallback">U</div>
    </div>
    
    <div 
      v-if="isOpen" 
      class="dropdown-menu"
      ref="menuRef"
    >
      <div class="dropdown-item" @click="handleProfileClick">
        <User class="mr-2 h-4 w-4" />
        <span>Profile</span>
      </div>
      <div class="dropdown-item" @click="handleSettingsClick">
        <Settings class="mr-2 h-4 w-4" />
        <span>Settings</span>
      </div>
      <div class="dropdown-item" @click="handleLogoutClick">
        <LogOut class="mr-2 h-4 w-4" />
        <span>Logout</span>
      </div>
    </div>
  </div>
</template>

<script>
import { defineComponent, ref, onMounted, onUnmounted } from 'vue';
import { useRouter } from 'vue-router';
import { User, Settings, LogOut } from 'lucide-vue-next';

export default defineComponent({
  name: 'UserAvatar',
  components: {
    User,
    Settings,
    LogOut
  },
  setup() {
    const router = useRouter();
    const isOpen = ref(false);
    const hasImage = ref(true);
    const avatarRef = ref(null);
    const menuRef = ref(null);

    const handleProfileClick = () => {
      router.push('/profile');
      isOpen.value = false;
    };

    const handleSettingsClick = () => {
      router.push('/settings');
      isOpen.value = false;
    };

    const handleLogoutClick = () => {
      // Handle logout logic
      isOpen.value = false;
    };

    const handleClickOutside = (event) => {
      if (
        isOpen.value &&
        avatarRef.value && 
        !avatarRef.value.contains(event.target) &&
        menuRef.value && 
        !menuRef.value.contains(event.target)
      ) {
        isOpen.value = false;
      }
    };

    onMounted(() => {
      document.addEventListener('click', handleClickOutside);
    });

    onUnmounted(() => {
      document.removeEventListener('click', handleClickOutside);
    });

    return {
      isOpen,
      hasImage,
      avatarRef,
      menuRef,
      handleProfileClick,
      handleSettingsClick,
      handleLogoutClick
    };
  }
});
</script>

<style scoped>
.avatar {
  @apply h-8 w-8 rounded-full bg-gray-200 flex items-center justify-center overflow-hidden;
}

.avatar img {
  @apply h-full w-full object-cover;
}

.avatar-fallback {
  @apply text-sm font-semibold text-gray-600;
}

.dropdown-menu {
  @apply absolute right-0 mt-2 w-48 rounded-md shadow-lg bg-white ring-1 ring-black ring-opacity-5 py-1 z-10;
}

.dropdown-item {
  @apply flex items-center px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 cursor-pointer;
}
</style> 