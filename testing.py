from __future__ import division
from java.lang import *
from java.sql import *
from math import *

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
p_prior = p_count/(p_count + n_count)
n_prior = n_count/(p_count + n_count)
print "pos_prior: %f"%(p_prior)
print "neg_prior: %f"%(n_prior)
p_sum = 0
n_sum = 0
lst = ['chinese','chinese','chinese','tokyo','japan']
for f in lst:
    print "\n%s"%(f)
    res = st.executeQuery("Select * from dict where word='"+f+"'")
    valid = 0
    while(res.next()):
        valid = valid+1

    if valid == 1: # word found in database
        res.prev()
        p_likelihood = res.getFloat("PROB_POS")
        n_likelihood = res.getFloat("PROB_NEG")
        print "p_likelihood:%f"%(p_likelihood)
        print "n_likelihood:%f"%(n_likelihood)
        p_sum = p_sum + log10(p_likelihood)
        n_sum = n_sum + log10(n_likelihood)

p_posterior = log10(p_prior)+p_sum
n_posterior = log10(n_prior)+n_sum
print "\nGood weightage:%f"%(p_posterior)
print "Bad weightage:%f"%(n_posterior)

if p_posterior > n_posterior:
    print "\nResult: GOOD"
else:
    print "\nResult: BAD"

con.close()
print"\nconnection closed"