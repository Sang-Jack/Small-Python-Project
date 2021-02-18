def main():
    less_than_1lt_count = int(input('Enter the number of containers with size less or equal to 1 lts: '))
    more_than_1lt_count = int(input('Enter the number of containers with size greater than 1 lts: '))

    refund_money = less_than_1lt_count * 0.25 + more_than_1lt_count * 0.50

    print('Refund money: {}{:.2f}'.format(u"\xA3", refund_money))


main()
