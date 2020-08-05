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


class Car:
    __vehicle = 'VX650'
    brand = 'Toyota'
    def __init__(self, brand='Toyota', model="Hilux", year=2016):
        print(f'Car object is created! {brand} {model} of {year}')

    def __place(self):
        return('Place method!')


hilux = Car()
print(hilux.brand)
print(hilux.__place())
