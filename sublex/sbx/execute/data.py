class ExecutionData:
    def __init__(self):
        self.data = {}
        self.steps_completed = 0
        self.result = None

    def step_completed(self):
        self.steps_completed += 1
