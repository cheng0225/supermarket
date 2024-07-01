<template>
    <div>
      <h1>监测页面关闭示例</h1>
    </div>
  </template>
  
  <script>
  export default {
    mounted() {
      // 添加beforeunload事件监听器
      window.addEventListener('beforeunload', this.handleBeforeUnload);
      // 添加unload事件监听器
      window.addEventListener('unload', this.handleUnload);
      // 重置sessionStorage中的状态
      sessionStorage.setItem('isFirstUnload', 'true');
    },
    beforeDestroy() {
      // 移除beforeunload事件监听器
      window.removeEventListener('beforeunload', this.handleBeforeUnload);
      // 移除unload事件监听器
      window.removeEventListener('unload', this.handleUnload);
    },
    methods: {
      handleBeforeUnload(event) {
        // 自定义提示消息
        const message = '你确定要离开吗？';
        event.returnValue = message; // 标准兼容方式
        return message; // 旧的浏览器兼容方式
      },
      handleUnload(event) {
        const isFirstUnload = sessionStorage.getItem('isFirstUnload');
        if (isFirstUnload === 'true') {
          // 执行一些操作
          console.log('页面即将关闭或刷新');
          // 标记为已卸载
          sessionStorage.setItem('isFirstUnload', 'false');
        }
      }
    }
  };
  </script>
  
  <style scoped>
  /* 你的样式 */
  </style>
  