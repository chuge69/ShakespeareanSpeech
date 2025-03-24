# Shakespearean Speech Processor

这是一个用于处理莎士比亚戏剧文本的Python工具，主要用于优化AI朗读体验。该工具将戏剧中的对话格式转换为更适合朗读的形式。

## 功能特点

- 自动识别并处理莎士比亚戏剧文本中的人物对话
- 在人物名字后添加"说："，使对话更自然
- 支持多种中文编码格式（UTF-8, GBK, GB2312, GB18030, Big5）
- 自动创建处理后的文件，保持原始文件不变
- 处理后的文件统一使用UTF-8编码保存

## 文件结构

- `Unprocessed/`: 存放原始的莎士比亚戏剧文本文件
- `Processed/`: 存放处理后的文件
- `main.py`: 处理脚本
- `README.md`: 项目说明文档

## 使用方法

1. 将莎士比亚戏剧的文本文件（.txt格式）放在 `Unprocessed` 文件夹中
2. 运行脚本：
   ```bash
   python main.py
   ```
3. 处理后的文件将保存在 `Processed` 文件夹中
4. 新文件命名格式为：`原文件名-莎士比亚.txt`

## 示例

原始文本（在 `Unprocessed/` 中）：
```
国王 你好
```

处理后（在 `Processed/` 中）：
```
国王说：你好
```

## 系统要求

- Python 3.6 或更高版本
- 支持中文编码的操作系统

## 安装

1. 克隆仓库：
   ```bash
   git clone git@github.com:chuge69/ShakespeareanSpeech.git
   ```
2. 进入项目目录：
   ```bash
   cd ShakespeareanSpeech
   ```

## 注意事项

- 请确保原始文本文件使用支持的编码格式
- 处理后的文件将统一使用UTF-8编码保存
- 原始文件不会被修改，处理后的文件将保存在新的文件夹中

## 许可证

MIT License

## 贡献

欢迎提交 Issue 和 Pull Request 来帮助改进这个项目。

## 作者

[Your Name]

## 致谢

感谢莎士比亚的经典作品，这个工具旨在让更多人能够更好地欣赏这些不朽的文学作品。 