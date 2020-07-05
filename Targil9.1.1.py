

def are_files_equal(file1, file2):
    content_file1_object = open(file1,'r').read()
    content_file2_object = open(file2,'r').read()

    if content_file1_object == content_file2_object:
        print(True)
    else:
        print(False)


def main():  # Call the function func
    are_files_equal(r"C:\Users\Shalom\PycharmProjects\Selfpy\vacation.txt",r"C:\Users\Shalom\PycharmProjects\Campus\work.txt")
   # False

if __name__ == "__main__":
    main()
