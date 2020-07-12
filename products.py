#while loop vs. for loop
#while loop 適用於不知道會執行幾次的情況
#for i in range(100) > 有固定次數


products = []
while True:
	name = input('請輸入商品名稱：')
	if name == 'q': # ==等於，比較對象是否相等
		break
	price = input('請輸入商品價格：')
	products.append([name, price]) #簡化寫法，效果同下三行
	#p = [] # 創造二維清單(2dimensional, xy軸)
	#p.append(name)
	#p.append(price)
	#products.append(p)
print(products)
#存取二維清單方式 products[0][0](第一個清單內的第一個項目)


