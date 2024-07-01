<template>
    <div>
        <el-table :data="things.filter(data => !search || data.name.toLowerCase().includes(search.toLowerCase()))"
            style="width: 100%" type="flex" justify="center">
            <el-table-column label="商品名称" prop="name">
            </el-table-column>
            <el-table-column label="图片">
                <template slot-scope="scope">
                    <el-image style="width: 100px; height: 100px" :src="scope.row.img"></el-image>
                </template>
            </el-table-column>
            <el-table-column label="单价" prop="price" sortable>
            </el-table-column>
            <el-table-column label="距离(米)" prop="latlon" :formatter="getDistance" sortable>
            </el-table-column>
            <el-table-column align="right">
                <template slot="header" slot-scope="scope">
                    <el-input v-model="search" size="mini" placeholder="输入商品名称搜索" />
                </template>
            </el-table-column>
            <el-table-column align="right">
                <template slot="header" slot-scope="scope">
                    <el-button type=""><a href="/#/cart/route">路线规划</a></el-button>
                    <el-button @click="del_all_cart()" type="">一键清空</el-button>
                </template>
            </el-table-column>
            <el-table-column align="right">
                <template slot-scope="scope">
                    <el-button @click="go_buy(scope.row)" type="primary">前往购买</el-button>
                    <el-button @click="del_cart(scope.row)" type="">移除购物车</el-button>
                </template>
            </el-table-column>
        </el-table>
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
import { get_cart, delete_cart, delete_all_cart } from "@/api/home.js"
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

            start_lng: '',
            start_lat: '',
        }
    },
    mounted() {
        this.show_cart()
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

        handleRemove() {
            this.imageUrl = ""
        },

        show_cart() {
            get_cart().then(
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
        del_cart(row) {
            console.log(row);
            delete_cart(row).then(response => {
                console.log('响应成功', response);
                this.msg = 'succeed'
                location.reload();
            },
                error => {
                    console.log('连接服务器失败', error);
                    this.msg = "连接服务器失败"
                })
        },

        get_start_ip() {// 没用？
            const _this = this
            var geolocation = new BMap.Geolocation();
            geolocation.enableSDKLocation();
            geolocation.getCurrentPosition(function (r) {
                if (this.getStatus() == BMAP_STATUS_SUCCESS) {
                    // var mk = new BMap.Marker(r.point);
                    // console.log('get ip',_this.start_lng ,_this.start_lat )
                    alert('您的位置：' + r.point.lng + ',' + r.point.lat);
                    _this.start_lng = r.point.lng
                    _this.start_lat = r.point.lat
                    console.log('get ip', _this.start_lng, _this.start_lat)
                }
                else {
                    alert('failed' + this.getStatus());
                }
            });
            // this.show(this.start_lng,this.start_lat)
        },
        getDistance(row, column, cellValue) {
            const str = "(121.205777, 31.048743)";
            const regex = /\d+\.\d+/g;
            const matches = str.match(regex);
            const result = matches.map(Number);
            var lng1 = this.start_lng || 0,
                lat1 = this.start_lat || 0,
                lng2 = result[0] || 0,
                lat2 = result[1] || 0;
            var rad1 = lat1 * Math.PI / 180.0;
            var rad2 = lat2 * Math.PI / 180.0;
            var a = rad1 - rad2;
            var b = lng1 * Math.PI / 180.0 - lng2 * Math.PI / 180.0;
            var r = 6378137;
            var distance = r * 2 * Math.asin(Math.sqrt(Math.pow(Math.sin(a / 2), 2) + Math.cos(rad1) * Math.cos(rad2) * Math.pow(Math.sin(b / 2), 2)));
            // 米
            return parseInt(distance);
        },

        del_all_cart(row) {
            console.log(row);
            delete_all_cart(row).then(response => {
                console.log('响应成功', response);
                this.msg = 'succeed'
                location.reload();
            },
                error => {
                    console.log('连接服务器失败', error);
                    this.msg = "连接服务器失败"
                })
        },
    }
}
</script>
  
