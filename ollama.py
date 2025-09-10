import base64
import requests

def main():
    # 输入图片
    inputImage = "jp.jpg"

    # 读取文件并转为base64格式
    def file_to_base64(path: str) -> str:
        # 以二进制模式读取文件
        with open(path, "rb") as f:
            file_data = f.read()
        # 转为base64并解码为utf-8字符串
        return base64.b64encode(file_data).decode("utf-8")

    # 将输入图片转为base64格式
    base64_str = file_to_base64(inputImage)

    # 调用ollama接口
    # 关闭流式输出
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "qwen2.5vl:7b", # 模型名称
        "prompt":"请识别图片中的原始文字", # 提示词
        "stream": False, # 关闭流式输出
        "images": [base64_str], # 
    }
    headers = {"Content-Type": "application/json"}

    response = requests.post(url, json=payload, headers=headers)
    # 打印识别的文字
    print(response.json()["response"])

if __name__ == "__main__":
    main()