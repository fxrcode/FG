class BrowserHistory:

    def __init__(self, homepage: str):
        self.stack = [""] * 5005
        self.p = self.t = 0
        self.stack[0] = homepage
        
    def visit(self, url: str) -> None:
        self.p += 1
        self.stack[self.p] = url
        self.t = self.p

    def back(self, steps: int) -> str:
        self.p = max(0, self.p-steps)
        return self.stack[self.p]
        
    def forward(self, steps: int) -> str:
        self.p = min(self.t, self.p + steps)
        return self.stack[self.p]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)