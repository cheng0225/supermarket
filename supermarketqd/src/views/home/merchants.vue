<!-- .filter(data => !search || data.name.toLowerCase().includes(search.toLowerCase())) -->
<template>
    <div>
        <!--type="flex" justify="center"  align="" -->
        <el-table :data="merchants" style="width: 100%" >
            <el-table-column label="商家编号" prop="number" align="center">
            </el-table-column>
            <el-table-column label="店名" prop="name">
            </el-table-column>
            <el-table-column label="地址" prop="address">
            </el-table-column>
            <el-table-column label="经纬度" prop="latlon">
            </el-table-column>
            <el-table-column align="right">
                <template slot-scope="scope">
                    <el-button @click="walk_go(scope.row)" type="primary" style="margin-left: 16px;">前往</el-button>
                </template>
            </el-table-column>
        </el-table>

        <div class="content-box">
            <div id="mapBox" class="map-box"></div>
            <!-- <el-drawer title="遵守交通，一路顺风" :visible.sync="drawer1" :with-header="false">
            </el-drawer> -->
        </div>
    </div>
</template>


<style scoped>

.map-box {
    width: 100%;
    height: 800px;
}
</style>

<script>
import { get_merchants } from '@/api/home.js'
export default {
    name: 'Merchants',
    data() {
        return {
            show_map: false,
            drawer1: false,
            msg: '',
            merchants: [],
        }
    },
    mounted() {
        this.m()
    },
    methods: {
        m() {
            get_merchants().then(
                res => {
                    console.log(res)
                    this.msg = 'succeed'
                    this.merchants = res.data
                },
                error => {
                    this.msg = '连接服务器失败'
                })
        },
        walk_go(val) {
            console.log('导航开始')
            const h = this.$router.resolve({path:'/map', query:{latlon: val.latlon}})
            window.open(h.href,'_blank')//'_self')
        },
    }
}
</script>