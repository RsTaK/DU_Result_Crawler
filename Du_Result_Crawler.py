'''Importing necessary libraries'''

from bs4 import BeautifulSoup
import requests
import csv

'''DO some formality shit'''

print("You are required to enter the college code and range of roll no. whose data you want to get ")
college_code = input("Enter the College Code")
start_roll_no = input("Enter the roll no. you want to start with")
last_roll_no = input("Enter the roll no. you want to end on")
file_name = input("Enter the name for the output CSV file")

'''Create a CSV file named according to user'''

csv_file=open(file_name,'w')
csv_writer=csv.writer(csv_file)
#csv_writer.writerow(['Exam Roll No.','Name','Course Name','College Name','Enrollment No.','Sem I','Sem II','Sem III','Sem IV','Sem V','Year I','Year II'])


'''Functions that we will be using to fetch data of specific semesters'''


def SemesterI():
    Exam_Roll_No = Info_Table.find('span', id='lblrollno').text
    Name = Info_Table.find('span', id='lblname').text
    Course_Name = Info_Table.find('span', id='lblcourse').text
    College_Name = Info_Table.find('span', id='lblcollege').text
    Enrollment_No = Info_Table.find('span', id='lbleno').text
    Result_Table = Info_Table.find('table', id='gv_sgpa')
    td_list = Result_Table.find_all('td')
    Sem_I = td_list[3].text
    '''Writing the data to that CSV file'''
    csv_writer.writerow([int(Exam_Roll_No), Name, Course_Name, College_Name, Enrollment_No, Sem_I])
    print('Data for roll no ' + str(i) + 'is fetched')


def SemesterIII():
    Exam_Roll_No = Info_Table.find('span', id='lblrollno').text
    Name = Info_Table.find('span', id='lblname').text
    Course_Name = Info_Table.find('span', id='lblcourse').text
    College_Name = Info_Table.find('span', id='lblcollege').text
    Enrollment_No = Info_Table.find('span', id='lbleno').text
    Result_Table = Info_Table.find('table', id='gv_sgpa')
    td_list = Result_Table.find_all('td')
    Sem_I = td_list[3].text
    Sem_II = td_list[9].text
    Year_I = td_list[11].text
    Sem_III = td_list[15].text
    '''Writing the data to that CSV file'''
    csv_writer.writerow(
        [int(Exam_Roll_No), Name, Course_Name, College_Name, Enrollment_No, Sem_I, Sem_II, Sem_III, Year_I])
    print('Data for roll no ' + str(i) + 'is fetched')


def SemesterV():
    Exam_Roll_No = Info_Table.find('span', id='lblrollno').text
    Name = Info_Table.find('span', id='lblname').text
    Course_Name = Info_Table.find('span', id='lblcourse').text
    College_Name = Info_Table.find('span', id='lblcollege').text
    Enrollment_No = Info_Table.find('span', id='lbleno').text
    Result_Table = Info_Table.find('table', id='gv_sgpa')
    td_list = Result_Table.find_all('td')
    Sem_I = td_list[3].text
    Sem_II = td_list[9].text
    Year_I = td_list[11].text
    Sem_III = td_list[15].text
    Sem_IV = td_list[21].text
    Year_II = td_list[23].text
    Sem_V = td_list[27].text
    '''Writing the data to that CSV file'''
    csv_writer.writerow(
        [int(Exam_Roll_No), Name, Course_Name, College_Name, Enrollment_No, Sem_I, Sem_II, Sem_III, Sem_IV, Sem_V,
         Year_I, Year_II])
    print('Data for roll no ' + str(i) + 'is fetched')




'''Main Stuff'''
i = int(start_roll_no)
while i <= int(last_roll_no):

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
        data['__EVENTVALIDATION'] = eventvalblock = soup.find('input', id='__EVENTVALIDATION')['value']
        data['__VIEWSTATE'] = viewstateblock = soup.find('input', id='__VIEWSTATE')['value']

        '''Created a session and pulled a post request with the required data'''
        session = requests.session()
        r = session.post(url=url, data=data, headers=headers)



        '''Time for some parsing shit'''
        Combine_GradeCard = BeautifulSoup(r.text, 'lxml')
        Info_Table = Combine_GradeCard.find('form')
        action = Info_Table['action'].split('?')[0]
        if action =='Combine_GradeCardReport_CBCS.aspx':
            givenSemester = Info_Table.find('span',id='lblsem').text
            cases = {
                'I': SemesterI,
                'III': SemesterIII,
                'V': SemesterV
            }
            func = cases.get(givenSemester)
            func()
            i += 1
        else :
            print('Data for roll no ' + str(i) + 'is not found')
            i += 1
    except Exception as e:
        print(str(e))
        pass
'''Good kids always close the file'''
csv_file.close()
print("Done")

