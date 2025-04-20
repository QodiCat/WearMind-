<template>
  <div class="space-y-6">
    <h1 class="text-3xl font-bold">虚拟试衣间</h1>
    
    <div class="grid gap-6 md:grid-cols-3">
      <div class="card md:col-span-1">
        <div class="card-header">
          <h2 class="card-title">选择衣物</h2>
        </div>
        <div class="card-content space-y-4">
          <div class="form-group">
            <label class="form-label">衣物类型</label>
            <select v-model="selectedCategory" class="form-select">
              <option value="all">所有类型</option>
              <option value="tops">上衣</option>
              <option value="bottoms">下装</option>
              <option value="dresses">连衣裙</option>
              <option value="outerwear">外套</option>
            </select>
          </div>
          
          <div class="grid grid-cols-2 gap-2 max-h-96 overflow-y-auto">
            <div 
              v-for="item in filteredItems" 
              :key="item.id" 
              class="clothing-item cursor-pointer" 
              :class="{ 'selected': selectedItem && selectedItem.id === item.id }"
              @click="selectItem(item)"
            >
              <img :src="item.image" :alt="item.name" class="h-32 w-full object-cover rounded" />
              <p class="text-xs mt-1">{{ item.name }}</p>
            </div>
          </div>
        </div>
      </div>
      
      <div class="card md:col-span-2">
        <div class="card-header">
          <h2 class="card-title">试穿效果</h2>
        </div>
        <div class="card-content">
          <div v-if="!generatedImage" class="flex flex-col items-center justify-center h-96">
            <Camera class="h-16 w-16 text-gray-300 mb-4" />
            <p class="text-gray-500">从左侧选择衣物开始虚拟试穿</p>
            
            <div class="mt-6 space-y-2">
              <button 
                class="btn btn-outline w-full" 
                @click="uploadModelImage"
              >
                上传模特照片
              </button>
              <button 
                class="btn btn-outline w-full"
              >
                使用AI生成模特
              </button>
            </div>
          </div>
          
          <div v-else class="space-y-4">
            <div class="relative">
              <img :src="generatedImage" alt="Virtual Try-On" class="w-full rounded-lg" />
              
              <div class="absolute top-2 right-2 flex space-x-2">
                <button class="btn-icon">
                  <Download class="h-4 w-4" />
                </button>
                <button class="btn-icon">
                  <Share2 class="h-4 w-4" />
                </button>
              </div>
            </div>
            
            <div class="grid grid-cols-3 gap-2">
              <button 
                v-for="pose in poses" 
                :key="pose.id" 
                class="btn-pose" 
                :class="{ 'selected': selectedPose === pose.id }"
                @click="selectedPose = pose.id"
              >
                <img :src="pose.thumbnail" alt="Pose" class="h-16 w-full object-cover rounded" />
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { defineComponent, ref, computed } from 'vue';
import { Camera, Download, Share2 } from 'lucide-vue-next';

export default defineComponent({
  name: 'TryOnPage',
  components: {
    Camera,
    Download,
    Share2
  },
  setup() {
    const selectedCategory = ref('all');
    const selectedItem = ref(null);
    const generatedImage = ref(null);
    const selectedPose = ref(1);
    
    // 示例数据
    const clothingItems = ref([
      {
        id: 1,
        name: '黑色T恤',
        category: 'tops',
        image: '/images/black-tshirt.jpg'
      },
      {
        id: 2,
        name: '蓝色牛仔裤',
        category: 'bottoms',
        image: '/images/blue-jeans.jpg'
      },
      {
        id: 3,
        name: '白色连衣裙',
        category: 'dresses',
        image: '/images/white-dress.jpg'
      },
      {
        id: 4,
        name: '灰色卫衣',
        category: 'tops',
        image: '/images/grey-hoodie.jpg'
      }
    ]);
    
    const poses = ref([
      {
        id: 1,
        thumbnail: '/images/poses/pose1.jpg'
      },
      {
        id: 2,
        thumbnail: '/images/poses/pose2.jpg'
      },
      {
        id: 3,
        thumbnail: '/images/poses/pose3.jpg'
      }
    ]);
    
    const filteredItems = computed(() => {
      if (selectedCategory.value === 'all') {
        return clothingItems.value;
      }
      return clothingItems.value.filter(item => item.category === selectedCategory.value);
    });
    
    const selectItem = (item) => {
      selectedItem.value = item;
      // 在实际应用中，这里会调用API生成试穿图片
      // 示例中简单返回一个静态图片
      generatedImage.value = '/images/try-on-example.jpg';
    };
    
    const uploadModelImage = () => {
      // 在实际应用中，这里会打开文件上传对话框
      alert('此功能在实际应用中会打开文件上传对话框');
    };
    
    return {
      selectedCategory,
      selectedItem,
      clothingItems,
      filteredItems,
      generatedImage,
      poses,
      selectedPose,
      selectItem,
      uploadModelImage
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

.btn-outline {
  @apply border border-gray-300 text-gray-700 hover:bg-gray-50;
}

.btn-icon {
  @apply p-2 bg-white bg-opacity-75 rounded-full shadow-sm hover:bg-opacity-100;
}

.clothing-item {
  @apply border border-gray-200 rounded p-1 hover:border-blue-300;
}

.clothing-item.selected {
  @apply border-blue-500 ring-2 ring-blue-200;
}

.btn-pose {
  @apply border border-gray-200 rounded p-1 hover:border-blue-300;
}

.btn-pose.selected {
  @apply border-blue-500 ring-2 ring-blue-200;
}
</style> 