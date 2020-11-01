from tkinter import *


def buttonTiep():
    stringHSA.set("")
    stringHSB.set("")
    stringKQ.set("")


def buttonGiai():
    a = float(stringHSA.get())
    b = float(stringHSB.get())
    kq = ""
    if a == 0 and b == 0:
        kq = "Vô số nghiệm"
    elif a == 0 and b != 0:
        kq = "Vô nghiệm"
    else:
        kq = "x={0}".format(-b/a)
    stringKQ.set(kq)


window = Tk()
window.title("Giải phương trình")


lblTitle = Label(window, text="Phương Trình Bậc 1", fg="red", font=(
                "tahoma", 16), justify=CENTER).grid(row=0, columnspan=2)

stringHSA = StringVar()
stringHSB = StringVar()
stringKQ = StringVar()

# label cho người dùng biết cách sử dụng và và entry cho người dùng nhập giá trị vào
lblA = Label(window, text="Hệ số a:").grid(row=1)
entryA = Entry(window, width=30, textvariable=stringHSA).grid(row=1, column=1)
lblB = Label(window, text="Hệ số b:").grid(row=2)
entryB = Entry(window, width=30, textvariable=stringHSB).grid(row=2, column=1)
lblKQ = Label(window, text="Kết quả:").grid(row=4)
entryKQ = Entry(window, width=30, textvariable=stringKQ).grid(row=4, column=1)

# button điều khiển: Giải, tiếp, thoát
frmButton = Frame(window, borderwidth=2)
btnGiai = Button(frmButton, text="Giải", command=buttonGiai).pack(side=LEFT)
btnTiep = Button(frmButton, text="Tiếp", command=buttonTiep).pack(side=LEFT)
btnThoat = Button(frmButton, text="Thoát", command=window.quit).pack(side=LEFT)
frmButton.grid(row=3, columnspan=2)


window.mainloop()
