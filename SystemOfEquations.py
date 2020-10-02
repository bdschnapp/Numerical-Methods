class SystemOfLinearEquations:

    def __init__(self, n, input_array):
        # | [0][0], [0][1] ... [0][n], [0][n+1] |
        # | [1][0], [1][1] ... [1][n], [1][n+1] |
        # | ...                                 |
        # | [n][0], [n][1] ... [n][n], [n][n+1] |

        # Solves for incorrect input size n
        # TODO: implement solution for invalid input_array length case
        if len(input_array) != (n * (n + 1)):
            i = 0
            while (i * (i + 1)) < len(input_array):
                i += 1
                if (i * (i + 1)) == len(input_array):
                    n = i
        # Sets size and initializes matrix to all 0
        self.size = n
        self.matrix = [[0 for i in range(n + 1)] for j in range(n)]

        # Sets matrix to correct values based on input_array
        for i in range(n):
            for j in range(n+1):
                self.matrix[i][j] = input_array[(n * i) + j]

    # Swaps rows in self.matrix
    def swap(self, i):
        n = 0
        if (i + 1) < self.size:
            n = i+1
        temp = self.matrix[i]
        self.matrix[i] = self.matrix[n]
        self.matrix[n] = temp

    # Solves a system of linear equations iteratively
    # Returns vector x[self.size] of closest results if successful, returns false if invalid input
    # Runtime O(iterations*(n^2))
    def gauss_seidel(self, max_iterations):
        # Pivots rows so that matrix[i][i] is never 0
        repeat = False
        count = 0
        while repeat:
            repeat = False
            for i in range(self.size):
                if self.matrix[i][i] == 0:
                    self.swap(i)
                repeat = True
            if count > self.size:
                return False
            count += 1

        # Initializes vectors for tracing iteration results and checking if its the final answer
        x = [0 for i in range(self.size)]
        correct = [False for i in range(self.size)]

        # Loops through up to the max iteration number, or until the correct result is found
        for k in range(max_iterations):
            for i in range(self.size):
                xn = 0
                for j in range(self.size):
                    if i != j:
                        xn = xn + self.matrix[i][j] * x[j]
                x[i] = (self.matrix[i][self.size + 1] - xn) / self.matrix[i][i]

                # Checks if the current x value for the current iteration is correct
                if(xn + (self.matrix[i][i] * x[i])) == self.matrix[i][self.size + 1]:
                    correct[i] = True

            # Checks if all x values for the current iteration are correct
            if not(False in correct):
                # Returns x before max iterations is reached if all values are correct
                return x
        # Returns x once max iterations is reached, x will contain approximate values
        return x

    def gauss_seidel_relaxed(self, max_iterations, guess=1, omega=1.5):
        # Pivots rows so that matrix[i][i] is never 0
        repeat = False
        count = 0
        while repeat:
            repeat = False
            for i in range(self.size):
                if self.matrix[i][i] == 0:
                    self.swap(i)
                repeat = True
            if count > self.size:
                return False
            count += 1

        # Initializes vectors for tracing iteration results and checking if its the final answer
        x = [guess for i in range(self.size)]
        correct = [False for i in range(self.size)]

        # Loops through up to the max iteration number, or until the correct result is found
        for k in range(max_iterations):
            for i in range(self.size):
                xn = 0
                for j in range(self.size):
                    if i != j:
                        xn = xn + self.matrix[i][j] * x[j]
                x[i] = (omega * (self.matrix[i][self.size + 1] - xn) / self.matrix[i][i]) + ((1 - omega) * guess)

                # Checks if the current x value for the current iteration is correct
                if(xn + (self.matrix[i][i] * x[i])) == self.matrix[i][self.size + 1]:
                    correct[i] = True

            # Checks if all x values for the current iteration are correct
            if not(False in correct):
                # Returns x before max iterations is reached if all values are correct
                return x
        # Returns x once max iterations is reached, x will contain approximate values
        return x