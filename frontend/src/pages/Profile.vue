<template>
  <div class="space-y-6">
    <div class="flex justify-between items-center">
      <h1 class="text-3xl font-bold">个人中心</h1>
      <button class="btn btn-primary flex items-center">
        <Settings class="mr-2 h-4 w-4" />
        编辑资料
      </button>
    </div>

    <div class="grid gap-4 md:grid-cols-3">
      <div class="card md:col-span-1">
        <div class="card-header">
          <h2 class="card-title">头像</h2>
        </div>
        <div class="card-content">
          <div class="flex flex-col items-center space-y-4">
            <div class="relative">
              <img
                src="/avatars/default.png"
                alt="头像"
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
              生成AI头像
            </button>
          </div>
        </div>
      </div>

      <div class="card md:col-span-2">
        <div class="card-header">
          <h2 class="card-title">个人信息</h2>
        </div>
        <div class="card-content">
          <div class="grid gap-4">
            <div class="grid grid-cols-2 gap-4">
              <div class="space-y-2">
                <label class="text-sm font-medium">姓</label>
                <input type="text" class="input" placeholder="张" />
              </div>
              <div class="space-y-2">
                <label class="text-sm font-medium">名</label>
                <input type="text" class="input" placeholder="三" />
              </div>
            </div>
            <div class="space-y-2">
              <label class="text-sm font-medium">邮箱</label>
              <input type="email" class="input" placeholder="zhangsan@example.com" />
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
            <h2 class="card-title">风格偏好</h2>
          </div>
          <div class="card-content">
            <!-- 添加风格偏好表单 -->
          </div>
        </div>
      </div>

      <div v-if="activeTab === 'body'" class="tab-content">
        <div class="card">
          <div class="card-header">
            <h2 class="card-title">身体数据</h2>
          </div>
          <div class="card-content">
            <!-- 添加身体测量表单 -->
          </div>
        </div>
      </div>

      <div v-if="activeTab === 'virtual'" class="tab-content">
        <div class="card">
          <div class="card-header">
            <h2 class="card-title">虚拟模型</h2>
          </div>
          <div class="card-content">
            <!-- 添加虚拟模型设置 -->
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
      { label: '风格偏好', value: 'style' },
      { label: '身体数据', value: 'body' },
      { label: '虚拟模型', value: 'virtual' }
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