<template>
    <div>
        <el-row :gutter="52">
            <el-col :span="6">
                <a @click="drawer1 = true">
                    <div class="grid-content bg-purple">
                        修改个人信息
                    </div>
                </a>
            </el-col>
            <el-col :span="6">
                <a @click="drawer2 = true">
                    <div class="grid-content bg-purple">
                        员工认证
                    </div>
                </a>
            </el-col>
            <el-col :span="6">
                <a @click="drawer3 = true">
                    <div class="grid-content bg-purple">
                        商家入驻
                    </div>
                </a>
            </el-col>
        </el-row>

        <el-drawer title="修改信息" :visible.sync="drawer1" direction="ltr" :before-close="handleClose">
            <div style="margin: 20px;">
            <el-form label-position="right" label-width="80px" :model="user_form" ref="user_form">
                <el-form-item label="用户名" style="margin: 20px;">
                    <el-input v-model="user_form.user"></el-input>
                </el-form-item>
                <el-form-item label="密码" style="margin: 20px;">
                    <el-input v-model="user_form.password"></el-input>
                </el-form-item>
                <el-button type="primary" @click="submit_user_form('user_form')">提交</el-button>
            </el-form>
            </div>
        </el-drawer>

        <el-drawer title="员工认证" :visible.sync="drawer2" direction="ltr" :before-close="handleClose">
            <div style="margin: 20px;">
            <el-form label-position="right" label-width="80px" :model="emp_form" ref="emp_form">
                <el-form-item label="所属商家" style="margin: 20px;">
                    <el-input v-model="emp_form.merchant"></el-input>
                </el-form-item>
                <el-form-item label="员工编号" style="margin: 20px;">
                    <el-input v-model="emp_form.number"></el-input>
                </el-form-item>
                <el-form-item label="姓名" style="margin: 20px;">
                    <el-input v-model="emp_form.name"></el-input>
                </el-form-item>
                <el-form-item label="职位" style="margin: 20px;">
                    <el-input v-model="emp_form.position"></el-input>
                </el-form-item>
                <el-button type="primary" @click="submit_emp_form('emp_form')">提交</el-button>
            </el-form>
            </div>
        </el-drawer>

        <el-drawer title="商家入驻" :visible.sync="drawer3" direction="ltr" :before-close="handleClose">
            <div style="margin: 20px;">
            <el-form label-position="right" label-width="80px" :model="mer_form" ref="mer_form">
                <el-form-item label="名称" style="margin: 20px;">
                    <el-input v-model="mer_form.name"></el-input>
                </el-form-item>
                <el-form-item label="编号" style="margin: 20px;">
                    <el-input v-model="mer_form.number"></el-input>
                </el-form-item>
                <el-form-item label="地址" style="margin: 20px;">
                    <el-input v-model="mer_form.address"></el-input>
                </el-form-item>
                <el-form-item label="经纬度" style="margin: 20px;">
                    <el-input v-model="mer_form.latlon"></el-input>
                </el-form-item>
                <el-button type="primary" @click="get_ip()">获取位置信息</el-button>
                <el-button type="primary" @click="submit_mer_form('mer_form')">提交</el-button>
                <!-- <el-button @click="resetform('mer_form')">重置</el-button> -->
            </el-form>
            </div>
        </el-drawer>
    </div>
</template>
<style scoped>
@import '../../assets/css/样式1.css';


.el-row {
    margin-bottom: 20px;

    /* &:last-child {
        margin-bottom: 0;
    } */
}

.el-col {
    border-radius: 4px;
}

.bg-purple-dark {
    background: #99a9bf;
}

.bg-purple {
    background: #d3dce6;
}

.bg-purple-light {
    background: #e5e9f2;
}

.grid-content {
    border-radius: 4px;
    min-height: 36px;
}

.row-bg {
    padding: 10px 0;
    background-color: #f9fafc;
}
</style>

<script>

import { post_merchants } from '@/api/home.js'
import {patch_user, post_emp} from '@/api/users.js'

export default {
    name: 'index',
    data() {
        return {
            form: {},
            msg: '',
            drawer1: false,
            drawer2: false,
            drawer3: false,
            mer_form: {
                // latlon: ''
            },
            user_form: {},
            emp_form: {},
        }
    },
    mounted() { },
    methods: {
        handleClose(done) {
            done();
        },
        open1() {
            this.$message({
                message: '提交成功',
                type: 'success'
            });
        },
        open4(data) {
        this.$alert(data, '信息有误，请核对', {
          confirmButtonText: '确定',
        });
      },
      
        submit() {
            console.log('aaaa', this.form);
            post_login(this.form).then(response => {
                console.log('响应成功', response);
                this.msg = 'succeed'
                // this.changeLogin({token: response.data})
                localStorage.setItem("token", response.data.token)
                this.$router.push('/home/things');
            },
                error => {
                    console.log('连接服务器失败', error);
                    this.msg = "连接服务器失败"
                })
        },
        go_register() {
            console.log("执行跳转")
            this.$router.push('/register')
        },
        resetform(formName) {
            console.log(this.mer_form)
            this.$refs[formName].resetFields();
        },
        submit_user_form() {
            patch_user(this.user_form).then(
                response => {
                    console.log('响应成功', response);
                    this.msg = 'succeed'
                    this.open1()
                    this.drawer1=false
                },
                error => {
                    console.log('连接服务器失败', error);
                    this.msg = "连接服务器失败"
                    this.open4(error.response.data)
                })
        },
        submit_emp_form() {
            post_emp(this.emp_form).then(
                response => {
                    console.log('响应成功', response);
                    this.msg = 'succeed'
                    this.open1()
                    this.drawer2=false
                },
                error => {
                    console.log('连接服务器失败', error);
                    this.msg = "连接服务器失败"
                    this.open4(error.response.data)
                })
        },
        submit_mer_form() {
            post_merchants(this.mer_form).then(
                response => {
                    console.log('响应成功', response);
                    this.msg = 'succeed'
                    this.open1()
                    this.drawer3=false
                },
                error => {
                    console.log('连接服务器失败', error);
                    this.msg = "连接服务器失败"
                    this.open4(error.response.data)
                })
        },
        get_ip() {
            var geolocation = new BMap.Geolocation();
            geolocation.getCurrentPosition(function (r) {
                if (this.getStatus() == BMAP_STATUS_SUCCESS) {
                    var mk = new BMap.Marker(r.point);
                    alert('您的位置：' + r.point.lng + ',' + r.point.lat);
                    // this.$set(this.mer_form.latlon,'latlon',r.point.lng + ',' + r.point.lat)
                }
                else {
                    alert('failed' + this.getStatus());
                }
            });
        },
    }
}
</script>