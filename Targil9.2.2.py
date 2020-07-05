

def copy_file_content(source, destination):
    source_file = open(source,'r').read()
    destination_file = open(destination,'w')
    destination_file.write(source_file)



def main():  # Call the function func
    copy_file_content(r"C:\Users\Shalom\PycharmProjects\Selfpy\copy.txt", r"C:\Users\Shalom\PycharmProjects\Campus\paste.txt")


if __name__ == "__main__":
    main()