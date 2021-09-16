from operator import add, sub, mul, truediv

class RPN_Calculator():
    def __init__(self):
        self.STACK = []
        self.APPEND = self.STACK.append
        self.CLEAR = self.STACK.clear
        self.POP = self.STACK.pop

        self.OPERATORS = {
                            '*': mul,
                            '+': add,
                            '-': sub,
                            '/': truediv
                            }

    def apply(self, token):
        '''
        Perform Arithametic operation 
        Input : Arithametic operator
        OutPut: True/False based on operation 
        '''
        if (op := self.OPERATORS.get(token)) is not None:
            last = self.POP()
            try:
                self.APPEND(op(self.POP(), last))
                return True
            except IndexError:
                self.APPEND(last)
                raise
        else:
            return False


    def evaluate(self, expression):
        '''
        Perform Arthametic operation 
        Input : String Expression
        OutPut: String Value
        '''
        token_list = expression.split()
        if token_list is None:
            print('Error:SyntaxError')
            return None
        for token in token_list:
            try:
                if self.apply(token) is not False:
                    continue
            except IndexError:
                print('Error: Must have at least two parameters to perform operation.')
                continue
            except Exception as e:
                print("Exception :"+str(e))
            try:
                try:
                    result = int(token)
                except ValueError:
                    result = float(token)
            except ValueError as e:
                print("Please Enter valid value.["+str(e)+"]")
            else:
                self.APPEND(result)
        try:
            return self.STACK[-1]
        except IndexError:
            return None

def run():
    calculator = RPN_Calculator()
    while True:
        input_expression = input('>')
        if input_expression in ['quit','q','exit']:
            exit()
        last_element = calculator.evaluate(input_expression)
        if last_element is not None:
            print(f'{last_element}')


if __name__ == '__main__':
    run()