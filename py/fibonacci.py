class Fibonacci(object):

    def fib(self, n):
        """
        递归求斐波拉契数列
        :param n: 第 n 个
        :return: 第 n 个斐波拉契数
        """
        if n > 2:
            return self.fib(n - 1) + self.fib(n - 2)
        if 1 == n or n == 2:
            return 1
        return 0

    @staticmethod
    def fibonacci(n):
        """
        自底向上的动态规划
        :param n: 第 n 个
        :return: 第 n 个斐波拉契数
        """
        fibonacci_list = [1 for _ in range(n)]
        for i in range(2, n):
            fibonacci_list[i] = fibonacci_list[i - 1] + fibonacci_list[i - 2]
        if fibonacci_list:
            return fibonacci_list[-1]
        return 0

    @staticmethod
    def fibonacci_(n):
        """
        自顶向下的备忘录法
        :param n: 第 n 个
        :return: 第 n 个斐波拉契数
        """
        fibonacci_list = [1 for _ in range(n)]
        # 字典的0，1表示该fib是否已经求得
        fibonacci_dict = {i: 0 for i in range(n)}
        fibonacci_dict[0] = fibonacci_dict[1] = 1
        num_list = [0, 0]

        def fibonacci(l):
            for i in range(1, 3):
                if fibonacci_dict[l - i]:
                    num_list[i - 1] = fibonacci_list[l - i]
                else:
                    fibonacci_list[l - i] = num_list[i-1] = fibonacci(l - i)
                    fibonacci_dict[l - i] = 1
            return sum(num_list)

        for i in range(n-1, 1, -1):
            fibonacci_list[i] = fibonacci(i)
        if fibonacci_list:
            return fibonacci_list[-1]
        return 0


fib = Fibonacci()
for j in range(-1, 10):
    print(fib.fib(j), fib.fibonacci(j), fib.fibonacci_(j))
