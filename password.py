password = 'a123456'
i = 3
while True:
    pwd = input('請輸入您的密碼：')
    if pwd == password:
	    print('登入成功！')
	    break
    else:
	    print('登入失敗！您還有', i,'次機會！')
	    i = i-1
	    if i == 0:
		    break