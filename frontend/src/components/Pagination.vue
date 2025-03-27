<template>
    <div class="pagination" v-if="totalPages > 1">
      <button :disabled="currentPage === 1" @click="prevPage">Anterior</button>
      <button
        v-for="page in visiblePages"
        :key="page"
        :class="{ active: page === currentPage }"
        @click="goToPage(page)"
      >
        {{ page }}
      </button>
      <button :disabled="currentPage === totalPages" @click="nextPage">Próxima</button>
    </div>
  </template>
  
  <script>
  export default {
    name: 'PaginationMain',
    props: {
      total: {
        type: Number,
        required: true,
      },
      limit: {
        type: Number,
        default: 25,
      },
      currentPage: {
        type: Number,
        default: 1,
      },
      maxButtons: {
        type: Number,
        default: 5,
      },
    },
    computed: {
      totalPages() {
        return Math.ceil(this.total / this.limit);
      },
      visiblePages() {
        const half = Math.floor(this.maxButtons / 2);
        let start = Math.max(1, this.currentPage - half);
        let end = Math.min(this.totalPages, start + this.maxButtons - 1);
  
        if (end - start + 1 < this.maxButtons) {
          start = Math.max(1, end - this.maxButtons + 1);
        }
  
        const pages = [];
        for (let i = start; i <= end; i++) {
          pages.push(i);
        }
        return pages;
      },
    },
    methods: {
      prevPage() {
        if (this.currentPage > 1) {
          this.$emit('change-page', this.currentPage - 1);
        }
      },
      nextPage() {
        if (this.currentPage < this.totalPages) {
          this.$emit('change-page', this.currentPage + 1);
        }
      },
      goToPage(page) {
        if (page !== this.currentPage) {
          this.$emit('change-page', page);
        }
      },
    },
  };
  </script>
  
<style scoped>
.pagination {
    display: flex;
    gap: 5px;
    justify-content: center;
    margin-top: 20px;
}

.pagination button {
    padding: 8px 12px;
    border: 1px solid #555;
    background: #f1efe3;
    border-radius: 5px;
    cursor: pointer;
    transition: all 0.3s ease;
}

.pagination button:hover {
    background: #dc5d51;
    color: #fff;
}

.pagination button.active {
    background: #dc5d51;
    color: #fff;
    font-weight: bold;
}

.pagination button:disabled {
    background: #ccc;
    cursor: not-allowed;
}
</style>