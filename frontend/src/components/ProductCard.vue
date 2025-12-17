<template>
  <div class="bg-white rounded-lg shadow-sm overflow-hidden hover:shadow-md transition-shadow relative">

    <!-- Уведомление -->
    <Transition name="fade-slide">
      <div v-if="showNotification" class="notification-box">
        <div class="notification-icon">
          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M5 13l4 4L19 7"
            />
          </svg>
        </div>
        <p class="notification-title">Добавлено в корзину!</p>
      </div>
    </Transition>

    <!-- Картинка -->
    <div
      class="aspect-square bg-gray-200 flex items-center justify-center cursor-pointer"
      @click="$emit('view-product', product.id)"
    >
      <img
        v-if="product.image_url"
        :src="product.image_url"
        :alt="product.name"
        class="w-full h-full object-cover"
      />
      <span v-else class="text-gray-400">Нет фото</span>
    </div>

    <!-- Контент -->
    <div class="p-4">
      <span class="text-xs text-blue-600 font-medium">
        {{ product.category.name }}
      </span>

      <h3
        class="font-semibold text-gray-900 mt-1 mb-2 cursor-pointer hover:text-blue-600"
        @click="$emit('view-product', product.id)"
      >
        {{ product.name }}
      </h3>

      <p
        v-if="product.description"
        class="text-sm text-gray-600 mb-3 line-clamp-2"
      >
        {{ product.description }}
      </p>

      <div class="flex items-center justify-between mt-4">
        <span class="text-xl font-bold text-gray-900">
          ${{ product.price.toFixed(2) }}
        </span>

        <button
          @click="handleAddToCart"
          :disabled="showNotification"
          class="px-4 py-2 bg-blue-600 text-white rounded-lg
                 hover:bg-blue-700 transition-colors
                 disabled:opacity-50 disabled:cursor-not-allowed"
        >
          В корзину
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const props = defineProps({
  product: {
    type: Object,
    required: true,
  },
});

const emit = defineEmits(['add-to-cart', 'view-product']);

const showNotification = ref(false);

function handleAddToCart() {
  emit('add-to-cart', props.product.id);

  showNotification.value = true;

  setTimeout(() => {
    showNotification.value = false;
  }, 2000);
}
</script>

<style scoped>
/* Обрезка текста */
.line-clamp-2 {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

/* Уведомление */
.notification-box {
  position: absolute;
  top: 12px;
  left: 12px;
  right: 12px;

  padding: 14px 16px;
  background: linear-gradient(135deg, #10b981 0%, #059669 100%);
  border-radius: 12px;

  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;

  z-index: 20;
  box-shadow: 0 6px 16px rgba(16, 185, 129, 0.35);
}

.notification-icon {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background-color: rgba(255, 255, 255, 0.2);

  display: flex;
  align-items: center;
  justify-content: center;

  color: white;
  flex-shrink: 0;
}

.notification-title {
  color: white;
  font-weight: 600;
  font-size: 14px;
  margin: 0;
}

/* Анимация */
.fade-slide-enter-active {
  animation: fadeSlideDown 0.35s ease-out;
}

.fade-slide-leave-active {
  animation: fadeSlideUp 0.25s ease-in;
}

@keyframes fadeSlideDown {
  from {
    opacity: 0;
    transform: translateY(-15px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes fadeSlideUp {
  from {
    opacity: 1;
    transform: translateY(0);
  }
  to {
    opacity: 0;
    transform: translateY(-10px);
  }
}
</style>
