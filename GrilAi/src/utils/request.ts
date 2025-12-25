import axios from 'axios'

const BaseUrl = import.meta.env.BASE_URL

const request = axios.create({
    baseURL: BaseUrl,
});

request.interceptors.request.use(function (config) {
    return config;
});

request.interceptors.response.use(function (response) {
    return response;
    });
export default request;