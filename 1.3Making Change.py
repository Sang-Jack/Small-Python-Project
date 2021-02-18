def main():
    pences = int(input('Enter the total amount of pence [0-2000]: '))
    if 0 <= pences <= 2000:
        two_pounds, pences = pences // 200, pences % 200
        one_pounds, pences = pences // 100, pences % 100
        fifty_pences, pences = pences // 50, pences % 50
        twenty_five_pences, pences = pences // 25, pences % 25
        twenty_pences, pences = pences // 20, pences % 20
        ten_pences, pences = pences // 10, pences % 10
        five_pences, pences = pences // 5, pences % 5
        two_pences, pences = pences // 2, pences % 2
        one_pences = pences

        print('Change as follows: ')
        print('{} - {}2 bills'.format(two_pounds,u'\xa3'))
        print('{} - {}1 bills'.format(one_pounds,u'\xa3'))
        print('{} - 50 pences'.format(fifty_pences))
        print('{} - 25 pences'.format(twenty_five_pences))
        print('{} - 20 pences'.format(twenty_pences))
        print('{} - 10 pences'.format(ten_pences))
        print('{} -  5 pences'.format(five_pences))
        print('{} -  2 pences'.format(two_pences))
        print('{} -  1 pences'.format(one_pences))

    else:
        print('Error: pences not in range [0-2000]')


main()
