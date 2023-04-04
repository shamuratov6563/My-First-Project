

def isprime(son):
    for i in range(2, son):
        if son % i == 0:
            return False
    return True
    

print(isprime(29))
print(isprime(27))

# o'zingizga clon qilib olmoqchi bo'lsangiz
# git clone <repository_path>

# git init
# git add .
# git commit -m "message" 
# git remote add origin "repository_path"
# git push origin master



# git status - bu o'zgarishlar bor yo'ki yo'qligini tekshirish
# git add .(new.py)
# git commit -m "commit xabari"
# git push origin master(main)

