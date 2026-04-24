# 💖 Aura
<div align="center">
  
![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Vue.js](https://img.shields.io/badge/Vue.js-3.x-4FC08D?logo=vuedotjs)
![TypeScript](https://img.shields.io/badge/TypeScript-5.x-3178C6?logo=typescript)
![LangChain](https://img.shields.io/badge/LangChain-1.0+-1C3C3C?logo=langchain)
![FastAPI](https://img.shields.io/badge/FastAPI-0.127+-009688?logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16+-336791?logo=postgresql)



</div>

## 简介
Aura意为 灵气、光环、氛围。
就像AI本身所说:"Aura像晨光初透时的微晕，像老唱片转动时的温润声场，也像你疲惫归家、推开门那一瞬心里悄悄亮起的光。 它不喧哗，却存在；不强制，却陪伴；不占有，却始终环绕着你"

## 🌟 功能特色

### 🧠 核心智能功能
- **情景记忆**：利用LangChain的记忆模块，记住你们的对话历史、重要日期和个人偏好
- **情感状态**：AI能够识别并记住你的情绪状态，调整回应方式
- **TTL记忆管理**：自动清理过期/不重要的记忆，保持记忆库相关性

## 快速开始

### clone
~~~bash
git clone https://github.com/07XYGIN/AI-GRIL-FRIEND.git
~~~

### 前端

~~~bash
cd GrilAi

# 安装依赖
pnpm install  # 或 npm install / yarn install

# 开发模式运行
pnpm dev

# 构建生产版本
pnpm build
~~~

### serve
~~~bash
uv sync

# 激活虚拟环境

# Windows:
.venv\Scripts\activate

# 启动服务

uvicorn main:app --reload --host 0.0.0.0 --port 8000
~~~


## 🏗️ 技术架构

```mermaid
graph TB
    subgraph "客户端层"
        A[Web应用]
        C[WebSocket客户端]
    end
    
    subgraph "API网关层"
        D[FastAPI服务器]
    end
    
    subgraph "业务逻辑层"
        G[对话管理]
        H[记忆引擎]
        I[情感分析]
    end
    
    subgraph "AI服务层"
        K[LangChain智能引擎]
        L[LLM集成]
        M[向量化处理]
    end
    
    subgraph "数据存储层"
        N[(PostgreSQL<br/>结构化数据)]
        O[(向量数据库<br/>记忆存储)]
    end
    
    
    A --> D
    C --> D
    
    D --> G
    G --> H
    G --> I
    
    H --> K
    I --> K
    
    K --> L
    K --> M
    
    G --> N
    H --> O
```

## 里程碑

当前已完成:

- 引入langgraph graphstate概念优化model