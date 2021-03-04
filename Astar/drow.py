# -*- coding:utf-8 -*-


from Tkinter import *

def draw_chess(pointlist, title):  # 根据传进来的地图绘制图片，参数为：1.地图（含各方格的涂色）2.窗口名
    print "开始画图"
    row_num = len(pointlist)
    col_num = len(pointlist[0])
    tk = Tk()
    tk.title(title)
    canvas = Canvas(tk, width=col_num * 40, height=row_num * 40)
    canvas.pack()
    for i in range(row_num):  # 按照行列画出方格
        for j in range(col_num):
            canvas.create_rectangle(j * 30, i * 30, (j + 1) * 30, (i + 1) * 30, fill=pointlist[i][j].color)
    tk.mainloop()


def for_a_star():
    # Make a 9x9 grid...
    nrows, ncols = 9, 9
    image = np.zeros(nrows * ncols)

    # Set every other cell to a random number (this would be your data)
    image[::2] = np.random.random(nrows * ncols // 2 + 1)

    # Reshape things into a 9x9 grid.
    image = image.reshape((nrows, ncols))

    row_labels = range(nrows)
    col_labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    plt.matshow(image)
    plt.xticks(range(ncols), col_labels)
    plt.yticks(range(nrows), row_labels)
    plt.show()

if __name__ == "__main__":
    for_a_star()





