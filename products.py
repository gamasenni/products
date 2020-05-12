import os #operating system

products = []
if os.path.isfile('product.csv') :
	print('找到檔案了')
	#讀取檔案
	products = []
	with open ('product.csv', 'r', encoding = 'utf-8') as f :
		for line in f :
			if '商品,價格' in line :
				continue#跳到下一迴
			name, price = line.strip().split(',')
			products.append([name,price])
	print(products)
else:
	print('找不到檔案...')


#讓使用者輸入
while True :
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	price = int(price)
	products.append([name,price])
print(products)

#印出所有購買紀錄
for p in products :
	print(p[0], '的價格是', p[1])

#寫入檔案
with open('product.csv', 'w', encoding = 'utf-8') as f :
	f.write('商品,價格\n')
	for p in products :
		f.write(p[0] + ',' + str(p[1]) + '\n')
		#有逗點和換行符號區隔，excel才會分隔
		#str(p[1])轉換為字串才能用加法合併

