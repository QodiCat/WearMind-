import { createRouter, createWebHistory } from 'vue-router';

// Lazy-load components
const Dashboard = () => import('../pages/Dashboard.vue');
const Wardrobe = () => import('../pages/Wardrobe.vue');
const Stylist = () => import('../pages/Stylist.vue');
const TryOn = () => import('../pages/TryOn.vue');
const Shop = () => import('../pages/Shop.vue');
const Profile = () => import('../pages/Profile.vue');

const routes = [
  {
    path: '/',
    name: 'Dashboard',
    component: Dashboard
  },
  {
    path: '/wardrobe',
    name: 'Wardrobe',
    component: Wardrobe
  },
  {
    path: '/stylist',
    name: 'Stylist',
    component: Stylist
  },
  {
    path: '/try-on',
    name: 'TryOn',
    component: TryOn
  },
  {
    path: '/shop',
    name: 'Shop',
    component: Shop
  },
  {
    path: '/profile',
    name: 'Profile',
    component: Profile
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router; 