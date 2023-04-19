<template>
	<div id="building">
		<div class="us-container">
			<h1>登录</h1>
			<form :model="form" id="login-form" @submit.prevent="submit" novalidate>
				<div class="form-group">
					<label for="email">邮箱</label>
					<input v-model="form.email" type="email" id="email" name="email" required />
				</div>
				<div class="form-group">
					<label for="password">密码</label>
					<input v-model="form.password" type="password" id="password" name="password" required />
				</div>
				<div class="form-group">
					<button @click="go_register">注册</button>
					<button type="submit">登录</button>
				</div>
				<div class="form-group">
					<span class="error" id="login-error"></span>
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
import { post_login } from '@/api/users.js'
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
			console.log('aaaa', this.form);
			post_login(this.form).then(response => {
				console.log('响应成功', response);
				this.msg = 'succeed'
				// this.changeLogin({token: response.data})
				localStorage.setItem("token", response.data.token)
				this.$router.push('/home/things');
				this.$router.go(0)
			},
				error => {
					console.log('连接服务器失败', error);
					this.msg = "连接服务器失败"
				})
		},
		go_register() {
			console.log("执行跳转")
			this.$router.push('/users/register')
		}
	}
}
</script>

<!-- <template>
<el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
	<el-form-item label="用户名" prop="username">
	  <el-input v-model="ruleForm.username"></el-input>
	</el-form-item>
	<el-form-item label="密码" prop="password">
	  <el-input v-model="ruleForm.password"></el-input>
	</el-form-item>
	<el-form-item>
	  <el-button type="primary" @click="submitForm('ruleForm')">立即创建</el-button>
	  <el-button @click="resetForm('ruleForm')">重置</el-button>
	</el-form-item>
  </el-form>
  </template>
  <script>
	export default {
	  data() {
		return {
		  ruleForm: {
			password: '',
			username: ''
		  },
		  rules: {
			username: [
			  { required: true, message: '请输入用户', trigger: 'blur' }
			],
			password: [
			  { required: true, message: '请输入密码', trigger: 'blur' }
			],
		  }
		};
	  },
	  methods: {
		submitForm(formName) {
		  this.$refs[formName].validate((valid) => {
			if (valid) {
			  alert('submit!');
			} else {
			  console.log('error submit!!');
			  return false;
			}
		  });
		},
		resetForm(formName) {
		  this.$refs[formName].resetFields();
		}
	  }
	}
  </script> -->