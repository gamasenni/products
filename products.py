import os #operating system

def read_file(filename) :	#讀取檔案
	products = []
	with open (filename, 'r', encoding='utf-8') as f :
		for line in f :
			if '商品,價格' in line :
				continue#跳到下一迴
			name, price = line.strip().split(',')
			products.append([name,price])
	return products
#讓使用者輸入
def user_input(products):
	while True :
		name = input('請輸入商品名稱: ')
		if name == 'q':
			break
		price = input('請輸入商品價格: ')
		price = int(price)
		products.append([name,price])
	print(products)
	return products
#印出所有購買紀錄
def print_products(products) :
	for p in products :
		print(p[0], '的價格是', p[1])
#寫入檔案
def write_file(filename, products) :
	with open(filename, 'w', encoding='utf-8') as f :
		f.write('商品,價格\n')
		for p in products :
			f.write(p[0] + ',' + str(p[1]) + '\n')
			#有逗點和換行符號區隔，excel才會分隔
			#str(p[1])轉換為字串才能用加法合併



def main(x) :
	if os.path.isfile(x) :#檢查檔案在不在
		products = read_file(x)	
	else:
		print('找不到檔案...')
		products = []

	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)

x = input('請輸入檔案名:')
if __name__ == '__main__':
	main(x)

