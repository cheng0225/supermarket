<!-- <template>
    <div class="content-box">
      <div id="mapBox" ></div>
    </div>
  </template> -->
<template>
    <div>
        <el-button type="primary" @click="ip()">更新定位</el-button>
        <el-button type="primary" @click="go()">出发</el-button>
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
            lng: '',
            lat: '',
        }
    },
    mounted() {
        this.init()
        this.show()
    },
    methods: {
        init() {
            // 在页面dom元素加载完成后，才可以通过BMapGL.Map('mapBox')加载地图
	var map = new BMapGL.Map("map1");
	var point = new BMapGL.Point(116.404, 39.925);
	map.centerAndZoom(point, 15);
            // 百度地图API功能
            var marker = new BMapGL.Marker(point);  // 创建标注
            map.addOverlay(marker);              // 将标注添加到地图中
            var opts = {
                width: 200,     // 信息窗口宽度
                height: 100,     // 信息窗口高度
                title: "故宫博物院", // 信息窗口标题
                message: "这里是故宫"
            }
            var infoWindow = new BMapGL.InfoWindow("地址：北京市东城区王府井大街88号乐天银泰百货八层", opts);  // 创建信息窗口对象 
            marker.addEventListener("click", function () {
                map.openInfoWindow(infoWindow, point); //开启信息窗口
            });
        },
        ip() {
            // var map = new BMapGL.Map("mapBox");
            // var point = new BMapGL.Point(116.331398, 39.897445);
            // map.centerAndZoom(point, 12);
            const _this = this
            var geolocation = new BMap.Geolocation();
            // geolocation.enableSDKLocation();
            geolocation.getCurrentPosition(function (r) {
                if (this.getStatus() == BMAP_STATUS_SUCCESS) {
                    var mk = new BMap.Marker(r.point);
                    // map.addOverlay(mk);
                    // map.panTo(r.point);
                    console.log(_this.lng,_this.lat)
                    alert('您的位置：' + r.point.lng + ',' + r.point.lat);
                    _this.lng = r.point.lng
                    _this.lat = r.point.lat
                    console.log(_this.lng,_this.lat)
                }
                else {
                    alert('failed' + this.getStatus());
                }
            });
        },
        // go() {
        //     var map = new BMap.Map("mapBox");
        //     map.centerAndZoom(new BMap.Point(116.404, 39.915), 14);
        //     var walk = new BMap.WalkingRoute(map, {
        //         renderOptions: { map: map }
        //     });
        //     var start = new BMap.Point(116.310791, 40.003419);
        //     var end = new BMap.Point(116.486419, 39.877282);
        //     walk.search(start, end);
        // },

        go() {
            console.log( 'go', this.lng,this.lat)
            var map = new BMap.Map("map1");
            map.enableScrollWheelZoom();
            map.centerAndZoom(new BMap.Point(116.404, 39.915), 11);
            var walk = new BMap.WalkingRoute(map, { renderOptions: { map: map, autoViewport: true } });
            var start = new BMap.Point(121.20861929671, 31.057102696177);  // this.lng,this.lat
            var end = new BMap.Point(121.20862933903, 31.057094535783); //121.205959,31.049432
            walk.search(start, end);
            //  end 
            //map导航开始 start  end 
            // walking.search('西单', '慈云寺');
        },
        show() {
            // var map = new BMapGL.Map("map2");          // 创建地图实例 
            // var point = new BMapGL.Point(116.404, 39.915);  // 创建点坐标 
            // map.centerAndZoom(point, 15);                 // 初始化地图，设置中心点坐标和地图级别
            // map.enableScrollWheelZoom(true);     //开启鼠标滚轮缩放
            // map.setHeading(64.5);   //设置地图旋转角度
            // map.setTilt(73);       //设置地图的倾斜角度
            // // 禁止地图旋转和倾斜可以通过配置项进行设置
            // var map = new BMapGL.Map("map2", {
            //     enableRotate: false,
            //     enableTilt: false
            // });
            var map = new BMapGL.Map("map2");
            map.centerAndZoom(new BMapGL.Point(116.280190, 40.049191), 19);
            map.enableScrollWheelZoom(true);
            map.setHeading(64.5);
            map.setTilt(73);
            // 百度地图API功能
            var point = new BMapGL.Point(116.280190, 40.049191);
            var marker = new BMapGL.Marker(point);  // 创建标注
            map.addOverlay(marker);              // 将标注添加到地图中
            var opts = {
                width: 200,     // 信息窗口宽度
                height: 100,     // 信息窗口高度
                title: "故宫博物院", // 信息窗口标题
                message: "这里是故宫"
            }
            var infoWindow = new BMapGL.InfoWindow("地址：北京市东城区王府井大街88号乐天银泰百货八层", opts);  // 创建信息窗口对象 
            marker.addEventListener("click", function () {
                map.openInfoWindow(infoWindow, point); //开启信息窗口
            });
        },

        show2(){
            
            // console.log('shouw2',lng,lat)
            var map = new BMapGL.Map("map2",{ // 是否允许转动
                enableRotate: true,
                enableTilt: true
            });
            map.centerAndZoom(new BMapGL.Point(this.end_lng, this.end_lat), 19);
            map.enableScrollWheelZoom(true);
            map.setHeading(64.5);
            map.setTilt(73);
            // 百度地图API功能
            var point = new BMapGL.Point(this.end_lng, this.end_lat);
            var marker = new BMapGL.Marker(point);  // 创建标注
            map.addOverlay(marker);              // 将标注添加到地图中
            var opts = {
                width: 200,     // 信息窗口宽度
                height: 100,     // 信息窗口高度
                title: "商品位置", // 信息窗口标题
                message: "这里是故宫"
            }
            var infoWindow = new BMapGL.InfoWindow("地址：北京市东城区王府井大街88号乐天银泰百货八层", opts);  // 创建信息窗口对象 
            marker.addEventListener("click", function () {
                map.openInfoWindow(infoWindow, point); //开启信息窗口
            });
        }
    }
}
</script>

  
  



<!-- 

<template>
    <div>
        <meta name="viewport" content="initial-scale=1.0, user-scalable=no" />
        <el-button type="primary" @click="ip()">提交</el-button>
        <div id="container"></div> 
    </div>
</template>


<style type="text/css">  
    html{height:100%}    
    body{height:100%;margin:0px;padding:0px}    
    #container{height:100%}    
</style> 



<script>
// Vue.config.productionTip = false
import { post_login } from '@/api/users.js';


export default {
    name: 'Login',
    data() {
        return {
            form: {},
            msg: '',
        }
    },
    mounted() {
        this.init()
    },
    methods: {
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
        ip() {
            var map = new BMapGL.Map("container");
            var map = new BMap.Map("allmap");
            var point = new BMap.Point(116.331398, 39.897445);
            map.centerAndZoom(point, 12);

            var geolocation = new BMap.Geolocation();
            geolocation.getCurrentPosition(function (r) {
                if (this.getStatus() == BMAP_STATUS_SUCCESS) {
                    var mk = new BMap.Marker(r.point);
                    map.addOverlay(mk);
                    map.panTo(r.point);
                    alert('您的位置：' + r.point.lng + ',' + r.point.lat);
                }
                else {
                    alert('failed' + this.getStatus());
                }
            });
        },
        init() {
        // 在页面dom元素加载完成后，才可以通过BMapGL.Map('mapBox')加载地图
        BMapGL = window.BMapGL
        var mp = new BMapGL.Map('container'); 
        mp.centerAndZoom(new BMapGL.Point(121.491, 31.233), 11); 
        }
    }
}
</script>


<script type="text/javascript">
var map = new BMapGL.Map("container");
// 创建地图实例 
var point = new BMapGL.Point(116.404, 39.915);
// 创建点坐标 
map.centerAndZoom(point, 15);
// 初始化地图，设置中心点坐标和地图级别 
</script> 

<script type="text/javascript" src="https://api.map.baidu.com/api?v=1.0&&type=webgl&ak=gfFB9cCjgePfYwQsRwKzyk60kUDoVo2h">
</script> -->

