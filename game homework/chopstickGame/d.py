import time
import os
import shutil
import 추출


# [ Notice ]
def notice(message):
    print('[ ' + time.strftime('%H:%M:%S') + ' ] [ Notice ] : ' + message)


# [ Warning ]
def warning(message):
    print('[ ' + time.strftime('%H:%M:%S') + ' ] [ Warning ] : ' + message)


# <tr>태그 자동 생성
def tabler(message):
    htmlwrite('        	<tr name="' + rjcodedata + ' ' + titledata + ' ' + originaltitledata + ' ' +
              makerdata + ' ' + genredata + '' + tagdata + '">\n                ' + message + '\n            </tr>\n')


# <td>태그 자동 생성
def tabled(message, style):
    htmlwrite('                <td' + style + '>\n                    ' +
              message + '\n                </td>\n')


# HTML 작성
def htmlwrite(message):
    global errormesbin
    try:
        html.write(message)
        makerhtml.write(message)
    except:
        if not errormesbin:
            warning(titledata + '게임의 제작 서클이 공백입니다')
            errormesbin = True


# 할 작업 선택
workchoice = input('할 작업을 정해주세요\n①추출 ②변환\n(잘못된 값 입력시 2번으로 작동)\n')

# 추출작업 실행
if workchoice == '1':
    추출.extract()

# 변환작업 실행
else:
    # maker 폴더 삭제 후 재생성 시도
    try:
        shutil.rmtree('maker')
        os.makedirs('maker')
    # maker 폴더가 처음부터 없었을 경우
    except:
        os.makedirs('maker')
    # 파일들 열기
    originaldata = open('../data.xml', encoding='UTF-8', mode='r')
    html = open('result.html', encoding='UTF-8', mode='w')
    gamename = open('gamename.txt', encoding='UTF-8', mode='r')
    gamelink = open('gamelink.txt', encoding='UTF-8', mode='r')
    makername = open('makername.txt', encoding='UTF-8', mode='r')
    makercode = open('makercode.txt', encoding='UTF-8', mode='r')
    reviewlink = open('reviewlink.txt', encoding='UTF-8', mode='r')
    # 기본 변수들 선언
    gamedic = {}
    reviewdic = {}
    makerdic = {}
    counter = 0
    taglist = ''
    commentlist = ''
    stringmode = 'NONE'
    genredata = ''
    # 게임 이름, 게임 링크, 리뷰 링크 리스트화
    while True:
        gn = gamename.readline()
        gl = gamelink.readline()
        rl = reviewlink.readline()
        gamedic[gn.replace('\n', '')] = gl.replace('\n', '')
        if rl[0:4] == 'http':
            reviewdic[gn.replace('\n', '')] = rl.replace('\n', '')
        else:
            reviewdic[gn.replace('\n', '')] = '후기글 없음'
        if not gn:
            break

    while True:
        mn = makername.readline()
        mc = makercode.readline()
        makerdic[mn.replace('\n', '')] = mc.replace('\n', '')
        if not mn:
            break

    imgtoogle = input('이미지 활성화 여부를 골라주세요\n①활성화 ②비활성화\n(잘못된 값 입력시 자동 비활성화)\n')
    if imgtoogle != '1' and imgtoogle != '2':
        imgtoogle = '2'
    html.write('<!DOCTYPE=html>\n<meta charset=\"UTF-8\">\n<head>\n')
    html.write(
        '    <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.4.2/jquery.min.js"></script>\n	<script type="text/javascript">\n	function filter(){\n	if($("#txtFilter").val()=="")\n	$("#languageTBody tr").css("display","");\n	else{\n	$("#languageTBody tr").css("display","none");\n	$("#languageTBody tr[name*=\'\"+$("#txtFilter").val()+\"\']").css("display","");\n	}\n	return false;\n	}\n	</script>\n')
    html.write('    <title>게임 데이터베이스 v6.0</title>\n')
    html.write('</head>\n<body">\n')
    html.write(
        '	<p>검색 : <input type="text" id="txtFilter" onkeyup="{filter();return false}" onkeypress="javascript:if(event.keyCode==13){ filter(); return false;}"></p>\n')
    html.write(
        '	<p>(아직은 개발중이라 제목, 원제목, 서클, 장르, 태그가 동시에 검색됩니다 또한 영어의 경우 대, 소문자를 구분합니다...)</p>\n')
    html.write(
        '	<table border=2 style="font-size:12px; border-collapse:collapse;">\n')
    html.write(
        '        <thead>\n            <tr>\n                <td colspan=3 style="text-align:center;">게임 데이터베이스 v6.0</td>\n            </tr>\n        </thead>\n')
    while True:
        line = originaldata.readline()
        if not line:
            break
        if line.replace(' ', '')[0:8] == '<rjCode>':  # RJ코드 저장
            rjcodedata = line.split('>')[1].split('<')[0]
            errormesbin = False
        if line.replace(' ', '')[0:9] == '<rjCode/>':  # RJ코드가 없을 때
            rjcodedata = 'NONE'
        if line.replace(' ', '')[0:7] == '<title>':  # 제목 저장
            titledata = line.split('>')[1].split('<')[0]
            linkdata = (gamedic[titledata])  # 링크 저장
            if linkdata == 'NONE':  # 링크가 없을 때
                warning(titledata + ' : 해당 링크 없음')
        if line.replace(' ', '')[0:12] == '<title_orig>':  # 원제목 저장
            originaltitledata = line.split('>')[1].split('<')[0]
        if line.replace(' ', '')[0:7] == '<maker>':  # 서클명 저장
            makerdata = line.split('>')[1].split('<')[0]
            if os.path.isfile(
                    'maker/' + makerdata.replace('/', '／').replace('*', '＊').replace('?', '？') + '.html'):
                # 파일이 존재할 경우
                makerhtml = open('maker/' + makerdata.replace('/', '／').replace(
                    '*', '＊').replace('?', '？') + '.html', encoding='UTF-8', mode='a')
            else:
                # 파일이 존재하지 않을 경우
                makerhtml = open('maker/' + makerdata.replace('/', '／').replace(
                    '*', '＊').replace('?', '？') + '.html', encoding='UTF-8', mode='a')
                makerhtml.write(
                    '<!DOCTYPE=html>\n<meta charset=\"UTF-8\">\n<head>\n</head>\n<body>\n	<table border=2 style="font-size:12px; border-collapse:collapse;">\n')
        if line.replace(' ', '')[0:7] == '<genre>':  # 장르 저장
            genredata = line.split('>')[1].split('<')[0]
        if genredata == '':
            genredata = '장르 없음'
        if line.replace(' ', '')[0:8] == '<rating>':  # 평점 저장
            ratingdata = line.split('>')[1].split(
                '<')[0].replace('-1', '평점 없음')
        if line.replace(' ', '')[0:9] == '<tagList>':  # 태그 수집 시작
            stringmode = 'tag'
        if stringmode == 'tag':
            if line.replace(' ', '')[0:8] == '<string>':  # 태그 수집
                taglist = taglist + ', ' + line.split('>')[1].split('<')[0]
        if line.replace(' ', '')[0:10] == '</tagList>':  # 태그 저장
            tagdata = taglist[1:]
            taglist = ''
            stringmode = 'NONE'
        if line.replace(' ', '')[0:10] == '<tagList/>':  # 태그 없을 경우
            tagdata = ' 태그 없음'
        if line.replace(' ', '')[0:13] == '<commentList>':  # 코멘트 수집 시작
            stringmode = 'comment'
        if stringmode == 'comment':
            if line.replace(' ', '')[0:8] == '<string>':  # 코멘트 수집
                commentlist = commentlist + ', ' + line.split('>')[1].split('<')[0]
        if line.replace(' ', '')[0:14] == '</commentList>':  # 코멘트 저장
            commentdata = commentlist[1:].replace('&lt;br&gt;', '<br>')
            commentlist = ''
            stringmode = 'NONE'
        if line.replace(' ', '')[0:14] == '<commentList/>':  # 코멘트 없을 경우
            commentdata = '특이사항 없음'
        if line.replace(' ', '')[0:9] == '<imgData>':  # 이미지 저장
            imgdata = line.split('>')[1].split('<')[0]
        if line.replace(' ', '')[0:9] == '<>':  # 이미지 저장
            imgdata = line.split('>')[1].split('<')[0]
        if line.replace(' ', '')[0:11] == '</GameData>':  # HTML 작성 시작
            htmlwrite('	    <tbody id="languageTBody">\n')
            htmlwrite('	        <tr name="' + rjcodedata + ' ' + titledata + ' ' +
                      originaltitledata + ' ' + makerdata + ' ' + genredata + '' + tagdata + '">\n')
            # 이미지가 있을 때
            if imgdata != '' and imgtoogle == '1':
                tabled('<img style="width:224px; height:168px;" src="data:image:jpeg;base64,' +
                       imgdata + '">', ' rowspan=5')
            # 이미지가 없거나 이미지가 비활성화되었을 때
            else:
                htmlwrite(
                    '                <td style="width:224px; height:168px;" rowspan=5></td>\n')
            if rjcodedata == 'NONE':  # RJ코드가 없을 때
                htmlwrite('                <td>NULL</td>\n')
            else:
                tabled('<a href=https://www.dlsite.com/maniax/work/=/product_id/' +
                       rjcodedata + '>' + rjcodedata + '</a>', '')
            try:
                if makerdic[makerdata] != 'NONE' and makerdic[makerdata][0:2] == 'RG' or makerdic[makerdata][
                                                                                         0:2] == 'VG':
                    tabled(
                        '<a href=maker/' + makerdata.replace('/', '／').replace('*', '＊').replace('?', '？').replace(' ',
                                                                                                                   '%20') + '.html>' +
                        makerdata + '</a> <a href=https://www.dlsite.com/maniax/circle/profile/=/maker_id/' + makerdic[
                            makerdata] + '>(DL)</a>', '')
                else:
                    warning(titledata + ' 게임의 제작 서클 코드가 없습니다')
                    tabled('<a href=maker/' + makerdata.replace('/', '／').replace('*', '＊').replace(
                        '?', '？').replace(' ', '%20') + '.html>' + makerdata + '</a>', '')
            except:
                tabled('<a href=maker/' + makerdata.replace('/', '／').replace('*',
                                                                              '＊').replace('?', '？').replace(' ',
                                                                                                             '%20') + '.html>' + makerdata + '</a>',
                       '')
            htmlwrite('            </tr>\n')
            tabler('<td>' + titledata +
                   '</td>\n                <td>' + ratingdata + '</td>')
            tabler('<td>' + originaltitledata +
                   '</td>\n                <td>' + commentdata + '</td>')
            tabler('<td colspan=2>' + genredata + ' /' + tagdata + '</td>')
            # 매칭되는 링크가 있을 때
            if linkdata[0:5] == 'https':
                htmlwrite('            <tr name="' + rjcodedata + ' ' + titledata + ' ' +
                          originaltitledata + ' ' + makerdata + ' ' + genredata + '' + tagdata + '">\n')
                tabled('<a href=' + linkdata + '>' + linkdata + '</a>', '')
                htmlwrite('                <td>' +
                          reviewdic[titledata] + '</td>\n')
                htmlwrite('            </tr>\n')
            # 매칭되는 링크가 없을 때
            else:
                htmlwrite('            <tr name="' + rjcodedata + ' ' + titledata + ' ' +
                          originaltitledata + ' ' + makerdata + ' ' + genredata + '' + tagdata + '">\n')
                htmlwrite('                <td>링크 없음</td>\n')
                htmlwrite('                <td>' +
                          reviewdic[titledata] + '</td>\n')
                htmlwrite('            </tr>\n')
            htmlwrite('        </tbody>\n')
            notice(rjcodedata + ' / ' + titledata + ' 정리 완료')
            rjcodedata = ''
            titledata = ''
            originaltitledata = ''
            makerdata = ''
            genredata = ''
            ratingdata = ''
            tagdata = ''
            taglist = ''
            imgdata = ''
            makerhtml.close()
    html.write('    </table>\n</body>')
    originaldata.close()
    html.close()
    gamename.close()
    gamelink.close()
    makername.close()
    makercode.close()
    reviewlink.close()
    notice('Finish')  # 종료
    os.system('pause')
