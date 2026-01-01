import request from "@/utils/request"

export const sendMsg = (msg:object)=>{
    return request({
        url:'/msg/send',
        method:'post',
        data:msg
    })
}