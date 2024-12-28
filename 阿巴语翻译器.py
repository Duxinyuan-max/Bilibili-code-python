import tkinter as tk
from tkinter import messagebox

def text_to_custom_binary(text):
    custom_result = []
    for char in text:
        unicode_val = ord(char)
        binary_str = bin(unicode_val)[2:]
        custom_binary_str = binary_str.replace('0', '阿').replace('1', '巴')
        custom_result.append(custom_binary_str)
    return ' '.join(custom_result)

def custom_binary_to_text(custom_binary_str):
    binary_values = custom_binary_str.split()
    text = ''.join([chr(int(b.replace('阿', '0').replace('巴', '1'), 2)) for b in binary_values])
    return text

def convert():
    input_text = entry.get()
    if input_text:
        custom_binary_text = text_to_custom_binary(input_text)
        result_label.config(text=f"阿巴语: {custom_binary_text}")
    else:
        messagebox.showwarning("输入错误", "请输入一些文本。")

def revert():
    input_custom_binary = entry.get()
    if input_custom_binary:
        try:
            original_text = custom_binary_to_text(input_custom_binary)
            result_label.config(text=f"原始文本: {original_text}")
        except ValueError:
            messagebox.showerror("转换错误", "无效的阿巴语输入。")
    else:
        messagebox.showwarning("输入错误", "请输入一些阿巴语文本。")

def copy_to_clipboard():
    root.clipboard_clear()
    result_text = result_label.cget("text").split(': ')[-1]  # 只复制结果部分
    root.clipboard_append(result_text)
    messagebox.showinfo("复制到剪贴板", "结果已复制到剪贴板！")

# 创建主窗口
root = tk.Tk()
root.title("文本与阿巴语转换器")

# 创建标签和输入框
label = tk.Label(root, text="输入文本或阿巴语:")
label.pack(pady=5)

entry = tk.Entry(root, width=50)
entry.pack(pady=5)

# 创建转换按钮
convert_button = tk.Button(root, text="转换为阿巴语", command=convert)
convert_button.pack(pady=10)

# 创建还原按钮
revert_button = tk.Button(root, text="从阿巴语还原", command=revert)
revert_button.pack(pady=10)

# 创建复制按钮
copy_button = tk.Button(root, text="复制到剪贴板", command=copy_to_clipboard)
copy_button.pack(pady=10)

# 创建结果显示标签
result_label = tk.Label(root, text="结果: ")
result_label.pack(pady=5)

# 运行主循环
root.mainloop()
