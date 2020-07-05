

def task_file(file,task):
    content_file_object = open(file,'r')
    word_list_sorted = []
    new_sentence = []
    new_sentence1 = []
    if task == 'sort':
        new_sentence = content_file_object.read().split()
        for word in new_sentence:
            if word not in new_sentence1:
                new_sentence1.append(word)
        print(sorted(new_sentence1))
        content_file_object.close()
    elif task == 'rev':
        for row in content_file_object:
            new_sentence += row.split("\n")
        print(new_sentence[0][::-1])
        print(new_sentence[2][::-1])
        content_file_object.close()


def main():  # Call the function func
    file_path = input('Enter a file path : ')
    task_choose = input('Enter a task : ')
    task_file(file_path,task_choose)


if __name__ == "__main__":
    main()