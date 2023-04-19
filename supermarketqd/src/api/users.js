import request from '@/util/request.js' //引入我们封装好的request

export function post_login(obj) {
    return request({ //利用我们封装好的request发送请求
        url: '/users/login',//请求地址 已经去除前面request中baseUrl相同的内容
        method: 'post',//请求方法
        data: obj//向后端传递数据
    })
}

export function post_register(obj) {
    return request({ 
        url: '/users/register',
        method: 'post',
        data: obj
    })
}

export function patch_user(obj) {
    return request({ 
        url: '/users/up',
        method: 'patch',
        data: obj
    })
}

export function post_emp(obj) {
    return request({ 
        url: '/users/emp',
        method: 'post',
        data: obj
    })
}