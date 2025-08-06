# magic_sealed_generator
About:
This project simulates opening 6 Play Booster packs of Edge of Eternities like you would for a sealed event at your local game store.  You can use this to familiarize yourself with the cards from Edge of Eternities, think about what deck you would build with the given cards, or just open more packs for fun to see what you get. 

It uses a bulk data file downloaded from Scryfall, then parses that data to pull out the cards that can appear in Play Booster packs of the Edge of Eternities set.  Once the data has been parsed it simulates opening 6 packs and places information about the cards into an excel file.

Prerequisites:
You will need the following:
•	Python 3.12
•	openpyxl 3.1.5
•	pandas 2.3.1
•	xlsxwriter 3.2.5
•	Microsoft Excel 

Installation:
1.	Clone the repo: git clone https://github.com/NateHaskell/magic_sealed_generator
2.	Download the Default Cards JSON file from Scryfall: https://scryfall.com/docs/api/bulk-data
3.	Rename the file to cards.json and move it into the same directory as the project

Usage:
1.	Run main.py from the terminal (uv run main.py) – Note that the initial parsing of the data is a little slow since cards.json is a large file. Once the parsing is done generating the sealed pool takes around 10 seconds.
2.	Once that completes there will be a “sealed_pool.xlsx” file in your directory
3.	Open the “sealed_pool.xlsx” to view information about the cards you opened.  The scryfall_uri column contains the Scryfall link for each card so you can see the images of the cards.
4.	Close the excel file and run again to generate a new sealed pool




