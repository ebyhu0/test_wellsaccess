        ss="db_table = '"
                                x=line.find(ss)
                                ll=len(ss)
                                if x > 0 :
                                        x2=line.find("'",x+ll)
                                        str1=line[0:x+ll-1]
                                        str2=line[x+ll-1:x2].lower()
                                        str3=line[x2:]
                                        line=str1+str2+str3
                                        
                                        f3.write(str2)
                                f2.write( line )#     print(line)
                                # line=f.readline()
                                # pri