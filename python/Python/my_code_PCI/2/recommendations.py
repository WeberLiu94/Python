#-----------------------------------------------------------------------------
critics={'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
 'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5, 
 'The Night Listener': 3.0},
'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5, 
 'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0, 
 'You, Me and Dupree': 3.5}, 
'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
 'Superman Returns': 3.5, 'The Night Listener': 4.0},
'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
 'The Night Listener': 4.5, 'Superman Returns': 4.0, 
 'You, Me and Dupree': 2.5},
'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0, 
 'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
 'You, Me and Dupree': 2.0}, 
'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
 'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
'Toby': {'Snakes on a Plane':4.5,'You, Me and Dupree':1.0,'Superman Returns':4.0}}
#----------------------------------------偏好库------------------------------------
#欧几里得距离评价
from math import sqrt
#返回一个有关Person1 与Person2 的基于距离的相似度评价
def sim_distance_o(prefs,person1,person2):
	si={}
	for item in prefs[person1]:
		if item in prefs[person2]:
			si[item]=1  #统计有几个共同偏好的
	if len(si)==0:return 0
	sum_of_squares=sum([pow(prefs[person1][item]-prefs[person2][item],2) 
						for item in prefs[person1] if item in prefs[person2]])
	return 1/(1+sqrt(sum_of_squares))


#------------------------------------------------------------------------------------
#皮尔逊相关度评价
from math import sqrt
def sim_distance_p(prefs,p1,p2):
	si={}
	for item in prefs[p1]:
		if item in prefs[p2]: si[item]=1  #统计有几个共同偏好的\
	#得到元素的个数
	n=len(si)

	#如果没有共同之处，则返回1
	if n==0: return 1

	#对所有偏好求和
	sum1=sum([prefs[p1][it] for it in si])
	sum2=sum([prefs[p2][it] for it in si])


	#平方和
	sum1Sq=sum([pow(prefs[p1][it],2) for it in si])
	sum2Sq=sum([pow(prefs[p2][it],2) for it in si])
   
	#求乘积和
	pSum=sum([prefs[p1][it]*prefs[p2][it] for it in si])

	#计算皮尔逊评价值
	num=pSum-(sum1*sum2/n)
	den=sqrt((sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))
	if den==0: return 0
	return num/den


#print(sim_distance_p(critics,'Lisa Rose','Gene Seymour'))	#计算2个人的皮尔逊相关程度
#print(sim_distance_o(critics,'Lisa Rose','Gene Seymour')) #计算2个的欧氏距离偏好相关度
#print(sim_distance_p(critics,'Toby','Lisa Rose'))	#计算2个人的皮尔逊相关程度
#print(sim_distance_o(critics,'Michael Phillips','Gene Seymour')) #计算2个的欧氏距离偏好相关度
def getRecommendations(prefs,person,similarity=sim_distance_p):
 	totals={}
 	simSum={}
 	for other in prefs:
 		if other==person:continue
 		sim=similarity(prefs,person,other)

 		if sim<=0: continue
 		for item in prefs[other]:
 			if item not in prefs[person] or prefs[person][item]==0: #只对没看过的作推测评价
 			#计算相似度与评分的乘积和
 				totals.setdefault(item,0)
 				totals[item]+=prefs[other][item]*sim

 			#计算相似度和
 				simSum.setdefault(item,0)
 				simSum[item]+=sim
 	#建立一个归一化列表
 	rankings=[(total/simSum[item],item) for item,total in totals.items()]

 	rankings.sort()
 	rankings.reverse()
 	return rankings