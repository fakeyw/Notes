import math

#欧几里得距离：坐标系中的直线段距离
#缺陷是P1(4,4),P2(7,7)这种坐标的相似性无法体现
#p,q [a,b,c,d,e,......]
def ecu_distance(p,q):
	sum = 0
	for i,j in zip(p,q):
		sum += (i-j)**2
	return math.sqrt(sum)
	
#相关度
def ecu_sim(ecu_d):
	return 1/(1+ecu_d)
	
#---------------------------------------------
#修正了夸大分值(grade inflation)
#协方差/双标准差

#相减前先提出一个1/len，可选择最后再加
#pub选项用于简化计算，上下抵消一个1/len （ 协方差 1/len 双标准差 sqrt(1/len)*sqrt(1/len) ）
#不太清楚程序会不会自动优化
def cov(x,y,pub=False):
	len = len(x)
	if len(y) != len:
		return None
	else:
		sumXY = 0
		EXY = 0
		if x == y:
			#普通方差
			sumXY = sum([ a**2 for a in x ])
			EXY = sum(x)**2/len
		else:
			sumXY = sum([ a*b for (a,b) in zip(x,y) ])
			EXY = sum(x)*sum(y)/len
		
		if pub:
			return sumXY-EXY
		else:
			return (sumXY-EXY)/len

#直接用协方差，双参变单参
def sd(x,pub=False):
	return math.sqrt(cov(x,x,pub=pub))

def person_correlathon(p,q):
	c = cov(pq,pub=True)
	sd2 = sqrt(sd(p,pub=True)*sd(q,pub=True))
	return c/sd2
	
