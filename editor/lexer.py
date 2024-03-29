from PyQt4.Qsci import QsciLexerCPP,QsciStyle,QsciScintilla,QsciLexerPython, QsciLexerJavaScript
from PyQt4.QtCore import QString
from PyQt4.QtGui import QFont, QColor
from globals import fontName, fontSize

class QsciLexerSquirrel(QsciLexerJavaScript):#QsciLexerPython
    words1 = [
         'base','break','case','catch','class','clone',
         'continue','const','default','delete','else','enum',
         'extends','for','foreach','function',' if',' in',
         'local','null','resume','return','switch','this',
         'throw','try','typeof','while','yield','constructor',
         'instanceof','true','false','static'
        ]
        
    words2 = [
         'init', 'dest', 'onLoad', 'onDispose', 'onGainedFocus','onMotionEvent',
         'onLostFocus','onUpdate','onFps','onKeyEvent','onSensorEvent',
         'onControlEvent','onDrawFrame','onError','onLowMemory','onNetCallBack'
        ]

    words3 = [
        'rawdelete', 'rawin', 'array', 'seterrorhandler', 'setdebughook',
        'enabledebuginfo', 'getroottable', 'setroottable', 'getconsttable',
        'setconsttable', 'assert', 'print', 'compilestring', 'collectgarbage',
        'type', 'getstackinfos', 'newthread', 'tofloat', 'tostring',
        'tointeger', 'tochar', 'weakref', 'slice', 'find', 'tolower',
        'toupper', 'len', 'rawget', 'rawset', 'clear', 'append', 'push',
        'extend', 'pop', 'top', 'insert', 'remove', 'resize', 'sort',
        'reverse', 'call', 'pcall', 'acall', 'pacall', 'bindenv', 'instance',
        'getattributes', 'getclass', 'getstatus', 'ref'
        ]
        
    def __init__(self,parent,colorStyle):
        #QsciLexerPython.__init__(self, parent)
        QsciLexerJavaScript.__init__(self, parent)
        self.parent = parent
        self.colorStyle = colorStyle
        self.plainFont = QFont()
        self.plainFont.setFamily(fontName)
        self.plainFont.setFixedPitch(True)
        self.plainFont.setPointSize(fontSize)
        self.boldFont = QFont(self.plainFont)
        self.boldFont.setBold(True)
        self.setFoldCompact(True)
        
        self.styles = [
          #index description color paper font eol 
          QsciStyle(0, QString("base"), self.colorStyle.color, self.colorStyle.paper, self.plainFont, True),
          QsciStyle(1, QString("comment"), QColor("#3f7f5f"), self.colorStyle.paper, self.plainFont, True),
          QsciStyle(4, QString("number"), QColor("#008000"), self.colorStyle.paper, self.plainFont, True),
          QsciStyle(5, QString("Keyword"), QColor("#7f0055"), self.colorStyle.paper, self.boldFont, True),
          QsciStyle(6, QString("String"), QColor("#7f0010"),self.colorStyle.paper, self.plainFont, True),
          #QsciStyle(10, QString("Operator"), QColor("#ff0000"), self.colorStyle.paper, self.plainFont, False),
          #QsciStyle(11, QString("Identifier"), QColor("#000000"), self.colorStyle.paper, self.plainFont, False),
          #QsciStyle(12, QString("CommentBlock"), QColor("#3f5fbf"), self.colorStyle.paper, self.plainFont, False),
          #QsciStyle(13, QString("UnclosedString"), QColor("#010101"), self.colorStyle.paper, self.plainFont, False),
          #QsciStyle(14, QString("HighlightedIdentifier"), QColor("#0000ff"), self.colorStyle.paper, self.plainFont, False),
          #QsciStyle(15, QString("Decorator"), QColor("#000000"), self.colorStyle.paper, self.plainFont, False),
        ]
        
    def setColorStyle(self,cs):
        self.colorStyle = cs
        for i in self.styles:
            i.setPaper(self.colorStyle.paper)
        self.styles[0].setColor(self.colorStyle.color)
        
        
    def language(self):
        return 'Squirrel'
    
    def foldCompact(self):
        return self._foldcompact

    def setFoldCompact(self, enable):
        self._foldcompact = bool(enable)

    def description(self, ix):
        for i in self.styles:
          if i.style() == ix:
            return i.description()
        return QString("")
    
    def defaultColor(self, ix):
        for i in self.styles:
          if i.style() == ix:
            return i.color()
        return QsciLexerCPP.defaultColor(self, ix)

    def defaultFont(self, ix):
        for i in self.styles:
          if i.style() == ix:
            return i.font()
        return QsciLexerCPP.defaultFont(self, ix)

    def defaultPaper(self, ix):
        for i in self.styles:
          if i.style() == ix:
            return i.paper()
        return QsciLexerCPP.defaultPaper(self, ix)

    def defaultEolFill(self, ix):
        for i in self.styles:
          if i.style() == ix:
            return i.eolFill()
        return QsciLexerCPP.defaultEolFill(self, ix)
    
'''
    def styleText(self, start, end):
        editor = self.editor()
        if editor is None:
            return
        SCI = editor.SendScintilla
        GETFOLDLEVEL = QsciScintilla.SCI_GETFOLDLEVEL
        SETFOLDLEVEL = QsciScintilla.SCI_SETFOLDLEVEL
        HEADERFLAG = QsciScintilla.SC_FOLDLEVELHEADERFLAG
        LEVELBASE = QsciScintilla.SC_FOLDLEVELBASE
        NUMBERMASK = QsciScintilla.SC_FOLDLEVELNUMBERMASK
        WHITEFLAG = QsciScintilla.SC_FOLDLEVELWHITEFLAG
        INDIC_SET = QsciScintilla.SCI_INDICSETSTYLE
        INDIC_SETCURRENT = QsciScintilla.SCI_SETINDICATORCURRENT
        INDIC_FILL = QsciScintilla.SCI_INDICATORFILLRANGE
        INDIC_CLEAR = QsciScintilla.SCI_INDICATORCLEARRANGE
        INDIC_START = QsciScintilla.SCI_INDICATORSTART
        INDIC_END = QsciScintilla.SCI_INDICATOREND
        
        # using indicator 7 with Boxed style
        SCI(INDIC_SET, 7 ,QsciScintilla.INDIC_BOX)
        SCI(INDIC_SETCURRENT, 7)
        
        set_style = self.setStyling
        source = ''
        if end > editor.length():
            end = editor.length()
        if end > start:
            source = bytearray(end - start)
            SCI(QsciScintilla.SCI_GETTEXTRANGE, start, end, source)
        if not source:
            return    
        #compact = self.foldCompact()
        index = SCI(QsciScintilla.SCI_LINEFROMPOSITION, start)
        self.startStyling(start, 0x1f)
        lineno = -1
        source = source.splitlines(True)
        for line in source:
            lineno += 1  
            length = len(line)
            if length == 0: #lol gg this had to be Zero
                return 
            if line.startswith('#'):
                newState = self.styles[1]
            else:
                pos = SCI(QsciScintilla.SCI_GETLINEENDPOSITION, index) - length + 1
                i = 0
                while i < length:
                    wordLength = 1
                    self.startStyling(i + pos, 0x1f)
                    newState = self.styles[0]
                    for word in self.words2:
                        if line[i:].startswith(word):
                            newState = self.styles[4]
                            wordLength = len(word)
                        
                    if chr(line[i]) in '0123456789':
                        newState = self.styles[4]
                        'startpos=3, length=3, use current indicator'
                        #SCI(INDIC_FILL,pos+line[i],1)
                    else:
                        if line[i:].startswith('"'):
                            newState = self.styles[1]
                            pos2 = line.find('"',i+1)
                            size = pos2 - i
                            if(size != 0 and pos2 != -1 ):
                                wordLength = size
                            #print "line: ",lineno, "pos: ",pos1, pos2
                        elif line[i:].startswith("'"):
                            newState = self.styles[1]
                            pos2 = line.find("'",i+1)
                            size = pos2 - i
                            if(size != 0 and pos2 != -1 ):
                                wordLength = size
                            #print "line: ",lineno, "pos: ",pos1, pos2
                                     
                        elif line[i:].startswith("class"):
                                newState = self.styles[5]
                                wordLength = 5
                        elif line[i:].startswith('function'):
                                newState = self.styles[5]
                                wordLength = 8
                        elif line[i:].startswith('enum'):
                                newState = self.styles[5]
                                wordLength = 4
                        elif line[i:].startswith(' if'):
                                newState = self.styles[4]
                                wordLength = 3
                        elif line[i:].startswith('#'): 
                                # get end of line position and set word length to that
                                newState = self.styles[4]
                                pos = SCI(QsciScintilla.SCI_GETLINEENDPOSITION, lineno)
                                wordLength = pos
                                #print "#end", pos
                        #elif line[i:].startswith(','):
                        #        newState = self.styles[1]
                        #        wordLength = 1
                    i += wordLength
                    set_style(wordLength, newState)
            if newState: 
                set_style(length, newState)
            pos = SCI(QsciScintilla.SCI_GETLINEENDPOSITION, index)
            index += 1
'''