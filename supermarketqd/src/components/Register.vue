
<template>
	<div class="container">
		<h1>注册</h1>
		<form id="register-form" action="http://127.0.0.1:8000/user/register" method="post">
			<!-- enctype="application/json" -->
			<div class="form-group">
				<label for="reg-username">用户名</label>
				<input type="text" id="reg-username" name="user_name" required />
			</div>
			<div class="form-group">
				<label for="reg-email">电子邮件</label>
				<input type="email" id="reg-email" name="email" required />
			</div>
			<div class="form-group">
				<label for="reg-password">密码</label>
				<input type="password" id="reg-password" name="password" required />
			</div>
			<div class="form-group">
				<label for="reg-password-confirm">确认密码</label>
				<input type="password" id="reg-password-confirm" name="password-confirm" required />
			</div>
			<div class="form-group">
				<button type="submit">注册</button>
			</div>
			<div class="form-group">
				<span class="error" id="register-error"></span>
			</div>
		</form>
	</div>
</template>

<style scoped>
/* @import '@/assets/css/css1.css'; */
@import '../../assets/css/css1.css';
</style>