from queue import LifoQueue 
backward_history = LifoQueue()
forward_history = LifoQueue()
current_page = None 
NoOfVisit = int(input('enter the number of URL visit history'))
print('Enter URLs to visit')
for i in range(NoOfVisit):
    URL = input('URL')
    print(f'visiting {URL}')
    backward_history.put(current_page)
    current_page = URL
    print(f'current page:{current_page}')
    while input('do you want to go back?(yes/no):').lower()=='yes':
        if not backward_history.empty():
            forward_history.put(current_page)
            current_page=backward_history.get()
            print(f'going back to{current_page}')
        else:
            print('no previous page available')
    while input('do you want to go forward? (yes/no):').lower()=='yes':
        if not backward_history.empty():
            backward_history.put(current_page)
            current_page=forward_history.get()
            print(f'going forward to {current_page}')
        else:
            print('no forward page available')
            



