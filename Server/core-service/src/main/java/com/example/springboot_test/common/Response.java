package com.example.springboot_test.common;
import com.fasterxml.jackson.annotation.JsonInclude;
import lombok.Data;
@JsonInclude(JsonInclude.Include.NON_NULL)
@Data
public class Response<T> {
    private Integer code;
    private String message;
    private String token;
    private T data;

    public static <T> Response<T> Error(String message) {
        Response<T> result = new Response<>();
        result.setCode(500);
        result.setMessage(message);
        return result;
    }
    public static <T> Response<T> Success(T message) {
        Response<T> result = new Response<>();
        result.setCode(200);
        result.setMessage("操作成功");
        result.setData(message);
        return result;
    }
    public static <T> Response<T> ok(){
        Response<T> result = new Response<>();
        result.setCode(200);
        result.setMessage("操作成功");
        return result;
    };
    public static <T> Response<T> loginSuccess(String token){
        Response<T> result = new Response<>();
        result.setCode(200);
        result.setMessage("操作成功");
        result.setToken(token);
        return result;
    }
    
}
