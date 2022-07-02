import os
import PyPDF2

def get_all_file_by_type(path, type=(), get_all_dirs = True):  
# 获得以type类型结尾的所有文件，返回一个list

    filelist = []

    for a, b, c in os.walk(path):
        for name in c:
            fname = os.path.join(a, name)
            if fname.endswith(type):
                filelist.append(fname)
        if not get_all_dirs:        # 仅在当前目录查找文件
            print("跳出循环")
            break
    print("总共有%d个文件"%filelist.__len__())
    return filelist

def compute_pdfpage(path, get_all_dirs = False):
    counts = 0
    type = ("PDF","pdf")
    file_list = get_all_file_by_type(path=path, type=type, get_all_dirs = get_all_dirs)
    for pdf in file_list:
        try:
            reader = PyPDF2.PdfFileReader(pdf, strict=False)
            # 不解密可能会报错：PyPDF2.utils.PdfReadError: File has not been decrypted
            if reader.isEncrypted:
                reader.decrypt('')
            page_num = reader.getNumPages()
            counts += page_num
            print(pdf, page_num)
        except Exception as e:
            print("-"*70)
            print(pdf + "该文件出现异常，可能是权限问题")
            print(e)
            print("-"*70)
    return counts

if __name__ == '__main__':
    path = r"."
    counts = compute_pdfpage(path, get_all_dirs=True)
    print("总共%d页"%counts)
