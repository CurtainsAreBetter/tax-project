
uh ok never done documentation before and when I read docs,
I usually skim and then spend 3 hours googling a question I could
have answered had I read the docs in full instead of skimming.
But I don't believe in learning and I don't believe in conforming,
so good luck reading these docs.

I mean the code is so simple that it really should just be a non issue.
If you have trouble PLEASE let me know so I can help you out and do something
useful/ fun.



OK
tax.py
Contains two classes:
Bracket
&
Tax

# Bracket:

    args -> bottom_value, top_value, rate

    bottom_value
        The lowest value of the tax bracket. This number is exclusive, meaning
        if you set it to 10, the bracket would start at 10.000000000....1

    top_value
        The highest value of the tax bracket. This number is inclusive.

    rate
        Decimal expression of a ratio, usually if not always represents a percentage
        It's the actual tax of the given bracket


    Methods:
        .top() --> returns top_value
        .bottom() --> returns bottom_value
        .rate() --> returns rate
        .taxable(item)
            if the item (value) is in the Bracket then the value amount of the item
            that can be found in the Bracket is returned

    Attributes? Idk if that's the right term:
        Str()
        --> will print out an easy to read bracket info card.
        in
        --> checks if given # is greater than the bottom of the range.
            if true then returns true
            else returns false
        *
        --> num * Bracket() will return num * rate

Bracket Example:
The dc state tax rate for singles that make $0 - $10,000 is 4%
This dc state tax bracket is represented as....

    Bracket(bottom_value=0,
            top_value=10000
            rate=0.04)


# Tax:

    args -> brackets: list, total_deduction

    brackets
        list of Bracket() objects
        Even if only one Bracket being enter it still needs to be put within a list

    total_deduction
        A tax deduction. Usually I just use the standard deduction.

    Methods:
        .brackets() --> returns bracket list

    Arithmetic:
        * multi
        --> num * Tax() or Tax() * num will return the same value. That value will be
            the tax owed on the num (this accounts for tax brackets)
        Str()
        --> Returns Bracket() strings
