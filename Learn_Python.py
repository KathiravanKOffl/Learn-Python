def error(msg):
    print(("-"*50)+(" ERROR ")+("-"*50))
    print(("-"*107) + "\n")
    print(msg)
    print("\n"+("-"*107))

def display_score(sco):
    if sco <= 40:
        print(f"\n\nYour beautiful score is {sco}")
    elif sco <= 80:
        print(f"\n\nHmm.. Good Try!!!\nScore : {sco}")
    elif sco < 100:
        print(f"\n\nHmm.. Alomst Done!!!\nScore : {sco}")
    elif sco == 100:
        print(f"\n\nCongratulations!!!\nYou got full marks....\nscore : {sco}")

def challenge_1(func):

    def factorial_answer(n):
        if type(n) != int or n<0:
            return None
        fact = 1
        for i in range(1,n+1):
            fact *= i
        return fact
    
    tests = {
        1:7,
        2:-8,
        3:4.8,
        4:'kathir',
        5:True
    }

    def check(*args):

        score = 0
            
        try:
            for i in tests:
                print(f"Testing :{tests[i]}")
                if (type(tests[i]) != int) and (func(tests[i]) == None):
                    print(f"Test {i} passed !!!")
                    score += 20
                elif factorial_answer(tests[i]) == func(tests[i]):
                    print(f"Test {i} passed !!!")
                    score += 20
                else:
                    error(f"Expected : {factorial_answer(tests[i])}\nBut, Received : {func(tests[i])}")
                    break
        except TypeError:
            error("Make Sure that all inputs, except int, must returns None!!!")
        finally:
            display_score(score)

    return check

def challenge_2(func):
    def OE_ans(num):
        if num%2==0:
            return "Even"
        else:
            return "Odd"
        
    tests = [45,67,3,12,78]

    def check():
        score = 0
        try:
            for i in tests:
                print(f"Testing :{i}")
                if OE_ans(i) == func(i):
                    print(f"Test {i} passed !!!")
                    score += 20
                else:
                    error(f"Expected : {OE_ans(i)}\nBut, Received : {func(i)}")
                    break
        finally:
            display_score(score)

    return check