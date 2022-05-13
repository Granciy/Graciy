#程序目标：通过自定义函数，实现RPSLS游戏，即用户通过键盘输入任意一个选择（石头/剪刀/布/蜥蜴/史波克），计算机自动生成一个随机选择，根据RPSLS规则，产生最终的结果。
#程序作者：李金婷
import random

# 0 - 石头
# 1 - 史波克
# 2 - 纸
# 3 - 蜥蜴
# 4 - 剪刀

# 以下为完成游戏所需要用到的自定义函数

def name_to_number(name):
    """
    将游戏对象对应到不同的整数
    """
    if name=="石头":
        return 0
    if name=="史波克":
        return 1
    if name=="纸":
        return 2
    if name=="蜥蜴":
        return 3
    if name=="剪刀":
        return 4
# 使用if/elif/else语句将各游戏对象对应到不同的整数
# 不要忘记返回结果

def number_to_name(number):
    """
    将整数 (0, 1, 2, 3, or 4)对应到游戏的不同对象
    """
    if number==0:
        return "石头"
    if number==1:
        return "史波克"
    if number==2:
        return "纸"
    if number==3:
        return "蜥蜴"
    if number==4:
        return "剪刀"
# 使用if/elif/else语句将不同的整数对应到游戏的不同对象
# 不要忘记返回结果

    pass #编写执行代码,代码完成后将pass删除

def rpsls(player_choice):
    """
    用户玩家任意给出一个选择，根据RPSLS游戏规则，在屏幕上输出对应的结果

    """
    player_choice_number=name_to_number(player_choice)
    comp_number=random.randrange(0,4)
    print("计算机的选择为：%s"%number_to_name(comp_number))

    if player_choice_number==0 and comp_number==4 or 3:
        return print("您赢了")
    if player_choice_number==1 and comp_number==0 or 4:
        return print("您赢了")
    if player_choice_number==2 and comp_number==0 or 1:
        return print("您赢了")
    if player_choice_number==3 and comp_number==1 or 2:
        return print("您赢了")
    if player_choice_number==4 and comp_number==2 or 3:
        return print("您赢了")
    elif player_choice_number==comp_number:
        return print("您和计算机出的一样呢")
    else:
        return print("计算机赢了")

    # 输出"-------- "进行分割
    # 显示用户输入提示，用户通过键盘将自己的游戏选择对象输入，存入变量player_choice

    # 调用name_to_number()函数将用户的游戏选择对象转换为相应的整数，存入变量player_choice_number

    # 利用random.randrange()自动产生0-4之间的随机整数，作为计算机随机选择的游戏对象，存入变量comp_number

    # 调用number_to_name()函数将计算机产生的随机数转换为对应的游戏对象

    # 在屏幕上显示计算机选择的随机对象

    # 利用if/elif/else 语句，根据RPSLS规则对用户选择和计算机选择进行判断，并在屏幕上显示判断结果

    # 如果用户和计算机选择一样，则显示“您和计算机出的一样呢”，如果用户获胜，则显示“您赢了”，反之则显示“计算机赢了”

# 对程序进行测试
print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
choice_name=input()
rpsls(choice_name)
