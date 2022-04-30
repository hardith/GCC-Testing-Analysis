import os
import re
# from unittest import skip
import xlsxwriter
import pandas as pd
import pip

pip.main(["install", "openpyxl"])

directory = "../gcc-11.2.0"

def main():
    # cpt = sum([len(files) for r, d, files in
    #            os.walk("directory")])
    # print("Number of files", cpt)

    
    # try:

    workbook = xlsxwriter.Workbook('csv-data/stagedData.xlsx')
    worksheet = workbook.add_worksheet()

    worksheet.write('A1', 'Assert')
    worksheet.write('B1', 'gcc_assert')
    worksheet.write('C1', 'gcc_checking_assert')
    worksheet.write('D1', 'ASSERT_ALWAYS')
    worksheet.write('E1', 'FFI_ASSERT')
    worksheet.write('F1', 'CHECK')
    worksheet.write('G1', '_Static_assert')
    worksheet.write('H1', 'VERIFY')
    worksheet.write('I1', 'DEBUG')
    worksheet.write('J1', 'path')

    rowIndex = 2
    for root, subdirectories, files in os.walk(directory):
        for subdirectory in subdirectories:
            folder = root + '/' + subdirectory
        for file in files:
            try:
                count1 = 0
                count2 = 0
                count3 = 0
                count4 = 0
                count5 = 0
                count6 = 0
                count7 = 0
                count8 = 0
                count9 = 0
                print(file)
                path = root + '/' + file
                print(path)
                inputFile = open(path, 'r', encoding="utf8")
                lines = inputFile.readlines()
                for line in lines:
                    if re.match(r"^[' ']*assert", line):
                        count1 = count1 + 1
                    if re.match(r"^[' ']*gcc_assert", line):
                        count2 = count2 + 1
                    if re.match(r"^[' ']*gcc_checking_assert", line):
                        count3 = count3 + 1
                    if re.match(r"^[' ']*ASSERT_ALWAYS", line):
                        count4 = count4 + 1
                    if re.match(r"^[' ']*FFI_ASSERT", line):
                        count5 = count5 + 1
                    if re.match(r"^[' ']*CHECK", line):
                        count6 = count6 + 1
                    if re.match(r"^[' ']*_Static_assert", line):
                        count7 = count7 + 1
                    if re.match(r"^[' ']*VERIFY", line):
                        count8 = count8 + 1
                    if re.match(r"^[' ']*DEBUG", line):
                        count9 = count9 + 1
                # print("assert statements", count1) if count1 > 0 else skip
                # print("gcc_assert statements", count2) if count2 > 0 else skip
                # print("gcc_checking_assert statements", count3) if count3 > 0 else skip
                # print("ASSERT_ALWAYS statements", count4) if count4 > 0 else skip
                # print("FFI_ASSERT statements", count5) if count5 > 0 else skip
                # print("CHECK statements", count6) if count6 > 0 else skip
                # print("_Static_assert statements", count7) if count7 > 0 else skip
                # print("VERIFY statements", count8) if count8 > 0 else skip

                worksheet.write('A' + str(rowIndex), count1)
                worksheet.write('B' + str(rowIndex), count2)
                worksheet.write('C' + str(rowIndex), count3)
                worksheet.write('D' + str(rowIndex), count4)
                worksheet.write('E' + str(rowIndex), count5)
                worksheet.write('F' + str(rowIndex), count6)
                worksheet.write('G' + str(rowIndex), count7)
                worksheet.write('H' + str(rowIndex), count8)
                worksheet.write('I' + str(rowIndex), count9)
                worksheet.write('J' + str(rowIndex), path)

            except:
                print("error")

            rowIndex += 1
    workbook.close()

    path = 'csv-data/stagedData.xlsx'
    xlsx = pd.ExcelFile(path)
    df = pd.read_excel(xlsx, 'Sheet1')
    df.drop(df.index[(df['Assert'] == 0) & (df['gcc_assert'] == 0) & (df['gcc_checking_assert'] == 0)
                     & (df['ASSERT_ALWAYS'] == 0) & (df['FFI_ASSERT'] == 0) & (df['CHECK'] == 0) & (
                                 df['_Static_assert'] == 0) & (
                             df['VERIFY'] == 0) & (df['DEBUG'] == 0)], inplace=True)

    df.to_csv('csv-data/stagedData_Main.csv')
    print("----------------done--------------------------")


if __name__ == "__main__":
    main()
