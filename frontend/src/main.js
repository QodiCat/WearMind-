import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import './assets/tailwind.css';

// Create and mount the Vue application
const app = createApp(App);

// Use router
app.use(router);

// Mount the app to the DOM
app.mount('#app'); 