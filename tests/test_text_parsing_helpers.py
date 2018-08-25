from unittest import TestCase

from BattleShip.text_parsing_helpers import remove_comments_and_whitespace, parse_initial_states_text_into_args_list, \
    group_list_arguments_by_3, parse_actions_text_into_arg


class TestSimulation(TestCase):

    def test_remove_comments_and_whitespace(self):
        input = "(0, 0, N) (9, 2, E)     // 2 ships in different locations"
        output = remove_comments_and_whitespace(input)

        self.assertEqual(output, "(0,0,N)(9,2,E)")

    def test_parse_initial_states_text_into_args_list(self):
        input = "(0, 0, N)(9, 2, E)"
        output = parse_initial_states_text_into_args_list(input)

        self.assertEqual(output, ['0', '0', 'N', '9', '2', 'E'])

    def test_group_list_arguments_by_3(self):
        input = ['0', '0', 'N', '9', '2', 'E']
        output = group_list_arguments_by_3(input)

        self.assertEqual(output, [['0', '0', 'N'], ['9', '2', 'E']])

    def test_parse_actions_text_into_arg(self):
        input = "(0, 0) MRMLMM"
        output = parse_actions_text_into_arg(input)

        self.assertEqual(output, ['0', '0', 'MRMLMM'])
