<template>
	<div class="demo-block demo-zh-CN demo-form">
		<div class="us-container">
			<el-form :model="ruleForm" status-icon :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
				<el-form-item label="密码" prop="pass">
					<el-input type="password" v-model="ruleForm.pass" autocomplete="off"></el-input>
				</el-form-item>
				<el-form-item label="确认密码" prop="checkPass">
					<el-input type="password" v-model="ruleForm.checkPass" autocomplete="off"></el-input>
				</el-form-item>
				<el-form-item>
					<el-button @click="resetForm('ruleForm')">重置</el-button>
					<el-button type="primary" @click="submitForm('ruleForm')">注册</el-button>
				</el-form-item>
			</el-form>
		</div>
	</div>
</template>

<style scoped>
/* @import '../../assets/css/css1.css'; */

/* element.style {
} */
/* .demo-block .source {
	padding: 24px;
}

div {
	display: block;
} */

.us-container {
	max-width: 600px;
	margin: 10% auto;
	background-color: #fff;
	border-radius: 5px;
	box-shadow: 0px 0px 5px #ddd;
	padding: 20px;
} 
</style>

<script>
export default {
	data() {
		var validatePass = (rule, value, callback) => {
			if (value === '') {
				callback(new Error('请输入密码'));
			} else {
				if (this.ruleForm.checkPass !== '') {
					this.$refs.ruleForm.validateField('checkPass');
				}
				callback();
			}
		};
		var validatePass2 = (rule, value, callback) => {
			if (value === '') {
				callback(new Error('请再次输入密码'));
			} else if (value !== this.ruleForm.pass) {
				callback(new Error('两次输入密码不一致!'));
			} else {
				callback();
			}
		};
		return {
			ruleForm: {
				pass: '',
				checkPass: '',
			},
			rules: {
				pass: [
					{ validator: validatePass, trigger: 'blur' }
				],
				checkPass: [
					{ validator: validatePass2, trigger: 'blur' }
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
</script>