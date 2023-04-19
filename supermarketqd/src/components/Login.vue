<!-- <!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<link href='css1.css' type='text/css' rel='stylesheet' />
		<title></title>
	</head>
	<body> -->
<template>
	<div class="container">
		<h1>登录</h1>
		<form id="login-form" action="http://127.0.0.1:8000/user/login" method="post">
			<div class="form-group">
				<label for="username">用户名</label>
				<input type="text" id="username" name="username" required />
			</div>
			<div class="form-group">
				<label for="password">密码</label>
				<input type="password" id="password" name="password" required />
			</div>
			<div class="form-group">
				<button type="submit">登录</button>
			</div>
			<div class="form-group">
				<span class="error" id="login-error"></span>
			</div>
		</form>
	</div>
</template>

<style scoped>
/* @import '@/assets/css/css1.css'; */
@import '../assets/css/css1.css';
</style>