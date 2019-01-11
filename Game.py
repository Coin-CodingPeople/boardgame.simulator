"""
Created by hangeonho on 2018. 10. 2..
"""
# from User import User
from Stack import Stack


class Game:
    def __init__(self, n_of_users, n_of_stack, stack_length):
        # self.users = [User]
        self.stacks = [Stack(stack_length) for i in range(n_of_stack)]