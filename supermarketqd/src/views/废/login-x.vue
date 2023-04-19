<template>
	<div>
		<h3>
			<span style="display:inline-block;width:200px;text-align:right;">用户登录</span>
		</h3>
		<form action="" method="post" @submit.prevent="submit">
			<p>
				<span style="display:inline-block;width:80px;text-align:right;">用户名：</span>
				<input type="text" v-model="username" value="" autocomplete>
				<i v-if="unerror" style="color: #ff0000;font-size: small;">{{unerror}}</i>
			</p>
			<p>
				<span style="display:inline-block;width:80px;text-align:right;">密码：</span>
				<input type="password" v-model="password" value="" autocomplete>
				<i v-if="pwerror" style="color: #ff0000;font-size: small;">{{pwerror}}</i>
			</p>
			<span style="display:inline-block;width:160px;text-align:right;">
				<!-- disabled需使用v-bind绑定 -->
				<input type="submit" value="登录">
			</span>
		</form>
		<!-- 正常识别\n -->
		<div style="white-space: pre-line;">{{message}}</div>
		<p>{{cktest}}</p>
		<form style="display: inline" @click="main">
			<button type="button">主页</button>
		</form>
	</div>
</template>

<script>

import {post_login} from '@/api/users';
	export default {
		// 数据
		data() {
			return {
				list: "",
				unerror: "",
				pwerror: "",
				username: "",
				password: "",
				message: "",
				cktest: "",
			};
		},
		methods: {
			// 提交post
			submit: function(event) {
				var un = "";
				var pw = "";
				var n = -1;
				if (this.username == null || this.username == "") {
					this.unerror = "用户名不能为空";
				} else {
					un = this.username;
				}
				if (this.password == null || this.password == "") {
					this.pwerror = "密码不能为空";
				} else {
					pw = this.password;
				}
				if (this.password != null && this.password != "" && this.username != null && this.username != "") {
					var formData = JSON.stringify({
						username: un,
						password: pw
					});
					post_login(formData).then(response => {
						// success callback
						console.log(response);
						this.message = "\n返回: " + response.data.msg;
						// test 简单解决samesite问题，在前端添加cookie
						if(response.data.error_num == 0){
							document.cookie = "username="+response.data.name+"; id="+response.data.id
							// window.localStorage.setItem("username",response.data.username);
							this.cktest = document.cookie;
							this.$router.push("/home/things");
						}
					}, error => {
						// error callback
						console.log(error);
						// this.message = "\n返回: " + error.data.msg;
					});
				}
			},
			// 返回主页
			main() {
				this.$router.push("/");
			},
		},
		watch: {
			username: function() {
				if (this.username != null) {
					sessionStorage.setItem("lusername", this.username);
					if (this.username.length != 0) {
						this.unerror = "";
					}
				}
			},
			password: function() {
				if (this.password != null) {
					sessionStorage.setItem("lpassword", this.password);
					if (this.password.length != 0) {
						this.pwerror = "";
					}
				}
			},
		},
		created() {
			// 获取缓存
			if (this.username != null) {
				this.username = sessionStorage.getItem("lusername");
			}
			if (this.password != null) {
				this.password = sessionStorage.getItem("lpassword");
			}
		},
	}
</script>

<style>
</style>




