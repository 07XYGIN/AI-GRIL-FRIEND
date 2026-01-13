import request from "@/utils/request"

export const sendMsg = (msg:object)=>{
    return request({
        url:'/msg/send',
        method:'post',
        data:msg
    })
}
export const getMsgList = ()=>{
    return request({
        url:'/api/history/',
        method:'get',
    })
}
export const delMsgList = ()=>{
    return request({
        url:'/api/history',
        method:'delete',
    })
}