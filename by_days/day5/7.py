# Calculator

def cal(a, b, operation):
    if operation == "add":
        return a+b
    if operation == "sub":
        return a-b
    if operation == "mul":
        return a*b
    if operation == "div":
        return a/b

# cal(1,2, "add")
ans = cal(1,2, "add")
print(ans)

