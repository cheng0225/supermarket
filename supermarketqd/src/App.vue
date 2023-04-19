<template>
  <div id="app">
    <div style="margin-bottom: 52px">
      <template>
        <b-navbar type="is-light">
          <template #brand>
            <b-navbar-item href="/#/home/things">
              <img src="./assets/img/主页.png" alt="主页">
            </b-navbar-item>
          </template>
          <template #start>
            <b-navbar-item href="/#/home/merchants">
              商家
            </b-navbar-item>
            <b-navbar-dropdown label="商品管理">
              <b-navbar-item href="/#/api">
                api
              </b-navbar-item>
              <b-navbar-item @click="drawer1 = true">
                添加商品
              </b-navbar-item>
              <b-navbar-item href="/#/home/logs">
                操作日志
              </b-navbar-item>
            </b-navbar-dropdown>
            <b-navbar-dropdown label="订单管理">
              <b-navbar-item href="#">
                About
              </b-navbar-item>
            </b-navbar-dropdown>
          </template>

          <template #end>
            <b-navbar-item tag="div">
              <div class="buttons">
                <a v-if="login" class="button is-primary" @click="logout">
                  <strong>退出登录</strong>
                </a>
                <a v-if="nologin" class="button is-light" href="/#/users/login">
                  登录
                </a>
              </div>
            </b-navbar-item>
            <b-navbar-item href="/#/users/index">
              <img src="./assets/img/头像1.png" alt="个人中心">
            </b-navbar-item>
          </template>
        </b-navbar>
      </template>

      <el-drawer title="修改信息" :visible.sync="drawer1" direction="ltr" :before-close="handleClose">
        <div style="margin: 20px;">
          <el-form label-position="right" label-width="80px" :model="things_form" ref="things_form">
            <el-form-item label="商品编号" style="margin: 20px;">
              <el-input v-model="things_form.number"></el-input>
            </el-form-item>
            <el-form-item label="名称" style="margin: 20px;">
              <el-input v-model="things_form.name"></el-input>
            </el-form-item>
            <el-form-item label="数量" style="margin: 20px;">
              <el-input v-model="things_form.num"></el-input>
            </el-form-item>
            <el-form-item label="单价" style="margin: 20px;">
              <el-input v-model="things_form.price"></el-input>
            </el-form-item>
            <el-form-item label="类型" style="margin: 20px;">
              <el-input v-model="things_form.kind"></el-input>
            </el-form-item>
            <el-form-item label="位置" style="margin: 20px;">
              <el-input v-model="things_form.position"></el-input>
            </el-form-item>
            <el-form-item label="图片" style="margin: 20px;">
              <el-upload v-model="things_form.img" action="#" :show-file-list="false" :auto-upload="false"
                :multiple="false" :on-change="uploadFile" drag accept="image/jpg,image/jpeg,image/png">
                <i v-if="imageUrl" class="el-icon-circle-close deleteImg" @click.stop="handleRemove"></i>
                <img v-if="imageUrl" :src="imageUrl" class="el-upload--picture-car" />
                <div v-else>
                  <i class="el-icon-picture" style="margin-top: 40px; font-size: 40px; color: #999a9c"></i>
                  <div>上传图片</div>
                </div>
              </el-upload>
            </el-form-item>
            <el-button type="primary" @click="submit_things_form()">提交</el-button>
          </el-form>
        </div>
      </el-drawer>

    </div>
    <router-view />
  </div>
</template>


<style>
@import 'assets/css/样式1.css';
@import 'bootstrap/dist/css/bootstrap.css';
@import 'bootstrap-vue/dist/bootstrap-vue.css';

b-navbar-item,
a {
  text-decoration: none;
}


#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  /* margin-top: 60px; */
}
</style>

<script>

import { post_things } from '@/api/home.js'

export default {
  name: "App",
  data() {
    return {
      login: false,
      nologin: true,
      drawer1: false,
      imageUrl: "",
      things_form: {},
    };
  },
  mounted() {
    this.m()
  },
  methods: {
    handleClose(done) {
      done();
    },
    // 上传图片
    uploadFile(item) {
      this.img = item.raw; // 图片文件
      this.imageUrl = URL.createObjectURL(item.raw); // 图片上传浏览器回显地址
      console.log(this.imageUrl, "imageUrl")
      console.log(this.img, "img")
    },
    handleRemove() {
      this.imageUrl = ""
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

    logout() {
      localStorage.removeItem("token")
      console.log("执行跳转")
      this.$router.go(0)
      this.$router.push('/home/things')
    },
    m() {
      if (localStorage.getItem('token') !== null) {
        this.login = true;
        this.nologin = false
      }
      console.log('aaa', localStorage.getItem('token'), this.login, this.nologin)
    },
    // 添加商品提交
    submit_things_form() {
      var form_data = new FormData()
      form_data.append('img', this.img)
      // console.log('things_form',this.things_form)
      for (var key in this.things_form) {
        // console.log(key, this.things_form[key])
        form_data.append(key, this.things_form[key])
      }
      post_things(form_data).then(
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
  }
}
</script>

