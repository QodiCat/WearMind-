<template>
  <div class="space-y-6">
    <div class="flex justify-between items-center">
      <h1 class="text-3xl font-bold">Profile</h1>
      <button class="btn btn-primary flex items-center">
        <Settings class="mr-2 h-4 w-4" />
        Edit Profile
      </button>
    </div>

    <div class="grid gap-4 md:grid-cols-3">
      <div class="card md:col-span-1">
        <div class="card-header">
          <h2 class="card-title">Profile Picture</h2>
        </div>
        <div class="card-content">
          <div class="flex flex-col items-center space-y-4">
            <div class="relative">
              <img
                src="/avatars/default.png"
                alt="Profile"
                class="h-32 w-32 rounded-full"
              />
              <button
                class="btn btn-icon absolute bottom-0 right-0 rounded-full"
              >
                <Camera class="h-4 w-4" />
              </button>
            </div>
            <button class="btn btn-outline flex items-center">
              <Wand2 class="mr-2 h-4 w-4" />
              Generate AI Avatar
            </button>
          </div>
        </div>
      </div>

      <div class="card md:col-span-2">
        <div class="card-header">
          <h2 class="card-title">Personal Information</h2>
        </div>
        <div class="card-content">
          <div class="grid gap-4">
            <div class="grid grid-cols-2 gap-4">
              <div class="space-y-2">
                <label class="text-sm font-medium">First Name</label>
                <input type="text" class="input" placeholder="John" />
              </div>
              <div class="space-y-2">
                <label class="text-sm font-medium">Last Name</label>
                <input type="text" class="input" placeholder="Doe" />
              </div>
            </div>
            <div class="space-y-2">
              <label class="text-sm font-medium">Email</label>
              <input type="email" class="input" placeholder="john@example.com" />
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="tabs-container">
      <div class="tabs">
        <button 
          v-for="tab in tabs" 
          :key="tab.value" 
          :class="['tab', { active: activeTab === tab.value }]"
          @click="activeTab = tab.value"
        >
          {{ tab.label }}
        </button>
      </div>

      <div v-if="activeTab === 'style'" class="tab-content">
        <div class="card">
          <div class="card-header">
            <h2 class="card-title">Style Preferences</h2>
          </div>
          <div class="card-content">
            <!-- Add style preferences form -->
          </div>
        </div>
      </div>

      <div v-if="activeTab === 'body'" class="tab-content">
        <div class="card">
          <div class="card-header">
            <h2 class="card-title">Body Measurements</h2>
          </div>
          <div class="card-content">
            <!-- Add body measurements form -->
          </div>
        </div>
      </div>

      <div v-if="activeTab === 'virtual'" class="tab-content">
        <div class="card">
          <div class="card-header">
            <h2 class="card-title">Virtual Model</h2>
          </div>
          <div class="card-content">
            <!-- Add virtual model settings -->
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue';
import { Settings, Camera, Wand2 } from 'lucide-vue-next';

export default {
  name: 'ProfilePage',
  components: {
    Settings,
    Camera,
    Wand2
  },
  setup() {
    const activeTab = ref('style');
    const tabs = [
      { label: 'Style Preferences', value: 'style' },
      { label: 'Body Measurements', value: 'body' },
      { label: 'Virtual Model', value: 'virtual' }
    ];

    return {
      activeTab,
      tabs
    };
  }
};
</script>

<style scoped>
.card {
  @apply bg-white shadow-sm rounded-lg;
}

.card-header {
  @apply px-4 py-5 border-b border-gray-200;
}

.card-title {
  @apply text-lg font-medium text-gray-900;
}

.card-content {
  @apply p-4;
}

.btn {
  @apply px-4 py-2 rounded-md font-medium;
}

.btn-primary {
  @apply bg-blue-500 text-white hover:bg-blue-600;
}

.btn-outline {
  @apply border border-gray-300 text-gray-700 hover:bg-gray-50;
}

.btn-icon {
  @apply p-2 bg-blue-500 text-white hover:bg-blue-600;
}

.input {
  @apply border-gray-300 rounded-md w-full px-3 py-2 shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent;
}

.tabs-container {
  @apply space-y-4;
}

.tabs {
  @apply flex space-x-2 border-b border-gray-200;
}

.tab {
  @apply px-4 py-2 text-sm font-medium text-gray-600 hover:text-gray-900;
}

.tab.active {
  @apply text-blue-600 border-b-2 border-blue-500;
}

.tab-content {
  @apply py-4;
}
</style> 