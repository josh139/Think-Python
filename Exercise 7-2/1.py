def eval_loop():
    while True:
        answer = input('> ')
        if answer.lower() == 'done':
            break
        else:
            print(eval(answer))


eval_loop()
