'''
读取txt文件readlines
去除字符串前后空格（字符串操作strf()），并且以 ','分割（split(',')),转换成元组添加到列表
用切片返回列表中除了标题之外的内容

'''
from config import BASE_DIR
def read_login_txt(filename):

    with open('{}/data/'.format(BASE_DIR)+filename,'r',encoding='utf-8')as f:
        arr = []

        for data in f.readlines():
            arr.append(tuple(data.strip().split(",")))
        return arr[1::]

if __name__ == '__main__':
    print(read_login_txt('login.txt'))