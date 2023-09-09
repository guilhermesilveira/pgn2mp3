from pgn import parse_chess

# Test
s = "1. e4 e5 2. Nc3 Nc6 { C25 Vienna Game: Max Lange Defense } 3. Bc4 Nf6 (3... Bc5 4. Qg4 { Vienna Copycat Variation }) 4. d3 { Vienna Hybrid } 4... Na5 (4... Bc5) 5. Nge2 Nxc4 6. dxc4 Bc5 7. Qd3 { Vienna Open Variation } *"
parse_chess(s, core_key="vienna")
