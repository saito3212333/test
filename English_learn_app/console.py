import random

import termcolor


input_txt = "data.txt"
words_count = 2
output_txt = 'result_txt'
start_n = 0
end_n = 20


def main():
    while True:
        view()
        with open(input_txt) as f:
            l_strip = [s.strip() for s in f.readlines()]
            #おそらく改行を取り除いてくれるメソッド strip
            for i in range(words_count):
                n = random.randint(start_n,end_n)
                print(termcolor.colored(str(n+1)+':'+l_strip[n],'red'))
        view()

        s = input('会話を作ってください。：')
        if s != '':
            with open(output_txt, mode='a') as f:#wだとずっとデータが消えるので、anにしてあげらたらいいと思う。
                f.write(s + '★' + str(words_count)+'\n')

def view():
    print("-"*30)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('おつかれさまでした。')