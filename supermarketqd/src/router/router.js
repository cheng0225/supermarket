
router.beforeEach((to, from, next) => {
    if (to.path === '/login') {
        next();
      } else {
        let token = localStorage.getItem('token');
     
        if (token === 'null' || token === '') {
          next('/login');
        } else {
          next();
        }
      }
})