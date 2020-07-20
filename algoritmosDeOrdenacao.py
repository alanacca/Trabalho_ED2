
import sys
sys.setrecursionlimit(1000000)
class Insert_SortAux(object):
	def ordenar(self,colecao,comeco,fim,l):
		for i in range (1,len(colecao)):
			elem = colecao[i]
			j = i-1
			while(j>=0 and int(elem['weight'])<int(colecao[j]['weight'])):
				colecao[j+1] = colecao[j]
				j = j-1
			colecao[j+1] = elem
		return colecao

class Insert_Sort(object):
	def ordenar(self, colecao,comeco,fim,L):
		for i in range (comeco,fim):
			elem = colecao[i]
			j = i-1
			while(j>=0 and int(elem['weight'])<int(colecao[j]['weight'])):
				colecao[j+1] = colecao[j]
				j = j-1
			colecao[j+1] = elem
		return colecao

class Quicksort(object):
	def ordenar(self,colecao,comeco,fim, L):
		return self.recursao(colecao, 0, len(colecao)-1, L)

	def recursao(self,colecao,comeco,fim,L):
		if(len(colecao)>0):
			if(comeco<=fim):
				posPivo = self.partir(colecao,comeco, fim,L)
			
				self.recursao(colecao,comeco,posPivo-1,L)
				self.recursao(colecao,posPivo+1,fim,L)
		return colecao

	def partir(self,colecao,comeco,fim,L):
		pivo = int(colecao[comeco]['weight'])
		c = comeco+1
		f = fim 

		while(c<=f):
			if(int(colecao[c]['weight']) <= pivo):
				c=c+1
			elif pivo < int(colecao[f]['weight']):
				f=f-1
			else:
				troca = colecao[c]
				colecao[c] = colecao[f]
				colecao[f] = troca
				c=c+1
				f=f-1
		colecao[comeco] = colecao[f]
		colecao[f]['weight'] = pivo
		return f

class Quicksort_InsertP(object):
	def ordenar(self,colecao,comeco,fim, L):
		return self.recursao(colecao, 0, len(colecao)-1, 3)

	def recursao(self,colecao,comeco,fim,L):
		posPivo = 0
		if(comeco<fim):
			posPivo = self.partir(colecao,comeco,fim,3)

			self.recursao(colecao,comeco,posPivo-1,3)
			plista = posPivo - comeco
			cInsertion = fim-posPivo
			ins = Insert_Sort()
			if(plista<=L):
				ins.ordenar(colecao,comeco,posPivo,0)
			else:
				self.recursao(colecao,comeco,posPivo-1,3)
			if(cInsertion<=L):
				ins.ordenar(colecao,posPivo+1,fim,0)
			else:
				self.recursao(colecao,posPivo+1,fim,3)
		return colecao

	def partir(self,colecao,comeco,fim,L):
		pivo = int(colecao[comeco]['weight'])
		c = comeco+1
		f = fim 

		while(c<=f):
			if(int(colecao[c]['weight']) <= pivo):
				c=c+1
			elif pivo < int(colecao[f]['weight']):
				f=f-1
			else:
				troca = colecao[c]
				colecao[c] = colecao[f]
				colecao[f] = troca
				c=c+1
				f=f-1
		colecao[comeco] = colecao[f]
		colecao[f]['weight'] = pivo
		return f

class Quicksort_InsertF(object):
	def ordenar(self,colecao,comeco,fim, L):
		return self.recursao(colecao, 0, len(colecao)-1, 3)

	def recursao(self,colecao,comeco,fim,L):
		posPivo = 0
		if(comeco<fim):
			posPivo = self.partir(colecao,comeco,fim,3)

			self.recursao(colecao,comeco,posPivo-1,3)
			plista = posPivo - comeco
			slista = fim-posPivo
			cInsertion = (fim-comeco)+1
			ins = Insert_Sort()
			if(plista>L):
				self.recursao(colecao,comeco,posPivo-1,3)
			if(slista>L):
				self.recursao(colecao,posPivo+1,fim,3)
			if(cInsertion==len(colecao)):
				ins.ordenar(colecao,comeco,fim,0)
		return colecao

	def partir(self,colecao,comeco,fim,L):
		pivo = int(colecao[comeco]['weight'])
		c = comeco+1
		f = fim 

		while(c<=f):
			if(int(colecao[c]['weight']) <= pivo):
				c=c+1
			elif pivo < int(colecao[f]['weight']):
				f=f-1
			else:
				troca = colecao[c]
				colecao[c] = colecao[f]
				colecao[f] = troca
				c=c+1
				f=f-1
		colecao[comeco] = colecao[f]
		colecao[f]['weight'] = pivo
		return f

class Mergesort(object):
	def ordenar(self,colecao,comeco,fim, L):
		return self.recursao(colecao, 0, len(colecao)-1, 0)

	def recursao(self,colecao,comeco,fim,L):
		if(len(colecao)>1):
			tam = len(colecao)/2
			colecao_L = colecao[:int(tam)]
			colecao_R = colecao[int(tam):]

			self.recursao(colecao_L,comeco,fim,L)
			self.recursao(colecao_R,comeco,fim,L)

			i=0
			j=0
			k=0
			tam_L = len(colecao_L)
			tam_R = len(colecao_R)
			while i<tam_L and j<tam_R:
				if(int(colecao_L[i]['weight'])<int(colecao_R[j]['weight'])):
					colecao[k]['weight'] = colecao_L[i]['weight']
					i=i+1
				else:
					colecao[k]['weight'] = colecao_R[j]['weight']
					j=j+1
				k=k+1
			while i<len(colecao_L):
				colecao[k]['weight'] = colecao_L[i]['weight']
				i=i+1
				k=k+1
			while j<len(colecao_R):
				colecao[k]['weight'] = colecao[j]['weight']
				j=j+1
				k=k+1
		return colecao

class Mergesort_InsertP(object):
	def ordenar(self,colecao,comeco,fim, L):
		return self.recursao(colecao, 0, len(colecao)-1, 3)

	def recursao(self,colecao,comeco,fim,L):
		if len(colecao)>L:
			tam = len(colecao)/2
			colecao_L = colecao[:int(tam)]
			colecao_R = colecao[int(tam):]

			self.recursao(colecao_L,comeco,fim,3)
			self.recursao(colecao_R,comeco,fim,3)

			i=0
			j=0
			k=0
			tam_L = len(colecao_L)
			tam_R = len(colecao_R)
			while i<tam_L and j<tam_R:
				if(int(colecao_L[i]['weight'])<int(colecao_R[j]['weight'])):
					colecao[k]['weight'] = colecao_L[i]['weight']
					i=i+1
				else:
					colecao[k]['weight'] = colecao_R[j]['weight']
					j=j+1
				k=k+1
			while i<len(colecao_L):
				colecao[k]['weight'] = colecao_R[i]['weight']
				i=i+1
				k=k+1
			while j<len(colecao_R):
				colecao[k]['weight'] = colecao_R[j]['weight']
				j=j+1
				k=k+1
		else:
			ins = Insert_Sort()
			ins.ordenar(colecao,0,len(colecao)-1,0)
		return colecao

class Mergesort_InsertF(object):
	def ordenar(self,colecao,comeco,fim, L):
		return self.recursao(colecao, 0, len(colecao)-1, 3)
	def recursao(self,colecao,comeco,fim,L):
		if len(colecao)>1:
			tam = len(colecao)/2
			colecao_L = colecao[:int(tam)]
			colecao_R = colecao[int(tam):]
		if len(colecao)>L:
			self.recursao(colecao_L,comeco,fim,3)
			self.recursao(colecao_R,comeco,fim,3)

			i=0
			j=0
			k=0
			tam_L = len(colecao_L)
			tam_R = len(colecao_R)

			while i<tam_L and j<tam_R:
				if(colecao_L[i]['weight']<colecao_R[j]['weight']):
					colecao[k]['weight'] = colecao_L[i]['weight']
					i=i+1
				else:
					colecao[k]['weight'] = colecao_R[j]['weight']
					j=j+1
				k=k+1
			while i<len(colecao_L):
				colecao[k]['weight'] = colecao_L[i]['weight']
				i=i+1
				k=k+1
			while j<len(colecao_R):
				colecao[k]['weight'] = colecao_R[j]['weight']
				j=j+1
				k=k+1
		else:
			i=0
			j=0
			k=0
			while i<len(colecao_L):
				colecao[k]['weight'] = colecao_L[i]['weight']
				i=i+1
				k=k+1
			while j<len(colecao_R):
				colecao[k]['weight'] = colecao_R[j]['weight']
				j=j+1
				k=k+1
			ins = Insert_Sort()
			ins.ordenar(colecao,0,len(colecao)-1,0)
		return colecao