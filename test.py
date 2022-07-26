"""
=======================================================
@Project --- File : PythonProjects --- test
@Author : 黄强
@Date   : 2022/7/21 9:15
1-功能描述:

2-实现步骤:

https://zhuanlan.zhihu.com/p/394061914
https://www.byhy.net/tut/py/gui/qt_03/
https://zhuanlan.zhihu.com/p/269273821
https://blog.csdn.net/qq_38463737/article/details/106574408

=======================================================
"""
import os
import os.path
import shutil


# 将目录的文件复制到指定目录
def copy_demo(src_dir, dst_dir):
    """
    复制src_dir目录下的所有内容到dst_dir目录  递归调用，实现递归复制文件
    :param src_dir: 源文件目录
    :param dst_dir: 目标目录
    :return:
    """
    try:
        if not os.path.exists(dst_dir):
            print("创建目标文件夹")
            os.makedirs(dst_dir)
        if os.path.exists(src_dir):
            print("拷贝主图文件夹")
            for file in os.listdir(src_dir):  # [目录1, 目录2, ...]
                file_path = os.path.join(src_dir, file)  # 每个源文件路径
                dst_path = os.path.join(dst_dir, file)
                if os.path.isfile(os.path.join(src_dir, file)):
                    shutil.copyfile(file_path, dst_path)
                else:
                    copy_demo(src_dir, dst_dir)
        else:
            print("复制的文件不存在!")
    except Exception as error_msg:
        print("出现异常:", error_msg)


def dir_list_data(inPath):
    dirList = os.listdir(inPath)  # 该路径下的文件和文件夹（不递进遍历），列表
    print(dirList)
    return dirList


def copy_file_fileTree(inPath_src, inPath_dst):  # 递归复制文件夹（把一个文件夹下所有文件目录递归原样复制到另一个文件夹下）
    try:
        shutil.copytree(inPath_src, inPath_dst)
        print("新品文件拷贝成功")
        return True
    except Exception as e:
        print("新品文件拷贝失败，目标文件已存在。出现异常:", e)
        # 调用删除文件目录的方法，做成弹框是否确认删除，事件控制
        return False


def copy_dirs(source, destination):
    # 不存在文件夹时创建
    if not os.path.exists(destination):
        os.mkdir(destination)
    for f in os.listdir(source):
        if os.path.isfile(os.path.join(source, f)):
            shutil.copy(os.path.join(source, f), os.path.join(destination, f))
        else:
            copy_dirs(os.path.join(source, f), os.path.join(destination, f))


if __name__ == '__main__':  # 执行的方法     每一个执行失败出现异常的方法（封装，报错变量），并提示
    # input_PFiles = input("要备份的文件路径:").replace('\\', '/')  # E:\P盘产品中心\产品资料库
    # input_QFiles = input("备份到的文件路径:").replace('\\', '/')  # E:\testFiles\test1
    # # dir_list_data(input_PFiles)
    # # ret = copy_file_fileTree(input_PFiles, input_QFiles)
    # # print(ret)
    # copy_demo(input_PFiles, input_QFiles)
    # # copy_dirs(input_PFiles, input_QFiles)

    var_y_or_n = ""
    while True:
        in_y_or_n = input("是否删除文件(y/n):")
        if in_y_or_n == 'y':
            # os.rmdir(inPath_dst)
            print("删除文件夹成功!")
            var_y_or_n = "y"
            break
        elif in_y_or_n == 'n':
            print("推出不删除!")
            var_y_or_n = "n"
            break
        else:
            print("输入不正确，请重新输入(y/n):")
            continue
    print(var_y_or_n)
    if var_y_or_n == "y":
        print("存在的文件夹已删除，重新拷贝成功!")