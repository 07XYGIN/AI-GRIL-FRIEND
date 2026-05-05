package com.example.springboot_test.common;

import org.springframework.http.HttpStatus;
import org.springframework.validation.FieldError;
import org.springframework.web.bind.MethodArgumentNotValidException;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.ResponseStatus;
import org.springframework.web.bind.annotation.RestControllerAdvice;

import java.util.HashMap;
import java.util.Map;

@RestControllerAdvice
public class GlobalExceptionHandler {
    @ExceptionHandler(MethodArgumentNotValidException.class)
    @ResponseStatus(HttpStatus.UNPROCESSABLE_ENTITY) // 422 对应 UNPROCESSABLE_ENTITY
    public Map<String, Object> handleValidationExceptions(MethodArgumentNotValidException ex) {
        FieldError firstError = ex.getBindingResult().getFieldErrors().stream()
                .findFirst()
                .orElse(null);

        String errorMessage = firstError != null ? firstError.getDefaultMessage() : "参数校验失败";

        Map<String, Object> response = new HashMap<>();
        response.put("code", 422);
        response.put("msg", errorMessage);
        return response;
    }
}