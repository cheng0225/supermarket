<template>
    <div class="pos-a" id="allmap">
    </div>
</template>

<style scoped>
#allmap {
    width: 100%;
    /* height: 100%; */
    height: 800px;
    overflow: hidden;
    margin: 0;
    font-family: "微软雅黑";
}
</style>

<script>
import { get_cart, } from "@/api/home.js"

export default {
    data() {
        return {
            things: [],
            start_lng: '',
            start_lat: '',
            end_lng: '',
            end_lat: '',
        }
    },
    mounted() {
        this.get_start_ip()
        // this.get_data()
    },
    methods: {
        get_start_ip() {
            const _this = this
            var geolocation = new BMapGL.Geolocation();
            geolocation.enableSDKLocation();
            geolocation.getCurrentPosition(function (r) {
                if (this.getStatus() == BMAP_STATUS_SUCCESS) {
                    // var mk = new BMap.Marker(r.point);
                    // console.log('get ip',_this.start_lng ,_this.start_lat )
                    alert('您的位置：' + r.point.lng + ',' + r.point.lat);
                    _this.start_lng = r.point.lng
                    _this.start_lat = r.point.lat
                    console.log('get ip', _this.start_lng, _this.start_lat)
                    _this.get_data()
                }
                else {
                    alert('failed' + this.getStatus());
                }
            });
            // this.show(this.start_lng,this.start_lat)
        },
        async get_data() {
            await get_cart().then(
                response => {
                    console.log(response)
                    this.msg = 'succeed'
                    this.things = response.data
                },
                error => {
                    this.msg = '连接服务器失败'
                    console.log('连接服务器失败', error)
                })
            this.show()
        },
        show() {
            // 百度地图API功能
            var map = new BMap.Map("allmap");
            map.centerAndZoom(new BMap.Point(this.start_lng, this.start_lat), 13);
            map.enableScrollWheelZoom(true);


            function showPoly(pointList) {

                //循环显示点对象
                for (var c = 0; c < pointList.length; c++) {
                    var marker = new BMap.Marker(pointList[c]);
                    map.addOverlay(marker);
                    //将途经点按顺序添加到地图上
                    var label = new BMap.Label(c + 1, { offset: new BMap.Size(20, -10) });
                    marker.setLabel(label);
                }

                var group = Math.floor(pointList.length / 11);
                var mode = pointList.length % 11;

                var driving = new BMap.DrivingRoute(map, {//驾车实例
                    onSearchComplete: function (results) {
                        if (driving.getStatus() == BMAP_STATUS_SUCCESS) {
                            var plan = driving.getResults().getPlan(0);
                            var num = plan.getNumRoutes();
                            alert("plan.num ：" + num);
                            for (var j = 0; j < num; j++) {
                                var pts = plan.getRoute(j).getPath();    //通过驾车实例，获得一系列点的数组
                                var polyline = new BMap.Polyline(pts);
                                map.addOverlay(polyline);
                            }
                        }
                    }
                });
                for (var i = 0; i < group; i++) {
                    var waypoints = pointList.slice(i * 11 + 1, (i + 1) * 11);
                    //注意这里的终点如果是11的倍数的时候，数组可是取不到最后一位的，所以要注意终点-1喔。感谢song141的提醒，怪我太粗心大意了~
                    driving.search(pointList[i * 11], pointList[(i + 1) * 11 - 1], { waypoints: waypoints });//waypoints表示途经点
                }
                if (mode != 0) {
                    var waypoints = pointList.slice(group * 11, pointList.length - 1);//多出的一段单独进行search
                    driving.search(pointList[group * 11], pointList[pointList.length - 1], { waypoints: waypoints });
                }

            }

            var arrayList = [];
            var setList = new Set();

            console.log('start', this.start_lng, this.start_lat);
            var p1 = new BMap.Point(this.start_lng, this.start_lat);
            arrayList.push(p1);
            //将坐标点放入数据中
            for (var i = 0; i < this.things.length; i++) {
                const str = this.things[i]["latlon"];
                if (setList.has(str)) { continue }
                setList.add(str)
                const regex = /\d+\.\d+/g;
                const matches = str.match(regex);
                const result = matches.map(Number);
                var p1 = new BMap.Point(result[0], result[1]);
                arrayList.push(p1);
            }
            //显示轨迹
            var p1 = new BMap.Point(this.start_lng, this.start_lat);
            arrayList.push(p1);
            showPoly(arrayList);

        }
    }
}

</script>
