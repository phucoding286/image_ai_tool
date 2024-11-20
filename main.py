import requests
import colorama
from googletrans import Translator
colorama.init()

translator = Translator()
API_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-dev"
headers = {"Authorization": "Bearer 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"}

def error_color(string: str):
    return colorama.Fore.RED + str(string) + colorama.Style.RESET_ALL
def success_color(string: str):
    return colorama.Fore.GREEN + str(string) + colorama.Style.RESET_ALL
def system_color(string: str):
    return colorama.Fore.YELLOW + str(string) + colorama.Style.RESET_ALL
def wait_color(string: str):
    return colorama.Fore.BLUE + str(string) + colorama.Style.RESET_ALL
def purple_color(string: str):
    return colorama.Fore.MAGENTA + str(string) + colorama.Style.RESET_ALL

def query(inp, output_path="./output_image.png"):
    try:
        print(wait_color("[#] Đang tạo ảnh cho bạn..."))
        payload = {"inputs": inp}
        response = requests.post(API_URL, headers=headers, json=payload)
        with open(output_path, "wb") as f:
            f.write(response.content)
        print(system_color(f"[!] Ảnh đã được lưu ở đường dẫn '{output_path}'"))
        return {"img_cont": response.content}
    except Exception as e:
        return {"error": f"Đã có lỗi khi tạo ảnh, mã lỗi -> {e}"}

def main():
    print(system_color("[*] Bạn có thể nhập 'exit' để thoát chương trình."))
    prompt = ""
    while prompt != "exit":
        prompt = input(system_color("[?] Nhập vào prompt ảnh mà bạn muốn AI tạo\n-> "))
        while True:
            try:
                prompt = translator.translate(text=prompt).text
                break
            except:
                continue
        print(success_color(f"[*] Promt đã chuyển đổi -> {prompt}"))
        qout = query(prompt)
        if "error" in qout:
            print(error_color(qout['error']))

if __name__ == "__main__":
    main()