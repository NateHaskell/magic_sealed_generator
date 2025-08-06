import pandas as pd
from parse_json import parse_json
from pack import generate_sealed_pool


def main():

    parse_json("cards.json")
    packs = generate_sealed_pool()

    # Fields to include in the excel file
    filter_fields = ["name", "oracle_text", "colors", "mana_cost", "cmc", "rarity", "scryfall_uri"]

    # Create dataframe 
    filtered_sealed_pool = []
    for item in packs:
        filtered_item = {field: item[field] for field in filter_fields}
        filtered_sealed_pool.append(filtered_item)

    df = pd.DataFrame(filtered_sealed_pool)

    # Create excel writer
    writer = pd.ExcelWriter("sealed_pool.xlsx", engine="xlsxwriter")

    df.to_excel(writer, sheet_name="Sheet1", index=False)

    workbook = writer.book
    worksheet = writer.sheets["Sheet1"]

    # Add formatting for text wrap, hyperlinks, and alignment
    oracle_text_format = workbook.add_format({"text_wrap": True,})
    hyperlink_format = workbook.add_format({"color": "blue", "underline": True})
    cell_alignment = workbook.add_format()
    cell_alignment.set_align("center")
    cell_alignment.set_align("bottom")

    # Apply formating to columns
    worksheet.set_column("A:A", 29, cell_alignment)
    worksheet.set_column("B:B", 65, oracle_text_format)
    worksheet.set_column("C:C", 17, cell_alignment)
    worksheet.set_column("D:D", 12, cell_alignment)
    worksheet.set_column("E:E", 12, cell_alignment)
    worksheet.set_column("F:F", 12, cell_alignment)
    worksheet.set_column("G:G", 75, hyperlink_format)

    writer.close()


if __name__ == "__main__":
    main()
