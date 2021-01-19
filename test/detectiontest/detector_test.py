#中国移动
CHINA MOBILE
如果我输入一大堆中文汉字其中包括移和动会怎么样呢
message = Message(subject='cn_移=动管理员申请', sender='1074612393@qq.com', recipients=['hengztian@163.com'], body='from ' +email + '\n' + reason)
sql_view = 'SELECT team_name,category,description,create_user from team where team_name = "%s"' % (
message = Message(subject='中国移动管理员申请', sender='1074612393@qq.com', recipients=['hengztian@163.com'], body='from ' +email + '\n' + reason)
return render_template('manage_team_view.html', result=team_result)  # 返回到动主界面
return render_template(m0bile.html', result=team_result)