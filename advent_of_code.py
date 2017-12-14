x = [123123]
y = [823936645345581272695677318513459491834641129844393742672553544439126314399846773234845535593355348931499496184839582118817689171948635864427852215325421433717458975771369522138766248225963242168658975326354785415252974294317138511141826226866364555761117178764543435899886711426319675443679829181257496966219435831621565519667989898725836639626681645821714861443141893427672384716732765884844772433374798185955741311116365899659833634237938878181367317218635539667357364295754744829595842962773524584225427969467467611641591834876769829719248136613147351298534885563144114336211961674392912181735773851634298227454157885241769156811787611897349965331474217223461176896643242975397227859696554492996937235423272549348349528559432214521551656971136859972232854126262349381254424597348874447736545722261957871275935756764184378994167427983811716675476257858556464755677478725146588747147857375293675711575747132471727933773512571368467386151966568598964631331428869762151853634362356935751298121849281442128796517663482391226174256395515166361514442624944181255952124524815268864131969151433888721213595267927325759562132732586252438456569556992685896517565257787464673718221817783929691626876446423134331749327322367571432532857235214364221471769481667118117729326429556357572421333798517168997863151927281418238491791975399357393494751913155219862399959646993428921878798119215675548847845477994836744929918954159722827194721564121532315459611433157384994543332773796862165243183378464731546787498174844781781139571984272235872866886275879944921329959736315296733981313643956576956851762149275521949177991988236529475373595217665112434727744235789852852765675189342753695377219374791548554786671473733124951946779531847479755363363288448281622183736545494372344785112312749694167483996738384351293899149136857728545977442763489799693492319549773328626918874718387697878235744154491677922317518952687439655962477734559232755624943644966227973617788182213621899579391324399386146423427262874437992579573858589183571854577861459758534348533553925167947139351819511798829977371215856637215221838924612644785498936263849489519896548811254628976642391428413984281758771868781714266261781359762798]


# def halfway_pnt_summer(lst):
#     """takes sum of numbers if num matches halfway num"""

#     sum_lst = 0
#     ind = 0
#     t = lst[0]
#     d = [int(i) for i in str(t)]
#     pnt = len(d)/2

#     for item in d:
#         if ind == len(d) - 1 and d[ind] == d[ind + pnt]:
#             sum_lst += item
#         elif d[ind] == d[ind + pnt]:
#             sum_lst += item
#             ind += 1
#         else:
#             ind += 1
#     return sum_lst
# halfway_pnt_summer(x)

#problem is wrapping around list - initial soln only wrapped on last number,
#this one does more. Could try making if statement and when needs to wrap,
#resets second ind

# for item in d:
#     if item == d[ind + pnt]:
#         sum_lst += item
#         ind += 1


# def halfway_summer(lst):
#     """sums numbers that match the number midpoint steps ahead"""

#     t = lst[0]
#     d = [int(i) for i in str(t)]
#     steps = len(lst)/2
#     summer = 0
#     ind = 0

#     for i in d:
#         if ind > (len(d) - steps - 1):
#             ind = -1 * steps
#             if i == d[(ind + steps)]:
#                 summer += i
#                 ind += 1
#             else:
#                 ind += 1

#         elif i == d[(ind + steps)]:
#             summer += i
#             ind += 1

#         else:
#             ind += 1
#     return summer
    
# print halfway_summer(y)

# pattern needed:

# 0 1 2 3 4 5 6 7 8 9

# use range when want to map indices

def halfway_summer(lst):
    """sums numbers that match the number midpoint steps ahead"""

    t = lst[0]
    d = [int(i) for i in str(t)]
    summer = 0

    for i in range(len(d)):
        if d[i] == d[int(i + len(d) / 2) % len(d)]:
            summer += int(d[i])
    return summer


def checksum(filename):

    file_data = open(filename)

    list_of_numbers = []
    checksum = []

    for line in file_data:
        line = line.rstrip()
        numbers = line.split("\t")
        numbers = [int(num) for num in numbers]
        list_of_numbers.append(numbers)

    checksum = [(max(lst) - min(lst)) for lst in list_of_numbers]
    return sum(checksum)

def check_div(filename):

    file_data = open(filename)

    list_of_rows = []
    checkdiv = []

    for line in file_data:
        line = line.rstrip()
        numbers = line.split("\t")
        numbers = [int(num) for num in numbers]
        list_of_rows.append(numbers)

        for i in range(len(list_of_rows)):
            if list_of_rows[i] % list_of_rows[i+1] == 0:
                checkdiv.append(list_of_rows[i])
            # elif list_of_rows[-i + 1] % list_of_rows[i] == 0:
            #     checkdiv.append(list_of_rows[i])
            else:
                print "not this time!"
        return sum(checkdiv)
