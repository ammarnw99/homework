import json
s=0
List1 = []
name_ = input("enter name :")
with open("q3.json","r") as f:
    r =json.loads(f.read())
    for i in r :
        print(i)
        answer = input("enter the answer a/b :")
        List1.append(answer)
        if answer ==r[i]:
            print("correct answer,you got 1 point")
            s=s+1
        else:
            print("wrong answer,you lost 1 point")
            

    ammar ={name_:List1}
    print(ammar)

    print("final score is :",s)
ammar_=json.dumps(ammar)
with open("q3_3.json","w")as f:
    f.write(ammar_)
