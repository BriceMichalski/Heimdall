"""Cli interface for Heimdall"""
import click
from loguru import logger

from heimdall.HeimdallServer import HeimdallServer

server = HeimdallServer()

@click.group()
def main():
    """Virtualization API"""
    
@main.command()
def start():
    """Start heimdall server"""
    server.run()
    
if __name__ == "__main__":
    main()