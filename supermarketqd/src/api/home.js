import request from '@/util/request.js' //引入我们封装好的request
import { data } from 'jquery'

export function get_merchants() {
    return request({  //利用我们封装好的request发送请求
        url: '/home/merchants',//请求地址 已经去除前面request中baseUrl相同的内容
        method: 'get',//请求方法
        data: ''//向后端传递数据
    })
}

export function post_merchants(obj) {
    return request({  
        url: '/home/merchants',
        method: 'post',
        data: obj
    })
}

export function post_things(obj) {
    return request({  
        url: '/home/things/add',
        method: 'post',
        data: obj,
        Headers:{'Content-Type': 'multipart/form-data'}
    })
}

export function get_latlon(id) {
    return request({  
        url: '/home/latlon',
        method: 'get',
        params: {id} // cnm 要加大括号
    })
}

export function get_things() {
    return request({  
        url: '/home/things',
        method: 'get',
        params: ''
    })
}

export function put_things(obj) {
    return request({
        url: '/home/things/add',
        method: 'put',
        data: obj
    })
}

export function patch_things(obj) {
    return request({
        url: '/home/things/add',
        method: 'patch',
        data: obj
    })
}

export function get_logs(obj) {
    return request ({
        url: '/home/logs',
        method: 'get',
        params: {obj}
    })
}