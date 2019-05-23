password = 'a123456'
i = 3 #剩余次数
while True:
	mima = input('请输入密码：')
	if mima == password:
		print('登录成功！')
		break #逃出循环
	else:
		i = i - 1
		print('密码错误！还有', i, '次机会')
		if i ==0:
			break


