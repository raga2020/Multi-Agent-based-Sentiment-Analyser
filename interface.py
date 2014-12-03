from java.awt import *
from java.awt.GridBagConstraints import *
from javax.swing import *
from javax.swing.border import *
from java.lang import *
from java.sql import *

file_count = 0

class Main(JFrame):
    def __init__(self):
        JFrame.__init__(self,
                        'Hello',
                        defaultCloseOperation=JFrame.EXIT_ON_CLOSE,
                        size=(600,400),
                        layout = GridLayout(1,2))
        self.add(self.getTrainingPane())
        self.add(self.getTestingPane())
        #self.pack()
        self.visible = True

    def getTrainingPane(self):
        def openTraining(event):
            global file_count
            file_count = 0
            file = JFileChooser()
            file.setMultiSelectionEnabled(True)
            val = file.showOpenDialog(self)
            if (val == JFileChooser.APPROVE_OPTION):
                f = file.getSelectedFiles()
                for fname in f:
                    #print fname.getName()
                    file_count = file_count+1
                    tb.append(fname.getName()+' selected \n')

        def runTrain(event):
            driverName="com.mysql.jdbc.Driver"
            Class.forName(driverName).newInstance()
            url = "jdbc:mysql://localhost/data"
            con = DriverManager.getConnection(url,"root","matin")
            print "connected"
            st = con.createStatement()
            res = st.executeQuery("select * from doc_count")
            res.next()
            p_count = res.getInt("POS_DOC")
            n_count = res.getInt("NEG_DOC")
            print "file count: %d"%(file_count)
            fo = open("cat.txt","w")
            if r1.isSelected():
                fo.write("positive")
                print "positive selected"
                st.executeUpdate("Update doc_count set POS_DOC =%d"%(file_count+p_count))
            else:
                fo.write("negative")
                print "negative selected"
                st.executeUpdate("Update doc_count set NEG_DOC =%d"%(file_count+n_count))
            fo.close()
            con.close()
            print "connection closed"
          
        t = TitledBorder('Training')
        bg = ButtonGroup()
        p = JPanel(GridBagLayout())
        c = GridBagConstraints(anchor=WEST)
        p.add(JLabel('Choose file for training:     '),c)
        c = GridBagConstraints(gridx=1,gridy=0,anchor=EAST)
        b = JButton('Open file', actionPerformed = openTraining)
        p.add(b,c)
        c = GridBagConstraints(gridx=0,gridy=1,anchor=WEST)
        r1 = JRadioButton('Positive')
        bg.add(r1)
        p.add(r1,c)
        c = GridBagConstraints(gridx=0,gridy=2,anchor=WEST)
        r2 = JRadioButton('Negative')
        bg.add(r2)
        p.add(r2,c)
        c = GridBagConstraints(gridx=1,gridy=2,anchor=EAST)
        train = JButton('Train', actionPerformed = runTrain)
        p.add(train,c)
        c = GridBagConstraints(gridx=0,gridy=3,anchor=WEST)
        p.add(JLabel('Display'),c)
        c = GridBagConstraints(gridx=0,gridy=4,gridwidth=2, fill = GridBagConstraints.HORIZONTAL )
        tb = JTextArea(rows = 9)
        scroll = JScrollPane(tb)
        p.add(scroll,c)
        p.setBorder(t)
        return p

    def getTestingPane(self):
        def openTesting(event):
            file = JFileChooser()
            file.showOpenDialog(self)
            val = file.showOpenDialog(self)
            if (val == JFileChooser.APPROVE_OPTION):
                f = file.getSelectedFile()
                #print f.getName()
                tb.append(f.getName()+' selected \n')

        def runTest(event):
            print "test running"

        t = TitledBorder('Testing')
        p = JPanel(GridBagLayout())
        c = GridBagConstraints(anchor=WEST)
        p.add(JLabel('Choose file for testing:      '),c)
        c = GridBagConstraints(gridx=1,gridy=0,anchor=EAST)
        b = JButton('Open file', actionPerformed = openTesting)
        p.add(b,c)
        c = GridBagConstraints(gridx=0,gridy=2,gridwidth=2,anchor=WEST)
        test = JButton('Test', actionPerformed = runTest)
        p.add(test,c)
        c = GridBagConstraints(gridx=0,gridy=3,anchor=WEST)
        p.add(JLabel('Display'),c)
        c = GridBagConstraints(gridx=0,gridy=4,gridwidth=2, fill = GridBagConstraints.HORIZONTAL )
        tb = JTextArea(rows = 9)
        scroll = JScrollPane(tb)
        p.add(scroll,c)
        p.setBorder(t)
        return p

if __name__ == "__main__":
    Main()