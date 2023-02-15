#!/usr/bin/env python

"""Script used to test the network with batfish"""

import os
from pybatfish.client.commands import *
from pybatfish.question import load_questions
from pybatfish.client.asserts import (
    assert_no_incompatible_bgp_sessions,
    assert_no_incompatible_ospf_sessions,
    assert_no_unestablished_bgp_sessions,
)
from rich.console import Console

NET = os.environ.get("net")

console = Console(color_system="truecolor")


def test_bgp_compatibility(snap):
    """Testing for incompatible BGP sessions"""
    console.print(
        ":white_exclamation_mark: [bold yellow]Testing for incompatible BGP sessions[/bold yellow] :white_exclamation_mark:"
    )
    assert_no_incompatible_bgp_sessions(
        snapshot=snap,
    )
    console.print(
        ":green_heart: [bold green]All BGP sessions compatible![/bold green] :green_heart:"
    )


def test_ospf_compatibility(snap):
    """Testing for incompatible OSPF sessions"""
    console.print(
        ":white_exclamation_mark: [bold yellow]Testing for incompatible OSPF sessions[/bold yellow] :white_exclamation_mark:"
    )
    assert_no_incompatible_ospf_sessions(
        snapshot=snap,
    )
    console.print(
        ":green_heart: [bold green]All OSPF sessions compatible![/bold green] :green_heart:"
    )


def test_bgp_unestablished(snap):
    """Testing for BGP sessions that are not established"""
    console.print(
        ":white_exclamation_mark: [bold yellow]Testing for unestablished BGP sessions[/bold yellow] :white_exclamation_mark:"
    )
    assert_no_unestablished_bgp_sessions(
        snapshot=snap,
    )
    console.print(
        ":green_heart: [bold green]All BGP sessions are established![/bold green] :green_heart:"
    )

def main():
    """init all the things"""
    NETWORK_NAME = "ATD_NET"
    SNAPSHOT_NAME = "snapshot00"
    SNAPSHOT_DIR = f"./atd-inventory/{NET}/intended/snapshots/"
    bf_session.host = "batfish"
    bf_set_network(NETWORK_NAME)
    init_snap = bf_init_snapshot(SNAPSHOT_DIR, name=SNAPSHOT_NAME, overwrite=True)
    load_questions()
    test_bgp_compatibility(init_snap)
    test_ospf_compatibility(init_snap)
    test_bgp_unestablished(init_snap)


if __name__ == "__main__":
    main()