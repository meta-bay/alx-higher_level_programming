#!/usr/bin/python3
class LockedClass:
    '''
        prevents the user from 
        dynamically creating new instance attributes,
        except for first_name
    '''
    __slots__ = ("first_name",)
