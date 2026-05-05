package com.example.springboot_test.util;


import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.redis.core.StringRedisTemplate;
import org.springframework.stereotype.Component;

import java.util.concurrent.TimeUnit;

@Component
public class RedisUtil {
    @Autowired
    private StringRedisTemplate redisTemplate;

    /**
     * 存入 Redis
     * @param key     键
     * @param value   值
     * @param time    过期时间
     * @param unit    时间单位
     */
    public void set(String key, String value, long time, TimeUnit unit){
        redisTemplate.opsForValue().set(key, value, time, unit);
    }

    /**
     * 从 Redis 取值
     * @param key  键
     * @return     值，不存在则返回 null
     */
    public String get(String key) {
        return redisTemplate.opsForValue().get(key);
        // 根据 key 取出对应的 value
        // 如果 key 不存在或已过期，返回 null
    }

    /**
     * 删除 Redis 中的键
     * @param key  键
     */
    public void delete(String key) {
        redisTemplate.delete(key);
        // 直接删除这个 key
        // 退出登录时用，删了之后 token 立即失效
    }

    /**
     * 判断 key 是否存在
     * @param key  键
     * @return     存在返回 true，不存在返回 false
     */
    public Boolean hasKey(String key) {
        return redisTemplate.hasKey(key);
        // 检查 key 是否存在于 Redis 中
        // 用于验证 token 是否已经失效
    }
}
