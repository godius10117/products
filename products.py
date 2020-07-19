#while loop vs. for loop
#while loop 適用於不知道會執行幾次的情況
#for i in range(100) > 有固定次數

# 讀取檔案
# split切割完的結果是清單
products = []
with open('products.csv', 'r', encoding ='UTF-8') as f:
	for line in f:
		if '商品,價格' in line:
			continue # 跳過直接到下一回，用於迴圈(for loop/while loop)常用於不讀取檔案中的標題
		name, price = line.strip().split(',')
		#s = line.strip().split(',') 同上方一行完成
		#name = s[0]
		#price = s[1]
		products.append([name,price])
print(products)

# 讓使用者輸入
while True:
	name = input('請輸入商品名稱：')
	if name == 'q': # ==等於，比較對象是否相等
		break
	price = input('請輸入商品價格：')
	price = int(price)
	products.append([name, price]) #簡化寫法，效果同下三行
	#p = [] # 創造二維清單(2dimensional, xy軸)
	#p.append(name)
	#p.append(price)
	#products.append(p)
print(products)
# 存取二維清單方式 products[0][0](第一個清單內的第一個項目)

# 印出所有購買紀錄
for p in products:
	# print(p) #印出商品及價格
	# print(p[0]) #印出商品
	print(p[0], '的價格是', p[1])

# 寫入檔案
with open('products.csv','w', encoding= 'UTF-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] +',' + str(p[1]) + '\n')





