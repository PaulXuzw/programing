class Solution:
    def numTrees(self, n: int) -> int:
    #List存储第n个的所有值
    #由于搜索二叉树的特性，从所有节点中选出一个节点作为根节点，那么子树就可以根据大小分为两部分，这两部分的个数可以用之前的表示
    #当n为奇数时，f(n) = f(0)*f(n-1)*2 + f(1)*f(n-2)*2 + ... + f(i-1)*f(n-i)*2 + f(i)*f(n-i-1)    i=n-i-1
    #偶数： f(n) = f(0)*f(n-1)*2 + f(1)*f(n-2)*2 + ... + f(i-1)*f(n-i)*2 + f(i)*f(n-i-1)*2  i+1 = n-i-1
        List = [1,1,2]
        for i in range(3,n+1):
            result = 0
            if i%2 == 0:
                for j in range(i//2):
                    result += List[j]*List[i-j-1]*2
            else:
                for j in range(i//2+1):
                    if j != i-j-1:
                        result = result+List[j]*List[i-j-1]*2
                    else:
                        result = result + List[j]*List[i-j-1]
            List.append(result)
        return List[n]
