import axios from 'axios'

const BaseUrl = "http://127.0.0.1:8000/"

const request = axios.create({
    baseURL: BaseUrl,
});

request.interceptors.request.use(function (config) {    
    return config;
});

request.interceptors.response.use(function (response) {
    console.log(response);

    return response.data;
    });
export default request;