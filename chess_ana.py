from converter.pgn_data import PGNData
import pandas as pd

# Convert PGN to CSV
pgn_data = PGNData("lichess_partial_2025-01.pgn")
result = pgn_data.export()
if result.is_complete:
    print("Files created!")
else:
    print("Files not created!")