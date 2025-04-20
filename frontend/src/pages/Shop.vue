<template>
  <div class="space-y-6">
    <h1 class="text-3xl font-bold">智能购物</h1>
    
    <div class="flex justify-between items-center">
      <div class="flex space-x-2">
        <button 
          v-for="category in categories" 
          :key="category.id"
          class="btn btn-outline"
          :class="{ 'btn-active': selectedCategory === category.id }"
          @click="selectedCategory = category.id"
        >
          {{ category.name }}
        </button>
      </div>
      
      <div class="relative">
        <input
          type="text"
          placeholder="搜索商品..."
          class="form-input pl-9"
          v-model="searchQuery"
        />
        <Search class="absolute left-3 top-1/2 transform -translate-y-1/2 h-4 w-4 text-gray-400" />
      </div>
    </div>
    
    <div class="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-4 gap-4">
      <div v-for="product in filteredProducts" :key="product.id" class="product-card">
        <div class="relative">
          <img :src="product.image" :alt="product.name" class="h-64 w-full object-cover rounded-t-lg" />
          <button 
            class="absolute top-2 right-2 btn-icon" 
            :class="{ 'favorite': product.isFavorite }"
            @click="toggleFavorite(product)"
          >
            <Heart :fill="product.isFavorite ? 'currentColor' : 'none'" class="h-4 w-4" />
          </button>
          
          <button class="absolute bottom-2 right-2 btn-icon" @click="showTryOn(product)">
            <Shirt class="h-4 w-4" />
          </button>
        </div>
        
        <div class="p-4">
          <div class="flex justify-between items-start">
            <div>
              <h3 class="font-medium">{{ product.name }}</h3>
              <p class="text-sm text-gray-500">{{ product.brand }}</p>
            </div>
            <div class="text-lg font-semibold">¥{{ product.price }}</div>
          </div>
          
          <div class="mt-4 flex space-x-2">
            <div 
              v-for="color in product.colors" 
              :key="color"
              class="color-option" 
              :style="{ backgroundColor: color }"
            ></div>
          </div>
          
          <button class="btn btn-primary w-full mt-4" @click="addToCart(product)">
            加入购物车
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { defineComponent, ref, computed } from 'vue';
import { Search, Heart, Shirt } from 'lucide-vue-next';
import { useRouter } from 'vue-router';

export default defineComponent({
  name: 'ShopPage',
  components: {
    Search,
    Heart,
    Shirt
  },
  setup() {
    const router = useRouter();
    const selectedCategory = ref('all');
    const searchQuery = ref('');
    
    const categories = ref([
      { id: 'all', name: '全部' },
      { id: 'tops', name: '上衣' },
      { id: 'bottoms', name: '下装' },
      { id: 'dresses', name: '连衣裙' },
      { id: 'shoes', name: '鞋子' }
    ]);
    
    const products = ref([
      {
        id: 1,
        name: '黑色宽松T恤',
        brand: 'Basics',
        price: 99,
        category: 'tops',
        image: '/images/shop/black-tshirt.jpg',
        colors: ['#000000', '#FFFFFF', '#808080'],
        isFavorite: false
      },
      {
        id: 2,
        name: '蓝色做旧牛仔裤',
        brand: 'Denim Co',
        price: 299,
        category: 'bottoms',
        image: '/images/shop/blue-jeans.jpg',
        colors: ['#0000FF', '#000000'],
        isFavorite: true
      },
      {
        id: 3,
        name: '白色连衣裙',
        brand: 'Elegance',
        price: 399,
        category: 'dresses',
        image: '/images/shop/white-dress.jpg',
        colors: ['#FFFFFF', '#FF0000', '#000000'],
        isFavorite: false
      },
      {
        id: 4,
        name: '黑色运动鞋',
        brand: 'Sport',
        price: 599,
        category: 'shoes',
        image: '/images/shop/black-sneakers.jpg',
        colors: ['#000000', '#FFFFFF'],
        isFavorite: false
      }
    ]);
    
    const filteredProducts = computed(() => {
      let result = products.value;
      
      // 按类别筛选
      if (selectedCategory.value !== 'all') {
        result = result.filter(product => product.category === selectedCategory.value);
      }
      
      // 按搜索关键词筛选
      if (searchQuery.value) {
        const query = searchQuery.value.toLowerCase();
        result = result.filter(product => 
          product.name.toLowerCase().includes(query) || 
          product.brand.toLowerCase().includes(query)
        );
      }
      
      return result;
    });
    
    const toggleFavorite = (product) => {
      product.isFavorite = !product.isFavorite;
    };
    
    const addToCart = (product) => {
      // 在实际应用中，这里会调用购物车API
      alert(`已将 ${product.name} 加入购物车`);
    };
    
    const showTryOn = (product) => {
      // 在实际应用中，这里会跳转到虚拟试穿页面并预加载该产品
      router.push({
        path: '/try-on',
        query: { productId: product.id }
      });
    };
    
    return {
      selectedCategory,
      searchQuery,
      categories,
      products,
      filteredProducts,
      toggleFavorite,
      addToCart,
      showTryOn
    };
  }
});
</script>

<style scoped>
.btn {
  @apply px-4 py-2 rounded-md font-medium;
}

.btn-outline {
  @apply border border-gray-300 text-gray-700 hover:bg-gray-50;
}

.btn-active {
  @apply bg-gray-100 border-gray-400;
}

.btn-primary {
  @apply bg-blue-500 text-white hover:bg-blue-600;
}

.btn-icon {
  @apply p-2 bg-white rounded-full shadow-sm hover:bg-gray-100;
}

.btn-icon.favorite {
  @apply text-red-500;
}

.form-input {
  @apply border-gray-300 rounded-md px-3 py-2 w-64 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent;
}

.product-card {
  @apply bg-white rounded-lg shadow-sm overflow-hidden transition-transform duration-200;
}

.product-card:hover {
  @apply transform translate-y-[-4px] shadow-md;
}

.color-option {
  @apply h-5 w-5 rounded-full border border-gray-300;
}
</style> 