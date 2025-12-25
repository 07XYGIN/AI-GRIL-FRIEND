# 💖 AI GRIL FRIEND

<div align="center">
  
![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![uv](https://img.shields.io/badge/uv-0.9+-blue?logo=uv&logoColor=white)
![Vue.js](https://img.shields.io/badge/Vue.js-3.x-4FC08D?logo=vuedotjs&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-5.x-3178C6?logo=typescript&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1.0+-1C3C3C?logo=langchain&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.127+-009688?logo=fastapi&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16+-336791?logo=postgresql&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.x-009688?logo=fastapi&logoColor=white&style=for-the-badge)

一个具备**长期记忆**和**情感认知**的智能虚拟伴侣，使用现代AI技术栈构建。


</div>

## 🌟 功能特色

### 🧠 核心智能功能
- **情景记忆**：利用LangChain的记忆模块，记住你们的对话历史、重要日期和个人偏好
- **情感状态**：AI能够识别并记住你的情绪状态，调整回应方式
- **TTL记忆管理**：自动清理过期/不重要的记忆，保持记忆库相关性

## 🏗️ 技术架构

```mermaid
graph TB
    subgraph "前端层"
        V[Vue.js 3 + TypeScript]
        UI[响应式UI组件]
        WS[WebSocket实时通信]
    end
    
    subgraph "后端层"
        F[FastAPI服务器]
        LC[LangChain智能引擎]
        M[记忆管理系统]
    end
    
    subgraph "数据层"
        PG[(PostgreSQL)]
        VEC[向量数据库<br/>记忆存储]
        CACHE[Redis缓存<br/>TTL管理]
    end
    
    V -->|HTTP/WebSocket| F
    F --> LC
    LC --> M
    M --> PG
    M --> VEC
    M --> CACHE
    F --> PG
```
