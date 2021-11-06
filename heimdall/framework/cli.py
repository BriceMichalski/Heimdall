"""Cli interface for Heimdall"""
import click
import pyfiglet

from heimdall.framework.HeimdallServer import HeimdallServer

server = HeimdallServer()

@click.group()
def main():
    """Virtualization API"""
    
@main.command()
def start():
    banner = pyfiglet.figlet_format("Heimdall")
    print(banner)
    print(" * Starting heimdall server")
    """Start heimdall server"""
    server.run()
    
if __name__ == "__main__":
    main()