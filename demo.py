"""
=======================================================
@Project --- File : PythonProjects --- demo
@Author : 黄强
@Date   : 2022/7/26 18:27
1-功能描述:

2-实现步骤:
=======================================================
"""
import os
import shutil


def copy_dirs_copytree():  # 拷贝文件，若目标文件已有存在（或同名文件），先删除，再拷贝
    """
    :param inPath_src: 要拷贝文件的路径（源文件路径）
    :param inPath_dst: 拷贝文件存放的路径（目标文件路径）
    :return: True/False
    """
    global var_del_or_break
    input_str = input("输入一个字符串:")
    try:
        if input_str == "dirs":  # os.path.exists(inPath_dst)
            print("已存在这个文件夹，确定删除？(输入y/n):")
            while True:
                in_y_or_n = input("确定删除？(输入y/n):")
                if in_y_or_n == 'y':
                    # os.rmdir(inPath_dst)
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
                # shutil.copytree(inPath_src, inPath_dst)  # 其中inPath_dst的路径已经创建，则会报错(所以先要删除)
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


if __name__ == '__main__':
    copy_dirs_copytree()