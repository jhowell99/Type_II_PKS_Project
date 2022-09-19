import pandas as pd

eight_all_clades_csv = pd.read_csv(
    "C16_all_clade_actinorhodin_ConSurf/grades_altered.txt", sep="\t"
)
eight_single_clade_csv = pd.read_csv(
    "C16_clade_actinorhodin_ConSurf/grades_altered.txt", sep="\t"
)
nine_ten_all_clades_csv = pd.read_csv(
    "C18_20_all_clades_warkmycin_ConSurf/grades_altered.txt", sep="\t"
)
nine_ten_single_clade_csv = pd.read_csv(
    "C18_20_clade_warkmycin_ConSurf/grades_altered.txt", sep="\t"
)
twelve_thirteen_all_clades_csv = pd.read_csv(
    "C24_26_all_clades_enduracylinone_ConSurf/grades_altered.txt", sep="\t"
)
twelve_thirteen_single_clade_csv = pd.read_csv(
    "C24_26_clade_enduracyclinone_ConSurf/grades_altered.txt", sep="\t"
)


def colour_score_difference_func(single_df, all_df, text_file_name):
    single_df["color_score_difference"] = single_df["COLOR"] - all_df["COLOR"]

    resi_number = []

    for i1 in range(0, len(single_df)):
        res_string = str(single_df.iloc[i1, 0])

        resi_number.append(res_string)

    color_diff_number = []

    for i3 in range(0, len(single_df)):
        color_string = str(single_df.loc[i3, "color_score_difference"])

        color_diff_number.append(color_string)

    path = text_file_name

    with open(path, "w") as file:
        for i2 in range(0, len(resi_number)):
            if color_diff_number[i2] == "8":
                color = "nothing1"
                file.write("sele chain C and resi " + resi_number[i2] + "\n")
                file.write("color " + color + ", sele" + "\n")
            elif color_diff_number[i2] == "7":
                color = "nothing2"
                file.write("sele chain C and resi " + resi_number[i2] + "\n")
                file.write("color " + color + ", sele" + "\n")
            elif color_diff_number[i2] == "6":
                color = "nothing3"
                file.write("sele chain C and resi " + resi_number[i2] + "\n")
                file.write("color " + color + ", sele" + "\n")
            elif color_diff_number[i2] == "5":
                color = "nothing4"
                file.write("sele chain C and resi " + resi_number[i2] + "\n")
                file.write("color " + color + ", sele" + "\n")
            elif color_diff_number[i2] == "4":
                color = "nothing5"
                file.write("sele chain C and resi " + resi_number[i2] + "\n")
                file.write("color " + color + ", sele" + "\n")
            elif color_diff_number[i2] == "3":
                color = "nothing6"
                file.write("sele chain C and resi " + resi_number[i2] + "\n")
                file.write("color " + color + ", sele" + "\n")
            elif color_diff_number[i2] == "2":
                color = "nothing7"
                file.write("sele chain C and resi " + resi_number[i2] + "\n")
                file.write("color " + color + ", sele" + "\n")
            elif color_diff_number[i2] == "1":
                color = "nothing8"
                file.write("sele chain C and resi " + resi_number[i2] + "\n")
                file.write("color " + color + ", sele" + "\n")
            elif color_diff_number[i2] == "0":
                color = "nothing9"
                file.write("sele chain C and resi " + resi_number[i2] + "\n")
                file.write("color " + color + ", sele" + "\n")
            elif color_diff_number[i2] == "-1":
                color = "nothing10"
                file.write("sele chain C and resi " + resi_number[i2] + "\n")
                file.write("color " + color + ", sele" + "\n")
            elif color_diff_number[i2] == "-2":
                color = "nothing11"
                file.write("sele chain C and resi " + resi_number[i2] + "\n")
                file.write("color " + color + ", sele" + "\n")
            elif color_diff_number[i2] == "-3":
                color = "nothing12"
                file.write("sele chain C and resi " + resi_number[i2] + "\n")
                file.write("color " + color + ", sele" + "\n")
            elif color_diff_number[i2] == "-4":
                color = "nothing13"
                file.write("sele chain C and resi " + resi_number[i2] + "\n")
                file.write("color " + color + ", sele" + "\n")
            elif color_diff_number[i2] == "-5":
                color = "nothing14"
                file.write("sele chain C and resi " + resi_number[i2] + "\n")
                file.write("color " + color + ", sele" + "\n")
            elif color_diff_number[i2] == "-6":
                color = "nothing15"
                file.write("sele chain C and resi " + resi_number[i2] + "\n")
                file.write("color " + color + ", sele" + "\n")
            elif color_diff_number[i2] == "-7":
                color = "nothing16"
                file.write("sele chain C and resi " + resi_number[i2] + "\n")
                file.write("color " + color + ", sele" + "\n")
            elif color_diff_number[i2] == "-8":
                color = "nothing17"
                file.write("sele chain C and resi " + resi_number[i2] + "\n")
                file.write("color " + color + ", sele" + "\n")


clade_list_single = [
    eight_single_clade_csv,
    nine_ten_single_clade_csv,
    twelve_thirteen_single_clade_csv,
]
clade_list_all = [
    eight_all_clades_csv,
    nine_ten_all_clades_csv,
    twelve_thirteen_all_clades_csv,
]
output_name = [
    "eight_clade_color.txt",
    "nine_ten_clade_color.txt",
    "twelve_thirteen_clade_color.txt",
]


for i in range(0, 3):
    colour_score_difference_func(
        clade_list_single[i], clade_list_all[i], output_name[i]
    )
