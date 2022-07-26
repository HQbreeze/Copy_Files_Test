"""
=======================================================
@Project --- File : PythonProjects --- copy_files
@Author : 黄强
@Date   : 2022/7/21 9:15
1-功能描述:

2-实现步骤:
=======================================================
"""
import os
import os.path
import shutil


def get_files_path(input_path):  # 拼接路径，拷贝的目标文件夹
    pass

def copy_files_coverFile():
    pass


""" ========================= 复制文件及文件夹，不该表文件夹结构层层递进复制 ========================= """
def copy_dirs_copytree(inPath_src, inPath_dst):  # 拷贝文件，若目标文件已有存在（或同名文件），先删除，再拷贝
    """
    :param inPath_src: 要拷贝文件的路径（源文件路径）
    :param inPath_dst: 拷贝文件存放的路径（目标文件路径）
    :return: True/False
    """
    var_del_or_break = ""
    try:
        if os.path.exists(inPath_dst):
            print("已存在这个文件夹，确定删除？(输入y/n):")
            while True:
                in_y_or_n = input("确定删除？(输入y/n):")
                if in_y_or_n == 'y':
                    os.rmdir(inPath_dst)
                    var_del_or_break = "y"
                    print("删除文件夹成功!")
                    break
                elif in_y_or_n == 'n':
                    print("退出不删除!")
                    break
                else:
                    print("输入不正确，请重新输入(y/n):")
                    continue

        else:
            if var_del_or_break == "y":
                shutil.copytree(inPath_src, inPath_dst)  # 其中inPath_dst的路径已经创建，则会报错(所以先要删除)
                print("新品文件拷贝成功")
                return True
            else:
                print("没有做任何处理")

    except OSError as err:
        print("Error message: %s", err)
        return False

    except Exception as e:
        print("新品文件拷贝失败，目标文件已存在。出现异常:", e)
        # 调用删除文件目录的方法，做成弹框是否确认删除，事件控制
        return False


def copy_dirs(path_source, path_destination):
    """
    :param path_source: 要拷贝文件的路径（源文件路径）
    :param path_destination: 拷贝文件存放的路径（目标文件路径）
    :return:
    """
    # 不存在文件夹时创建
    if not os.path.exists(path_destination):  # 目标文件夹不存在就新建
        os.mkdir(path_destination)

    for f in os.listdir(path_source):  # 遍历文件夹下的文件及文件名（仅当前文件夹下，不是层层递进遍历）
        if os.path.isfile(os.path.join(path_source, f)):  # 复制文件
            shutil.copy(os.path.join(path_source, f), os.path.join(path_destination, f))
            print("return '文件复制成功'")
        else:
            copy_dirs(os.path.join(path_source, f), os.path.join(path_destination, f))  # 复制文件夹，递归实现
            print("return '文件夹复制成功'")


""" ========================================================================================== """


""" ===================================== 删除文件及文件夹 ====================================== """
def delete_dirs_rmtree(path_dirs):
    try:
        shutil.rmtree(path_dirs)
    except [OSError, Exception] as e:
        print("Error message: %s; %s", e.filename, e.strerror)
    pass


def delete_dirs(path_rootDir):
    """
    :param path_rootDir: 传入要删除的文件/文件夹路径
    :return:
    """

    with open('deleteFile') as f:
        for line in f.readlines():
            path = path_rootDir + line.strip()
            if os.path.exists(path) and os.path.isfile(path):
                os.remove(path)
                print("deleteFile:" + path)
                # return "deleteFile"
            elif os.path.exists(path) and os.path.isdir(path):
                os.rmdir(path)
                print('deleteDir:' + path)
                # return 'deleteDir'
            else:
                print('Path not Exists!')
                return False


if __name__ == '__main__':
    input_PFiles = input("P盘要备份的文件路径:").replace('\\', '/')
    input_QFiles = input("备份到Q盘的文件路径:").replace('\\', '/')









