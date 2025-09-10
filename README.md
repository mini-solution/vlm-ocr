# 本项目使用 VLM(视觉-语言模型)，实现图片中文字的识别

# 开始

- 安装 ollama
  - 通用安装
  - AMD GPU
- 安装 vlm 模型，本示例使用的是 qwen

```bash
ollama pull qwen2.5vl:7b
```

# 安装依赖

```bash
pip install -r ./requirements.txt
```

# 执行 python 脚本

```bash
python main.py
```

可以看到输出

```bash
名称
商用电源灯
自家発電源灯
階床灯
方向灯（UP，DN）
運転灯
異常灯
完了灯
停電時自動着床灯
緊急地震速報灯
```

# 执行步骤

```mermaid
graph LR;
输入图片 e1@--> 转为base64;
e1@{ animate: true }
转为base64 e2@--> 调用ollama接口;
e2@{ animate: true }
调用ollama接口 e3@--> 打印识别结果;
e3@{ animate: true }
```
