import random


def generate_code(code_len=8):
    all_chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos = len(all_chars) - 1
    code = ''
    for _ in range(code_len):
        index = random.randint(0,last_pos)
        code += all_chars[index]
    return code

if __name__ == '__main__':

    print(generate_code())
    '''
    a = input('请输入验证码长度：')
    if a.isnumeric():
        print(generate_code(int(a)))
    else:
        print('请输入正确的验证码长度')
'''