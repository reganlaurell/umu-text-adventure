from ebb import enter_ebb_west
from khic import enter_khic_north, enter_khic_east

def enter_academic_mall():
    print('This is the Academic Mall. ' +
        'To the left, you will see EBB. ' + 
        'To the right, you will see the old part of KHIC ' +
        'and straight ahead you see the new part of KHIC.')
    print('Where would you like to go? EBB or Old KHIC or New KHIC?')
    choice = input('EBB or Old KHIC or New KHIC > ').lower()

    if('ebb' in choice):
        enter_ebb_west()
    elif('old' in choice):
        enter_khic_east()
    elif('new' in choice):
        enter_khic_north()
    else:
        enter_academic_mall()

def exit_academic_mall():
    print('You are exiting the Academic Mall. Where would you like to go? Enter EBB, Exit Campus, or Enter Academic Mall')