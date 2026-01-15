import request from "@/utils/request"


export const getUserInfo = ()=>{
    return request({
        url:'/api/user/info',
        method:'get',
    })
}