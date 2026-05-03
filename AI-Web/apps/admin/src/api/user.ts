import request from "@/utils/requests";
import {User} from "@/type/user";

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
export const login = (data:User)=>{
    return request({
        url:"/user/Login",
        method:"POST",
        data
    })
}
