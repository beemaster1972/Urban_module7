def custom_write(file_name:str, strings:list)->dict:
    result = {}
    with open(file_name,'w+', encoding='utf-8') as f:
        for i, string in enumerate(strings):
            pos = f.tell()
            f.write(string+'\n')
            result[(i+1,pos)] = string
    return result


if __name__ == "__main__":
    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
    ]

    result = custom_write('test.txt', info)
    for elem in result.items():
        print(elem)