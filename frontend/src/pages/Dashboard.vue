<template>
  <div class="space-y-6">
    <h1 class="text-3xl font-bold">Dashboard</h1>
    
    <div class="grid gap-4 md:grid-cols-2 lg:grid-cols-4">
      <div class="card">
        <div class="card-header">
          <h2 class="card-title">Today's Outfit</h2>
          <Shirt class="h-4 w-4 text-muted-foreground" />
        </div>
        <div class="card-content">
          <div class="text-2xl font-bold">Casual Friday</div>
          <p class="text-xs text-muted-foreground">
            Perfect for the office
          </p>
        </div>
      </div>
      
      <div class="card">
        <div class="card-header">
          <h2 class="card-title">AI Recommendations</h2>
          <Wand2 class="h-4 w-4 text-muted-foreground" />
        </div>
        <div class="card-content">
          <div class="text-2xl font-bold">3 New</div>
          <p class="text-xs text-muted-foreground">
            Based on your preferences
          </p>
        </div>
      </div>
      
      <div class="card">
        <div class="card-header">
          <h2 class="card-title">Style Score</h2>
          <TrendingUp class="h-4 w-4 text-muted-foreground" />
        </div>
        <div class="card-content">
          <div class="text-2xl font-bold">85%</div>
          <p class="text-xs text-muted-foreground">
            +2% from last week
          </p>
        </div>
      </div>
      
      <div class="card">
        <div class="card-header">
          <h2 class="card-title">Upcoming Events</h2>
          <Calendar class="h-4 w-4 text-muted-foreground" />
        </div>
        <div class="card-content">
          <div class="text-2xl font-bold">2</div>
          <p class="text-xs text-muted-foreground">
            Need outfit suggestions
          </p>
        </div>
      </div>
    </div>
    
    <div class="grid gap-4 md:grid-cols-2">
      <div class="card">
        <div class="card-header">
          <h2 class="card-title">Recent Outfits</h2>
        </div>
        <div class="card-content">
          <!-- Add recent outfits grid -->
        </div>
      </div>
      
      <div class="card">
        <div class="card-header">
          <h2 class="card-title">Style Insights</h2>
        </div>
        <div class="card-content">
          <!-- Add style insights -->
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