import logging
logging.basicConfig(level=logging.DEBUG,
format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# 获取Logger并记录日志
logger = logging.getLogger("my_app")
logger.debug("这是一条调试信息")
logger.info("程序运行正常")
logger.warning("发现潜在问题")
logger.error("发生了一个错误")
