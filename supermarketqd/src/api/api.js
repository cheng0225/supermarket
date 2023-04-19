// import axiosInstance from '@/api/index'

// const axios = axiosInstance

// export const get_merchants = ()=>{return this.$axios.get('/home/merchants')}

import request from '@/util/request.js' //引入我们封装好的request
//定义一个函数 getLogin
export function get_merchants() {
    return request({  //利用我们封装好的request发送请求
        url: '/home/merchants',//请求地址 已经去除前面request中baseUrl相同的内容
        method: 'get',//请求方法
        data: ''//向后端传递数据
    })
}

//定义一个函数 getUser
export function getUser(obj) {
    return request({ //利用我们封装好的request发送请求
        url: '/generator/workuser/list',//请求地址 已经去除前面request中baseUrl相同的内容
        method: 'get',//请求方法
        params: obj//向后端传递数据
    })
}