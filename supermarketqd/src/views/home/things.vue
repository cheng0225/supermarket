<template>
    <div>
        <el-table :data="things.filter(data => !search || data.name.toLowerCase().includes(search.toLowerCase()))"
            style="width: 100%" type="flex" justify="center">
            <el-table-column type="expand">
                <template slot-scope="props">
                    <el-form label-position="left" inline class="demo-table-expand">
                        <el-form-item label="商品名称">
                            <span>{{ props.row.name }}</span>
                        </el-form-item>
                        <el-form-item label="编号">
                            <span>{{ props.row.number }}</span>
                        </el-form-item>
                        <el-form-item label="库存">
                            <span>{{ props.row.num }}</span>
                        </el-form-item>
                        <el-form-item label="单价">
                            <span>{{ props.row.price }}</span>
                        </el-form-item>
                        <el-form-item label="类型">
                            <span>{{ props.row.kind }}</span>
                        </el-form-item>
                        <el-form-item label="位置">
                            <span>{{ props.row.position }}</span>
                        </el-form-item>
                        <el-form-item label="所属商家">
                            <span>{{ props.row.merchant }}</span>
                        </el-form-item>
                        <el-form-item label="图片">
                            <el-image style="width: auto; height: 100px" :src="props.row.img"
                                :preview-src-list="[props.row.img]">
                            </el-image>
                        </el-form-item>
                    </el-form>
                </template>
            </el-table-column>
            <el-table-column label="商品名称" prop="name">
            </el-table-column>
            <el-table-column label="库存" prop="num">
            </el-table-column>
            <el-table-column label="单价" prop="price" sortable>
            </el-table-column>
            <el-table-column align="right">
                <template slot="header" slot-scope="scope">
                    <el-input v-model="search" size="mini" placeholder="输入商品名称搜索" />
                </template>
            </el-table-column>
            <el-table-column align="right">
                <template slot-scope="scope">
                    <el-button @click="go_buy(scope.row)" type="primary">前往购买</el-button>
                    <el-button @click="patch_show(scope.row)">修改</el-button>
                </template>
            </el-table-column>
        </el-table>

        <el-drawer title="修改信息" :visible.sync="drawer1" direction="ltr" :before-close="handleClose">
            <div style="margin: 20px;">
                <el-form :model="things_form" :rules="rules" label-position="right" label-width="80px" ref="things_form">
                    <el-form-item label="备注" style="margin: 20px;" prop="txt">
                        <el-input type="textarea" :rows="2" placeholder="修改/操作 说明" v-model="things_form.txt"></el-input>
                    </el-form-item>
                    <el-form-item label="数量" style="margin: 20px;">
                        <el-input v-model="things_form.num"></el-input>
                    </el-form-item>
                    <el-form-item label="单价" style="margin: 20px;">
                        <el-input v-model="things_form.price"></el-input>
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
                    <el-button type="primary" @click="submit_things_form(things_form)">提交</el-button>
                </el-form>
            </div>
        </el-drawer>
        
    </div>
</template>
  
  
    
<style scoped>
.demo-table-expand {
    font-size: 0;
}

.demo-table-expand label {
    width: 90px;
    color: #99a9bf;
}

.demo-table-expand .el-form-item {
    margin-right: 0;
    margin-bottom: 0;
    width: 50%;
}
</style>
    
<script>
import { get_things, get_latlon, patch_things } from "@/api/home.js"
export default {
    data() {
        return {
            src: '',
            url: '',
            imageUrl: '',
            img: '',
            drawer1: false,
            search: '',
            srcList: [],
            things: [],
            things_form: {},
            rules: {
                txt: [{ required: true, message: '请填写备注说明', trigger: 'blur' }]
            }
        }
    },
    mounted() {
        this.show_things()
    },
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

        uploadFile(item) {
            this.img = item.raw; // 图片文件
            this.imageUrl = URL.createObjectURL(item.raw); // 图片上传浏览器回显地址
            console.log(this.imageUrl, "imageUrl")
            console.log(this.img, "img")
        },
        handleRemove() {
            this.imageUrl = ""
        },

        show_things() {
            get_things().then(
                response => {
                    console.log(response)
                    this.msg = 'succeed'
                    this.things = response.data
                },
                error => {
                    this.msg = '连接服务器失败'
                    console.log(error)
                })
        },
        go_buy(row) {
            get_latlon(row.id).then(
                response => {
                    console.log(response);
                    var latlon = response.data.latlon;
                    var address = response.data.address;
                    console.log('导航开始', latlon, address);
                    const h = this.$router.resolve({ path: '/map', query: { latlon: latlon } });
                    window.open(h.href, '_blank')//'_self' );
                },
                error => {
                    console.log(error)
                }
            )
        },

        patch_show(row) {
            this.drawer1 = true
            this.things_form = row
            console.log('show things_form', this.things_form)
        },

        submit_things_form(form) {
            this.$refs.things_form.validate((valid) => {
                if (valid) {
                    console.log('submit things_form', form)
                    var form_data = new FormData()
                    form_data.append('img', this.img)
                    // console.log('things_form',this.things_form)
                    for (var key in form) {
                        // console.log(key, this.things_form[key])
                        form_data.append(key, form[key])
                    }
                    // put_things(form_data).then(
                    patch_things(form_data).then(
                        response => {
                            console.log('响应成功', response);
                            this.msg = 'succeed'
                            this.open1()
                            this.drawer1 = false
                        },
                        error => {
                            console.log('连接服务器失败', error);
                            this.msg = "连接服务器失败"
                            this.open4(error.response.data)
                        })
                } else {
                    return false;
                }
            })
        },
    }
}
</script>
  
