import argparse
from BattleShip.Simulation import Simulation

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Run simulation given an input text file")
    parser.add_argument("input_file", type=str, help="input text file")
    parser.add_argument("output_file", type=str, help="output text file")
    args = parser.parse_args()

    sim = Simulation(args.input_file, args.output_file)
    sim.run_simulation()
