from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter.filedialog import askopenfilename
from  tkinter import messagebox
import datetime
import pyodbc

connection = '15389135543.qicp.vip,13732'
name = 'sa'
pwd = 'admin888'

class SqlServerHelper(object):
    # 需要有mysql的链接
    # 还需要有游标（cursor）
    def __init__(self):
        self.conn = pyodbc.connect(DRIVER='{SQL Server}', SERVER=connection, DATABASE='informations', UID=name, PWD=pwd)
        self.cursor = self.conn.cursor()

    def execute_modify_sql(self, sql, data):
        self.cursor.execute(sql, data)
        self.conn.commit()

    def modify_sql(self, sql):
        self.cursor.execute(sql)
        self.conn.commit()


    def get_info(self, sql):
        self.cursor.execute(sql)
        # self.conn.commit()
        return self.cursor.fetchall()

    def __del__(self):
        self.cursor.close()
        self.conn.close()





type_user = ''

welcome = ''








def show_add():
    # 实例化一个新窗口
    tk = Toplevel()

    # 设置窗口大小
    tk.geometry("1550x800")

    # 设置窗口的标题
    tk.title("人力管理系统\n@zs")

    # 在窗口中添加标签
    label = Label(tk, text=welcome, bg="#0078D7", fg="black", font=("宋体", 18))

    # 标签出现在窗口的位置
    label.pack(side=TOP, fill="x")

    # 实例化底部大容器
    bottomFrame = Frame(tk)

    # 实例化底部大容器中的左右两个容器
    leftFrame = Frame(bottomFrame)
    rightFrame = Frame(bottomFrame)

    department = StringVar()
    name = StringVar()
    idcard = StringVar()
    gender = StringVar()
    age = StringVar()
    phone = StringVar()
    type = StringVar()
    machine_id = StringVar()
    caozuo = StringVar()
    type_do = StringVar()
    type_hang = StringVar()
    do_id = StringVar()
    do_date = StringVar()
    do_last = StringVar()
    check_date = StringVar()
    pay = StringVar()
    room_id = StringVar()
    type_bankcard = StringVar()
    bankcard_id = StringVar()
    in_time = StringVar()
    out_time = StringVar()
    out_reson = StringVar()
    is_on = StringVar()
    address = StringVar()
    emergency_name = StringVar()
    emergency_phone = StringVar()
    relationship = StringVar()
    remark = StringVar()
    training_bef = StringVar()
    training_mid = StringVar()

    global photo
    global id_card_front
    global idcard_back
    global operation_certificate
    photo = '无照片'
    id_card_front = '无照片'
    idcard_back = '无照片'
    operation_certificate = '无照片'

    def get_sql_list(sql):
        helper = SqlServerHelper()
        value = helper.get_info(sql)
        list = []
        for item in value:
            list.append(item[0])
        return list

    departments_list = get_sql_list('select department from departments')
    typedo_list = get_sql_list('select type_do from type_dos')
    typehang_list = get_sql_list('select type_hang from type_hangs')
    type_list = get_sql_list('select type from types')

    def delete():
        pass

    def treeViewSelect(event):
        pass

    # 左边容器
    def shuru(frame, content, v_name, la_row, la_column, en_row, en_column):
        label = Label(frame, text=content)
        entry = Entry(leftFrame, textvariable=v_name)
        label.grid(row=la_row, column=la_column)
        entry.grid(row=en_row, column=en_column)

    def xiala(frame, content, values, v_name, la_row, la_column, xia_row, xia_column):
        label = Label(frame, text=content)
        label.grid(row=la_row, column=la_column)
        gender = ttk.Combobox(leftFrame, textvariable=v_name)  # #创建下拉菜单
        gender["value"] = values  # #给下拉菜单设定值
        if content == '部门':
            if type_user:
                for i in range(len(values)):
                    if type_user == values[i]:
                        break
                gender.current(i)
        else:
            gender.current(0)

        def xFunc(event):
            # print(gender.get())  # #获取选中的值方法1
            # v_name = gender.get()
            pass

        gender.bind("<<ComboboxSelected>>", xFunc)  # #给下拉菜单绑定事件
        gender.grid(row=xia_row, column=xia_column)

    def resize(w_box, h_box, pil_image):  # 参数是：要适应的窗口宽、高、Image.open后的图片
        w, h = pil_image.size  # 获取图像的原始大小
        f1 = 1.0 * w_box / w
        f2 = 1.0 * h_box / h
        factor = min([f1, f2])
        width = int(w * factor)
        height = int(h * factor)
        return pil_image.resize((width, height), Image.ANTIALIAS)

    def choosepic1():
        w_box = 600  # 期望图像显示的大小（窗口大小）
        h_box = 120
        path = StringVar()
        file_entry = Entry(leftFrame, state='readonly', text=path)
        image_label = Label(leftFrame)
        image_label.grid(row=17, column=0)
        path_ = askopenfilename()
        path.set(path_)
        img_open = Image.open(file_entry.get())
        pil_image_resized = resize(w_box, h_box, img_open)
        img = ImageTk.PhotoImage(pil_image_resized)
        image_label.config(image=img)
        image_label.image = img  # keep a reference

        global photo
        photo = file_entry.get()

    def choosepic2():
        w_box = 600  # 期望图像显示的大小（窗口大小）
        h_box = 120
        path = StringVar()
        file_entry = Entry(leftFrame, state='readonly', text=path)
        image_label = Label(leftFrame)
        image_label.grid(row=17, column=1)
        path_ = askopenfilename()
        path.set(path_)
        img_open = Image.open(file_entry.get())
        pil_image_resized = resize(w_box, h_box, img_open)
        img = ImageTk.PhotoImage(pil_image_resized)
        image_label.config(image=img)
        image_label.image = img  # keep a reference

        global id_card_front
        id_card_front = file_entry.get()

    def choosepic3():
        w_box = 600  # 期望图像显示的大小（窗口大小）
        h_box = 120
        path = StringVar()
        file_entry = Entry(leftFrame, state='readonly', text=path)
        image_label = Label(leftFrame)
        image_label.grid(row=17, column=2)
        path_ = askopenfilename()
        path.set(path_)
        img_open = Image.open(file_entry.get())
        pil_image_resized = resize(w_box, h_box, img_open)
        img = ImageTk.PhotoImage(pil_image_resized)
        image_label.config(image=img)
        image_label.image = img  # keep a reference

        global idcard_back
        idcard_back = file_entry.get()

    def choosepic4():
        w_box = 600  # 期望图像显示的大小（窗口大小）
        h_box = 120
        path = StringVar()
        file_entry = Entry(leftFrame, state='readonly', text=path)
        image_label = Label(leftFrame)
        image_label.grid(row=17, column=3)
        path_ = askopenfilename()
        path.set(path_)
        img_open = Image.open(file_entry.get())
        pil_image_resized = resize(w_box, h_box, img_open)
        img = ImageTk.PhotoImage(pil_image_resized)
        image_label.config(image=img)
        image_label.image = img  # keep a reference

        global operation_certificate
        operation_certificate = file_entry.get()

    # shuru(leftFrame, "序号", 0, 0, 0, 1)
    xiala(leftFrame, "部门", departments_list, department, 0, 0, 0, 1)
    shuru(leftFrame, "姓名", name, 0, 2, 0, 3)
    shuru(leftFrame, "身份证号", idcard, 1, 0, 1, 1)
    xiala(leftFrame, "性别", ("男", "女"), gender, 1, 2, 1, 3)
    shuru(leftFrame, "年龄", age, 2, 0, 2, 1)
    shuru(leftFrame, "联系电话", phone, 2, 2, 2, 3)
    xiala(leftFrame, "工种", type_list, type, 3, 0, 3, 1)
    shuru(leftFrame, "操作设备号码", machine_id, 3, 2, 3, 3)
    xiala(leftFrame, "有无操作证", ("无", "有"), caozuo, 4, 0, 4, 1)
    xiala(leftFrame, "执证工种", typedo_list, type_do, 4, 2, 4, 3)
    xiala(leftFrame, "行业类别", typehang_list, type_hang, 5, 0, 5, 1)
    shuru(leftFrame, "操作证号码", do_id, 5, 2, 5, 3)
    shuru(leftFrame, "领证日期", do_date, 6, 0, 6, 1)
    shuru(leftFrame, "复审日期", do_last, 6, 2, 6, 3)
    shuru(leftFrame, "体检日期", check_date, 7, 0, 7, 1)
    shuru(leftFrame, "月工资", pay, 7, 2, 7, 3)
    shuru(leftFrame, "宿舍号", room_id, 8, 0, 8, 1)
    shuru(leftFrame, "开户行", type_bankcard, 8, 2, 8, 3)
    shuru(leftFrame, "开户卡号", bankcard_id, 9, 0, 9, 1)
    shuru(leftFrame, "入职时间", in_time, 9, 2, 9, 3)
    shuru(leftFrame, "离职时间", out_time, 10, 0, 10, 1)
    shuru(leftFrame, "离职原因", out_reson, 10, 2, 10, 3)
    xiala(leftFrame, "是否在岗", ("是", "否"), is_on, 11, 0, 11, 1)
    shuru(leftFrame, "家庭住址", address, 11, 2, 11, 3)
    shuru(leftFrame, "紧急联系人姓名", emergency_name, 12, 0, 12, 1)
    shuru(leftFrame, "紧急联系人号码", emergency_phone, 12, 2, 12, 3)
    shuru(leftFrame, "与本人关系", relationship, 13, 0, 13, 1)
    shuru(leftFrame, "备注", remark, 13, 2, 13, 3)
    shuru(leftFrame, "岗前培训时间", training_bef, 14, 0, 14, 1)
    shuru(leftFrame, "岗中培训时间", training_mid, 14, 2, 14, 3)

    Button(leftFrame, text='选择本人图片', command=choosepic1).grid(row=15, column=0)
    Button(leftFrame, text='选择身份证正面图片', command=choosepic2).grid(row=15, column=1)
    Button(leftFrame, text='选择身份证反面图片', command=choosepic3).grid(row=15, column=2)
    Button(leftFrame, text='选择操作证图片', command=choosepic4).grid(row=15, column=3)

    def calage():
        birth = idcard.get()[6:10]
        now = datetime.datetime.now().year
        age.set(int(now) - int(birth))


    def insert():
        list = []
        list.append(department.get())
        list.append(name.get())
        list.append(idcard.get())
        list.append(gender.get())
        list.append(age.get())
        list.append(phone.get())
        list.append(type.get())
        list.append(machine_id.get())
        list.append(caozuo.get())
        list.append(type_do.get())
        list.append(type_hang.get())
        list.append(do_id.get())
        list.append(do_date.get())
        list.append(do_last.get())
        list.append(check_date.get())
        list.append(pay.get())
        list.append(room_id.get())
        list.append(type_bankcard.get())
        list.append(bankcard_id.get())
        list.append(in_time.get())
        list.append(out_time.get())
        list.append(out_reson.get())
        list.append(is_on.get())
        list.append(address.get())
        list.append(emergency_name.get())
        list.append(emergency_phone.get())
        list.append(relationship.get())
        list.append(remark.get())
        list.append(training_bef.get())
        list.append(training_mid.get())
        list.append(photo)
        list.append(id_card_front)
        list.append(idcard_back)
        list.append(operation_certificate)
        date_of_reg = datetime.datetime.now().strftime('%Y-%m-%d')
        list.append(date_of_reg)
        list.append(usr_name)



        helper = SqlServerHelper()
        insert_sql = 'INSERT INTO info(department, name , idcard, gender, age, phone, type, machine_id, caozuo, type_do, type_hang, do_id, do_date, do_last, check_date, pay, room_id, type_bankcard, bankcard_id, in_time, out_time, out_reson, is_on, address, emergency_name, emergency_phone, relationship, remark, training_bef, training_mid, photo, id_card_front, idcard_back, operation_certificate, date_of_reg, registrant) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
        helper.execute_modify_sql(insert_sql, list)

        messagebox.showinfo('提示', '添加成功')

        tk.destroy()


    # 右边容器
    calage = Button(rightFrame, text="计算", command=calage)
    calage.grid(row = 0, column = 0)


    insertBtn = Button(rightFrame, text="添加", command=insert)
    insertBtn.grid(row = 1, column = 0)

    # 显示左右容器
    leftFrame.pack(side=LEFT)
    rightFrame.pack(side=RIGHT)

    # 显示底部大容器
    bottomFrame.pack()

    # # 获取电脑屏幕的宽度和高度
    winWidth = tk.winfo_screenwidth()
    winHeight = tk.winfo_screenheight()
    #
    # 窗口的宽度
    tkWidth = 1200
    tkHeight = 600
    #
    # # 居中的px
    x = (winWidth - tkWidth) / 2
    y = (winHeight - tkHeight) / 2

    tk.geometry("%dx%d+%d+%d" % (tkWidth, tkHeight, x, y))

    tk.mainloop()


def show(list = []):
    # 实例化一个新窗口
    tk = Toplevel()

    # 设置窗口大小
    tk.geometry("1550x800")

    # 设置窗口的标题
    tk.title("人力管理系统\n@pdp")

    # 在窗口中添加标签
    label = Label(tk, text=welcome, bg="#0078D7", fg="black", font=("宋体", 18))

    # 标签出现在窗口的位置
    label.pack(side=TOP, fill="x")

    # 实例化底部大容器
    bottomFrame = Frame(tk)

    # 实例化底部大容器中的左右两个容器
    leftFrame = Frame(bottomFrame)
    rightFrame = Frame(bottomFrame)


    id = StringVar(value=list[0])
    department = StringVar(value=list[1])
    name = StringVar(value=list[2])
    idcard = StringVar(value=list[3])
    gender = StringVar(value=list[4])
    age = StringVar(value=list[5])
    phone = StringVar(value=list[6])
    type = StringVar(value=list[7])
    machine_id = StringVar(value=list[8])
    caozuo = StringVar(value=list[9])
    type_do = StringVar(value=list[10])
    type_hang = StringVar(value=list[11])
    do_id = StringVar(value=list[12])
    do_date = StringVar(value=list[13])
    do_last = StringVar(value=list[14])
    check_date = StringVar(value=list[15])
    pay = StringVar(value=list[16])
    room_id = StringVar(value=list[17])
    type_bankcard = StringVar(value=list[18])
    bankcard_id = StringVar(value=list[19])
    in_time = StringVar(value=list[20])
    out_time = StringVar(value=list[21])
    out_reson = StringVar(value=list[22])
    is_on = StringVar(value=list[23])
    address = StringVar(value=list[24])
    emergency_name = StringVar(value=list[25])
    emergency_phone = StringVar(value=list[26])
    relationship = StringVar(value=list[27])
    remark = StringVar(value=list[28])
    training_bef = StringVar(value=list[29])
    training_mid = StringVar(value=list[30])





    global photo
    global id_card_front
    global idcard_back
    global operation_certificate
    photo = list[31]
    id_card_front = list[32]
    idcard_back = list[33]
    operation_certificate = list[34]

    def get_sql_list(sql):
        helper = SqlServerHelper()
        value = helper.get_info(sql)
        list = []
        for item in value:
            list.append(item[0])
        return list

    departments_list = get_sql_list('select department from departments')
    typedo_list = get_sql_list('select type_do from type_dos')
    typehang_list = get_sql_list('select type_hang from type_hangs')
    type_list = get_sql_list('select type from types')

    def delete():
        pass

    def treeViewSelect(event):
        pass

    # 左边容器
    def shuru(frame, content, v_name, la_row, la_column, en_row, en_column):
        label = Label(frame, text=content)
        entry = Entry(leftFrame, textvariable=v_name)
        label.grid(row=la_row, column=la_column)
        entry.grid(row=en_row, column=en_column)

    def xiala(frame, content, values, v_name, la_row, la_column, xia_row, xia_column):
        label = Label(frame, text=content)
        label.grid(row=la_row, column=la_column)
        choose = ttk.Combobox(leftFrame, textvariable=v_name)  # #创建下拉菜单
        choose["value"] = values  # #给下拉菜单设定值
        if v_name:
            print(v_name.get())
            for i in range(len(values)):
                print(values[i])
                if v_name.get() == values[i]:
                    break
            choose.current(i)
        else:
            choose.current(0)

        choose.grid(row=xia_row, column=xia_column)

    def resize(w_box, h_box, pil_image):  # 参数是：要适应的窗口宽、高、Image.open后的图片
        w, h = pil_image.size  # 获取图像的原始大小
        f1 = 1.0 * w_box / w
        f2 = 1.0 * h_box / h
        factor = min([f1, f2])
        width = int(w * factor)
        height = int(h * factor)
        return pil_image.resize((width, height), Image.ANTIALIAS)

    def choosepic1():
        w_box = 600  # 期望图像显示的大小（窗口大小）
        h_box = 120
        path = StringVar()
        file_entry = Entry(leftFrame, state='readonly', text=path)
        image_label = Label(leftFrame)
        image_label.grid(row=17, column=0)
        path_ = askopenfilename()
        path.set(path_)
        img_open = Image.open(file_entry.get())
        pil_image_resized = resize(w_box, h_box, img_open)
        img = ImageTk.PhotoImage(pil_image_resized)
        image_label.config(image=img)
        image_label.image = img  # keep a reference

        global photo
        photo = file_entry.get()

    def choosepic2():
        w_box = 600  # 期望图像显示的大小（窗口大小）
        h_box = 120
        path = StringVar()
        file_entry = Entry(leftFrame, state='readonly', text=path)
        image_label = Label(leftFrame)
        image_label.grid(row=17, column=1)
        path_ = askopenfilename()
        path.set(path_)
        img_open = Image.open(file_entry.get())
        pil_image_resized = resize(w_box, h_box, img_open)
        img = ImageTk.PhotoImage(pil_image_resized)
        image_label.config(image=img)
        image_label.image = img  # keep a reference

        global id_card_front
        id_card_front = file_entry.get()

    def choosepic3():
        w_box = 600  # 期望图像显示的大小（窗口大小）
        h_box = 120
        path = StringVar()
        file_entry = Entry(leftFrame, state='readonly', text=path)
        image_label = Label(leftFrame)
        image_label.grid(row=17, column=2)
        path_ = askopenfilename()
        path.set(path_)
        img_open = Image.open(file_entry.get())
        pil_image_resized = resize(w_box, h_box, img_open)
        img = ImageTk.PhotoImage(pil_image_resized)
        image_label.config(image=img)
        image_label.image = img  # keep a reference

        global idcard_back
        idcard_back = file_entry.get()

    def choosepic4():
        w_box = 600  # 期望图像显示的大小（窗口大小）
        h_box = 120
        path = StringVar()
        file_entry = Entry(leftFrame, state='readonly', text=path)
        image_label = Label(leftFrame)
        image_label.grid(row=17, column=3)
        path_ = askopenfilename()
        path.set(path_)
        img_open = Image.open(file_entry.get())
        pil_image_resized = resize(w_box, h_box, img_open)
        img = ImageTk.PhotoImage(pil_image_resized)
        image_label.config(image=img)
        image_label.image = img  # keep a reference

        global operation_certificate
        operation_certificate = file_entry.get()

    # shuru(leftFrame, "序号", 0, 0, 0, 1)
    xiala(leftFrame, "部门", departments_list, department, 0, 0, 0, 1)
    shuru(leftFrame, "姓名", name, 0, 2, 0, 3)
    shuru(leftFrame, "身份证号", idcard, 1, 0, 1, 1)
    xiala(leftFrame, "性别", ("男", "女"), gender, 1, 2, 1, 3)
    shuru(leftFrame, "年龄", age, 2, 0, 2, 1)
    shuru(leftFrame, "联系电话", phone, 2, 2, 2, 3)
    xiala(leftFrame, "工种", type_list, type, 3, 0, 3, 1)
    shuru(leftFrame, "操作设备号码", machine_id, 3, 2, 3, 3)
    xiala(leftFrame, "有无操作证", ("无", "有"), caozuo, 4, 0, 4, 1)
    xiala(leftFrame, "执证工种", typedo_list, type_do, 4, 2, 4, 3)
    xiala(leftFrame, "行业类别", typehang_list, type_hang, 5, 0, 5, 1)
    shuru(leftFrame, "操作证号码", do_id, 5, 2, 5, 3)
    shuru(leftFrame, "领证日期", do_date, 6, 0, 6, 1)
    shuru(leftFrame, "复审日期", do_last, 6, 2, 6, 3)
    shuru(leftFrame, "体检日期", check_date, 7, 0, 7, 1)
    shuru(leftFrame, "月工资", pay, 7, 2, 7, 3)
    shuru(leftFrame, "宿舍号", room_id, 8, 0, 8, 1)
    shuru(leftFrame, "开户行", type_bankcard, 8, 2, 8, 3)
    shuru(leftFrame, "开户卡号", bankcard_id, 9, 0, 9, 1)
    shuru(leftFrame, "入职时间", in_time, 9, 2, 9, 3)
    shuru(leftFrame, "离职时间", out_time, 10, 0, 10, 1)
    shuru(leftFrame, "离职原因", out_reson, 10, 2, 10, 3)
    xiala(leftFrame, "是否在岗", ("是", "否"), is_on, 11, 0, 11, 1)
    shuru(leftFrame, "家庭住址", address, 11, 2, 11, 3)
    shuru(leftFrame, "紧急联系人姓名", emergency_name, 12, 0, 12, 1)
    shuru(leftFrame, "紧急联系人号码", emergency_phone, 12, 2, 12, 3)
    shuru(leftFrame, "与本人关系", relationship, 13, 0, 13, 1)
    shuru(leftFrame, "备注", remark, 13, 2, 13, 3)
    shuru(leftFrame, "岗前培训时间", training_bef, 14, 0, 14, 1)
    shuru(leftFrame, "岗中培训时间", training_mid, 14, 2, 14, 3)



    Button(leftFrame, text='选择本人图片', command=choosepic1).grid(row=15, column=0)
    if photo and photo != '无照片':
        w_box = 600  # 期望图像显示的大小（窗口大小）
        h_box = 120
        image_label = Label(leftFrame)
        image_label.grid(row=17, column=0)
        img_open = Image.open(photo)
        pil_image_resized = resize(w_box, h_box, img_open)
        img = ImageTk.PhotoImage(pil_image_resized)
        image_label.config(image=img)
        image_label.image = img  # keep a reference
    if id_card_front and id_card_front != '无照片':
        w_box = 600  # 期望图像显示的大小（窗口大小）
        h_box = 120
        image_label = Label(leftFrame)
        image_label.grid(row=17, column=1)
        img_open = Image.open(id_card_front)
        pil_image_resized = resize(w_box, h_box, img_open)
        img = ImageTk.PhotoImage(pil_image_resized)
        image_label.config(image=img)
        image_label.image = img  # keep a referenc

    if idcard_back and idcard_back != '无照片':
        w_box = 600  # 期望图像显示的大小（窗口大小）
        h_box = 120
        image_label = Label(leftFrame)
        image_label.grid(row=17, column=2)
        img_open = Image.open(idcard_back)
        pil_image_resized = resize(w_box, h_box, img_open)
        img = ImageTk.PhotoImage(pil_image_resized)
        image_label.config(image=img)
        image_label.image = img  # keep a referenc
    if operation_certificate and operation_certificate != '无照片':
        w_box = 600  # 期望图像显示的大小（窗口大小）
        h_box = 120
        image_label = Label(leftFrame)
        image_label.grid(row=17, column=3)
        img_open = Image.open(operation_certificate)
        pil_image_resized = resize(w_box, h_box, img_open)
        img = ImageTk.PhotoImage(pil_image_resized)
        image_label.config(image=img)
        image_label.image = img  # keep a referenc









    Button(leftFrame, text='选择身份证正面图片', command=choosepic2).grid(row=15, column=1)
    Button(leftFrame, text='选择身份证反面图片', command=choosepic3).grid(row=15, column=2)
    Button(leftFrame, text='选择操作证图片', command=choosepic4).grid(row=15, column=3)

    def calage():
        birth = idcard.get()[6:10]
        now = datetime.datetime.now().year
        age.set(int(now) - int(birth))


    def update():
        list = []
        list.append(department.get())
        list.append(name.get())
        list.append(idcard.get())
        list.append(gender.get())
        list.append(age.get())
        list.append(phone.get())
        list.append(type.get())
        list.append(machine_id.get())
        list.append(caozuo.get())
        list.append(type_do.get())
        list.append(type_hang.get())
        list.append(do_id.get())
        list.append(do_date.get())
        list.append(do_last.get())
        list.append(check_date.get())
        list.append(pay.get())
        list.append(room_id.get())
        list.append(type_bankcard.get())
        list.append(bankcard_id.get())
        list.append(in_time.get())
        list.append(out_time.get())
        list.append(out_reson.get())
        list.append(is_on.get())
        list.append(address.get())
        list.append(emergency_name.get())
        list.append(emergency_phone.get())
        list.append(relationship.get())
        list.append(remark.get())
        list.append(training_bef.get())
        list.append(training_mid.get())
        list.append(photo)
        list.append(id_card_front)
        list.append(idcard_back)
        list.append(operation_certificate)

        date_of_reg = datetime.datetime.now().strftime('%Y-%m-%d')



        helper = SqlServerHelper()
        insert_sql = "update info set department = '{}', name = '{}' , idcard = '{}', gender = '{}', age = '{}', phone = '{}', type = '{}', machine_id = '{}', caozuo = '{}', type_do = '{}', type_hang = '{}', do_id = '{}', do_date = '{}', do_last = '{}', check_date = '{}', pay = '{}', room_id = '{}', type_bankcard = '{}', bankcard_id = '{}', in_time = '{}', out_time ='{}', out_reson ='{}', is_on ='{}', address ='{}', emergency_name ='{}', emergency_phone = '{}', relationship = '{}', remark ='{}',  training_bef ='{}', training_mid ='{}', photo ='{}', id_card_front ='{}', idcard_back ='{}', operation_certificate ='{}',date_of_reg = '{}', registrant = '{}'  where id = {}".format(department.get(), name.get() , idcard.get(), gender.get(), age.get(), phone.get(), type.get(), machine_id.get(), caozuo.get(), type_do.get(), type_hang.get(), do_id.get(), do_date.get(), do_last.get(), check_date.get(), pay.get(), room_id.get(), type_bankcard.get(), bankcard_id.get(), in_time.get(), out_time.get(), out_reson.get(), is_on.get(), address.get(), emergency_name.get(), emergency_phone.get(), relationship.get(), remark.get(), training_bef.get(), training_mid.get(), photo, id_card_front, idcard_back, operation_certificate, date_of_reg, usr_name,  id.get())
        helper.modify_sql(insert_sql)

        messagebox.showinfo('提示', '更新成功')

        tk.destroy()
    def delete():
        helper = SqlServerHelper()
        delete_sql = "DELETE FROM info WHERE id = '{}'".format(id.get())
        helper.modify_sql(delete_sql)
        tk.destroy()


    # 右边容器
    calage = Button(rightFrame, text="计算", command=calage)
    calage.grid(row = 0, column = 0)


    insertBtn = Button(rightFrame, text="更新", command=update)
    insertBtn.grid(row=2, column=0)

    insertBtn = Button(rightFrame, text="删除", command=delete)
    insertBtn.grid(row=4, column=0)

    # 显示左右容器
    leftFrame.pack(side=LEFT)
    rightFrame.pack(side=RIGHT)

    # 显示底部大容器
    bottomFrame.pack()

    # # 获取电脑屏幕的宽度和高度
    winWidth = tk.winfo_screenwidth()
    winHeight = tk.winfo_screenheight()
    #
    # 窗口的宽度
    tkWidth = 1200
    tkHeight = 600
    #
    # # 居中的px
    x = (winWidth - tkWidth) / 2
    y = (winHeight - tkHeight) / 2

    tk.geometry("%dx%d+%d+%d" % (tkWidth, tkHeight, x, y))

    tk.mainloop()





def output():
    result = open('data.xls', 'w', encoding='gbk')
    result.write('序号\t部门\t姓名\t身份证号\t性别\t年龄\t联系电话\t工种\t操作设备号码\t有无操作证\t执业工种\t行业类别\t操作证号码\t领证日期\t有效期\t体检日期\t月工资\t宿舍号\t开户行\t银行卡号\t入职时间\t离职时间\t离职原因\t是否在岗\t家庭住址\t紧急联系人姓名\t紧急联系人电话\t与本人关系\t备注\t岗前培训时间\t岗中培训时间\t本人照片\t身份证正面\t身份证反面\t操作证照片\t登记日期\t登记人\n')
    for m in range(len(value)):
        for n in range(len(value[m])):
            result.write(str(value[m][n]))
            result.write('\t')
        result.write('\n')
    result.close()
    messagebox.showinfo('提示', '导出成功')




def info():
    win = Tk()
    win.title('人员信息')
    win.geometry('800x500')

    helper = SqlServerHelper()

    if "施工" in type_user:
        sql_all = "select count(*) from info where department='{}'".format(type_user)
        all_num = helper.get_info(sql_all)
        sql_on = "select count(*) from info where is_on = '是' and department='{}'".format(type_user)
        all_on = helper.get_info(sql_on)
        all_off = int(all_num[0][0]) - int(all_on[0][0])
    else:
        sql_all = 'select count(*) from info'
        all_num = helper.get_info(sql_all)
        sql_on = "select count(*) from info where is_on = '是'"
        all_on = helper.get_info(sql_on)
        all_off = int(all_num[0][0]) - int(all_on[0][0])

    Label(win, text='总人数：').place(x=100, y=100)
    Label(win, text='在职人数：').place(x=100, y=140)
    Label(win, text='离职人数：').place(x=100, y=180)
    Label(win, text=all_num[0][0]).place(x=150, y=100)
    Label(win, text=all_on[0][0]).place(x=150, y=140)
    Label(win, text=all_off).place(x=150, y=180)


def mainface(type_user):





    root = Tk()
    root.geometry("800x600")

    root.title("人力管理系统\n")

    # 在窗口中添加标签
    label=Label(root,text=welcome, bg="#0078D7",fg="black",font=("宋体",18))

    # 标签出现在窗口的位置
    label.pack(side=TOP,fill="x")

    def refresh():
        root.destroy()
        mainface(type_user)








    treeView = ttk.Treeview(root, show="headings",height=20, columns=("id","department","name","idcard", "gender",
            "age", "phone", "type", "machine_id", "caozuo", "type_do", "type_hang", "do_id",
           "do_date", "do_last", "check_date", "pay", "room_id", "type_bankcard", "bankcard_id",
            "in_time", "out_time", "out_reson", "is_on", "address", "emergency_name",
            "emergency_phone", "relationship", "remark", "training_bef", "training_mid","photo", "id_card_front",
            "idcard_back", "operation_certificate", "date_of_reg","registrant"))

    treeView.column("id",width=50,anchor="center")
    treeView.column("department",width=100,anchor="center")
    treeView.column("name",width=50,anchor="center")
    treeView.column("idcard",width=200,anchor="center")
    treeView.column("gender",width=50,anchor="center")
    treeView.column("age",width=50,anchor="center")
    treeView.column("phone",width=120,anchor="center")
    treeView.column("type",width=80,anchor="center")

    treeView.column("machine_id",width=90,anchor="center")
    treeView.column("caozuo",width=100,anchor="center")
    treeView.column("type_do",width=100,anchor="center")
    treeView.column("type_hang",width=100,anchor="center")
    treeView.column("do_id",width=150,anchor="center")
    treeView.column("do_date",width=80,anchor="center")
    treeView.column("do_last",width=60,anchor="center")
    treeView.column("check_date",width=80,anchor="center")

    treeView.column("pay",width=60,anchor="center")
    treeView.column("room_id",width=60,anchor="center")
    treeView.column("type_bankcard",width=60,anchor="center")
    treeView.column("bankcard_id",width=200,anchor="center")
    treeView.column("in_time",width=80,anchor="center")
    treeView.column("out_time",width=80,anchor="center")
    treeView.column("out_reson",width=100,anchor="center")
    treeView.column("is_on",width=80,anchor="center")

    treeView.column("address",width=200,anchor="center")
    treeView.column("emergency_name",width=120,anchor="center")
    treeView.column("emergency_phone",width=120,anchor="center")
    treeView.column("relationship",width=100,anchor="center")
    treeView.column("remark",width=100,anchor="center")
    treeView.column("training_bef", width=100, anchor="center")
    treeView.column("training_mid", width=100, anchor="center")
    treeView.column("photo",width=60,anchor="center")
    treeView.column("id_card_front",width=100,anchor="center")
    treeView.column("idcard_back",width=100,anchor="center")

    treeView.column("operation_certificate",width=100,anchor="center")

    treeView.heading("id",text="序号")
    treeView.heading("department",text="部门")
    treeView.heading("name",text="姓名")
    treeView.heading("idcard",text="身份证号")
    treeView.heading("gender",text="姓别")
    treeView.heading("age",text="年龄")
    treeView.heading("phone",text="联系电话")
    treeView.heading("type",text="工种")


    treeView.heading("machine_id",text="操作设备号码")
    treeView.heading("caozuo",text="有无操作证")
    treeView.heading("type_do",text="执业工种")
    treeView.heading("type_hang",text="行业类别")
    treeView.heading("do_id",text="操作证号码")
    treeView.heading("do_date",text="领证日期")
    treeView.heading("do_last",text="有效期")
    treeView.heading("check_date",text="体检日期")


    treeView.heading("pay",text="月工资")
    treeView.heading("room_id",text="宿舍号")
    treeView.heading("type_bankcard",text="开户行")
    treeView.heading("bankcard_id",text="银行卡号")
    treeView.heading("in_time",text="入职时间")
    treeView.heading("out_time",text="离职时间")
    treeView.heading("out_reson",text="离职原因")
    treeView.heading("is_on",text="是否在岗")

    treeView.heading("address",text="家庭住址")
    treeView.heading("emergency_name",text="紧急联系人姓名")
    treeView.heading("emergency_phone",text="紧急联系人电话")
    treeView.heading("relationship",text="与本人关系")
    treeView.heading("remark",text="备注")
    treeView.heading("training_bef", text="岗前培训时间")
    treeView.heading("training_mid", text="岗中培训时间")
    treeView.heading("photo",text="本人照片")
    treeView.heading("id_card_front",text="身份证正面")
    treeView.heading("idcard_back",text="身份证反面")

    treeView.heading("operation_certificate",text="操作证照片")
    treeView.heading("date_of_reg", text="登记日期")
    treeView.heading("registrant", text="登记人")






    if "施工" in type_user:
        helper = SqlServerHelper()
        sql = "select * from info where department = '{}'".format(type_user)
        global value
        value = helper.get_info(sql)
        for i in range(len(value)):
            value[i] = tuple(value[i])
            treeView.insert('', i, values = value[i])

        def showTree(event):
            for item in treeView.selection():
                item_text = treeView.item(item)
                show(item_text['values'])


        treeView.bind('<<TreeviewSelect>>', showTree)
        treeView.pack()




    else:
        helper = SqlServerHelper()
        tree = ttk.Treeview(root, show="tree")
        sql_tree = 'select department from departments'
        value_tree = helper.get_info(sql_tree)
        tree.insert("", 1, "甲方", text="甲方", values="1")  # ""表示父节点是根
        myidy = tree.insert("", 0, "施工队", text="施工队", values="2")
        for i in range(1, len(value_tree)):
            tree.insert(myidy, 0, value_tree[i][0], text=value_tree[i][0], values="{}".format(i + 3))

        def selectTree(event):

            helper = SqlServerHelper()
            #清空原表
            items = treeView.get_children()
            [treeView.delete(item) for item in items]
            for item in tree.selection():
                item_text = tree.item(item, "text")
                if item_text != "施工队":
                    sql = "select * from info where department = '{}'".format(item_text)
                    # global value
                    # value = helper.get_info(sql)
                    for i in range(len(value)):
                        value[i] = tuple(value[i])
                        treeView.insert('', i, values=value[i])

                    def showTree(event):
                        for item in treeView.selection():
                            item_text = treeView.item(item)
                            show(item_text['values'])


                    treeView.bind('<<TreeviewSelect>>', showTree)
                    treeView.pack()



        # 选中行
        tree.bind('<<TreeviewSelect>>', selectTree)

        tree.pack(expand=True, fill=BOTH)


        sql = 'select * from info '
        value = helper.get_info(sql)

        for i in range(len(value)):
            value[i] = tuple(value[i])
            treeView.insert('', i, values=value[i])
        # treeView.place(x = 200, y = 20)

        def showTree(event):
            for item in treeView.selection():
                item_text = treeView.item(item)
                show(item_text['values'])

        treeView.bind('<<TreeviewSelect>>', showTree)
        treeView.pack()




    # 创建一个顶级菜单
    menubar = Menu(root)
    menubar.add_command(label="新建", command=show_add)
    menubar.add_command(label="导出", command=output)
    menubar.add_command(label="刷新", command=refresh)
    menubar.add_command(label="人员信息", command=info)
    menubar.add_command(label="退出", command=root.quit)

    # 显示菜单
    root.config(menu=menubar)



    # ----horizontal scrollbar----------
    hbar = ttk.Scrollbar(root, orient=HORIZONTAL, command=treeView.xview)
    treeView.configure(xscrollcommand=hbar.set)
    # hbar.grid(row=1, column=0, sticky=EW)
    hbar.pack(side = BOTTOM, fill = X)

    winWidth=treeView.winfo_screenwidth()
    winHeight=treeView.winfo_screenheight()
    #
    # 窗口的宽度
    tkWidth = 1550
    tkHeight = 700
    #
    # # 居中的px
    x = (winWidth-tkWidth) / 2
    y = (winHeight-tkHeight) / 2

    root.geometry("%dx%d+%d+%d" %(tkWidth,tkHeight,x,y))

    root.mainloop()

def main():
    window = Tk()
    window.title('用户登录')
    window.geometry('800x500')






    # 登陆界面
    Label(window, text='账户：').place(x=100, y=100)
    Label(window, text='密码：').place(x=100, y=140)

    Label(window, text='连接名：').place(x=400, y=100)
    Label(window, text='用户名：').place(x=400, y=140)
    Label(window, text='密码：').place(x=400, y=180)

    Label(window, text='本软件为内部信息管理系统，账号密码请到管理员处登记获取，登录异常请联系 杨卫 联系电话：15561125543').place(x=100, y=400)


    var_usr_name = StringVar()
    enter_usr_name = Entry(window, textvariable=var_usr_name)
    enter_usr_name.place(x=160, y=100)

    var_usr_pwd = StringVar()
    enter_usr_pwd = Entry(window, textvariable=var_usr_pwd, show='*')
    enter_usr_pwd.place(x=160, y=140)

    var_Connection = StringVar(value=connection)
    enter_Connection = Entry(window, textvariable=var_Connection)
    enter_Connection.place(width = 180, x=460, y=100)

    var_con_name = StringVar(value=name)
    enter_con_name = Entry(window, textvariable=var_con_name, show='*')
    enter_con_name.place(width = 180, x=460, y=140)

    var_con_pwd = StringVar(value=pwd)
    enter_con_pwd = Entry(window, textvariable=var_con_pwd, show='*')
    enter_con_pwd.place(width = 180, x=460, y=180)

    def search(sql, usr_name, usr_pwd):
        helper = SqlServerHelper()
        value = helper.get_info(sql)
        for item in value:
            if usr_name in item and usr_pwd in item:
                return item[2]
        return False

    # 登陆
    def usr_log_in():
        # 输入框内容
        global usr_name
        global connection
        global name
        global pwd
        usr_name = var_usr_name.get()
        usr_pwd = var_usr_pwd.get()
        connection = var_Connection.get()
        name = var_con_name.get()
        pwd = var_con_pwd.get()


        # 判断
        if search('select * from users', usr_name, usr_pwd):
            global welcome
            global type_user
            type_user = search('select * from users', usr_name, usr_pwd)
            helper = SqlServerHelper()
            welcome = helper.get_info('select * from welcome')[0][0]

            window.destroy()
            mainface(type_user)


        # 用户名密码不能为空
        elif usr_name == '' or usr_pwd == '':
            messagebox.showerror(message='用户名不能为空！')

        else:
            messagebox.showerror(message='ERROR!')

    def usr_sign_quit():
        window.destroy()

    # 登录 注册按钮
    bt_login = Button(window, text='登录', command=usr_log_in)
    bt_login.place(x=150, y=230)

    bt_logquit = Button(window, text='退出', command=usr_sign_quit)
    bt_logquit.place(x=240, y=230)

    window.mainloop()

main()