# print("Hello! python!")

# 輸出與輸入
name = input("請輸入你的名字：")
print("你好,", name)

# 基本數學處理
scores = [80, 90, 70]
print("總分：", sum(scores))
print("最高分：", max(scores))

# 型別與轉換
value = "123"
print(int(value) + 1)  # 輸出 124

# 迴圈搭配 range()
for i in range(3):
    print(f"第 {i+1} 次")
