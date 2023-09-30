import time
import smtplib
from email.mime.text import MIMEText


while True:
	xuanze=input("请输入要办理的业务：1.发邮件2.计算器3.退出:")
	

	if xuanze=="1":
		while True:
			quending=input("此作品的作者为梁峻，而且免费，未经同意，不许转载     1.同意2.返回：")

			if quending=="1":
				msg_from=input("请输入发送方邮箱账号：")
				if msg_from=="":
					ex = Exception("请输入发送方邮箱帐号")
					raise ex
				else:
					pwd=input("请输入发送方邮箱授权码：")
					if pwd=="":
						ex = Exception("请输入授权码！")
						raise ex
					else:
						to=input("请输入接受方邮箱账号：")
						if to == "":
							ex = Exception("请输入接收方邮箱账号！")
							raise ex
						else:
							smtp=input("请输入发送方邮箱服务器smtp地址：")
							if smtp == "":
								ex = Exception("请输入发送方邮箱服务器smtp地址！")
								raise ex
							else:
								sumject=input("请输入邮件主题：")
								if smtp == "":
									ex = Exception("邮件主题不能小于3个字！")
									raise ex
								else:
									content=input("请输入邮件内容：")
									if smtp == "":
										ex = Exception("邮件内容不得小于10个字")
										raise ex
									else:
										print("正在读取您的邮件内容中！")
										msg=MIMEText(content)
										msg["Subject"]=sumject
										msg["From"]=msg_from
										msg["To"]=to
										ss=smtplib.SMTP_SSL(smtp,465)
										ss.login(msg_from,pwd)
										ss.sendmail(msg_from,to,msg.as_string())
										print("发送完毕,发送方:",msg_from," 接受方:",to," 内容是：",content)
										continue
			elif quending=="2":
				print("即将返回")
				time.sleep(1)
				break

	elif xuanze=="3":
		print("10秒后退出")
		time.sleep(10)
		break
	elif xuanze=="2":
		print("欢迎来到Python计算器")
		time.sleep(1)
		while True:
			tongyi = input(
				"请确保您已经阅读《python计算器用户使用条款》和《Python计算器禁止抄袭条款》作者：梁峻1.同意2.拒绝并退出")
			if tongyi == "1":
				yunsuan = input("请输入运算法：1.加法2.减法3.乘法4.减法")
				if yunsuan == "1":
					time.sleep(1)
					J1 = int(input("请输入第一个加数:"))
					time.sleep(1)
					J2 = int(input("请输入第二个加数:"))
					time.sleep(1)
					print("你的加法结果是:", J1 + J2)
				elif yunsuan == "2":
					time.sleep(1)
					A1 = int(input("请输入第一个减数:"))
					time.sleep(1)
					A2 = int(input("请输入第二个减数:"))
					time.sleep(1)
					print("你的减法结果是:", A1 - A2)
				elif yunsuan == "3":
					time.sleep(1)
					C1 = int(input("请输入第一个乘数:"))
					time.sleep(1)
					C2 = int(input("请输入第二个乘数:"))
					time.sleep(1)
					print("你的乘法结果是:", C1 * C2)
				elif yunsuan == "4":
					time.sleep(1)
					U1 = int(input("请输入第一个除数:"))
					time.sleep(1)
					U2 = int(input("请输入第二个除数："))
					time.sleep(1)
					print("你的除法结果是:", U1 / U2)
				else:
					print("输入错误，请确保输入正确!")
			elif tongyi == "2":
				print("感谢您使用Python计算器!再见！作者：梁峻")
				time.sleep(5)
				break
			else:
				print("输入错误，请确保输入正确!")
	else:
		print("输入错误，请确保输入正确!")
