def follow_order(cur, open, close, n):
    if len(cur) == n * 2:
        print(cur)
        return 
    if open < n:
        follow_order(cur + '(', open + 1, close, n)
    if close < open:
        follow_order(cur + ')', open, close + 1, n)

def gen_parentheses(n):
    follow_order('', 0,0,n)

if __name__=='__main__':
    n = 3
    gen_parentheses(n)


    