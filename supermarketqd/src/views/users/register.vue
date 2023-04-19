<template>
    <div id="building">
        <div class="us-container">
            <h1>注册</h1>
            <form :model="form" id="login-form" @submit.prevent="submit" novalidate>
                <div class="form-group">
                    <label for="user">用户名</label>
                    <input v-model="form.user" type="text" id="user" name="user" required />
                </div>
                <div class="form-group">
                    <label for="email">邮箱</label>
                    <input v-model="form.email" type="email" id="email" name="email" required />
                </div>
                <div class="form-group">
                    <label for="password">密码</label>
                    <input v-model="form.password" type="password" id="password" name="password" required />
                </div>
                <div class="form-group">
                    <span class="error" id="register-error"></span>
                </div>
                <div class="form-group">
                    <button @click="go_home">取消</button>
                    <button type="submit">注册</button>
                </div>
            </form>
        </div>
    </div>
</template>

<style scoped>
@import '../../assets/css/css1.css';
</style>

<script>
// Vue.config.productionTip = false
import { post_register } from '@/api/users.js'
export default {
    name: 'Login',
    data() {
        return {
            form: {},
            msg: '',
        }
    },
    methods: {
        submit() {
            console.log('aaa', this.form);
            post_register(this.form).then(response => {
                console.log('响应成功', response);
                this.msg = 'succeed'
                // this.changeLogin({token: response.data})
                localStorage.setItem("token", response.data.token)
                this.$router.push('/users/login');
            },
                error => {
                    console.log('连接服务器失败', error);
                    this.msg = "连接服务器失败"
                })
        },
        go_home() {
            console.log("执行跳转")
            this.$router.push('/home/things')
        }
    }
}
</script>
