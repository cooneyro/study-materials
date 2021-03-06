import sys

RED = "\033[1;31m"
BLUE = "\033[1;34m"
CYAN = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD = "\033[;1m"
REVERSE = "\033[;7m"


# Q1


def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b."""
    while b:
        a, b = b, a % b
    return a


sys.stdout.write(BLUE)
print("Q1: Suppose we roll a red die and a green die\n")

# (i)
print("(i) What is the sample space for this experiment?")
sys.stdout.write(RESET)
outcomes = [1, 2, 3, 4, 5, 6]
s = ""
for i in outcomes:
    for j in outcomes:
        s += str("{{{i:0},{j:0}}} ".format(i=i, j=j))
    print("\t {}".format(s))
    s = ""

sys.stdout.write(BLUE)
# (ii)
print("\n(ii) What is the probability that the number on the green die is larger than the number "
      "on the red die?")
sys.stdout.write(RESET)
count = 0
for i in outcomes:
    for j in outcomes:
        if i > j:
            count += 1
common_divisor = gcd(count, len(outcomes) ** 2)
(reduced_num, reduced_den) = (count / common_divisor, len(outcomes) ** 2 / common_divisor)
print("\t{0:g}/{1:g}".format(reduced_num, reduced_den))

sys.stdout.write(BLUE)
# (iii)
print("\n(iii)Define what it means for two events E and F to be independent.")
sys.stdout.write(RESET)
print("\tTwo events E and F are independent if the order in which they occur doesn't matter. "
      "Alternatively, if observing one doesn't affect the other.")
print("\tP(E ∩ F) = P(E)P(F)")

sys.stdout.write(BLUE)
# (iv)
print("\n(iv) Let event E be that the sum of the dice equals 2 or 3 and event F be that"
      " the sum equals 3. Are E and F independent? Explain with reference to the "
      "definition given above")
sys.stdout.write(RESET)
print("\tNo, E and F are not independent. Observing E affects the outcome of F. Using the mathematical definition "
      "P(E ∩ F) = P(E)P(F):")
print("\tP(E ∩ F) = 1/36, P(E)P(F) = 1/12 * 1/18 = 1/216")
print("\tThus, E and F are dependent as P(E ∩ F) != P(E)P(F)")

sys.stdout.write(BLUE)
# Q2
print("\nQ2:")

# (i)
print("\n(i) State Bayes Rule")

sys.stdout.write(RESET)
print("\tP(E|F) = (P(F|E)P(E))/P(F)")

sys.stdout.write(BLUE)
print("\n(ii) Suppose 1% of computers are infected with a virus.There is an imperfect test for detecting the virus."
      "When applied to a computer with the virus the test gives a positive result 90% of the time.")
print("When applied to a computer which does not have the virus, the test gives a negative result 99% of the time."
      "Suppose that the test is positive for a computer.What is the probability that the computer has the virus?")

sys.stdout.write(RESET)
prop_infected = 0.01
false_pos = 0.01
p_f_given_e = 0.9
p_e = 0.01
p_f = (p_f_given_e * prop_infected) + (false_pos * (1 - prop_infected))
p_e_given_f = (p_f_given_e * p_e) / p_f
print("\tE = actually has virus, F = test positive for virus")
print("\tP(F|E) = {}, P(E)={}, P(F) = (0.9*0.01 + 0.01*(1-0.01)) = {}".format(p_f_given_e, p_e, p_f))
print("\tP(E|F) = ({}*{})/{} = {}%".format(p_f_given_e, p_e, p_f, p_e_given_f))

sys.stdout.write(BLUE)
# Q3
print("\nQ3: You invent a game where the player bets €1, and rolls two dice. If the sum is 7, the player wins €k, "
      "and otherwise loses their bet.")

# (i)
print("\n(i)Define the expectation and variance of a discrete random variable.")

sys.stdout.write(RESET)
print("\tFor random variable X taking values x1, …, xn the expected value is E[X]=x1*P(X=x1)+… xn*P(X=xn)."
      "The variance is Var(X)=E[(X-E[X])^2] = (x1-E[X])^2*P(X=x1)+… (xn-E[X])^2*P(X=xn).")

sys.stdout.write(BLUE)
print("\n(ii) What is the expected reward in this game?")

sys.stdout.write(RESET)
print("\tProbability of winning = 1/6 -> expected reward = k/6 - 5/6")

sys.stdout.write(BLUE)
print("\n(iii)What value of k makes the game fair (i.e. makes the expected reward zero)?What is the variance "
      "of the reward in this case ?")

sys.stdout.write(RESET)
print("\tTo make the expected reward zero, k=5. Variance = (5-0)^2 * 1/6 + (-1-0)^2 * 5/6 = 5^2/6 + 5/6 = 5.")

sys.stdout.write(BLUE)
print("\n(iv)For two independent random variables X and Y show that Var(X+Y)=Var(X)+Var(Y). "
      "Hint: Recall that E[X+Y]=E[X]+E[Y] and that when X and Y are independent then E[XY]=E[X]E[Y]")

sys.stdout.write(RESET)
print("\tVar(X+Y) = E[(X+Y)^2] - E[X+Y]^2 ")
print("\t         = E[X^2 + 2XY + Y^2] - (E[X] + E[Y])^2 ")
print("\t         = E[X^2] + 2E[XY] + E[Y^2] - E[X]^2 - 2E[X]E[Y] - E[Y]^2 ")
print("\t         = E[X^2] - E[X]^2 + E[Y^2] - E[Y]^2")
print("\t         = Var(X) + Var(Y)")

sys.stdout.write(BLUE)
print("\n(v)Suppose that you play the game 2 times in a row with k=5.What is the expected value of the reward "
      "(i.e. of the aggregate winnings after playing 2 times)?What is its variance ? What is the expectation "
      "and variance of the reward after 100 plays ?")

sys.stdout.write(RESET)
print("\tExpected value = 0 for both. Variance = 10 for 2 plays, 500 for 100 plays")
