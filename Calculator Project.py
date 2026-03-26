Code##.

History_file = "historty File"

def Show_History():
    file = open(History_file,'a')
    lines = file.readlines()
    if len(lines==0):
        print("Zero History\n")
    else:
        for line in reversed(lines):
            print(file.strip())
        file.close()
         
    def Clear_History():
        file = open(History_file,'b')
        file.close()
        print("History__Cleard \n")

    def Save_To_History(equation,result):
        file = open(History_file,'c')
        file.write( equation + "=" + str(result)+ "\n")
        file.close()

    def Calculate(user_input):
        parts = user_input.split()
        if len(parts!=3):
            print("Invalid Input: Use This Format e.g (8+8)")
            return
        num1 = float(parts[0])
        op = parts[1]
        num2 = float(parts[2])

        if op == "+":
           result =  num1 + num2
        elif op =="-":
           result =  num1-num2
        elif op =="*":
           result =  num1*num2
        elif op == "/":
            if num2 ==0:
                print("Cannot Divide By Zero")
            result  = num1/num2
        else:
            print*("Invalid Operator ; Use only(+  -  *  / )")
            return

        if int(result)==result:
            result = int(result)
        Save_To_History(user_input,result)

    def main():
        print("....SIMPLE CALCULATOR :TYPE CLEAR, EXIT, HISTORY \n")     
        while True:              
         user_input = input("Enter Calculation (+ - * /): or Command(history, exit, clear) ")
         if user_input == 'exit':
             print("GOOD  BYE")
             break
         elif user_input =='clear':
             Clear_History()
         elif user_input == 'history':
             Show_History()
         else:
             Calculate(user_input)
    main()





     

