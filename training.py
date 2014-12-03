from __future__ import division
from java.lang import *
from java.sql import *

fo=open("cat.txt","r")
category = fo.read(8)
fo.close()
driverName="com.mysql.jdbc.Driver"
Class.forName(driverName).newInstance()
url = "jdbc:mysql://localhost/data"
con = DriverManager.getConnection(url,"root","matin") #connect to database
print "connected"
st = con.createStatement()
var = "japan"
res = st.executeQuery("Select * from dict where word='"+var+"'")
valid = 0
while(res.next()):
    valid = valid+1
    
if valid == 1: # word found in database
    print("found")
    res.prev()
    if category == "positive": #positive review
        pos = res.getInt("COUNT_POS")+1
        print "in_pos:%d"%(pos)
        st.executeUpdate("update dict set COUNT_POS = %d where WORD ='%s'" % (pos,var))
    else:       #negative review
        neg = res.getInt("COUNT_NEG")+1
        print "in_neg:%d"%(neg)
        st.executeUpdate("update dict set COUNT_NEG = %d where WORD ='%s'" % (neg,var))    
else:           #word not found in database
    print("not found")
    if category == "positive": #positive review
        st.executeUpdate("insert into dict (word,count_pos) values('%s',%d)" % (var,1))
    else:        #negative review
        st.executeUpdate("insert into dict (word,count_neg) values('%s',%d)" % (var,1))

res = st.executeQuery("Select count(*) from dict")
res.next()
voc = res.getInt("count(*)")
res = st.executeQuery("Select sum(count_pos) as val from dict")
res.next()
p_total = res.getInt("val")
res = st.executeQuery("Select sum(count_neg) as val from dict")
res.next()
n_total = res.getInt("val")
new = con.createStatement()
res = st.executeQuery("Select * from dict")
while(res.next()):
    h = res.getString("WORD")
    p = res.getInt("COUNT_POS")
    n = res.getInt("COUNT_NEG")
    print h
    print "count_positive:%d"%(p)
    print "count_negative:%d"%(n)
    print "total pos count:%d"%(p_total)
    print "total neg count:%d"%(n_total)
    print "voc:%d"%(voc)
    p_prob = (p+1)/(p_total+voc)
    n_prob = (n+1)/(n_total+voc)
    print "pos prob:%f"%(p_prob)
    print "neg prob:%f"%(n_prob)
    v = new.executeUpdate("update dict set PROB_POS = %f, PROB_NEG = %f where WORD ='%s'" % (p_prob,n_prob,h))
    print "ok"
con.close()
print "connection closed"