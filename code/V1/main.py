from tkinter import filedialog      # Tcl/tk GUI 모듈
from tkinter import *               # Tcl/tk GUI 모듈
import re                           # 정규표현식 모듈
import sqlite3                      # Sqlite3


chatDaySelectRe = re.compile('\d{4}년\s\d{1,2}월\s\d{1,2}일\s[월화수목금토일]요일')      # 카카오톡에서 채팅했던 날짜선택하는 정규표현식
# 카카오톡은 채팅했던 날을 'xxxx년 xx월 x일 x요일'로 그 날 한번 기록
theChatSelectRe = re.compile('(?P<year>\d{4})[.]\s(?P<month>\d{1,2})[.]\s(?P<day>\d{1,2})[.]\s(?P<meridiem>[오전후]{2})\s(?P<hour>\d{1,2})[:](?P<minute>\d{1,2})[,]\s(?P<name>.+(?=\s:\s))\s:\s(?P<text>.+)', re.DOTALL)      # 햔제 체팅 내용을 분석하는 정규표현식
# group()번호별 해당되는 내용, 1:year, 2:month, 3:day, 4:meridiem, 5:hour, 6:minute, 7:name, 8:text
chatPeopleSelectRe = re.compile('[ ][:][ ]')

chatStatisticDics = {}   # 채팅 통계를 위한 딕셔너리를 생성, 여기에는 몇일날 카톡을 주고 받았는지 넣을 예정
chatStatisticLists = []    # 채팅 통계를 위한 리스트를 생성, 해당일에 누가 카톡을 얼마나 주고받았는지
chatPeopleLists = []    # 채팅한 사람을 기록하기 위한 리스트를 생

openText = Tk()     # tkinter 모듈을 사용하겠다고 선언
openText.fileName = filedialog.askopenfile(title = "choose your file")  # 파일 선택 후 경로 저장

print(openText.fileName.name)

openedText = open(openText.fileName.name, 'r')      # 선택한 파일의 경로로 채팅 파일 불러옴
textLines = openedText.readlines()      # 선택한 파일의 채팅을 모두 읽어 저장

i = 0
for textLine in textLines:      # 채팅 한줄 한줄 아래에 대입
    matchingCDSR = chatDaySelectRe.match(textLine)     # 채팅했던 날을 찾기
    matchingTCSR = theChatSelectRe.match(textLine)
    if matchingCDSR is not None:      # 채팅내용이 아닌 채팅했던 날 값이 맞는 경우
        i += 1
        chatStatisticDics[matchingCDSR.group()] = str(i) + 'day'     # 채팅했던 날짜를 딕셔너리에 추가
        print(matchingCDSR.group())
    elif matchingTCSR is not None:
        if matchingTCSR.group(7) in chatPeopleLists:
            nowListPosition = chatPeopleLists.index(matchingTCSR.group(7))

        else:
            chatPeopleLists.append(matchingTCSR.group(7))

    # elif bool(searching) == True:
    #     theChatDay = searching.group()[0:12]
    #     theChatTime = searching.group()[13:21]
    #     theChatContent = searching.group()[23:]
    #     theChatContentCheckPoint = chatPeopleSelectRe.search(theChatContent)
    #     print(theChatContentCheckPoint)
    #     if theChatContentCheckPoint is not None:
    #         theChatPerson = theChatContent[:theChatContentCheckPoint.start()] # 현재 채팅한 사람이 누구인지 찾음
    #         if theChatPerson in chatPeopleLists:
    #             continue
    #         else:
    #             chatPeopleLists.append(theChatPerson)
    #         theChatText = theChatContent[theChatContentCheckPoint.end():]


print(textLines)
openedText.close()

for chatStatisticDic in chatStatisticDics.items():      # 채팅 통계 딕셔너리를 하나씩 분해
    print(chatStatisticDic)
print(chatStatisticDics)
# print(theChatDay)
# print(theChatTime)
# print(theChatContent)
# print(theChatContentCheckPoint)
# print(theChatPerson)
# print(theChatText)
print(chatPeopleLists)
print(matchingTCSR.group(1))
print(matchingTCSR.group(2))
print(matchingTCSR.group(3))
print(matchingTCSR.group(4))
print(matchingTCSR.group(5))
print(matchingTCSR.group(6))
print(matchingTCSR.group(7))
print(matchingTCSR.group(8))
print(nowListPosition)

testcon = sqlite3.connect('test.db')

testcon.close()