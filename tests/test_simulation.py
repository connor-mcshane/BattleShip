from unittest import TestCase

from BattleShip.Simulation import Simulation


class TestSimulation(TestCase):
    """
    Test class to test our simulation, ideally we would of had more tests but there wasn't enough time
    """

    def test_run_simulation(self):
        import filecmp

        sim1 = Simulation("tests/test_files/input_1.txt", "tests/test_files/output_1.txt")
        sim1.run_simulation()

        self.assertTrue(filecmp.cmp("tests/test_files/output_1.txt", "tests/test_files/output_control_1.txt"))

        sim2 = Simulation("tests/test_files/input_2.txt", "tests/test_files/output_2.txt")
        sim2.run_simulation()




