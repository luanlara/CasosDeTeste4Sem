class CodigoTestado2():
	def limparPreco(preco):
		if preco == None or preco == '':
			return -1
		try:
			preco = preco.replace('R$ ', '')
			preco = preco.replace(',', '.')
			preco = float(preco)
		except:
			preco = -1
		return preco

