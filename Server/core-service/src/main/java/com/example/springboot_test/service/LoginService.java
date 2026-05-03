package com.example.springboot_test.service;

import com.example.springboot_test.DTO.UserDto;
import com.example.springboot_test.common.Response;
import com.example.springboot_test.mapper.userMapper;
import com.example.springboot_test.util.Crypto;
import com.example.springboot_test.util.JWTUtil;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;

@Service
public class LoginService {
    @Autowired
    private userMapper userMapper;
    @Autowired
    private Crypto cipher;
    @Autowired
    private JWTUtil Jwt;
    @Autowired
    private JWTUtil jWTUtil;

    public void register(UserDto user){
        user.setPassword(cipher.encodedPassword(user.getPassword()));
        userMapper.insertUser(user);
    };

    public Response<String> Login(UserDto user) {
        UserDto userinfo = userMapper.findUser(user);

        if (userinfo == null) {
            return Response.Error("用户不存在");
        }

        if (!cipher.matches(user.getPassword(), userinfo.getPassword())) {
            return Response.Error("密码错误");
        }
        String token = jWTUtil.generateToken(user.getUsername());
        return Response.loginSuccess(token);
    }
}
