from bs4 import BeautifulSoup
import requests
import csv
import Get_table


def Du_Crawler(college_code, start_roll_no, last_roll_no, file_name):

    """print("You are required to enter the college code and range of roll no. whose data you want to get ")
    college_code = input("Enter the College Code  ")
    start_roll_no = input("Enter the roll no. you want to start with  ")
    last_roll_no = input("Enter the roll no. you want to end on  ")
    file_name = input("Enter the name for the output CSV file(with extension)  ")"""

    csv_file = open('static/Scrapped csv files/'+file_name, 'w')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(
        ['Exam Roll No.', 'Name', 'Course Name', 'College Name', 'Enrollment No.', 'Sem I', 'Sem II','Year I', 'Sem III'
            , 'Sem IV', 'Year II', 'Sem V', 'Sem VI', 'Year III', 'Total_Credit_Year_I', 'Total_Credit_Point_Year_I',
         'Total_Credit_Year_II', 'Total_Credit_Point_Year_II', 'Total_Credit_Year_III', 'Total_Credit_Point_Year_III'])

    flag = 0
    i = int(start_roll_no)
    while i <= int(last_roll_no):
        if flag <= 10:
            try:
                '''Some required data that we'll be sending with post request to the required url'''

                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
                }

                data = {
                    '__EVENTTARGET': '',
                    '__EVENTARGUMENT': '',
                    'ddlcollege': college_code,
                    'txtrollno': i,
                    'btnsearch': 'Print Score Card',
                    '__VIEWSTATEGENERATOR': '35D4F7A9',
                }

                '''Accessing the url and parsing the required data for our post request'''
                url = 'http://duresult.in/students/Combine_GradeCard.aspx'
                source = requests.get(url).text
                soup = BeautifulSoup(source, 'lxml')
                captcha_block = soup.find('div', id='UP1')
                data['txtcaptcha'] = captcha_block.img['src'].split('&')[0].split('=')[1]
                data['__EVENTVALIDATION'] = soup.find('input', id='__EVENTVALIDATION')['value']
                data['__VIEWSTATE'] = soup.find('input', id='__VIEWSTATE')['value']

                '''Created a session and pulled a post request with the required data'''
                session = requests.session()
                r = session.post(url=url, data=data, headers=headers)

                '''Time for some parsing'''
                Combine_GradeCard = BeautifulSoup(r.text, 'lxml')
                Info_Table = Combine_GradeCard.find('form')
                action = Info_Table['action'].split('?')[0]
                if action == 'Combine_GradeCardReport_CBCS.aspx':
                    givenSemester = Info_Table.find('span', id='lblsem').text
                    Exam_Roll_No = Info_Table.find('span', id='lblrollno').text
                    Name = Info_Table.find('span', id='lblname').text
                    Course_Name = Info_Table.find('span', id='lblcourse').text
                    College_Name = Info_Table.find('span', id='lblcollege').text
                    Enrollment_No = Info_Table.find('span', id='lbleno').text
                    try:
                        Result_Table = Info_Table.find('table', id='gv_sgpa')
                        td_list = Result_Table.find_all('td')
                        cases = {
                            'II': Get_table.SemesterII,
                            'IV': Get_table.SemesterIV,
                            'VI': Get_table.SemesterVI
                        }
                        fun = cases.get(givenSemester)
                        return_values = fun(td_list)
                    except Exception as e:
                        print('ER')
                        return_values = ['ER', 'ER', 'ER']

                    csv_writer.writerow(
                        [int(Exam_Roll_No), Name, Course_Name, College_Name, Enrollment_No, *return_values])
                    print('Data for roll no ' + str(i) + ' is fetched')
                    flag = 0
                    i += 1
                else:
                    print('Data for roll no ' + str(i) + ' is not found')
                    flag += 1
                    i += 1

            except Exception as e:
                print(str(e))
                pass
        else:
            break
    csv_file.close()
    print("Done")

"""
if __name__ == "__main__":
    print("Welcome To This Software")
    print("We provide you just one feature right now")
    print("Feature 1 : Scrape Result data from duresult.in and store data in a csv")
    options = input("Type I to select Feature 1")
    cases = {
        'I': Du_Crawler,
    }

    func = cases.get(options)
    func()
"""