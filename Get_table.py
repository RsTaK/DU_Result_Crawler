def SemesterII(td_list):

    data_to_return = []

    Sem_I = td_list[3].text
    data_to_return.append(Sem_I)

    Sem_II = td_list[9].text
    data_to_return.append(Sem_II)

    Year_I = td_list[11].text
    data_to_return.append(Year_I)

    Sem_III = "N/A"
    data_to_return.append(Sem_III)

    Sem_IV = "N/A"
    data_to_return.append(Sem_IV)

    Year_II = "N/A"
    data_to_return.append(Year_II)

    Sem_V = "N/A"
    data_to_return.append(Sem_V)

    Sem_VI = "N/A"
    data_to_return.append(Sem_VI)

    Year_III = "N/A"
    data_to_return.append(Year_III)

    Total_Credit_Year_I = int(td_list[1].text) + int(td_list[7].text)
    data_to_return.append(Total_Credit_Year_I)

    Total_Credit_Point_Year_I = int(td_list[2].text) + int(td_list[8].text)
    data_to_return.append(Total_Credit_Point_Year_I)

    Total_Credit_Year_II = "N/A"
    data_to_return.append(Total_Credit_Year_II)

    Total_Credit_Point_Year_II = "N/A"
    data_to_return.append(Total_Credit_Point_Year_II)

    Total_Credit_Year_III = "N/A"
    data_to_return.append(Total_Credit_Year_III)

    Total_Credit_Point_Year_III = "N/A"
    data_to_return.append(Total_Credit_Point_Year_III)

    return data_to_return

def SemesterIV(td_list):

    data_to_return = []

    Sem_I = td_list[3].text
    data_to_return.append(Sem_I)

    Sem_II = td_list[9].text
    data_to_return.append(Sem_II)

    Year_I = td_list[11].text
    data_to_return.append(Year_I)

    Sem_III = td_list[15].text
    data_to_return.append(Sem_III)

    Sem_IV = td_list[21].text
    data_to_return.append(Sem_IV)

    Year_II = td_list[23].text
    data_to_return.append(Year_II)

    Sem_V = "N/A"
    data_to_return.append(Sem_V)

    Sem_VI = "N/A"
    data_to_return.append(Sem_VI)

    Year_III = "N/A"
    data_to_return.append(Year_III)

    Total_Credit_Year_I = int(td_list[1].text) + int(td_list[7].text)
    data_to_return.append(Total_Credit_Year_I)

    Total_Credit_Point_Year_I = int(td_list[2].text) + int(td_list[8].text)
    data_to_return.append(Total_Credit_Point_Year_I)

    Total_Credit_Year_II = int(td_list[13].text) + int(td_list[19].text)
    data_to_return.append(Total_Credit_Year_II)

    Total_Credit_Point_Year_II = int(td_list[14].text) + int(td_list[20].text)
    data_to_return.append(Total_Credit_Point_Year_II)

    Total_Credit_Year_III = "N/A"
    data_to_return.append(Total_Credit_Year_III)

    Total_Credit_Point_Year_III = "N/A"
    data_to_return.append(Total_Credit_Point_Year_III)

    return data_to_return

def SemesterVI(td_list):

    data_to_return = []

    Sem_I = td_list[3].text
    data_to_return.append(Sem_I)

    Sem_II = td_list[9].text
    data_to_return.append(Sem_II)

    Year_I = td_list[11].text
    data_to_return.append(Year_I)

    Sem_III = td_list[15].text
    data_to_return.append(Sem_III)

    Sem_IV = td_list[21].text
    data_to_return.append(Sem_IV)

    Year_II = td_list[23].text
    data_to_return.append(Year_II)

    Sem_V = td_list[27].text
    data_to_return.append(Sem_V)

    Sem_VI = td_list[33].text
    data_to_return.append(Sem_VI)

    Year_III = td_list[35].text
    data_to_return.append(Year_III)

    Total_Credit_Year_I = int(td_list[1].text) + int(td_list[7].text)
    data_to_return.append(Total_Credit_Year_I)

    Total_Credit_Point_Year_I = int(td_list[2].text) + int(td_list[8].text)
    data_to_return.append(Total_Credit_Point_Year_I)

    Total_Credit_Year_II = int(td_list[13].text) + int(td_list[19].text)
    data_to_return.append(Total_Credit_Year_II)

    Total_Credit_Point_Year_II = int(td_list[14].text) + int(td_list[20].text)
    data_to_return.append(Total_Credit_Point_Year_II)

    Total_Credit_Year_III = int(td_list[25].text) + int(td_list[31].text)
    data_to_return.append(Total_Credit_Year_III)

    Total_Credit_Point_Year_III = int(td_list[26].text) + int(td_list[32].text)
    data_to_return.append(Total_Credit_Point_Year_III)

    return data_to_return