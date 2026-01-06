import axios from 'axios'

const BaseUrl = "http://127.0.0.1:8000/"

const request = axios.create({
    baseURL: BaseUrl,
});

request.interceptors.request.use(
    function (config) {    
        return config;
    }
);

request.interceptors.response.use(
    function (response) {
        return response.data;
    },
    function(err){
        console.log(err);
    }
);
export default request;