from langchain_community.document_loaders import PyPDFLoader
from pathlib import Path

# 1. PDF 路径（更安全的写法）
pdf_path = Path(r"E:\XYGin\AIfrd\Server\app\test\a.pdf")

load = PyPDFLoader(
    file_path=pdf_path,
)

i = 0

for doc in load.lazy_load():
    i+=1
    print(doc)
    print('='*20,i)