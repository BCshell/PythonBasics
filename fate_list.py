'''
1. 魏璎珞请所有嫔妃吃饭 包括 太后、皇后、纯妃、小嘉嫔、舒妃、以及皇上
2. 创建一个列表 存储所有嫔妃的列表，并打印出每个人的名字
4. 小缤妃没有3. 告诉大家”春节将至，请大家过来延禧宫小聚
参加，打印出谁没有参加
5. 魏璎珞想要请尔晴参加，修改列表，并打印出名单
6. 皇上开心，让魏可以邀请更多的人到御花园，用insert方法把'哥哥'放在邀请名单开头
7. 把傅恒append方法放在名单最后，并打印所有人的名单，并且使用len（）函数打印出移动邀请了多少人人，
8. 复制一个新的列表备份
9. 明玉看到名单后，先打印了前三个名字，后打印了后三个人的名字，感觉顺序不对，颠倒了顺序
10. 皇上收回了魏璎珞在御花园宴请宾客的命令
11. 魏把宴会搬回延禧宫，只能邀请2个嫔妃，皇后和尔晴，用pop方法删除多余的名单
12. 并告知‘特别遗憾不能邀请大家吃饭，如何告知皇后和尔晴依然在
13. 宴会开始后，用del语句删除邀请名单

'''

print('----------------------------------')
fate_name = ['太后', '皇后', '纯妃', '小嘉嫔', '舒妃', '皇上']
print('第一种打印列表方法')
print(f'春节将至，请{fate_name}过来延禧宫小聚。')
# 第二种打印列表方法
print('')
print('第二种方法:for 循坏给每一个人打印一条消息')
for name in fate_name:
    print(f'春节将至，请 {name} 过来延禧宫小聚')
# 第三种打印方法，使用索引访问每个元素
print('')
print('第三种打印方法,使用索引访问每一个element')
print(f'春节将至，请 {fate_name[0]} 过来延禧宫小聚')
print(f'春节将至，请 {fate_name[1]} 过来延禧宫小聚')
print(f'春节将至，请 {fate_name[2]} 过来延禧宫小聚')
print(f'春节将至，请 {fate_name[3]} 过来延禧宫小聚')
print(f'春节将至，请 {fate_name[4]} 过来延禧宫小聚')
print(f'春节将至，请 {fate_name[5]} 过来延禧宫小聚')

print('---------------------------------')
print('2,小嘉嫔拒绝邀请，并且打印不能参加的人')
print('')
# 删除小嘉嫔的信息
index_name = fate_name.index('小嘉嫔')
del_name = fate_name.pop(index_name)
print(f'不能参加宴会的人是: {del_name}')

print('3.尔晴参加，请修改列表，并打印邀请名单')
fate_name.append('尔晴')
print(f'添加尔晴一以后的人员名单{fate_name}')

print('')
print('4.宴会地点改为御花园')
garden_name = fate_name
print(f'地点从延禧宫变成御花园后的人员名单{garden_name}')

print('-----------------------------------------')
print('5. insert 方法把‘哥哥’放在邀请名单的开头；append 方法把‘傅恒’放着名单最后。')
garden_name.insert(0,'哥哥')
garden_name.append('傅恒')
print(f'在御花园的人员名单变成{garden_name}')

print('')
print('使用 len 方法打印出，一共邀请了多少人 ，并且复制一个新的列表备份。')
total = len(garden_name)
print(f'魏璎珞在御花园一共邀请了{total} 人 参加宴会。')

#备份列表
copy_garden_name = garden_name

print('')
print('---------------------------------------')
print('前三个人员名单')
print(f'参加宴会的前三个人员名单, {garden_name[:3]}')
print(f'参加宴会的后三个人员名单, {garden_name[-3:]}')

# 列表反转
garden_name.reverse()
print(f'发转以后的人员名单{garden_name}')

print('')
print('-----------------------------------------')
print('地点从御花园变成延禧宫，只请皇后和尔晴，告知依然在受邀之列。')
yaoQing_name = ['皇后', '尔晴']
print(F'宴会从御花园变成延禧宫，您，{yaoQing_name[0]},依然在邀请之列')
print(F'宴会从御花园变成延禧宫，您，{yaoQing_name[1]},依然在邀请之列')

print('------------------------------------------')
print('删除多余人员，并告知"特别遗憾不能邀请大家吃饭')
print('目前宴会名单有:', garden_name)
# 为了删除列表中多余人员，我们使用 pop(index)方法删除宴会列表中的元素。因为每一次
# 删除一个元素，列表中的元素位置会整体移动一个位置，所以我们根据项目᧿述多次使用 pop(0)
# 或者 pop(1)。最后使用 del 语句删除列表
name_1 = garden_name.pop(0)
name_2 = garden_name.pop(1)
name_3 = garden_name.pop(1)
name_4 = garden_name.pop(1)
name_5 = garden_name.pop(2)
name_6 = garden_name.pop(2)

print('删除后的人员名单:',garden_name)
print(f'特别遗憾不能邀请您 {name_1} 来参加宴会。')
print(f'特别遗憾不能邀请您 {name_2} 来参加宴会。')
print(f'特别遗憾不能邀请您 {name_3} 来参加宴会。')
print(f'特别遗憾不能邀请您 {name_4} 来参加宴会。')
print(f'特别遗憾不能邀请您 {name_5} 来参加宴会。')
print(f'特别遗憾不能邀请您 {name_6} 来参加宴会。')
print('=====================================')
print(' ')
print('9.删除名单。')

# del yaoQing_name[0]
del yaoQing_name

del garden_name
del fate_name
del copy_garden_name

# print(f'人员名单{yaoQing_name}')