<template>
  <div class="space-y-6">
    <h1 class="text-3xl font-bold">我的衣橱</h1>
    
    <div class="flex justify-between items-center">
      <div class="flex space-x-2">
        <button class="btn btn-outline">所有物品</button>
        <button class="btn btn-outline">上衣</button>
        <button class="btn btn-outline">下装</button>
        <button class="btn btn-outline">鞋子</button>
        <button class="btn btn-outline">配饰</button>
      </div>
      <button class="btn btn-primary flex items-center">
        <Plus class="mr-2 h-4 w-4" />
        添加物品
      </button>
    </div>
    
    <div class="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-4 gap-4">
      <div v-for="item in clothingItems" :key="item.id" class="card">
        <div class="card-image">
          <img :src="item.image" :alt="item.name" class="h-64 w-full object-cover" />
        </div>
        <div class="card-content">
          <h3 class="card-title">{{ item.name }}</h3>
          <p class="text-sm text-gray-500">{{ item.category }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { defineComponent, ref } from 'vue';
import { Plus } from 'lucide-vue-next';

export default defineComponent({
  name: 'WardrobePage',
  components: {
    Plus
  },
  setup() {
    const clothingItems = ref([
      {
        id: 1,
        name: '黑色T恤',
        category: '上衣',
        image: '/images/black-tshirt.jpg'
      },
      {
        id: 2,
        name: '蓝色牛仔裤',
        category: '下装',
        image: '/images/blue-jeans.jpg'
      },
      {
        id: 3,
        name: '白色运动鞋',
        category: '鞋子',
        image: '/images/white-sneakers.jpg'
      },
      {
        id: 4,
        name: '灰色卫衣',
        category: '上衣',
        image: '/images/grey-hoodie.jpg'
      }
    ]);

    return {
      clothingItems
    };
  }
});
</script>

<style scoped>
.card {
  @apply bg-white shadow-sm rounded-lg overflow-hidden;
}

.card-image img {
  @apply transition-transform duration-200;
}

.card:hover .card-image img {
  @apply scale-105;
}

.card-content {
  @apply p-4;
}

.card-title {
  @apply font-medium;
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
</style> 