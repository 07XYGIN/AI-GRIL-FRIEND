# 💖 AI GRIL FRIEND

<div align="center">
  
![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![uv](https://img.shields.io/badge/uv-0.9+-blue?logo=uv)
![Vue.js](https://img.shields.io/badge/Vue.js-3.x-4FC08D?logo=vuedotjs)
![TypeScript](https://img.shields.io/badge/TypeScript-5.x-3178C6?logo=typescript)
![LangChain](https://img.shields.io/badge/LangChain-1.0+-1C3C3C?logo=langchain)
![FastAPI](https://img.shields.io/badge/FastAPI-0.127+-009688?logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16+-336791?logo=postgresql)



</div>

## 🌟 功能特色

### 🧠 核心智能功能
- **情景记忆**：利用LangChain的记忆模块，记住你们的对话历史、重要日期和个人偏好
- **情感状态**：AI能够识别并记住你的情绪状态，调整回应方式
- **TTL记忆管理**：自动清理过期/不重要的记忆，保持记忆库相关性

## 🏗️ 技术架构

```mermaid
graph TB
        V[Vue.js 3 + TypeScript]
        UI[响应式UI组件]
        WS[WebSocket实时通信]
    end
        F[FastAPI服务器]
        LC[LangChain智能引擎]
        M[记忆管理系统]
    end
        PG[(PostgreSQL)]
    end
    V -->|HTTP/SSE| F
    F --> LC
    LC --> M
    M --> PG
    F --> PG
```
