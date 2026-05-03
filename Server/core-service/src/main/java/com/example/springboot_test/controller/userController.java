package com.example.springboot_test.controller;

import com.example.springboot_test.common.Response;
import com.example.springboot_test.DTO.UserDto;
import com.example.springboot_test.service.LoginService;
import jakarta.validation.Valid;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/user")
@CrossOrigin

public class userController {

    private final LoginService loginService;

    public userController(LoginService loginService) {
        this.loginService = loginService;
    }


    @PostMapping("register")
    public Response<UserDto> register(@Valid @RequestBody UserDto user) {
        loginService.register(user);
        return Response.ok();
    }

    @PostMapping("Login")
    public Response<String> Login(@RequestBody UserDto user) {
        return loginService.Login(user);
    }
}
