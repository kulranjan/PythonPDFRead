import camelot

#tables = camelot.read_pdf("12 2021 120 Day OS Checks 05 18 21 to 08 07 21  143 2 pg-1.pdf")

tables = camelot.read_pdf("04 2022 120 Day OS Checks 09 10 21 to 12 08 21   179  2pg-1.pdf", flavor = 'stream')

tables[0].df[4][tables[0].df[4].str.strip().astype(bool)]

