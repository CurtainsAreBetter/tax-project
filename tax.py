"""
Tax contains Bracket class used most often if not only in the Tax class
Tax Class is also contained in this file
"""
from operator import attrgetter


# top is inclusive
# bottom is exclusive
class Bracket:
    def __init__(self, bottom_value=None, top_value=None, rate=float()):
        if bottom_value is None:
            bottom_value = 0
        if top_value is None:
            top_value = 92237203685477000
        self._rate = rate
        self._bottom = bottom_value
        self._top = top_value

    def __repr__(self):
        # There's a use I swear
        return f"<BracketObj({self._bottom}, {self._top}, {self._rate})>"

    def __str__(self):
        return f"BRACKET RANGE\nmin: {self._bottom} exclusive\nmax: {self._top} inclusive\nrate: {self._rate}"

    # check if a value or a part of a value is within bracket
    def __contains__(self, item):
        if item > self._bottom:
            return True
        else:
            return False

    def __mul__(self, other):
        return other * self._rate

    def __rmul__(self, other):
        return self._rate * other

    def top(self):
        return self._top

    def bottom(self):
        return self._bottom

    def rate(self):
        return self._rate

    # just need to come up with a better name
    # or find a dunder
    def taxable(self, item):
        if item <= self._bottom:
            return 0
        else:
            amount = item - self._bottom
            # the most value that can be in the bracket
            limit = self._top - self._bottom
            if amount < limit:
                return amount
            if amount >= limit:
                return limit


class Tax:
    def __init__(self, brackets=None, total_deduction=None):
        if brackets is None:
            brackets = []
        if total_deduction is None:
            total_deduction = 0
        # sort brackets
        if len(brackets) > 1:
            brackets.sort(key=attrgetter("_bottom"))
        self._brackets = brackets
        self._deduction = total_deduction

    def __repr__(self):
        return f"<{len(self._brackets)} bracket tax object>"

    def __str__(self):
        out = ""
        for brak in self._brackets:
            out += f"{str(brak)}\n"
        return out

    # god gave me eyes so that they could bleed
    # hear me out, income# * tax() obj = taxed income
    # other must be gross income
    def __rmul__(self, other):
        total_tax = 0
        other -= self._deduction
        for brack in self._brackets:
            if other in brack:
                portion = brack.taxable(other)
                total_tax += portion * brack
        return total_tax

    def __mul__(self, other):
        total_tax = 0
        other -= self._deduction
        for brack in self._brackets:
            if other in brack:
                portion = brack.taxable(other)
                total_tax += portion * brack
        return total_tax

    def brackets(self):
        return self._brackets


# tax + tax?
# like social security tax -> 12.4% @ [0:]
# and then medicare tax -> 2.9% @ [0:]
# so addition of two taxes only works if their brackets are the same?
# or should I instead be doing bracket addition?
# like would a tax + a tax conjoin brackets? if they didn't have the same
# range?
# as of right now I think I'm getting ahead of myself. What needs to be done is done

