#!/usr/bin/env python3

# class Myvalue:
 
#     def __init__(self , value="" ,value=""):
#         self.value = value
# 		self.value = value
		

#     @property
#     def value(self):
#         return self._value

#     @value.setter
#     def value(self, new_value):
#         if not isinstance(new_value, str):
#             print("The value must be a value.")
#         self._value = new_value

# 	def is_sentence(self):
# 		if self.dot.endswith('.'):
# 			return True
# 		else:
# 			return False

class MyString:

    def __init__(self, value=""):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):
            print("The value must be a string.")
        else:
            self._value = new_value

    def is_sentence(self):
        if self.value.endswith('.'):
            return True
        else:
            return False

    def is_question(self):
        if self.value.endswith('?'):
            return True
        else:
            return False

    def is_exclamation(self):
        if self.value.endswith('!'):
            return True
        else:
            return False


	