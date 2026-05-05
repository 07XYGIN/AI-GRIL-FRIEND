package com.example.springboot_test.interceptor;

import com.example.springboot_test.util.JWTUtil;
import com.example.springboot_test.util.RedisUtil;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
import org.springframework.web.servlet.HandlerInterceptor;


@Component
public class AuthInterceptor implements HandlerInterceptor {

    @Autowired
    private JWTUtil jwtUtil;

    @Autowired
    private RedisUtil redisUtil;

    @Override
    public boolean preHandle(HttpServletRequest request,
                             HttpServletResponse response,
                             Object handler) throws Exception {
        String authHeader = request.getHeader("Authorization");
        if ("OPTIONS".equals(request.getMethod())) {
            return true;
        }
        if (authHeader == null || !authHeader.startsWith("Bearer ")) {
            response.setStatus(200);
            response.setContentType("application/json;charset=UTF-8");
            response.getWriter().write("{\"code\":401,\"message\":\"未携带token\"}");
            return false;
        }

        String token = authHeader.replace("Bearer ", "");

        if (!jwtUtil.validateToken(token)) {
            response.setStatus(200);
            response.setContentType("application/json;charset=UTF-8");
            response.getWriter().write("{\"code\":401,\"message\":\"token已过期或非法\"}");
            return false;
        }

        String username = jwtUtil.getUsernameFromToken(token);

        String redisToken = redisUtil.get("token:" + username);

        if (redisToken == null || !redisToken.equals(token)) {
            response.setStatus(200);
            response.setContentType("application/json;charset=UTF-8");
            response.getWriter().write("{\"code\":401,\"message\":\"token已失效，请重新登录\"}");
            return false;
        }

        return true;
    }
}
