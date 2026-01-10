
# https://docs.python.org/3/library/enum.html

import enum


class BugStatus(enum.Enum):

    new = 7
    incomplete = 6
    invalid = 5
    wont_fix = 4
    in_progress = 3
    fix_committed = 2
    fix_released = 1


print("Member name: {}".format(BugStatus.wont_fix.name))    # ==> wont_fix
print("Member value: {}".format(BugStatus.wont_fix.value))  # ==> 4


for status in BugStatus:
    print("{:15} = {}".format(status.name, status.value))


actual_state = BugStatus.wont_fix
desired_state = BugStatus.fix_released

print("Equality:",
      actual_state == desired_state,       # ==> False
      actual_state == BugStatus.wont_fix)  # ==> True
print("Identity:",
      actual_state is desired_state,       # ==> False
      actual_state is BugStatus.wont_fix)  # ==> True


# Sometimes normal class members are easier to use
# ================================================


class BugStatusClass:
    new = 7
    incomplete = 6
    invalid = 5
    wont_fix = 4
    in_progress = 3
    fix_committed = 2
    fix_released = 1


print("Member name: HAS NO NAME !!!")  # HAS NO NAME !!!
print("Member value: {}".format(BugStatusClass.wont_fix))  # ==> 4

# Iterating through is not possible

actual_state = BugStatus.wont_fix
desired_state = BugStatus.fix_released

print("Equality:",
      actual_state == desired_state,       # ==> False
      actual_state == BugStatus.wont_fix)  # ==> True
print("Identity:",
      actual_state is desired_state,       # DO NOT USE IT, NEVER EVER
      actual_state is BugStatus.wont_fix)  # DO NOT USE IT, NEVER EVER

print(BugStatusClass)
