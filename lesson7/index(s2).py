#建立一個tkinter的基本樣板
#請使用物件導向的方式來建立一個簡單的GUI應用程式
import tkinter as tk
import wantgoo

class SimpleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("簡單的GUI應用程式")
        self.root.geometry("300x200")
        fetch_stock_code:list[dict] = wantgoo.get_stocks_with_twstock()
        print(fetch_stock_code)
        self.create_widgets()
        
    def create_widgets(self):
        self.label = tk.Label(self.root, text="即時股票資訊", font=("Arial", 20, "bold"))
        self.label.pack(pady=20)
        # 建立一個widget來顯示股票資訊
        # 讓使用者可以選擇股票代碼
        # 可以複選多個股票代碼
        # 請使用self.stock_info_label來顯示股票資訊
        self.stock_info_label = tk.Label(self.root, text="選擇股票代碼：")
        self.stock_info_label.pack()

        self.stock_listbox = tk.Listbox(self.root, selectmode=tk.MULTIPLE, width=30, height=60)
        for stock in wantgoo.get_stocks_with_twstock():
            code = stock.get("code", "")
            name = stock.get("name", "")
            self.stock_listbox.insert(tk.END, f"{code} {name}")
        self.stock_listbox.pack(pady=10)

     
if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleApp(root)
    root.mainloop()