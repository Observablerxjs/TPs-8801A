import argparse
from Shared.Parameters import Parameters


class ArgParser:
    @staticmethod
    def parse():
        parser = argparse.ArgumentParser(
            description='Relay between Oronos rocket & clients (PC/tablets).')

        parser.add_argument('-b', '--baudrate', type=int,
                            help='Baudrate of the serial port')
        parser.add_argument('-c', '--connector_type',
                            help='Data source', choices=['serial', 'simulation'], default='simulation')
        parser.add_argument('-f', '--connector_file',
                            help='Connector type. COM serial port or CSV file')
        parser.add_argument('-s', '--server', type=int, default=3000,
                            help='Activates a server listening on a certain port')
        parser.add_argument('-r', '--rocket', default='11_valkyrieM2.xml',
                            help='XML configuration file')
        parser.add_argument('-m', '--map', default='spaceport_america',
                            help='Name of the map in Config/Other/Maps.xml')
        return parser.parse_args()