import axios from "axios";
import {ElMessage} from "element-plus";
import { useUserStore } from "@/store/user";

const request = axios.create({
    baseURL: 'http://localhost:8080',
});

request.interceptors.request.use(function (config) {
    const userStore = useUserStore();
    if (userStore.token) {
        config.headers.Authorization = `Bearer ${userStore.token}`;
    }
    return config;
}, function (error) {
    return Promise.reject(error);
});


request.interceptors.response.use(function (response) {
    if (response.data.code >= 200 && response.data.code < 300) {
        ElMessage.success(response.data.message);
    } else if (response.data.code >= 500 || response.data.code === 422) {
        ElMessage({
            message: response.data.message,
            type: 'error'
        });
    }
    return response.data.data;
}, function (error) {
    ElMessage.error(error.message);
    return Promise.reject(error);
});

export default request;
