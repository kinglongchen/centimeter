# coding=utf-8
from datetime import date,timedelta
import mimetypes
from common.config.Config import Config

__author__ = 'chenjinlong'
from email import encoders, MIMEBase
from email import MIMEMultipart
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib


class EmailTool(object):
    def __init__(self):
        self.msg = MIMEMultipart.MIMEMultipart()


    def start(self, smtpServer, fromAddrMap, password, port=25):
        self.server = smtplib.SMTP(smtpServer, port)
        self.server.set_debuglevel(1)
        self.fromAddr = fromAddrMap["fromAddr"]
        self.fromAddrUserName = fromAddrMap["userName"]
        self.server.login(self.fromAddr, password)

    def _format_addr(self, str):
        name, addr = parseaddr(str)
        return formataddr((Header(name, 'utf-8').encode(),
                           addr.encode('utf-8') if isinstance(addr, unicode) else addr))

    def attachText(self, text):
        # 邮件正文是MIMEText:
        self.msg.attach(MIMEText(self.__decode(text), 'plain', 'utf-8'))

    def attachFile(self, fileName):
        filePathName = fileName
        fileName = self.__pickFileName(fileName)
        ctype, subtype = self.__guessType(filePathName)

        with open(filePathName, 'rb') as f:
            # 设置附件的MIME和文件名，这里是png类型:
            mime = MIMEBase.MIMEBase(ctype, subtype, filename=self.__decode(fileName))
            # 加上必要的头信息:
            mime.add_header('Content-Disposition', 'attachment', filename="%s" %Header(self.__decode(fileName),"gb2312"))
            mime.add_header('Content-ID', '<0>')
            mime.add_header('X-Attachment-Id', '0')
            # 把附件的内容读进来:
            mime.set_payload(f.read())
            # 用Base64编码:
            encoders.encode_base64(mime)
            # 添加到MIMEMultipart:
            self.msg.attach(mime)

    def __pickFileName(self, filePathName):
        fileName = filePathName if not "/" in filePathName else filePathName.split("/")[-1]
        return fileName

    def __guessType(self, fileName):
        # 构造MIMEBase对象做为文件附件内容并附加到根容器
        ctype, encoding = mimetypes.guess_type(fileName)
        if ctype is None or encoding is not None:
            ctype = 'application/octet-stream'
        maintype, subtype = ctype.split('/', 1)
        return ctype, subtype

    def send(self, subject, toAddrMap):
        toAddrListStr = ",".join([self._format_addr('%s <%s>' % (self.__decode(k), self.__decode(v))) for k, v in toAddrMap.iteritems()])
        # 邮件对象:
        self.msg['From'] = self._format_addr('%s <%s>' % (self.__decode(self.fromAddrUserName), self.__decode(self.fromAddr)))
        self.msg['To'] = toAddrListStr
        self.msg['Subject'] = Header('%s' % self.__decode(subject), 'utf-8').encode()
        self.server.sendmail(self.fromAddr, [v for v in toAddrMap.values()], self.msg.as_string())

    def stop(self):
        self.server.quit()

    def __decode(self,str):
        return str.decode('utf-8') if not isinstance(str,unicode) else str

    @classmethod
    def sendMail(cls, fileName,toAddrMap=Config.lopToAddrMap,
                 emailTextFilePath=Config.defaultEmailTextFilePath,
                 subject=None):
        emailTool = cls()
        emailTool.start(Config.smtpServer, Config.fromAddrMap, Config.emailPassword)


        if fileName:
            file = open(emailTextFilePath,"r")
            emialText = file.read()
            emailTool.attachText(emialText)
            emailTool.attachFile(fileName)
        else:
            file = open(Config.noReportEmailTextFilePath,"r")
            emialText = file.read()
            emailTool.attachText(emialText)
        subjectName = (date.today() - timedelta(days=1)).strftime("%Y年%m月%d日报表");
        if subject is not None:
            subjectName = subject + subjectName
        emailTool.send(subjectName, toAddrMap)
        emailTool.stop()

    @classmethod
    def sendLopMail(cls,fileName):
        cls.sendMail(fileName,toAddrMap=Config.lopToAddrMap,emailTextFilePath=Config.lopEmailTextFilePath,subject="全车件")

    @classmethod
    def sendKingDeeReportMail(cls,fileName,):
        cls.sendMail(fileName,toAddrMap=Config.kingDeeToAddrMap,subject="金蝶号数据")



if __name__ == "__main__":
    file = open(Config.defaultEmailTextFilePath,"r")
    emialText = file.read()
    print emialText