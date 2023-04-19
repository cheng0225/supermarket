import axios from 'axios' //引入axios
import router from '../router'
// import { head } from 'shelljs';
 
//axios.create能创造一个新的axios实例
const server = axios.create({
  baseURL: "http://127.0.0.1:8000", //配置请求的url
  timeout: 6000, //配置超时时间
  headers:{
  }//配置请求头
})


server.interceptors.request.use(
  config=>{
    // 获取请求头数据
    const headers = config.headers
    console.log("请求头",headers)
    config.headers.token = localStorage.getItem('token'); //添加请求头就开始报跨域错 已解决
    return config
  },
  error=>{
    return Promise.reject(error)
  }
)


server.interceptors.response.use(
  response => {
    return response;
  },
  error => {
    if (error.response.status === 401){
      console.log('未登录')
      localStorage.removeItem('token');
      router.push('/users/login')
    }
    return Promise.reject(error);
  }
)

export default server

