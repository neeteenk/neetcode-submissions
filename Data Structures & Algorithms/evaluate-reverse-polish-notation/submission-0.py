class Solution:
    def calc(self, n1, n2, operator):
        match operator:
            case "+":
                return n2 + n1
            case "-":
                return n2 - n1
            case "*":
                return n2 * n1
            case "/":
                return int(n2/n1)

    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+", "-", "*", "/"} #set
        st = []
        for s in tokens:
            if s not in operators:
                st.append(int(s))
            else:
                n1 = st.pop()
                n2 = st.pop()
                st.append(self.calc(n1, n2, s))
        return st[-1]