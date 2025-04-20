<template>
  <div class="space-y-6">
    <h1 class="text-3xl font-bold">首页</h1>
    
    <div class="grid gap-4 md:grid-cols-2 lg:grid-cols-4">
      <div class="card">
        <div class="card-header">
          <h2 class="card-title">今日搭配</h2>
          <Shirt class="h-4 w-4 text-muted-foreground" />
        </div>
        <div class="card-content">
          <div class="text-2xl font-bold">休闲星期五</div>
          <p class="text-xs text-muted-foreground">
            适合办公室场合
          </p>
        </div>
      </div>
      
      <div class="card">
        <div class="card-header">
          <h2 class="card-title">AI推荐</h2>
          <Wand2 class="h-4 w-4 text-muted-foreground" />
        </div>
        <div class="card-content">
          <div class="text-2xl font-bold">3个新推荐</div>
          <p class="text-xs text-muted-foreground">
            基于您的偏好
          </p>
        </div>
      </div>
      
      <div class="card">
        <div class="card-header">
          <h2 class="card-title">风格评分</h2>
          <TrendingUp class="h-4 w-4 text-muted-foreground" />
        </div>
        <div class="card-content">
          <div class="text-2xl font-bold">85%</div>
          <p class="text-xs text-muted-foreground">
            比上周提高2%
          </p>
        </div>
      </div>
      
      <div class="card">
        <div class="card-header">
          <h2 class="card-title">即将到来的活动</h2>
          <Calendar class="h-4 w-4 text-muted-foreground" />
        </div>
        <div class="card-content">
          <div class="text-2xl font-bold">2个</div>
          <p class="text-xs text-muted-foreground">
            需要搭配建议
          </p>
        </div>
      </div>
    </div>
    
    <div class="grid gap-4 md:grid-cols-2">
      <div class="card">
        <div class="card-header">
          <h2 class="card-title">最近的搭配</h2>
        </div>
        <div class="card-content">
          <!-- 添加最近的搭配网格 -->
        </div>
      </div>
      
      <div class="card">
        <div class="card-header">
          <h2 class="card-title">风格洞察</h2>
        </div>
        <div class="card-content">
          <!-- 添加风格洞察 -->
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { defineComponent } from 'vue';
import { Calendar, Shirt, Wand2, TrendingUp } from 'lucide-vue-next';

export default defineComponent({
  name: 'DashboardPage',
  components: {
    Calendar,
    Shirt,
    Wand2,
    TrendingUp
  }
});
</script>

<style scoped>
.card {
  @apply bg-white shadow-sm rounded-lg;
}

.card-header {
  @apply flex flex-row items-center justify-between space-y-0 pb-2 px-4 pt-4;
}

.card-title {
  @apply text-sm font-medium;
}

.card-content {
  @apply px-4 pb-4;
}

.text-muted-foreground {
  @apply text-gray-500;
}
</style> 