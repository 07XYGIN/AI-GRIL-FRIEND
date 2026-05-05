import request from "@/utils/requests";
import type { User, LoginResponse } from "@/type/user";

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
export const login = (data:User): Promise<LoginResponse> =>{
    return request({
        url:"/user/Login",
        method:"POST",
        data
    });
}

/*
* 用户退出
* */

export const logout = (id:string)=>{
    return request({
        url:`/user/logout/${id}`,
        method:"GET",
    })
}

/**
 * 获取用户信息
 * */

export const getUserInfo = ()=>{
    return request({
        url:"/user/userInfo",
        method:"GET",
    })
}
