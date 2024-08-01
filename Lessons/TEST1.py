class fig:

    def reorgan(*args):
        args_list = list(args)
        for i in range(len(args_list)):
            print(f'{args_list[i]}')




circle1 = fig.reorgan((200, 200, 100), 10)
#cube1 = fig.reorgan((222, 35, 130), 6)