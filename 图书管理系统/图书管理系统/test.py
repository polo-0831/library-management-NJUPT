import tkinter as tk
from tkinter import ttk
import tkinter.messagebox

# # 页面信息
# self.window = window
# self.window.title("图书管理系统")
# self.window.geometry("800x500")

#  宏定义
# 主页面
but_x = 290  # 按钮横轴位置
butwidth = 200  # 按钮宽度
butheight = 50  # 按钮高度
# 增加界面
labelstep = 40  # 文本的垂直间隙
entry_x = 300  # 输入框的横坐标

# 主页面删除控件函数
def destroyall(self):
    self.addbut.destroy()
    self.changebut.destroy()
    self.deletebut.destroy()
    self.findbut.destroy()
    self.showallbut.destroy()
    self.quitbut.destroy()
    self.labelname.destroy()
    self.lzq.destroy()
    self.xjz.destroy()
    self.author.destroy()

# 判断ISBN号合法性
def cal(string):
    if len("".join(string.split('-'))) != 10 or string[-2] != '-' or string[-8] != '-' or string[-12] != '-' :
        # print('wrong')
        return 1
    S = sum([i * int(j) for i, j in zip(range(10, 1, -1), "".join(string.split('-'))[:-1])])
    N = 11 - S % 11
    if N == 10:
        N = 'X'
    if N == 11:
        N = '0'
    if "".join(string.split('-'))[-1] == str(N):
        # print('correct')
        return 0
    else:
        # print('wrong')
        return 1

# 主页面 OK
class MainMenu:
    def __init__(self, window):
        # 页面信息
        self.window = window
        self.window.title("史上最丑图书管理系统")
        self.window.geometry("800x500")

        # 文字标题
        self.labelname = tkinter.Label(window, text='图书管理系统', justify=tkinter.RIGHT, font=("华文行楷", 40), fg="blue",
                                       width=100)
        self.labelname.place(x=but_x - 200, y=25, width=600, height=80)

        # 作者落款
        self.lzq = tkinter.Label(window, text='罗梓淇', justify=tkinter.RIGHT, font=("华文行楷", 15), fg="black", width=100)
        self.lzq.place(x=but_x - 250, y=400, width=100, height=80)
        self.xjz = tkinter.Label(window, text='谢俊哲', justify=tkinter.RIGHT, font=("华文行楷", 15), fg="black", width=100)
        self.xjz.place(x=but_x - 250, y=350, width=100, height=80)
        self.author = tkinter.Label(window, text='制作人：', justify=tkinter.RIGHT, font=("华文行楷", 15), fg="black", width=100)
        self.author.place(x=but_x - 250, y=300, width=100, height=80)

        # 增加图书
        self.addbut = tk.Button(self.window, text="增加图书", bd=5, font=('黑体', 20, 'bold'), command=self.toadd)
        self.addbut.place(x=but_x, y=100, width=butwidth, height=butheight)

        # 修改图书信息
        self.changebut = tk.Button(self.window, text="修改图书信息", bd=5, font=('黑体', 20, 'bold'), command=self.tochange)
        self.changebut.place(x=but_x, y=160, width=butwidth, height=butheight)

        # 删除图书信息
        self.deletebut = tk.Button(self.window, text="删除图书信息", bd=5, font=('黑体', 20, 'bold'), command=self.todelete)
        self.deletebut.place(x=but_x, y=220, width=butwidth, height=butheight)

        # 查找图书信息
        self.findbut = tk.Button(self.window, text="查找图书信息", bd=5, font=('黑体', 20, 'bold'), command=self.tofind)
        self.findbut.place(x=but_x, y=280, width=butwidth, height=butheight)

        # 显示图书信息
        self.showallbut = tk.Button(self.window, text="显示图书信息", bd=5, font=('黑体', 20, 'bold'), command=self.toshowall)
        self.showallbut.place(x=but_x, y=340, width=butwidth, height=butheight)

        # 退出按钮
        self.quitbut = tk.Button(self.window, text="退出", bd=5, font=('黑体', 20, 'bold'), command=self.quit)
        self.quitbut.place(x=650, y=400, width=100, height=50)

    def toadd(self):
        destroyall(self)
        AddMenu(root)

    def tochange(self):
        destroyall(self)
        ChangeMenu(root)

    def todelete(self):
        destroyall(self)
        DeleteMenu(root)

    def tofind(self):
        destroyall(self)
        FindMenu(root)

    def toshowall(self):
        destroyall(self)
        ShowAllMenu(root)

    def quit(self):
        root.destroy()

# 增加图书页面 OK
class AddMenu:  # 增加图书页面
    def __init__(self, window):
        self.window = window
        self.window.title("史上最丑图书管理系统")
        self.window.geometry("800x500")
        # self.window.config(bg="#0F375A")

        # 返回主菜单按钮
        self.backbut = tk.Button(self.window, text="返回主菜单", bd=5, font=('黑体', 20, 'bold'), command=self.back)
        self.backbut.place(x=550, y=400, width=200, height=50)
        # 添加图书按钮
        self.addbut = tk.Button(self.window, text="添加", bd=5, font=('黑体', 20, 'bold'), command=self.addbook)
        self.addbut.place(x=300, y=80 + 7 * labelstep, width=80, height=40)

        # 定义标签和输入框
        if 1:
            # 标签：INBS号，书名，作者名称，出版社信息，出版时间（格式为2020.03），书本价格，图书简介
            self.label1 = tk.Label(window, text='ISBN号:')
            self.label1.place(x=150, y=80)
            self.label2 = tk.Label(window, text='书名:')
            self.label2.place(x=150, y=80 + 1 * labelstep)
            self.label3 = tk.Label(window, text='作者名称:')
            self.label3.place(x=150, y=80 + 2 * labelstep)
            self.label4 = tk.Label(window, text='出版社信息:')
            self.label4.place(x=150, y=80 + 3 * labelstep)
            self.label5 = tk.Label(window, text='出版时间（格式为2020.03）:')
            self.label5.place(x=150, y=80 + 4 * labelstep)
            self.label6 = tk.Label(window, text='书本价格:')
            self.label6.place(x=150, y=80 + 5 * labelstep)
            self.label7 = tk.Label(window, text='图书简介:')
            self.label7.place(x=150, y=80 + 6 * labelstep)
            # 输入框定义
            # ISBN
            self.ISBN = tk.StringVar()
            self.entry_INBR = tk.Entry(window, textvariable=self.ISBN)
            self.entry_INBR.place(x=entry_x, y=80)
            # 书名
            self.bookname = tk.StringVar()
            self.entry_bookname = tk.Entry(window, textvariable=self.bookname)
            self.entry_bookname.place(x=entry_x, y=80 + 1 * labelstep)
            # 作者名称
            self.author = tk.StringVar()
            self.entry_author = tk.Entry(window, textvariable=self.author)
            self.entry_author.place(x=entry_x, y=80 + 2 * labelstep)
            # 出版社信息
            self.press = tk.StringVar()
            self.entry_press = tk.Entry(window, textvariable=self.press)
            self.entry_press.place(x=entry_x, y=80 + 3 * labelstep)
            # 出版时间（格式为2020.03）
            self.pubtime = tk.StringVar()
            self.entry_pubtime = tk.Entry(window, textvariable=self.pubtime)
            self.entry_pubtime.place(x=entry_x, y=80 + 4 * labelstep)
            # 书本价格
            self.bookprice = tk.StringVar()
            self.entry_bookprice = tk.Entry(window, textvariable=self.bookprice)
            self.entry_bookprice.place(x=entry_x, y=80 + 5 * labelstep)
            # 图书简介
            self.bookintro = tk.StringVar()
            self.entry_bookintro = tk.Entry(window, textvariable=self.bookintro)
            self.entry_bookintro.place(x=entry_x, y=80 + 6 * labelstep)

    def back(self):
        # 删除添加界面内的所有东西
        if 1:
            self.backbut.destroy()
            self.addbut.destroy()
            self.label1.destroy()
            self.label2.destroy()
            self.label3.destroy()
            self.label4.destroy()
            self.label5.destroy()
            self.label6.destroy()
            self.label7.destroy()
            self.entry_INBR.destroy()
            self.entry_bookname.destroy()
            self.entry_author.destroy()
            self.entry_press.destroy()
            self.entry_pubtime.destroy()
            self.entry_bookprice.destroy()
            self.entry_bookintro.destroy()
        MainMenu(root)

    def addbook(self):
        # 输入框获取信息
        ISBN_get = self.ISBN.get()
        bookname_get = self.bookname.get()
        author_get = self.author.get()
        press_get = self.press.get()
        pubtime_get = self.pubtime.get()
        bookprice_get = self.bookprice.get()
        bookintro_get = self.bookintro.get()
        # 判断图书信息是否完整
        if ISBN_get == '' or bookname_get == '' or press_get == '' or author_get == '' or pubtime_get == '' or bookprice_get == '' or bookintro_get == '':
            tk.messagebox.showinfo(title='消息提示框', message='请完善图书信息！')
        elif cal(ISBN_get):  # 判断ISBN号合法性
            tk.messagebox.showinfo(title='消息提示框', message='ISBN号不合法！')
        else:
            ISBN_onlyflag = 1  # ISBN号唯一性，1为唯一， 0为有重复
            number = []
            lines_str = []
            with open('library.txt', 'r') as f:
                line = f.readline()
                while line:
                    lines_str.append(line.rstrip('\n'))
                    line = line.strip().split()
                    number.append(line[0])
                    line = f.readline()
                f.close()
            # 判断ISBN号唯一性
            for i in number:
                if i == ISBN_get: ISBN_onlyflag = 0
            # 往文件内写入信息
            if ISBN_onlyflag == 1:
                with open('library.txt', 'a') as f:
                    f.write(ISBN_get + ' ')
                    f.write(bookname_get + ' ')
                    f.write(author_get + ' ')
                    f.write(press_get + ' ')
                    f.write(pubtime_get + ' ')
                    f.write(bookprice_get + ' ')
                    f.write(bookintro_get + '\n')
                tk.messagebox.showinfo(title='消息提示框', message='添加成功！')
            else:
                tk.messagebox.showinfo(title='消息提示框', message='重复的ISBN号')

# 修改图书页面
class ChangeMenu:
    def __init__(self, window):
        # 页面信息
        self.window = window
        self.window.title("史上最丑图书管理系统")
        self.window.geometry("800x500")

        # 定义容器 self.tabel_frame
        self.tabel_frame = tkinter.Frame(window)
        self.tabel_frame.pack()
        # 定义滚动条及其表格
        if 1:
            xscroll = tk.Scrollbar(self.tabel_frame, orient=tk.HORIZONTAL)
            yscroll = tk.Scrollbar(self.tabel_frame, orient=tk.VERTICAL)
            columns = ['ISBN号', '书名', '作者名称', '出版社信息', '出版时间', '书本价格', '图书简介']
            self.table = tk.ttk.Treeview(
                master=self.tabel_frame,  # 父容器
                height=10,  # 表格显示的行数,height行
                columns=columns,  # 显示的列
                show='headings',  # 隐藏首列
                xscrollcommand=xscroll.set,  # x轴滚动条
                yscrollcommand=yscroll.set,  # y轴滚动条
            )
            # 定义表头
            self.table.heading(column='ISBN号', text='INBS号', )  # 点击表头出发lambda函数
            self.table.heading('书名', text='书名', )
            self.table.heading('作者名称', text='作者名称', )
            self.table.heading('出版社信息', text='出版社信息', )
            self.table.heading('出版时间', text='出版时间', )
            self.table.heading('书本价格', text='书本价格', )
            self.table.heading('图书简介', text='图书简介', )  # 点击表头出发lambda函数)
            # 定义列
            self.table.column('ISBN号', width=100, minwidth=100, anchor='s', )
            self.table.column('书名', width=100, minwidth=100, anchor='s')
            self.table.column('作者名称', width=100, minwidth=100, anchor='s')
            self.table.column('出版社信息', width=150, minwidth=150, anchor='s')
            self.table.column('出版时间', width=100, minwidth=100, anchor='s')
            self.table.column('书本价格', width=80, minwidth=80, anchor='s')
            self.table.column('图书简介', width=200, minwidth=100, anchor='s')
            # config绑定滚动条为滚动事件 pack放置滚动条再最边边
            xscroll.config(command=self.table.xview)
            xscroll.pack(side=tk.BOTTOM, fill=tk.X)
            yscroll.config(command=self.table.yview)
            yscroll.pack(side=tk.RIGHT, fill=tk.Y)
            self.table.pack(pady=120)

        # 设计搜索方法和关键字搜索框
        if 1:
            self.labelfindmethod = tkinter.Label(window, text='查找方式', justify=tkinter.RIGHT, width=50)
            self.labelfindmethod.place(x=10, y=40, width=50, height=30)

            self.labelenterkeywords = tkinter.Label(window, text='关键词', justify=tkinter.RIGHT, width=50)
            self.labelenterkeywords.place(x=220, y=40, width=50, height=30)
            # 搜索方法元组
            finemethod = ('ISBN号', '书名', '作者名称', '出版社信息', '出版时间', '书本价格')
            # 查找方式组合框
            self.comboFM = tkinter.ttk.Combobox(window, values=finemethod, width=50)
            self.comboFM.place(x=70, y=40, width=100, height=30)  # 选择框的位置
            # 绑定事件处理函数
            self.comboFM.bind('<<ComboboxSelected>> ', self.comboChange)

            # 输入框定义--关键字
            self.keywords = tk.StringVar()
            self.entry_keywords = tk.Entry(window, textvariable=self.keywords)
            self.entry_keywords.place(x=280, y=40, width=200, height=30)

            # 下面是关于修改内容的控件定义
            # 修改信息种类的label
            self.labelcitype = tkinter.Label(window, text='修改信息种类', justify=tkinter.RIGHT, width=50)
            self.labelcitype.place(x=10, y=360, width=80, height=30)
            # 修改信息种类的元组
            finemethod = ('ISBN号', '书名', '作者名称', '出版社信息', '出版时间', '书本价格', '图书简介')
            # 修改信息种类组合框
            self.comboCItype = tkinter.ttk.Combobox(window, values=finemethod, width=50)
            self.comboCItype.place(x=100, y=360, width=100, height=30)  # 选择框的位置
            # 绑定事件处理函数
            self.comboCItype.bind('<<ComboboxSelected>> ', self.comboChangeCItype)

            # 文本定义
            self.lebelenterchangeinfo = tkinter.Label(window, text='输入修改信息', justify=tkinter.RIGHT, width=50)
            self.lebelenterchangeinfo.place(x=220, y=360, width=100, height=30)
            # 输入框定义--修改内容
            self.changeinfo = tk.StringVar()
            self.entry_changeinfo = tk.Entry(window, textvariable=self.changeinfo)
            self.entry_changeinfo.place(x=330, y=360, width=150, height=30)

        # 定义按钮
        if 1:
            # 关键词查找按键
            self.findbut = tk.Button(self.window, text="关键词查找", bd=5, font=('黑体', 15, 'bold'), command=self.find)
            self.findbut.place(x=500, y=40, width=200, height=30)
            # 修改图书信息按键
            self.changebut = tk.Button(self.window, text="修改图书信息", bd=5, font=('黑体', 15, 'bold'), command=self.change)
            self.changebut.place(x=500, y=350, width=150, height=50)
            # 返回主菜单
            self.backbut = tk.Button(self.window, text="返回主菜单", bd=5, font=('黑体', 20, 'bold'), command=self.back)
            self.backbut.place(x=550, y=400, width=200, height=50)
            # 帮助按钮
            self.helpbut = tk.Button(self.window, text="帮助", bd=5, font=('黑体', 10, 'bold'), command=self.help)
            self.helpbut.place(x=60, y=420, width=50, height=30)

    def help(self):
        tk.messagebox.showinfo(title='消息提示框', message='请查询出你所需的图书，并选择修改信息的种类后修改')

    # 组合框：事件处理函数--关键字种类
    def comboChange(self, *args, **kwargs):
        self.method = self.comboFM.get()

    # 组合框：事件处理函数--修改信息种类
    def comboChangeCItype(self, *args, **kwargs):
        self.changeinfotype = self.comboCItype.get()
        # print(self.changeinfotype)
        # finemethod = ('ISBN号', '书名', '作者名称', '出版社信息', '出版时间', '书本价格', '图书简介', '删除')
        if self.changeinfotype == 'ISBN号':
            self.changeinfotype_number = 1
        elif self.changeinfotype == '书名':
            self.changeinfotype_number = 2
        elif self.changeinfotype == '作者名称':
            self.changeinfotype_number = 3
        elif self.changeinfotype == '出版社信息':
            self.changeinfotype_number = 4
        elif self.changeinfotype == '出版时间':
            self.changeinfotype_number = 5
        elif self.changeinfotype == '书本价格':
            self.changeinfotype_number = 6
        elif self.changeinfotype == '图书简介':
            self.changeinfotype_number = 7
        # print(self.changeinfotype_number)

    def back(self):
        self.labelcitype.destroy()
        self.lebelenterchangeinfo.destroy()
        self.helpbut.destroy()
        self.labelenterkeywords.destroy()
        self.comboCItype.destroy()
        self.entry_changeinfo.destroy()
        self.changebut.destroy()
        self.backbut.destroy()
        self.findbut.destroy()
        self.comboFM.destroy()
        self.entry_keywords.destroy()
        self.labelfindmethod.destroy()
        self.tabel_frame.destroy()
        MainMenu(root)

    # 删除treeview所有
    def delTreeview(self, *args, **kwargs):
        x = self.table.get_children()
        for item in x:
            self.table.delete(item)

    # 关键词查找函数
    def find(self):
        # self.keywords_get = self.keywords.get()  # 获取输入框内部的关键字
        # columns = ['ISBN号', '书名', '作者名称', '出版社信息', '出版时间', '书本价格', '图书简介']
        number = []
        name = []
        public_address = []
        public_time = []
        price = []
        author_name = []
        lines_str = []  # 字符串形式， 直接输出结果
        # self.finalfind_index = None   # 将找出来的书在库存里的序号放入finalfind_index

        result = []
        i = 0
        # 打开文件提取图书信息
        with open('library.txt', 'r') as f:
            line = f.readline()
            while line:
                # print(line.rstrip())  # 后面跟 ',' 将忽略换行符
                lines_str.append(line.rstrip('\n'))
                line = line.strip().split()
                number.append(line[0])
                name.append(line[1])
                public_address.append(line[2])
                public_time.append(line[3])
                price.append(line[4])
                author_name.append(line[5])
                line = f.readline()
            f.close()
        line2 = [t for t in lines_str]

        a = self.keywords.get() #获取关键词输入框内文字
        if a == '':
            tk.messagebox.showinfo(title='消息提示框', message='请输入关键词！')
        else:
        # 关键词查找种类的判定
            if self.method == 'ISBN号':
                index_gather = [e for e, m in enumerate(number) if a in m]  # 为了规避index只能查找一个
                copy = []  # 专门针对重复情况而设置的， 正常情况下copy不会动为0， 重复情况可由i == 1 引出
                if len(lines_str) > 0:  # 这一个判断用于删除treeview表格内之前的数据，然后再打印出新的图书信息覆盖
                    self.delTreeview(self)
                for index_ in index_gather:
                    if i == 0:  # 表示未重复初始输入状态
                        result.append(lines_str[index_])
                        self.table.insert('', tk.END, values=lines_str[index_].split())  # 添加数据到末尾
                    if lines_str[index_] in result and i == 1:  # 主要用于重复后第二次判断用的，如果不在里面，则代表是其他重复情况
                        copy.append(lines_str[index_])
                if i == 0:
                    length = len(result)
                    # print(length)
                if i == 1:
                    result = [co for co in copy]
                    if len(result) == 0:
                        # print('请输入其他有效信息！该信息在内部查不到任何内容！')
                        tk.messagebox.showinfo(title='消息提示框', message='请输入其他有效信息！该信息在内部查不到任何内容！')
                        # continue
                    elif len(result) >= 1:
                        length = len(result)
                if length > 1:
                    # k = input('查阅的图书不止一本！要想继续按照关键词查找图书吗？(y/n)')
                    tk.messagebox.showinfo(title='消息提示框', message='查阅的图书不止一本！请重新选择查找方式并按下列筛选图书输入新的关键词')
                    # if k == "Y" or k == 'y':
                    #     print('继续查询！')
                    #     print('请在下方选择追加输入的条件！')  # 然后这里就会挑出循环到达while(1)开头
                    i = 1
                    #     #continue
                    # if k == 'N' or k == 'n':
                    #     print('返回初始图书查找页面！')
                    #     lines_str = line2  # 为了防止图书查找有重复后再次查找后想继续查找别的；不然只会在result的范围内跑
                if length == 1:
                    # k = input('以上可能是您要的图书！请问还要继续查询吗(y/n)')
                    tk.messagebox.showinfo(title='消息提示框', message='以上可能是您要的图书！')
                    # if k == 'y' or k == "Y":
                    #     print('继续查找图书！')
                    result = []
                    i = 0
                    self.finalfind_index = index_  # 将找出来的书在库存里的序号放入finalfind_index
                    #     #continue
                    # if k == 'n' or k == "N":
                    #     print('查找结束，即将退出！')
                    #     #break
                if length == 0:
                    # k = input('没有找到您所要的书本！请更换关键词或按照其他方式查找！请问还要继续查询吗？(y/n)')
                    tk.messagebox.showinfo(title='消息提示框', message='没有找到您所要的书本！请更换关键词或按照其他方式查找！')
                    # if k == 'y' or k == "Y":
                    #     print('继续查找图书！')
                    #     #continue
                    # if k == 'n' or k == "N":
                    #     print('查找结束，即将退出！')
                    #     #break
            if self.method == '书名':
                index_gather = [e for e, m in enumerate(name) if a in m]  # 为了规避index只能查找一个
                print(name)
                copy = []  # 专门针对重复情况而设置的， 正常情况下copy不会动为0， 重复情况可由i == 1 引出
                if len(lines_str) > 0:  # 这一个判断用于删除treeview表格内之前的数据，然后再打印出新的图书信息覆盖
                    self.delTreeview(self)
                for index_ in index_gather:
                    if i == 0:  # 表示未重复初始输入状态
                        result.append(lines_str[index_])
                        self.table.insert('', tk.END, values=lines_str[index_].split())  # 添加数据到末尾
                    if lines_str[index_] in result and i == 1:  # 主要用于重复后第二次判断用的，如果不在里面，则代表是其他重复情况
                        copy.append(lines_str[index_])
                if i == 0:
                    length = len(result)
                    # print(length)
                if i == 1:
                    result = [co for co in copy]
                    if len(result) == 0:
                        tk.messagebox.showinfo(title='消息提示框', message='请输入其他有效信息！该信息在内部查不到任何内容！')
                    elif len(result) >= 1:
                        length = len(result)
                if length > 1:
                    tk.messagebox.showinfo(title='消息提示框', message='查阅的图书不止一本！请重新选择查找方式并按下列筛选图书输入新的关键词')
                    i = 1
                if length == 1:
                    tk.messagebox.showinfo(title='消息提示框', message='以上可能是您要的图书！')
                    result = []
                    i = 0
                    self.finalfind_index = index_  # 将找出来的书在库存里的序号放入finalfind_index
                if length == 0:
                    tk.messagebox.showinfo(title='消息提示框', message='没有找到您所要的书本！请更换关键词或按照其他方式查找！')
            if self.method == '作者名称':
                index_gather = [e for e, m in enumerate(public_address) if a in m]  # 为了规避index只能查找一个
                # print(public_address) #实际上是作者名称 public address
                copy = []  # 专门针对重复情况而设置的， 正常情况下copy不会动为0， 重复情况可由i == 1 引出
                if len(lines_str) > 0:  # 这一个判断用于删除treeview表格内之前的数据，然后再打印出新的图书信息覆盖
                    self.delTreeview(self)
                for index_ in index_gather:
                    if i == 0:  # 表示未重复初始输入状态
                        result.append(lines_str[index_])
                        self.table.insert('', tk.END, values=lines_str[index_].split())  # 添加数据到末尾
                    if lines_str[index_] in result and i == 1:  # 主要用于重复后第二次判断用的，如果不在里面，则代表是其他重复情况
                        copy.append(lines_str[index_])
                if i == 0:
                    length = len(result)
                    # print(length)
                if i == 1:
                    result = [co for co in copy]
                    if len(result) == 0:
                        tk.messagebox.showinfo(title='消息提示框', message='请输入其他有效信息！该信息在内部查不到任何内容！')
                    elif len(result) >= 1:
                        length = len(result)
                if length > 1:
                    tk.messagebox.showinfo(title='消息提示框', message='查阅的图书不止一本！请重新选择查找方式并按下列筛选图书输入新的关键词')
                    i = 1
                if length == 1:
                    tk.messagebox.showinfo(title='消息提示框', message='以上可能是您要的图书！')
                    result = []
                    i = 0
                    self.finalfind_index = index_  # 将找出来的书在库存里的序号放入finalfind_index
                if length == 0:
                    tk.messagebox.showinfo(title='消息提示框', message='没有找到您所要的书本！请更换关键词或按照其他方式查找！')
            if self.method == '出版社信息':
                index_gather = [e for e, m in enumerate(public_time) if a in m]  # 为了规避index只能查找一个
                # print(public_time)  #实际上是出版社信息 public time
                copy = []  # 专门针对重复情况而设置的， 正常情况下copy不会动为0， 重复情况可由i == 1 引出
                if len(lines_str) > 0:  # 这一个判断用于删除treeview表格内之前的数据，然后再打印出新的图书信息覆盖
                    self.delTreeview(self)
                for index_ in index_gather:
                    if i == 0:  # 表示未重复初始输入状态
                        result.append(lines_str[index_])
                        self.table.insert('', tk.END, values=lines_str[index_].split())  # 添加数据到末尾
                    if lines_str[index_] in result and i == 1:  # 主要用于重复后第二次判断用的，如果不在里面，则代表是其他重复情况
                        copy.append(lines_str[index_])
                if i == 0:
                    length = len(result)
                    # print(length)
                if i == 1:
                    result = [co for co in copy]
                    if len(result) == 0:
                        tk.messagebox.showinfo(title='消息提示框', message='请输入其他有效信息！该信息在内部查不到任何内容！')
                    elif len(result) >= 1:
                        length = len(result)
                if length > 1:
                    tk.messagebox.showinfo(title='消息提示框', message='查阅的图书不止一本！请重新选择查找方式并按下列筛选图书输入新的关键词')
                    i = 1
                if length == 1:
                    tk.messagebox.showinfo(title='消息提示框', message='以上可能是您要的图书！')
                    result = []
                    i = 0
                    self.finalfind_index = index_  # 将找出来的书在库存里的序号放入finalfind_index
                if length == 0:
                    tk.messagebox.showinfo(title='消息提示框', message='没有找到您所要的书本！请更换关键词或按照其他方式查找！')
            if self.method == '出版时间':
                index_gather = [e for e, m in enumerate(price) if a in m]  # 为了规避index只能查找一个
                # print(price) #实际上是出版时间 price
                copy = []  # 专门针对重复情况而设置的， 正常情况下copy不会动为0， 重复情况可由i == 1 引出
                if len(lines_str) > 0:  # 这一个判断用于删除treeview表格内之前的数据，然后再打印出新的图书信息覆盖
                    self.delTreeview(self)
                for index_ in index_gather:
                    if i == 0:  # 表示未重复初始输入状态
                        result.append(lines_str[index_])
                        self.table.insert('', tk.END, values=lines_str[index_].split())  # 添加数据到末尾
                    if lines_str[index_] in result and i == 1:  # 主要用于重复后第二次判断用的，如果不在里面，则代表是其他重复情况
                        copy.append(lines_str[index_])
                if i == 0:
                    length = len(result)
                    # print(length)
                if i == 1:
                    result = [co for co in copy]
                    if len(result) == 0:
                        tk.messagebox.showinfo(title='消息提示框', message='请输入其他有效信息！该信息在内部查不到任何内容！')
                    elif len(result) >= 1:
                        length = len(result)
                if length > 1:
                    tk.messagebox.showinfo(title='消息提示框', message='查阅的图书不止一本！请重新选择查找方式并按下列筛选图书输入新的关键词')
                    i = 1
                if length == 1:
                    tk.messagebox.showinfo(title='消息提示框', message='以上可能是您要的图书！')
                    result = []
                    i = 0
                    self.finalfind_index = index_  # 将找出来的书在库存里的序号放入finalfind_index
                if length == 0:
                    tk.messagebox.showinfo(title='消息提示框', message='没有找到您所要的书本！请更换关键词或按照其他方式查找！')
            if self.method == '书本价格':
                index_gather = [e for e, m in enumerate(author_name) if a in m]  # 为了规避index只能查找一个
                # print(author_name) #实际上对应的是书本价格author name
                copy = []  # 专门针对重复情况而设置的， 正常情况下copy不会动为0， 重复情况可由i == 1 引出
                if len(lines_str) > 0:  # 这一个判断用于删除treeview表格内之前的数据，然后再打印出新的图书信息覆盖
                    self.delTreeview(self)
                for index_ in index_gather:
                    if i == 0:  # 表示未重复初始输入状态
                        result.append(lines_str[index_])
                        self.table.insert('', tk.END, values=lines_str[index_].split())  # 添加数据到末尾
                    if lines_str[index_] in result and i == 1:  # 主要用于重复后第二次判断用的，如果不在里面，则代表是其他重复情况
                        copy.append(lines_str[index_])
                if i == 0:
                    length = len(result)
                    # print(length)
                if i == 1:
                    result = [co for co in copy]
                    if len(result) == 0:
                        tk.messagebox.showinfo(title='消息提示框', message='请输入其他有效信息！该信息在内部查不到任何内容！')
                    elif len(result) >= 1:
                        length = len(result)
                if length > 1:
                    tk.messagebox.showinfo(title='消息提示框', message='查阅的图书不止一本！请重新选择查找方式并按下列筛选图书输入新的关键词')
                    i = 1
                if length == 1:
                    tk.messagebox.showinfo(title='消息提示框', message='以上可能是您要的图书！')
                    result = []
                    i = 0
                    self.finalfind_index = index_  # 将找出来的书在库存里的序号放入finalfind_index
                if length == 0:
                    tk.messagebox.showinfo(title='消息提示框', message='没有找到您所要的书本！请更换关键词或按照其他方式查找！')

    # 修改图书信息函数
    def change(self):
        #print(self.finalfind_index)
        if self.finalfind_index != None:
            #print(self.finalfind_index)
            number = []
            name = []
            public_address = []
            public_time = []
            price = []
            author_name = []
            introduction = []
            lines_str = []  # 字符串形式， 直接输出结果
            with open('library.txt', 'r') as f:
                line = f.readline()
                while line:
                    # print(line.rstrip())  # 后面跟 ',' 将忽略换行符
                    lines_str.append(line.rstrip('\n'))
                    line = line.strip().split()
                    number.append(line[0])
                    name.append(line[1])
                    public_address.append(line[2])
                    public_time.append(line[3])
                    price.append(line[4])
                    author_name.append(line[5])
                    introduction.append(line[6])
                    line = f.readline()
                f.close()

            endtoend = {1: number,
                        2: name,
                        3: public_address,
                        4: public_time,
                        5: price,
                        6: author_name,
                        7: introduction

                        }
            toto = [1, 2, 3, 4, 5, 6, 7]
            # k1 = input(
            #     '请输入你所想要修改的图书的信息(INBS--1/book_name--2/public_address--3/public_time--4/prcie--5/author_name--6/introduction--7):')
            k1 = self.changeinfotype_number
            for to in toto:
                if k1 == to and k1 != 8:
                    # edition_ = input('请输入你所想要修改的内容:')
                    edition_ = self.changeinfo.get()
                    if edition_ == '':
                        tk.messagebox.showinfo(title='消息提示框', message='请输入修改信息！')
                    else:
                        endtoend[to][self.finalfind_index] = edition_  # 这里的index一定为1
                        with open('library.txt', 'w') as f:
                            for content_ in range(len(number)):
                                f.write(number[content_] + ' ')
                                f.write(name[content_] + ' ')
                                f.write(public_address[content_] + ' ')
                                f.write(public_time[content_] + ' ')
                                f.write(price[content_] + ' ')
                                f.write(author_name[content_] + ' ')
                                f.write(introduction[content_] + '\n')
                        tk.messagebox.showinfo(title='消息提示框', message='修改成功！')
            # if k1 == 8:
            #     del lines_str[self.finalfind_index]
            #     with open('library.txt', 'w') as f:
            #         for content2 in lines_str:
            #             f.write(content2 + '\n')
            #     tk.messagebox.showinfo(title='消息提示框', message='删除成功！')
        else:
            tk.messagebox.showinfo(title='消息提示框', message='请继续查找，确定修改书目！')

        # 修改完成后
        self.finalfind_index = None

# 删除图书页面
class DeleteMenu:
    def __init__(self, window):
        # 页面信息
        self.window = window
        self.window.title("史上最丑图书管理系统")
        self.window.geometry("800x500")

        # 定义容器 self.tabel_frame
        self.tabel_frame = tkinter.Frame(window)
        self.tabel_frame.pack()
        # 定义滚动条及其表格
        if 1:
            xscroll = tk.Scrollbar(self.tabel_frame, orient=tk.HORIZONTAL)
            yscroll = tk.Scrollbar(self.tabel_frame, orient=tk.VERTICAL)
            columns = ['ISBN号', '书名', '作者名称', '出版社信息', '出版时间', '书本价格', '图书简介']
            self.table = tk.ttk.Treeview(
                master=self.tabel_frame,  # 父容器
                height=10,  # 表格显示的行数,height行
                columns=columns,  # 显示的列
                show='headings',  # 隐藏首列
                xscrollcommand=xscroll.set,  # x轴滚动条
                yscrollcommand=yscroll.set,  # y轴滚动条
            )
            # 定义表头
            self.table.heading(column='ISBN号', text='INBS号', )  # 点击表头出发lambda函数
            self.table.heading('书名', text='书名', )
            self.table.heading('作者名称', text='作者名称', )
            self.table.heading('出版社信息', text='出版社信息', )
            self.table.heading('出版时间', text='出版时间', )
            self.table.heading('书本价格', text='书本价格', )
            self.table.heading('图书简介', text='图书简介', )  # 点击表头出发lambda函数)
            # 定义列
            self.table.column('ISBN号', width=100, minwidth=100, anchor='s', )
            self.table.column('书名', width=100, minwidth=100, anchor='s')
            self.table.column('作者名称', width=100, minwidth=100, anchor='s')
            self.table.column('出版社信息', width=150, minwidth=150, anchor='s')
            self.table.column('出版时间', width=100, minwidth=100, anchor='s')
            self.table.column('书本价格', width=80, minwidth=80, anchor='s')
            self.table.column('图书简介', width=200, minwidth=100, anchor='s')
            # config绑定滚动条为滚动事件 pack放置滚动条再最边边
            xscroll.config(command=self.table.xview)
            xscroll.pack(side=tk.BOTTOM, fill=tk.X)
            yscroll.config(command=self.table.yview)
            yscroll.pack(side=tk.RIGHT, fill=tk.Y)
            self.table.pack(pady=120)

        # 设计搜索方法和关键字搜索框
        if 1:
            self.labelfindmethod = tkinter.Label(window, text='查找方式', justify=tkinter.RIGHT, width=50)
            self.labelfindmethod.place(x=10, y=40, width=50, height=30)

            self.labelenterkeywords = tkinter.Label(window, text='关键词', justify=tkinter.RIGHT, width=50)
            self.labelenterkeywords.place(x=220, y=40, width=50, height=30)
            # 搜索方法元组
            finemethod = ('ISBN号', '书名', '作者名称', '出版社信息', '出版时间', '书本价格')
            # 查找方式组合框
            self.comboFM = tkinter.ttk.Combobox(window, values=finemethod, width=50)
            self.comboFM.place(x=70, y=40, width=100, height=30)  # 选择框的位置
            # 绑定事件处理函数
            self.comboFM.bind('<<ComboboxSelected>> ', self.comboChange)

            # 输入框定义--关键字
            self.keywords = tk.StringVar()
            self.entry_keywords = tk.Entry(window, textvariable=self.keywords)
            self.entry_keywords.place(x=280, y=40, width=200, height=30)

        # 定义按钮
        if 1:
            # 关键词查找按键
            self.findbut = tk.Button(self.window, text="关键词查找", bd=5, font=('黑体', 15, 'bold'), command=self.find)
            self.findbut.place(x=500, y=40, width=200, height=30)
            # 修改图书信息按键
            self.deletebut = tk.Button(self.window, text="删除图书信息", bd=5, font=('黑体', 15, 'bold'), command=self.delete)
            self.deletebut.place(x=350, y=350, width=150, height=50)
            # 返回主菜单
            self.backbut = tk.Button(self.window, text="返回主菜单", bd=5, font=('黑体', 20, 'bold'), command=self.back)
            self.backbut.place(x=550, y=400, width=200, height=50)
            # 帮助按钮
            self.helpbut = tk.Button(self.window, text="帮助", bd=5, font=('黑体', 10, 'bold'), command=self.help)
            self.helpbut.place(x=60, y=420, width=50, height=30)

    def help(self):
        tk.messagebox.showinfo(title='消息提示框', message='请查询出你所需的图书，点击删除按钮删除')

    # 组合框：事件处理函数--关键字种类
    def comboChange(self, *args, **kwargs):
        self.method = self.comboFM.get()

    def back(self):
        self.helpbut.destroy()
        self.labelenterkeywords.destroy()
        self.deletebut.destroy()
        self.backbut.destroy()
        self.findbut.destroy()
        self.comboFM.destroy()
        self.entry_keywords.destroy()
        self.labelfindmethod.destroy()
        self.tabel_frame.destroy()
        MainMenu(root)

    # 删除treeview所有
    def delTreeview(self, *args, **kwargs):
        x = self.table.get_children()
        for item in x:
            self.table.delete(item)

    # 关键词查找函数
    def find(self):
        # self.keywords_get = self.keywords.get()  # 获取输入框内部的关键字
        # columns = ['ISBN号', '书名', '作者名称', '出版社信息', '出版时间', '书本价格', '图书简介']
        number = []
        name = []
        public_address = []
        public_time = []
        price = []
        author_name = []
        lines_str = []  # 字符串形式， 直接输出结果
        # self.finalfind_index = None   # 将找出来的书在库存里的序号放入finalfind_index

        result = []
        i = 0
        # 打开文件提取图书信息
        with open('library.txt', 'r') as f:
            line = f.readline()
            while line:
                # print(line.rstrip())  # 后面跟 ',' 将忽略换行符
                lines_str.append(line.rstrip('\n'))
                line = line.strip().split()
                number.append(line[0])
                name.append(line[1])
                public_address.append(line[2])
                public_time.append(line[3])
                price.append(line[4])
                author_name.append(line[5])
                line = f.readline()
            f.close()
        line2 = [t for t in lines_str]

        a = self.keywords.get() #获取关键词输入框内文字
        if a == '':
            tk.messagebox.showinfo(title='消息提示框', message='请输入关键词！')
        else:
        # 关键词查找种类的判定
            if self.method == 'ISBN号':
                index_gather = [e for e, m in enumerate(number) if a in m]  # 为了规避index只能查找一个
                copy = []  # 专门针对重复情况而设置的， 正常情况下copy不会动为0， 重复情况可由i == 1 引出
                if len(lines_str) > 0:  # 这一个判断用于删除treeview表格内之前的数据，然后再打印出新的图书信息覆盖
                    self.delTreeview(self)
                for index_ in index_gather:
                    if i == 0:  # 表示未重复初始输入状态
                        result.append(lines_str[index_])
                        self.table.insert('', tk.END, values=lines_str[index_].split())  # 添加数据到末尾
                    if lines_str[index_] in result and i == 1:  # 主要用于重复后第二次判断用的，如果不在里面，则代表是其他重复情况
                        copy.append(lines_str[index_])
                if i == 0:
                    length = len(result)
                    # print(length)
                if i == 1:
                    result = [co for co in copy]
                    if len(result) == 0:
                        # print('请输入其他有效信息！该信息在内部查不到任何内容！')
                        tk.messagebox.showinfo(title='消息提示框', message='请输入其他有效信息！该信息在内部查不到任何内容！')
                        # continue
                    elif len(result) >= 1:
                        length = len(result)
                if length > 1:
                    # k = input('查阅的图书不止一本！要想继续按照关键词查找图书吗？(y/n)')
                    tk.messagebox.showinfo(title='消息提示框', message='查阅的图书不止一本！请重新选择查找方式并按下列筛选图书输入新的关键词')
                    # if k == "Y" or k == 'y':
                    #     print('继续查询！')
                    #     print('请在下方选择追加输入的条件！')  # 然后这里就会挑出循环到达while(1)开头
                    i = 1
                    #     #continue
                    # if k == 'N' or k == 'n':
                    #     print('返回初始图书查找页面！')
                    #     lines_str = line2  # 为了防止图书查找有重复后再次查找后想继续查找别的；不然只会在result的范围内跑
                if length == 1:
                    # k = input('以上可能是您要的图书！请问还要继续查询吗(y/n)')
                    tk.messagebox.showinfo(title='消息提示框', message='以上可能是您要的图书！')
                    # if k == 'y' or k == "Y":
                    #     print('继续查找图书！')
                    result = []
                    i = 0
                    self.finalfind_index = index_  # 将找出来的书在库存里的序号放入finalfind_index
                    #     #continue
                    # if k == 'n' or k == "N":
                    #     print('查找结束，即将退出！')
                    #     #break
                if length == 0:
                    # k = input('没有找到您所要的书本！请更换关键词或按照其他方式查找！请问还要继续查询吗？(y/n)')
                    tk.messagebox.showinfo(title='消息提示框', message='没有找到您所要的书本！请更换关键词或按照其他方式查找！')
                    # if k == 'y' or k == "Y":
                    #     print('继续查找图书！')
                    #     #continue
                    # if k == 'n' or k == "N":
                    #     print('查找结束，即将退出！')
                    #     #break
            if self.method == '书名':
                index_gather = [e for e, m in enumerate(name) if a in m]  # 为了规避index只能查找一个
                print(name)
                copy = []  # 专门针对重复情况而设置的， 正常情况下copy不会动为0， 重复情况可由i == 1 引出
                if len(lines_str) > 0:  # 这一个判断用于删除treeview表格内之前的数据，然后再打印出新的图书信息覆盖
                    self.delTreeview(self)
                for index_ in index_gather:
                    if i == 0:  # 表示未重复初始输入状态
                        result.append(lines_str[index_])
                        self.table.insert('', tk.END, values=lines_str[index_].split())  # 添加数据到末尾
                    if lines_str[index_] in result and i == 1:  # 主要用于重复后第二次判断用的，如果不在里面，则代表是其他重复情况
                        copy.append(lines_str[index_])
                if i == 0:
                    length = len(result)
                    # print(length)
                if i == 1:
                    result = [co for co in copy]
                    if len(result) == 0:
                        tk.messagebox.showinfo(title='消息提示框', message='请输入其他有效信息！该信息在内部查不到任何内容！')
                    elif len(result) >= 1:
                        length = len(result)
                if length > 1:
                    tk.messagebox.showinfo(title='消息提示框', message='查阅的图书不止一本！请重新选择查找方式并按下列筛选图书输入新的关键词')
                    i = 1
                if length == 1:
                    tk.messagebox.showinfo(title='消息提示框', message='以上可能是您要的图书！')
                    result = []
                    i = 0
                    self.finalfind_index = index_  # 将找出来的书在库存里的序号放入finalfind_index
                if length == 0:
                    tk.messagebox.showinfo(title='消息提示框', message='没有找到您所要的书本！请更换关键词或按照其他方式查找！')
            if self.method == '作者名称':
                index_gather = [e for e, m in enumerate(public_address) if a in m]  # 为了规避index只能查找一个
                # print(public_address) #实际上是作者名称 public address
                copy = []  # 专门针对重复情况而设置的， 正常情况下copy不会动为0， 重复情况可由i == 1 引出
                if len(lines_str) > 0:  # 这一个判断用于删除treeview表格内之前的数据，然后再打印出新的图书信息覆盖
                    self.delTreeview(self)
                for index_ in index_gather:
                    if i == 0:  # 表示未重复初始输入状态
                        result.append(lines_str[index_])
                        self.table.insert('', tk.END, values=lines_str[index_].split())  # 添加数据到末尾
                    if lines_str[index_] in result and i == 1:  # 主要用于重复后第二次判断用的，如果不在里面，则代表是其他重复情况
                        copy.append(lines_str[index_])
                if i == 0:
                    length = len(result)
                    # print(length)
                if i == 1:
                    result = [co for co in copy]
                    if len(result) == 0:
                        tk.messagebox.showinfo(title='消息提示框', message='请输入其他有效信息！该信息在内部查不到任何内容！')
                    elif len(result) >= 1:
                        length = len(result)
                if length > 1:
                    tk.messagebox.showinfo(title='消息提示框', message='查阅的图书不止一本！请重新选择查找方式并按下列筛选图书输入新的关键词')
                    i = 1
                if length == 1:
                    tk.messagebox.showinfo(title='消息提示框', message='以上可能是您要的图书！')
                    result = []
                    i = 0
                    self.finalfind_index = index_  # 将找出来的书在库存里的序号放入finalfind_index
                if length == 0:
                    tk.messagebox.showinfo(title='消息提示框', message='没有找到您所要的书本！请更换关键词或按照其他方式查找！')
            if self.method == '出版社信息':
                index_gather = [e for e, m in enumerate(public_time) if a in m]  # 为了规避index只能查找一个
                # print(public_time)  #实际上是出版社信息 public time
                copy = []  # 专门针对重复情况而设置的， 正常情况下copy不会动为0， 重复情况可由i == 1 引出
                if len(lines_str) > 0:  # 这一个判断用于删除treeview表格内之前的数据，然后再打印出新的图书信息覆盖
                    self.delTreeview(self)
                for index_ in index_gather:
                    if i == 0:  # 表示未重复初始输入状态
                        result.append(lines_str[index_])
                        self.table.insert('', tk.END, values=lines_str[index_].split())  # 添加数据到末尾
                    if lines_str[index_] in result and i == 1:  # 主要用于重复后第二次判断用的，如果不在里面，则代表是其他重复情况
                        copy.append(lines_str[index_])
                if i == 0:
                    length = len(result)
                    # print(length)
                if i == 1:
                    result = [co for co in copy]
                    if len(result) == 0:
                        tk.messagebox.showinfo(title='消息提示框', message='请输入其他有效信息！该信息在内部查不到任何内容！')
                    elif len(result) >= 1:
                        length = len(result)
                if length > 1:
                    tk.messagebox.showinfo(title='消息提示框', message='查阅的图书不止一本！请重新选择查找方式并按下列筛选图书输入新的关键词')
                    i = 1
                if length == 1:
                    tk.messagebox.showinfo(title='消息提示框', message='以上可能是您要的图书！')
                    result = []
                    i = 0
                    self.finalfind_index = index_  # 将找出来的书在库存里的序号放入finalfind_index
                if length == 0:
                    tk.messagebox.showinfo(title='消息提示框', message='没有找到您所要的书本！请更换关键词或按照其他方式查找！')
            if self.method == '出版时间':
                index_gather = [e for e, m in enumerate(price) if a in m]  # 为了规避index只能查找一个
                # print(price) #实际上是出版时间 price
                copy = []  # 专门针对重复情况而设置的， 正常情况下copy不会动为0， 重复情况可由i == 1 引出
                if len(lines_str) > 0:  # 这一个判断用于删除treeview表格内之前的数据，然后再打印出新的图书信息覆盖
                    self.delTreeview(self)
                for index_ in index_gather:
                    if i == 0:  # 表示未重复初始输入状态
                        result.append(lines_str[index_])
                        self.table.insert('', tk.END, values=lines_str[index_].split())  # 添加数据到末尾
                    if lines_str[index_] in result and i == 1:  # 主要用于重复后第二次判断用的，如果不在里面，则代表是其他重复情况
                        copy.append(lines_str[index_])
                if i == 0:
                    length = len(result)
                    # print(length)
                if i == 1:
                    result = [co for co in copy]
                    if len(result) == 0:
                        tk.messagebox.showinfo(title='消息提示框', message='请输入其他有效信息！该信息在内部查不到任何内容！')
                    elif len(result) >= 1:
                        length = len(result)
                if length > 1:
                    tk.messagebox.showinfo(title='消息提示框', message='查阅的图书不止一本！请重新选择查找方式并按下列筛选图书输入新的关键词')
                    i = 1
                if length == 1:
                    tk.messagebox.showinfo(title='消息提示框', message='以上可能是您要的图书！')
                    result = []
                    i = 0
                    self.finalfind_index = index_  # 将找出来的书在库存里的序号放入finalfind_index
                if length == 0:
                    tk.messagebox.showinfo(title='消息提示框', message='没有找到您所要的书本！请更换关键词或按照其他方式查找！')
            if self.method == '书本价格':
                index_gather = [e for e, m in enumerate(author_name) if a in m]  # 为了规避index只能查找一个
                # print(author_name) #实际上对应的是书本价格author name
                copy = []  # 专门针对重复情况而设置的， 正常情况下copy不会动为0， 重复情况可由i == 1 引出
                if len(lines_str) > 0:  # 这一个判断用于删除treeview表格内之前的数据，然后再打印出新的图书信息覆盖
                    self.delTreeview(self)
                for index_ in index_gather:
                    if i == 0:  # 表示未重复初始输入状态
                        result.append(lines_str[index_])
                        self.table.insert('', tk.END, values=lines_str[index_].split())  # 添加数据到末尾
                    if lines_str[index_] in result and i == 1:  # 主要用于重复后第二次判断用的，如果不在里面，则代表是其他重复情况
                        copy.append(lines_str[index_])
                if i == 0:
                    length = len(result)
                    # print(length)
                if i == 1:
                    result = [co for co in copy]
                    if len(result) == 0:
                        tk.messagebox.showinfo(title='消息提示框', message='请输入其他有效信息！该信息在内部查不到任何内容！')
                    elif len(result) >= 1:
                        length = len(result)
                if length > 1:
                    tk.messagebox.showinfo(title='消息提示框', message='查阅的图书不止一本！请重新选择查找方式并按下列筛选图书输入新的关键词')
                    i = 1
                if length == 1:
                    tk.messagebox.showinfo(title='消息提示框', message='以上可能是您要的图书！')
                    result = []
                    i = 0
                    self.finalfind_index = index_  # 将找出来的书在库存里的序号放入finalfind_index
                if length == 0:
                    tk.messagebox.showinfo(title='消息提示框', message='没有找到您所要的关键词！请更换关键词或按照其他方式查找！')

    # 修改图书信息函数
    def delete(self):
        #print(self.finalfind_index)
        if self.finalfind_index != None:
            #print(self.finalfind_index)
            number = []
            name = []
            public_address = []
            public_time = []
            price = []
            author_name = []
            introduction = []
            lines_str = []  # 字符串形式， 直接输出结果
            with open('library.txt', 'r') as f:
                line = f.readline()
                while line:
                    # print(line.rstrip())  # 后面跟 ',' 将忽略换行符
                    lines_str.append(line.rstrip('\n'))
                    line = line.strip().split()
                    number.append(line[0])
                    name.append(line[1])
                    public_address.append(line[2])
                    public_time.append(line[3])
                    price.append(line[4])
                    author_name.append(line[5])
                    introduction.append(line[6])
                    line = f.readline()
                f.close()

            del lines_str[self.finalfind_index]
            with open('library.txt', 'w') as f:
                for content2 in lines_str:
                    f.write(content2 + '\n')
            tk.messagebox.showinfo(title='消息提示框', message='删除成功！')

        # 修改完成后
        self.finalfind_index = None

# 查找图书页面 OK
class FindMenu:
    def __init__(self, window):
        # 页面信息
        self.window = window
        self.window.title("史上最丑图书管理系统")
        self.window.geometry("800x500")

        # 定义容器 self.tabel_frame
        self.tabel_frame = tkinter.Frame(window)
        self.tabel_frame.pack()
        # 定义滚动条及其表格
        if 1:
            xscroll = tk.Scrollbar(self.tabel_frame, orient=tk.HORIZONTAL)
            yscroll = tk.Scrollbar(self.tabel_frame, orient=tk.VERTICAL)
            columns = ['ISBN号', '书名', '作者名称', '出版社信息', '出版时间', '书本价格', '图书简介']
            self.table = tk.ttk.Treeview(
                master=self.tabel_frame,  # 父容器
                height=10,  # 表格显示的行数,height行
                columns=columns,  # 显示的列
                show='headings',  # 隐藏首列
                xscrollcommand=xscroll.set,  # x轴滚动条
                yscrollcommand=yscroll.set,  # y轴滚动条
            )
            # 定义表头
            self.table.heading(column='ISBN号', text='INBS号', )  # 点击表头出发lambda函数
            self.table.heading('书名', text='书名', )
            self.table.heading('作者名称', text='作者名称', )
            self.table.heading('出版社信息', text='出版社信息', )
            self.table.heading('出版时间', text='出版时间', )
            self.table.heading('书本价格', text='书本价格', )
            self.table.heading('图书简介', text='图书简介', )  # 点击表头出发lambda函数)
            # 定义列
            self.table.column('ISBN号', width=100, minwidth=100, anchor='s', )
            self.table.column('书名', width=100, minwidth=100, anchor='s')
            self.table.column('作者名称', width=100, minwidth=100, anchor='s')
            self.table.column('出版社信息', width=150, minwidth=150, anchor='s')
            self.table.column('出版时间', width=100, minwidth=100, anchor='s')
            self.table.column('书本价格', width=80, minwidth=80, anchor='s')
            self.table.column('图书简介', width=200, minwidth=100, anchor='s')
            # config绑定滚动条为滚动事件 pack放置滚动条再最边边
            xscroll.config(command=self.table.xview)
            xscroll.pack(side=tk.BOTTOM, fill=tk.X)
            yscroll.config(command=self.table.yview)
            yscroll.pack(side=tk.RIGHT, fill=tk.Y)
            self.table.pack(pady=120)

        # 设计搜索方法和关键字搜索框
        if 1:
            self.labelfindmethod = tkinter.Label(window, text='查找方式', justify=tkinter.RIGHT, width=50)
            self.labelfindmethod.place(x=10, y=40, width=50, height=30)

            self.labelenterkeywords = tkinter.Label(window, text='关键词', justify=tkinter.RIGHT, width=50)
            self.labelenterkeywords.place(x=220, y=40, width=50, height=30)
            # 搜索方法元组
            finemethod = ('ISBN号', '书名', '作者名称', '出版社信息', '出版时间', '书本价格')
            # 查找方式组合框
            self.comboFM = tkinter.ttk.Combobox(window, values=finemethod, width=50)
            self.comboFM.place(x=70, y=40, width=100, height=30)  # 选择框的位置
            # 绑定事件处理函数
            self.comboFM.bind('<<ComboboxSelected>> ', self.comboChange)

            # 输入框定义--关键字
            self.keywords = tk.StringVar()
            self.entry_keywords = tk.Entry(window, textvariable=self.keywords)
            self.entry_keywords.place(x=280, y=40, width=200, height=30)

        # 定义按钮
        if 1:
            # 关键词查找按键
            self.findbut = tk.Button(self.window, text="关键词查找", bd=5, font=('黑体', 15, 'bold'), command=self.find)
            self.findbut.place(x=500, y=40, width=200, height=30)
            # 返回主菜单
            self.backbut = tk.Button(self.window, text="返回主菜单", bd=5, font=('黑体', 20, 'bold'), command=self.back)
            self.backbut.place(x=550, y=400, width=200, height=50)
            # 帮助按钮
            self.helpbut = tk.Button(self.window, text="帮助", bd=5, font=('黑体', 10, 'bold'), command=self.help)
            self.helpbut.place(x=60, y=420, width=50, height=30)

    def help(self):
        tk.messagebox.showinfo(title='消息提示框', message='请选择搜索的关键词种类，输入关键词查询图书')

    # 组合框：事件处理函数--关键字种类
    def comboChange(self, *args, **kwargs):
        self.method = self.comboFM.get()

        # 组合框：事件处理函数--修改信息种类

    def back(self):
        self.helpbut.destroy()
        self.labelenterkeywords.destroy()
        self.backbut.destroy()
        self.findbut.destroy()
        self.comboFM.destroy()
        self.entry_keywords.destroy()
        self.labelfindmethod.destroy()
        self.tabel_frame.destroy()
        MainMenu(root)

        # 删除treeview所有

    def delTreeview(self, *args, **kwargs):
        x = self.table.get_children()
        for item in x:
            self.table.delete(item)

        # 关键词查找函数

    def find(self):
        # self.keywords_get = self.keywords.get()  # 获取输入框内部的关键字
        # columns = ['ISBN号', '书名', '作者名称', '出版社信息', '出版时间', '书本价格', '图书简介']
        number = []
        name = []
        public_address = []
        public_time = []
        price = []
        author_name = []
        lines_str = []  # 字符串形式， 直接输出结果
        # self.finalfind_index = None   # 将找出来的书在库存里的序号放入finalfind_index

        result = []
        i = 0
        # 打开文件提取图书信息
        with open('library.txt', 'r') as f:
            line = f.readline()
            while line:
                # print(line.rstrip())  # 后面跟 ',' 将忽略换行符
                lines_str.append(line.rstrip('\n'))
                line = line.strip().split()
                number.append(line[0])
                name.append(line[1])
                public_address.append(line[2])
                public_time.append(line[3])
                price.append(line[4])
                author_name.append(line[5])
                line = f.readline()
            f.close()
        line2 = [t for t in lines_str]

        a = self.keywords.get()  # 获取关键词输入框内文字
        if a == '':
            tk.messagebox.showinfo(title='消息提示框', message='请输入关键词！')
        else:
            # 关键词查找种类的判定
            if self.method == 'ISBN号':
                index_gather = [e for e, m in enumerate(number) if a in m]  # 为了规避index只能查找一个
                copy = []  # 专门针对重复情况而设置的， 正常情况下copy不会动为0， 重复情况可由i == 1 引出
                if len(lines_str) > 0:  # 这一个判断用于删除treeview表格内之前的数据，然后再打印出新的图书信息覆盖
                    self.delTreeview(self)
                for index_ in index_gather:
                    if i == 0:  # 表示未重复初始输入状态
                        result.append(lines_str[index_])
                        self.table.insert('', tk.END, values=lines_str[index_].split())  # 添加数据到末尾
                    if lines_str[index_] in result and i == 1:  # 主要用于重复后第二次判断用的，如果不在里面，则代表是其他重复情况
                        copy.append(lines_str[index_])
                if i == 0:
                    length = len(result)
                    # print(length)
                if i == 1:
                    result = [co for co in copy]
                    if len(result) == 0:
                        # print('请输入其他有效信息！该信息在内部查不到任何内容！')
                        tk.messagebox.showinfo(title='消息提示框', message='请输入其他有效信息！该信息在内部查不到任何内容！')
                        # continue
                    elif len(result) >= 1:
                        length = len(result)
                if length > 1:
                    # k = input('查阅的图书不止一本！要想继续按照关键词查找图书吗？(y/n)')
                    tk.messagebox.showinfo(title='消息提示框', message='查阅的图书不止一本！请重新选择查找方式并按下列筛选图书输入新的关键词')
                    # if k == "Y" or k == 'y':
                    #     print('继续查询！')
                    #     print('请在下方选择追加输入的条件！')  # 然后这里就会挑出循环到达while(1)开头
                    i = 1
                    #     #continue
                    # if k == 'N' or k == 'n':
                    #     print('返回初始图书查找页面！')
                    #     lines_str = line2  # 为了防止图书查找有重复后再次查找后想继续查找别的；不然只会在result的范围内跑
                if length == 1:
                    # k = input('以上可能是您要的图书！请问还要继续查询吗(y/n)')
                    tk.messagebox.showinfo(title='消息提示框', message='以上可能是您要的图书！')
                    # if k == 'y' or k == "Y":
                    #     print('继续查找图书！')
                    result = []
                    i = 0
                    self.finalfind_index = index_  # 将找出来的书在库存里的序号放入finalfind_index
                    #     #continue
                    # if k == 'n' or k == "N":
                    #     print('查找结束，即将退出！')
                    #     #break
                if length == 0:
                    # k = input('没有找到您所要的书本！请更换关键词或按照其他方式查找！请问还要继续查询吗？(y/n)')
                    tk.messagebox.showinfo(title='消息提示框', message='没有找到您所要的书本！请更换关键词或按照其他方式查找！')
                    # if k == 'y' or k == "Y":
                    #     print('继续查找图书！')
                    #     #continue
                    # if k == 'n' or k == "N":
                    #     print('查找结束，即将退出！')
                    #     #break
            if self.method == '书名':
                index_gather = [e for e, m in enumerate(name) if a in m]  # 为了规避index只能查找一个
                print(name)
                copy = []  # 专门针对重复情况而设置的， 正常情况下copy不会动为0， 重复情况可由i == 1 引出
                if len(lines_str) > 0:  # 这一个判断用于删除treeview表格内之前的数据，然后再打印出新的图书信息覆盖
                    self.delTreeview(self)
                for index_ in index_gather:
                    if i == 0:  # 表示未重复初始输入状态
                        result.append(lines_str[index_])
                        self.table.insert('', tk.END, values=lines_str[index_].split())  # 添加数据到末尾
                    if lines_str[index_] in result and i == 1:  # 主要用于重复后第二次判断用的，如果不在里面，则代表是其他重复情况
                        copy.append(lines_str[index_])
                if i == 0:
                    length = len(result)
                    # print(length)
                if i == 1:
                    result = [co for co in copy]
                    if len(result) == 0:
                        tk.messagebox.showinfo(title='消息提示框', message='请输入其他有效信息！该信息在内部查不到任何内容！')
                    elif len(result) >= 1:
                        length = len(result)
                if length > 1:
                    tk.messagebox.showinfo(title='消息提示框', message='查阅的图书不止一本！请重新选择查找方式并按下列筛选图书输入新的关键词')
                    i = 1
                if length == 1:
                    tk.messagebox.showinfo(title='消息提示框', message='以上可能是您要的图书！')
                    result = []
                    i = 0
                    self.finalfind_index = index_  # 将找出来的书在库存里的序号放入finalfind_index
                if length == 0:
                    tk.messagebox.showinfo(title='消息提示框', message='没有找到您所要的书本！请更换关键词或按照其他方式查找！')
            if self.method == '作者名称':
                index_gather = [e for e, m in enumerate(public_address) if a in m]  # 为了规避index只能查找一个
                # print(public_address) #实际上是作者名称 public address
                copy = []  # 专门针对重复情况而设置的， 正常情况下copy不会动为0， 重复情况可由i == 1 引出
                if len(lines_str) > 0:  # 这一个判断用于删除treeview表格内之前的数据，然后再打印出新的图书信息覆盖
                    self.delTreeview(self)
                for index_ in index_gather:
                    if i == 0:  # 表示未重复初始输入状态
                        result.append(lines_str[index_])
                        self.table.insert('', tk.END, values=lines_str[index_].split())  # 添加数据到末尾
                    if lines_str[index_] in result and i == 1:  # 主要用于重复后第二次判断用的，如果不在里面，则代表是其他重复情况
                        copy.append(lines_str[index_])
                if i == 0:
                    length = len(result)
                    # print(length)
                if i == 1:
                    result = [co for co in copy]
                    if len(result) == 0:
                        tk.messagebox.showinfo(title='消息提示框', message='请输入其他有效信息！该信息在内部查不到任何内容！')
                    elif len(result) >= 1:
                        length = len(result)
                if length > 1:
                    tk.messagebox.showinfo(title='消息提示框', message='查阅的图书不止一本！请重新选择查找方式并按下列筛选图书输入新的关键词')
                    i = 1
                if length == 1:
                    tk.messagebox.showinfo(title='消息提示框', message='以上可能是您要的图书！')
                    result = []
                    i = 0
                    self.finalfind_index = index_  # 将找出来的书在库存里的序号放入finalfind_index
                if length == 0:
                    tk.messagebox.showinfo(title='消息提示框', message='没有找到您所要的书本！请更换关键词或按照其他方式查找！')
            if self.method == '出版社信息':
                index_gather = [e for e, m in enumerate(public_time) if a in m]  # 为了规避index只能查找一个
                # print(public_time)  #实际上是出版社信息 public time
                copy = []  # 专门针对重复情况而设置的， 正常情况下copy不会动为0， 重复情况可由i == 1 引出
                if len(lines_str) > 0:  # 这一个判断用于删除treeview表格内之前的数据，然后再打印出新的图书信息覆盖
                    self.delTreeview(self)
                for index_ in index_gather:
                    if i == 0:  # 表示未重复初始输入状态
                        result.append(lines_str[index_])
                        self.table.insert('', tk.END, values=lines_str[index_].split())  # 添加数据到末尾
                    if lines_str[index_] in result and i == 1:  # 主要用于重复后第二次判断用的，如果不在里面，则代表是其他重复情况
                        copy.append(lines_str[index_])
                if i == 0:
                    length = len(result)
                    # print(length)
                if i == 1:
                    result = [co for co in copy]
                    if len(result) == 0:
                        tk.messagebox.showinfo(title='消息提示框', message='请输入其他有效信息！该信息在内部查不到任何内容！')
                    elif len(result) >= 1:
                        length = len(result)
                if length > 1:
                    tk.messagebox.showinfo(title='消息提示框', message='查阅的图书不止一本！请重新选择查找方式并按下列筛选图书输入新的关键词')
                    i = 1
                if length == 1:
                    tk.messagebox.showinfo(title='消息提示框', message='以上可能是您要的图书！')
                    result = []
                    i = 0
                    self.finalfind_index = index_  # 将找出来的书在库存里的序号放入finalfind_index
                if length == 0:
                    tk.messagebox.showinfo(title='消息提示框', message='没有找到您所要的书本！请更换关键词或按照其他方式查找！')
            if self.method == '出版时间':
                index_gather = [e for e, m in enumerate(price) if a in m]  # 为了规避index只能查找一个
                # print(price) #实际上是出版时间 price
                copy = []  # 专门针对重复情况而设置的， 正常情况下copy不会动为0， 重复情况可由i == 1 引出
                if len(lines_str) > 0:  # 这一个判断用于删除treeview表格内之前的数据，然后再打印出新的图书信息覆盖
                    self.delTreeview(self)
                for index_ in index_gather:
                    if i == 0:  # 表示未重复初始输入状态
                        result.append(lines_str[index_])
                        self.table.insert('', tk.END, values=lines_str[index_].split())  # 添加数据到末尾
                    if lines_str[index_] in result and i == 1:  # 主要用于重复后第二次判断用的，如果不在里面，则代表是其他重复情况
                        copy.append(lines_str[index_])
                if i == 0:
                    length = len(result)
                    # print(length)
                if i == 1:
                    result = [co for co in copy]
                    if len(result) == 0:
                        tk.messagebox.showinfo(title='消息提示框', message='请输入其他有效信息！该信息在内部查不到任何内容！')
                    elif len(result) >= 1:
                        length = len(result)
                if length > 1:
                    tk.messagebox.showinfo(title='消息提示框', message='查阅的图书不止一本！请重新选择查找方式并按下列筛选图书输入新的关键词')
                    i = 1
                if length == 1:
                    tk.messagebox.showinfo(title='消息提示框', message='以上可能是您要的图书！')
                    result = []
                    i = 0
                    self.finalfind_index = index_  # 将找出来的书在库存里的序号放入finalfind_index
                if length == 0:
                    tk.messagebox.showinfo(title='消息提示框', message='没有找到您所要的书本！请更换关键词或按照其他方式查找！')
            if self.method == '书本价格':
                index_gather = [e for e, m in enumerate(author_name) if a in m]  # 为了规避index只能查找一个
                # print(author_name) #实际上对应的是书本价格author name
                copy = []  # 专门针对重复情况而设置的， 正常情况下copy不会动为0， 重复情况可由i == 1 引出
                if len(lines_str) > 0:  # 这一个判断用于删除treeview表格内之前的数据，然后再打印出新的图书信息覆盖
                    self.delTreeview(self)
                for index_ in index_gather:
                    if i == 0:  # 表示未重复初始输入状态
                        result.append(lines_str[index_])
                        self.table.insert('', tk.END, values=lines_str[index_].split())  # 添加数据到末尾
                    if lines_str[index_] in result and i == 1:  # 主要用于重复后第二次判断用的，如果不在里面，则代表是其他重复情况
                        copy.append(lines_str[index_])
                if i == 0:
                    length = len(result)
                    # print(length)
                if i == 1:
                    result = [co for co in copy]
                    if len(result) == 0:
                        tk.messagebox.showinfo(title='消息提示框', message='请输入其他有效信息！该信息在内部查不到任何内容！')
                    elif len(result) >= 1:
                        length = len(result)
                if length > 1:
                    tk.messagebox.showinfo(title='消息提示框', message='查阅的图书不止一本！请重新选择查找方式并按下列筛选图书输入新的关键词')
                    i = 1
                if length == 1:
                    tk.messagebox.showinfo(title='消息提示框', message='以上可能是您要的图书！')
                    result = []
                    i = 0
                    self.finalfind_index = index_  # 将找出来的书在库存里的序号放入finalfind_index
                if length == 0:
                    tk.messagebox.showinfo(title='消息提示框', message='没有找到您所要的书本！请更换关键词或按照其他方式查找！')

# 显示图书页面 OK
class ShowAllMenu:
    def __init__(self, window):
        # 页面信息
        self.window = window
        self.window.title("史上最丑图书管理系统")
        self.window.geometry("800x500")

        # 插入数据
        def insert():
            lines = []  # 储存了数组形式， 每个元素都是分开的
            lines_str = []  # 字符串形式， 直接输出结果
            # 读取文件内数据
            with open('library.txt', 'r') as f:
                line = f.readline()
                while line:
                    # print(line.rstrip())  # 后面跟 ',' 将忽略换行符
                    lines_str.append(line.rstrip('\n'))
                    line = line.strip().split()
                    lines.append(line)
                    line = f.readline()
                f.close()
            for index, data in enumerate(lines):
                self.table.insert('', tk.END, values=data)  # 添加数据到末尾

        # 排序除价格外的书目
        def treeview_sort_column(tv, col, reverse):  # Treeview、列名、排列方式
            l = [(tv.set(k, col), k) for k in tv.get_children('')]
            #print(l)
            l.sort(reverse=reverse)  # 排序方式
            # rearrange items in sorted positions
            for index, (val, k) in enumerate(l):  # 根据排序后索引移动
                tv.move(k, '', index)
            tv.heading(col, command=lambda: treeview_sort_column(tv, col, not reverse))  # 重写标题，使之成为再点倒序的标题

        # 定义框架放置表格和滚动条
        if 1:
            self.tabel_frame = tkinter.Frame(window)
            self.tabel_frame.pack()
            # 定义滚动条
            xscroll = tk.Scrollbar(self.tabel_frame, orient=tk.HORIZONTAL)
            yscroll = tk.Scrollbar(self.tabel_frame, orient=tk.VERTICAL)
            columns = ['ISBN号', '书名', '作者名称', '出版社信息', '出版时间', '书本价格', '图书简介']
            self.table = tk.ttk.Treeview(
                master=self.tabel_frame,  # 父容器
                height=15,  # 表格显示的行数,height行
                columns=columns,  # 显示的列
                show='headings',  # 隐藏首列
                xscrollcommand=xscroll.set,  # x轴滚动条
                yscrollcommand=yscroll.set,  # y轴滚动条
            )
            # 定义表头
            self.table.heading(column='ISBN号', text='INBS号',
                               command=lambda _col='ISBN号': treeview_sort_column(self.table, _col,
                                                                                 False))  # 点击表头出发lambda函数
            self.table.heading('书名', text='书名', command=lambda _col='书名': treeview_sort_column(self.table, _col, False))
            self.table.heading('作者名称', text='作者名称',
                               command=lambda _col='作者名称': treeview_sort_column(self.table, _col, False))
            self.table.heading('出版社信息', text='出版社信息',
                               command=lambda _col='出版社信息': treeview_sort_column(self.table, _col, False))
            self.table.heading('出版时间', text='出版时间',
                               command=lambda _col='出版时间': treeview_sort_column(self.table, _col, False))
            self.table.heading('书本价格', text='书本价格',
                               command=lambda _col='书本价格': treeview_sort_column(self.table, _col, False))
            self.table.heading('图书简介', text='图书简介', command=lambda _col='图书简介': treeview_sort_column(self.table, _col,
                                                                                                     False))  # 点击表头出发lambda函数)
            # 定义列
            self.table.column('ISBN号', width=100, minwidth=100, anchor='s', )
            self.table.column('书名', width=100, minwidth=100, anchor='s')
            self.table.column('作者名称', width=100, minwidth=100, anchor='s')
            self.table.column('出版社信息', width=150, minwidth=150, anchor='s')
            self.table.column('出版时间', width=100, minwidth=100, anchor='s')
            self.table.column('书本价格', width=80, minwidth=80, anchor='s')
            self.table.column('图书简介', width=200, minwidth=100, anchor='s')
            # config绑定滚动条为滚动事件 pack放置滚动条再最边边
            xscroll.config(command=self.table.xview)
            xscroll.pack(side=tk.BOTTOM, fill=tk.X)
            yscroll.config(command=self.table.yview)
            yscroll.pack(side=tk.RIGHT, fill=tk.Y)
            self.table.pack(pady=20)
            insert()  # 插入library.txt内的数据

            # 返回主菜单按钮
            self.backbut = tk.Button(self.window, text="返回主菜单", bd=5, font=('黑体', 20, 'bold'), command=self.back)
            self.backbut.place(x=500, y=400, width=200, height=50)

    def back(self):
        self.backbut.destroy()
        self.tabel_frame.destroy()
        MainMenu(root)

# main
root = tk.Tk()  # root加入界面主循环
mainmenu = MainMenu(root)
root.mainloop()