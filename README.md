# 本项目使用 VLM(视觉-语言模型)，实现图片中文字的识别

# 开始

#### ollama 环境安装

- 安装 ollama
  - [通用安装](https://ollama.com/download)
  - [AMD GPU](https://github.com/ByronLeeeee/Ollama-For-AMD-Installer)
- 安装 vlm 模型，本示例使用的是 qwen
  ```bash
  ollama pull qwen2.5vl:7b
  ```

#### lm-studio 环境安装

- 安装 [lm-studio](https://lmstudio.ai/)
- 安装 google/gemma-3-12b 模型，（备注 google/gemma-3-4b 识别效果太差）
- 开启 lm-studio api server
  - 在 App Setting 中的 developer 中，启用 Local LLM Service(headless)
  - 在主界面 Developer Tab 页面，使 API service 处于 running 状态。此时显示：reachable at: http://127.0.0.1:1234

# 安装依赖

```bash
pip install -r ./requirements.txt
```

# 执行 python 脚本

```bash
# 基于ollama api 实现
python ollama.py
# 基于lm-studio api实现
python lm-studio.py
```

ollama.py 输出的结果

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

lm-studio.py 输出的结果

```bash
*   **商用電源灯 (Shāngyòng diàn yuán dēng)** - Commercial power indicator light
*   **自家発電源灯 (Jījiā fādian yuán dēng)** - Household power generation indicator light
*   **階床灯 (Jiēchuáng dēng)** - Tiered bed indicator light
*   **方向灯 (UP, DN) (Fāngxiàng dēng (UP, DN))** - Direction indicator light (UP, DN)
*   **運転灯 (Jùnxíng dēng)** - Operation indicator light
*   **異常灯 (Yìcháng dēng)** - Abnormality indicator light
*   **完了灯 (Wánjié dēng)** - Completion indicator light
*   **停電時白動着床灯 (Tíngdiàn shí bái dòng zháo chuáng dēng)** - White bed indicator light during power outage
*   **緊急地震速報灯 (Jǐnjí dìzhèn sùbào dēng)** - Emergency earthquake rapid report indicator light
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
