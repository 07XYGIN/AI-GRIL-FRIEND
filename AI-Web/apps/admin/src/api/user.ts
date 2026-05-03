import request from "@/utils/requests";
import {User, LoginResponse} from "@/type/user";
import { useUserStore } from "@/store/user";

/**
 * 注册
 * */
export const register = (data:User)=>{
    return request({
        url:"/user/register",
        method:"POST",
        data
    })
}

/*
* 用户登录
* */
export const login = async (data:User): Promise<LoginResponse> =>{
    const response: LoginResponse = await request({
        url:"/user/Login",
        method:"POST",
        data
    });
    const userStore = useUserStore();
    userStore.setToken(response.token);
    return response;
}
