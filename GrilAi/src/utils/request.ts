import axios from 'axios';
import useUserStore from '@/store/modules';
const BaseUrl = 'http://127.0.0.1:8000/';

const request = axios.create({
  baseURL: BaseUrl,
});

request.interceptors.request.use(function (config) {
  const { getCode,getUserId } = useUserStore();
  config.headers.CODE = getCode();
  config.headers.userId = getUserId();
  return config;
});

request.interceptors.response.use(
  function (response) {
    return response.data;
  },
  function (err) {
    console.log(err);
  }
);
export default request;
