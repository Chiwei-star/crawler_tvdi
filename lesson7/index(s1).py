# 建立一個tkinter的基本樣板
# 請使用物件導向的方法來建立一個簡單的GUI應用程式
import tkinter as tk
# from tkinter import ttk

class SimpleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("簡單的GUI應用程式")
        self.root.geometry("300x200") # 設定視窗大小

        # self.label
        # 請將文字變大、置中、粗體
        self.label = tk.Label(self.root, text="即時股票資訊", font=("Arial", 20, "bold"))
        #self.label = ttk.Label(root, text="Hello, Tkinter!")
        self.label.pack(padx=20, pady=20) # y = 上下距離

        self.button = tk.Button(root, text="點擊我", width=15,command=self.on_button_click)
        #self.button = ttk.Button(root, text="點擊我", command=self.on_button_click)
        self.button.pack() 

    def on_button_click(self):
        self.label.config(text="按鈕已被點擊!", fg="red")

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleApp(root)
    root.mainloop()