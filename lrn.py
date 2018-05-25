def display_arguments(func):
    def display_and_call(*args, **kwargs):
        args = list(args)
        print('must-have arguments are:')
        for i in args:
            print(i)
        print('optional arguments are:')
        for kw in kwargs.keys():
            print(kw + '=' + str(kwargs[kw]))
        return func(*args, **kwargs)

    return display_and_call


@display_arguments
def my_add(m1, p1=0):
    output_dict = {}
    output_dict['r1'] = m1+p1
    return output_dict

my_add(100,p1=1)
