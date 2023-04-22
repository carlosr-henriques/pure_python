from time import sleep

def countdown(timer):
    while timer:
        min, secs = divmod(timer, 60) # divmod recebe o numerador e divisor, e retorna quociente e o resto; portanto, se eu passo que quero dividir 60 segundos por 60 (também representa os segundos), eu terei como retorno (x//y, x%y), isto é, o quociente inteiro e o resto da divisão, sendo neste exemplo citado, 1 minuto (1, 0).
        countdown_timer = f'{min}:{secs}'
        print(countdown_timer, end="\r") # '\r' é responsável por fazer a magia do contador, reescrevendo o valor que sobre decréscimo de 1 unidade no valor anterior.
        sleep(1)
        timer -= 1

    print('Timer completed!')
timer = input("Enter the time in seconds: ")
countdown(int(timer))