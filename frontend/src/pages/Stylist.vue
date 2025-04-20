<template>
  <div class="space-y-6">
    <h1 class="text-3xl font-bold">AI造型师</h1>
    
    <div class="grid gap-6 md:grid-cols-2">
      <div class="card">
        <div class="card-header">
          <h2 class="card-title">创建新搭配</h2>
        </div>
        <div class="card-content space-y-4">
          <div class="form-group">
            <label class="form-label">场合</label>
            <select class="form-select">
              <option value="casual">日常休闲</option>
              <option value="work">工作场合</option>
              <option value="date">约会</option>
              <option value="formal">正式场合</option>
              <option value="party">派对</option>
            </select>
          </div>
          
          <div class="form-group">
            <label class="form-label">天气</label>
            <select class="form-select">
              <option value="hot">炎热</option>
              <option value="warm">温暖</option>
              <option value="mild">温和</option>
              <option value="cool">凉爽</option>
              <option value="cold">寒冷</option>
            </select>
          </div>
          
          <div class="form-group">
            <label class="form-label">风格偏好</label>
            <select class="form-select">
              <option value="casual">休闲</option>
              <option value="formal">正式</option>
              <option value="streetwear">街头</option>
              <option value="minimal">简约</option>
              <option value="vintage">复古</option>
            </select>
          </div>
          
          <button class="btn btn-primary w-full">
            生成搭配建议
          </button>
        </div>
      </div>
      
      <div class="card">
        <div class="card-header">
          <h2 class="card-title">搭配建议</h2>
        </div>
        <div class="card-content">
          <div v-if="!recommendation" class="flex flex-col items-center justify-center h-64">
            <Wand2 class="h-16 w-16 text-gray-300 mb-4" />
            <p class="text-gray-500">填写左侧表单生成搭配建议</p>
          </div>
          
          <div v-else class="space-y-4">
            <div class="outfit-preview bg-gray-100 h-64 flex items-center justify-center rounded-lg">
              <!-- Outfit preview image would go here -->
              <img :src="recommendation.image" alt="Outfit" class="max-h-full" />
            </div>
            
            <div>
              <h3 class="font-medium text-lg">{{ recommendation.name }}</h3>
              <p class="text-gray-600">{{ recommendation.description }}</p>
            </div>
            
            <div class="grid grid-cols-4 gap-2">
              <div v-for="item in recommendation.items" :key="item.id" class="bg-gray-100 p-2 rounded">
                <img :src="item.image" :alt="item.name" class="h-20 w-full object-cover rounded" />
                <p class="text-xs text-gray-600 mt-1">{{ item.name }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { defineComponent, ref } from 'vue';
import { Wand2 } from 'lucide-vue-next';

export default defineComponent({
  name: 'StylistPage',
  components: {
    Wand2
  },
  setup() {
    const recommendation = ref(null);
    
    // 示例数据，在实际应用中会通过API获取
    // 在此处省略，可根据需要后续添加示例数据

    return {
      recommendation
    };
  }
});
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

.form-group {
  @apply space-y-2;
}

.form-label {
  @apply block text-sm font-medium text-gray-700;
}

.form-select {
  @apply block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500;
}

.btn {
  @apply px-4 py-2 rounded-md font-medium;
}

.btn-primary {
  @apply bg-blue-500 text-white hover:bg-blue-600;
}
</style> 