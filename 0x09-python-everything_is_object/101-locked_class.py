#!/usr/bin/python3
'''
    Defines LockedClass
'''


class LockedClass:
    '''
        prevents the user from
        dynamically creating new instance attributes,
        except for first_name
    '''
    __slots__ = ("first_name",)
