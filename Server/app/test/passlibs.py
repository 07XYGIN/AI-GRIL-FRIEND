from passlib.context import CryptContext

# 核心修复点：直接用 argon2 哈希，去掉 sha256
pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)  # 直接哈希用户输入密码

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)  # 直接验证

# 示例
a = get_password_hash("123456")
print("hashed:", a)

# 验证
res = verify_password("123456", a)
print("verify result:", res)
