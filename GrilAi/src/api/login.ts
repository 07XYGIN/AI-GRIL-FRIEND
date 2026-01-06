import request from "@/utils/request"
export interface loginForm{
    userName:string|undefined
    password:string
    newPassword:string|undefined,
    code?:string
}
export const login = (login:loginForm)=>{
    return request({
        url:"api/register",
        method:"POST",
        data:login
    })
}