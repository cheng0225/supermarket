<template>
    <div>
        <el-button type="primary" @click="get_start_ip()">更新定位</el-button>
        <el-button type="primary" @click="walk_go()">出发</el-button>
        <div class="content-box">
            <div id="map1" class="map-box" style="float: left;"></div>
            <div id="map2" class="map-box" style="float: right;"></div>
        </div>
    </div>
</template>
  
<style scoped>
.map-box {
    width: 48%;
    height: 800px;
    margin: 0px;
    padding: 0px;
}
</style>

<script>

export default {
    data() {
        return {
            start_lng: '',
            start_lat: '',
            end_lng: '',
            end_lat: '',
        }
    },
    mounted() {
        this.get_start_ip()
        this.get_end_ip()
        this.walk_go()
        this.show()
    },
    methods: {
        get_start_ip() {
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

        get_end_ip() {
            var latlon = this.$route.query.latlon.split(',')
            // console.log(latlon)
            this.end_lng = latlon[0]
            this.end_lat = latlon[1]
            console.log('end ip ', this.end_lng, this.end_lat)
        },

        walk_go() {
            console.log('map导航开始 start', this.start_lng, this.start_lat, 'end', this.end_lng, this.end_lat)
            var map = new BMapGL.Map("map1");
            var navi3DCtrl = new BMapGL.NavigationControl3D();  // 添加3D控件
            map.addControl(navi3DCtrl);
            map.enableScrollWheelZoom();
            map.centerAndZoom(new BMapGL.Point(116.404, 39.915), 11);
            var walk = new BMapGL.WalkingRoute(map, { renderOptions: { map: map, autoViewport: true } });
            var start = new BMapGL.Point(this.start_lng, this.start_lat);
            var end = new BMapGL.Point(this.end_lng, this.end_lat);
            walk.search(start, end);
            console.log('shows')
            // this.show(this.end_lng,this.end_lat)
        },

        show() {
            var map = new BMapGL.Map('map2', { showControls: true }); // 创建Map实例  并添加室内图控件
            var point = new BMapGL.Point(this.end_lng, this.end_lat);
            var marker = new BMapGL.Marker(point);  // 创建标注
            map.addOverlay(marker);       
            map.centerAndZoom(new BMapGL.Point(this.end_lng, this.end_lat), 19); // 初始化地图,设置中心点坐标和地图级别
            map.enableScrollWheelZoom(true); // 开启鼠标滚轮缩放
        }
    }
}
</script>