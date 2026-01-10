

# in parenthesis the several strings are concatenated
print(
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
    "In orci nisl, aliquam ut sagittis sit amet, scelerisque id "
    "diam. Vivamus condimentum orci eget malesuada tincidunt. "
    "Vestibulum elementum congue erat, sit amet feugiat dolor "
    "porttitor non. Quisque erat leo, consectetur id pellentesque "
    "eget, mollis tempus eros. Morbi commodo, odio quis ultricies"
    " efficitur, elit urna fermentum ante, et suscipit "
)
# the \ concatenation can break easily


print(
    """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit.
    In orci nisl, aliquam ut sagittis sit amet, scelerisque id
    diam. Vivamus condimentum orci eget malesuada tincidunt.
    Vestibulum elementum congue erat, sit amet feugiat dolor
    porttitor non. Quisque erat leo, consectetur id pellentesque
    eget, mollis tempus eros. Morbi commodo, odio quis ultricies
    efficitur, elit urna fermentum ante, et suscipit
    """
)


def go_further_and_do():
    pass


something_very_long_condition_related_to_the_next_phase_1 = True
some_shorter_1 = True

something_very_long_condition_related_to_the_next_phase_2 = True
some_shorter_2 = True

something_very_long_condition_related_to_negative_of_the_next_phase_3 = False
some_shorter_3 = True

we_can_do_1 = something_very_long_condition_related_to_the_next_phase_1 and some_shorter_1
we_can_do_2 = something_very_long_condition_related_to_the_next_phase_2 or some_shorter_2
we_can_do_3 = not something_very_long_condition_related_to_negative_of_the_next_phase_3 and some_shorter_3

we_can_do = we_can_do_1 and we_can_do_2 and we_can_do_3

if we_can_do:
    go_further_and_do()

if (
    we_can_do_1
    and we_can_do_2
    and we_can_do_3
):
    go_further_and_do()


# Check the blank lines above: they separate the different logical parts
