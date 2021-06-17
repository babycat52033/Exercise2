#Accounting
products = []
#Read file
with open ("product.csv", "w", encoding = 'utf-8') as f:
	f.write('商品,價格\n')
	for line in f:
		if '商品, 價格' in line:
			continue
		name, price = line.strip().split(',')
		products.append([name, price])

#User input
while True:
	name = input ("請輸入商品名稱： ")
	if name == 'q':
		break
	price = int(input ("請輸入商品價格： "))
	p = []
	p.append(name)
	p.append(price)
	products.append(p)

print(products)

#Print
for p in products:
	print(p[0], '的價格', p[1])

#Write file
with open ("product.csv", "w", encoding = 'utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) +'\n')
		 