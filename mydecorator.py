import random
import datetime


def logger_decorator(filepath):

	def decorator(old_function):
		f_name = old_function.__name__

		def new_function(*args, **kwargs):
			nonlocal f_name
			f_time = datetime.datetime.now()
			f_args = args
			f_kwargs = kwargs
			old_function_result = old_function(*args, **kwargs)
			with open(filepath, 'a') as file:
				file.write(f'{f_name}\n{f_time}\n{f_args} {f_kwargs}\n{old_function_result}\n --- \n')
			return old_function_result
		return new_function
	return decorator

if __name__ == '__main__':

	@logger_decorator('log2.txt')
	def random_function(*args, **kwargs):
		random_number = random.randint(0, 100)
		random_division = random_number % 2
		if random_division == 1:
			return 'The random number was not even'
		else:
			return 'The random number was even'

	print(random_function('12','15', Privet = 'Hello'))





