package com.example.springboot_test.util;

import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Component;

@Component
public class Crypto {
    PasswordEncoder encoder = new BCryptPasswordEncoder();
    public String encodedPassword(String psd){
      return encoder.encode(psd);
    };
    public Boolean matches(String psd, String encodedPassword){
        return encoder.matches(psd, encodedPassword);
    }
}
