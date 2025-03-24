import os
import re

def read_file_with_encoding(file_path):
    # 尝试不同的编码格式
    encodings = ['utf-8', 'gbk', 'gb2312', 'gb18030', 'big5']
    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding) as f:
                return f.read()
        except UnicodeDecodeError:
            continue
    raise ValueError(f"无法使用支持的编码格式读取文件: {file_path}")

# 创建Processed文件夹（如果不存在）
if not os.path.exists('Processed'):
    os.makedirs('Processed')

# 获取当前目录下所有的txt文件
txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]

for file_name in txt_files:
    try:
        # 读取原文件
        content = read_file_with_encoding(file_name)
        
        # 使用正则表达式匹配人物对话
        # 匹配模式：开头是中文/英文字符，后面紧跟空格和对话内容
        processed_content = re.sub(r'([\u4e00-\u9fff\w]+)\s+([^\n]+)', r'\1说：\2', content)
        
        # 构建新文件名
        base_name = os.path.splitext(file_name)[0]  # 获取不带扩展名的文件名
        new_file_name = f"{base_name}-莎士比亚.txt"
        
        # 将处理后的内容写入新文件
        with open(os.path.join('Processed', new_file_name), 'w', encoding='utf-8') as f:
            f.write(processed_content)
        
        print(f"已处理: {file_name} -> {new_file_name}")
    except Exception as e:
        print(f"处理文件 {file_name} 时出错: {str(e)}")

print("所有文件处理完成！")