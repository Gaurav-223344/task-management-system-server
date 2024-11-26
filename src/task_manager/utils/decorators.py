class StandardSingletonDecorator(object):
    def __init__(self, klass):
        self.klass = klass
        self.instances = {}
        
    def __call__(self, *args, **kwargs):
        if self.klass not in self.instances:
            self.instances[self.klass] = self.klass(*args,**kwargs)
        return self.instances[self.klass]