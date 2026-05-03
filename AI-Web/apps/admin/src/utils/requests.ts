import axios from "axios";
import {ElMessage} from "element-plus";
const request = axios.create({
    baseURL: 'http://localhost:8080',
});

request.interceptors.request.use(function (config) {
    return config;
}, function (error) {
    return Promise.reject(error);
});


request.interceptors.response.use(function (response) {
    ElMessage.success(response.data.message);
    return response.data.data;
}, function (error) {
    ElMessage.error(error.message);
    return Promise.reject(error);
});

export default request;
