#!/usr/bin/python3
'''
    A Square module
'''
from models.rectangle import Rectangle


class Square(Rectangle):
    ''' Defines a square class'''
    def __init__(self, size, x=0, y=0, id=None):
        ''' initializes the square object'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
            )

    @property
    def size(self):
        ''' Returns the size '''
        return self.width

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        ''' update values '''
        selfs = [self.id, self.size, self.x, self.y]
        if args:
            for i in range(len(list(args))):
                if args[i]:
                    selfs[i] = args[i]
            self.id, self.size, self.x, self.y = selfs
        elif kwargs:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'size':
                    self.size = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value

    def to_dictionary(self):
        ''' converts to dictionary '''
        return {
            'id': self.id,
            'x': self.x,
            'size': self.size,
            'y': self.y,
        }
