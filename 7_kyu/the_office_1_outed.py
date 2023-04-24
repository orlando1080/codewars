# Description:
# Your colleagues have been looking over you shoulder. When you should have been doing your boring real job,
# you've been using the work computers to smash in endless hours of codewars.

# In a team meeting, a terrible, awful person declares to the group that you aren't working. You're in trouble.
# You quickly have to gauge the feeling in the room to decide weather or not you should gather your things and leave.
# Given an object (meet) containing team member names as keys, and their happiness rating out of 10 as the value,
# you need to assess the overall happiness rating of the group. If <= 5, return 'Get Out Now!'.
# Else return 'Nice Work Champ!'.
# Happiness rating will be total score / number of people in the room.

def outed(meet, boss):
    total = sum(meet[name] * 2 if name == boss else meet[name] for name in meet) / len(meet)
    return 'Get Out Now!' if total <= 5 else "Nice Work Champ!"

