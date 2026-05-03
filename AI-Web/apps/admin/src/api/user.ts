import request from "@/utils/requests";
import type { User, LoginResponse } from "@/type/user";
import { useUserStore } from "@/store/modules/user";

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
    return request({
        url:"/user/Login",
        method:"POST",
        data
    });
}
