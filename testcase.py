# from tkinter import *
# from tkinter import filedialog
#
#
# def Quit(ev):
#     global root
#     root.destroy()
#
#
# def LoadFile(ev):
#     fn = filedialog.Open(root, filetypes=[('*.txt files', '.txt')]).show()
#     if fn == '':
#         return
#     textbox.delete('1.0', 'end')
#     textbox.insert('1.0', open(fn, 'rt').read())
#
#
# def SaveFile(ev):
#     fn = filedialog.SaveAs(root, filetypes=[('*.txt files', '.txt')]).show()
#     if fn == '':
#         return
#     if not fn.endswith(".txt"):
#         fn += ".txt"
#     open(fn, 'wt').write(textbox.get('1.0', 'end'))
#
#
# root = Tk()
#
# panelFrame = Frame(root, height=60, bg='gray')
# textFrame = Frame(root, height=340, width=600)
#
# panelFrame.pack(side='top', fill='x')
# textFrame.pack(side='bottom', fill='both', expand=1)
#
# textbox = Text(textFrame, font='Arial 14', wrap='word')
# scrollbar = Scrollbar(textFrame)
#
# scrollbar['command'] = textbox.yview
# textbox['yscrollcommand'] = scrollbar.set
#
# textbox.pack(side='left', fill='both', expand=1)
# scrollbar.pack(side='right', fill='y')
#
# loadBtn = Button(panelFrame, text='Load')
# saveBtn = Button(panelFrame, text='Save')
# quitBtn = Button(panelFrame, text='Quit')
#
# loadBtn.bind("<Button-1>", LoadFile)
# saveBtn.bind("<Button-1>", SaveFile)
# quitBtn.bind("<Button-1>", Quit)
#
# loadBtn.place(x=10, y=10, width=40, height=40)
# saveBtn.place(x=60, y=10, width=40, height=40)
# quitBtn.place(x=110, y=10, width=40, height=40)
#
# root.mainloop()
#
# import asyncio
# import time
#
# async def spider(site_name):
#     for page in range(1, 4):
#         await asyncio.sleep(1)
#         print(site_name, page)
#
#
# spiders = [
#     asyncio.ensure_future(spider('Blog')),
#     asyncio.ensure_future(spider('News')),
#     asyncio.ensure_future(spider('Forum')),
# ]
#
# start = time.time()
#
# event_loop = asyncio.get_event_loop()
# event_loop.run_until_complete(asyncio.gather(*spiders))
# event_loop.close()
#
# print('{:.2F}'.format(time.time()-start))


# print(type(1151))
# print(type('^&*^#(*lfvjnfk'))
# print(type(1.02))
# print(type(True))
# print(type(False))

# choose = input('Выбери своего чемпиона: '
#                '\n1. Рыцарь '
#                '\n2. Маг '
#                '\n3. Целитель '
#                '\n4. Стрелок\n')
#
# if choose == '1':
#     print('Ты выбрал Рыцаря!')
# elif choose == '2':
#     print('Ты выбрал Мага!')
# elif choose == '3':
#     print('Ты выбрал Целителя!')
# elif choose == '4':
#     print('Ты выбрал Стрелка!')
#     print('testcase code')
#     print('hello world')
#     a = int(input())
#     b = int(input())
#     print(a+b)
# else:
#     print('Неправильный выбор!')

# statement = input('Do you have a baton? ')
#
# if statement == 'yes':
#     print('Baton kuplen!')
#
# elif statement == 'no':
#
#     statement = input('Do you have a bread? ')
#
#     if statement == 'yes':
#         print('Hleb kuplen!')
#
#     else:
#         print('Nichego ne kupleno')


''' >, <, >= ,<= , == '''

# print(5 <= 5)


''' тип данных bool - True, False
    операторы - >, <, >=, <=, ==
    if *statement1* - elif *statement2* - else
'''

