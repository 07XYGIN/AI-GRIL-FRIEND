package com.example.springboot_test.mapper;

import com.example.springboot_test.DTO.UserDto;
import org.apache.ibatis.annotations.Mapper;

@Mapper
public interface userMapper {
    int insertUser(UserDto userDto);
    UserDto findUser(UserDto userDto);
    UserDto findUserInfo(String username);
}

