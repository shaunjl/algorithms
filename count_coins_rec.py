"""
Top down Dynamic Programming (memoization)
pseudocode-

  def number_of_ways(amount, denominations):
    answer = 0
    for each denomination in denominations:
        for each num_times_to_use_denomination in \
                possible_num_times_to_use_denomination_without_overshooting_amount:
            answer += number_of_ways(amount_remaining, other_denominations)
    return answer

"""


class Change:

    def __init__(self):
        self.memo = {}

    def change_possibilities_top_down(self, amount_left, denominations,
                                      current_index=0):
        # Check our memo and short-circuit if we've already solved this one
        memo_key = str((amount_left, current_index))
        if memo_key in self.memo:
            print("grabbing memo[{}]".format(memo_key))
            return self.memo[memo_key]

        # Base cases:
        # We hit the amount spot on. yes!
        if amount_left == 0:
            return 1

        # We overshot the amount left (used too many coins)
        if amount_left < 0:
            return 0

        # We're out of denominations
        if current_index == len(denominations):
            return 0

        print("checking ways to make {} with {}".format(
            amount_left,
            denominations[current_index:],
        ))

        # Choose a current coin
        current_coin = denominations[current_index]

        # See how many possibilities we can get
        # for each number of times to use current_coin
        num_possibilities = 0
        while amount_left >= 0:
            num_possibilities += self.change_possibilities_top_down(
                amount_left,
                denominations,
                current_index + 1,
            )
            amount_left -= current_coin

        # Save the answer in our memo so we don't compute it again
        self.memo[memo_key] = num_possibilities
        return num_possibilities

change_maker = Change()
print(change_maker.change_possibilities_top_down(50, [1,5,10,25]))

