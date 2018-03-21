import pytest

from hr import cli

data = [
          {
            "name": "kevin",
            "groups": ["wheel", "dev"],
            "password": "$6$HXdlMJqcV8LZ1DIF$LCXVxmaI/ySqNtLI6b64LszjM0V5AfD.ABaUcf4j9aJWse2t3Jr2AoB1zZxUfCr8SOG0XiMODVj2ajcQbZ4H4/"
          },
          {
            "name": "lisa",
            "groups": ["wheel"],
            "password": "$6$HXdlMJqcV8LZ1DIF$LCXVxmaI/ySqNtLI6b64LszjM0V5AfD.ABaUcf4j9aJWse2t3Jr2AoB1zZxUfCr8SOG0XiMODVj2ajcQbZ4H4/"
          },
          {
            "name": "jim",
            "groups": [],
            "password": "$6$HXdlMJqcV8LZ1DIF$LCXVxmaI/ySqNtLI6b64LszjM0V5AfD.ABaUcf4j9aJWse2t3Jr2AoB1zZxUfCr8SOG0XiMODVj2ajcQbZ4H4/"
          }
        ]

@pytest.fixture
def parser():
    return cli.create_parser()

def test_parser_without_arguments(parser):
    """
    Without a specified argument the parser will exit
    """
    with pytest.raises(SystemExit):
        parser.parse_args([])

def test_parser_with_path_argument(parser):
    """
    The parser will not exit if it receives a path as an argument
    """
    args = parser.parse_args(['some/path/test.json'])
    assert args.path == 'some/path/test.json'

def test_parser_with_export_flag(parser):
    """
    The export value is set to True if the --export flag is given, otherwise is
    equal to False
    """
    args = parser.parse_args(['--export', 'some/path/test.json'])
    assert args.export == True

    args = parser.parse_args(['some/path/test.json'])
    assert args.export == False
