2021 / 10 / 7
#江苏大学
#董佳斌
#!/usr/bin/python
# -*- coding:utf-8 -*-
#1为矩形  2为菱形
import random

num1=str()
num2=str()
num3=str()
L=100
IS=0.1
AR=9
D=L*IS
B=(L-2*D)/(AR+1)
A=AR*B
for i in range(3):
    a=random.randint(1,2)                                                                                #region1-1
    #a=1
    if a==1:
        aa = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j1-1.txt", encoding='utf-8')
        aaa = aa.read()
        a1 = 4*A*B
    else:
        if a==2:
            aa = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l1-1.txt", encoding='utf-8')
            aaa = aa.read()
            a1 = 2*A*B
    #b=2
    b=random.randint(1,2)                                                                                #region1-2
    if b==1:
        if a==1:
            bb = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j1-2.txt", encoding='utf-8')
            bbb = bb.read()
            b1 = 4*A*B
        else:
            if a==2:
                bb = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j1-2z.txt", encoding='utf-8')
                bbb = bb.read()
                b1 = 7/2*A*B
    else:
        if b==2:
            if a==1:
                bb = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l1-2z.txt", encoding='utf-8')
                bbb = bb.read()
                b1 = 5/2*A*B
            else:
                if a==2:
                    bb = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l1-2.txt", encoding='utf-8')
                    bbb = bb.read()
                    b1 = 2*A*B
    #c=1
    c=random.randint(1,2)                                                                                #region1-3
    if c==1:
        if b==1:
            cc = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j1-3.txt", encoding='utf-8')
            ccc = cc.read()
            c1 = 4*A*B
        else:
            if b==2:
                cc = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j1-3z.txt", encoding='utf-8')
                ccc = cc.read()
                c1 = 7/2*A*B
    else:
        if c==2:
            if b==1:
                cc = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l1-3z.txt", encoding='utf-8')
                ccc = cc.read()
                c1 = 5/2*A*B
            else:
                if b==2:
                    cc = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l1-3.txt", encoding='utf-8')
                    ccc = cc.read()
                    c1 = 2*A*B
    #d=2
    d = random.randint(1, 2)                                                                                #region1-4
    if d == 1:
        if c==1:
            dd = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j1-4.txt", encoding='utf-8')
            ddd = dd.read()
            d1 = 4*A*B
        else:
            if c==2:
                dd = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j1-4z.txt", encoding='utf-8')
                ddd = dd.read()
                d1 = 7/2*A*B
    else:
        if d == 2:
            if c==1:
                dd = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l1-4z.txt", encoding='utf-8')
                ddd = dd.read()
                d1 = 5/2*A*B
            else:
                if c==2:
                    dd = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l1-4.txt", encoding='utf-8')
                    ddd = dd.read()
                    d1 = 2*A*B
    #e=1
    e = random.randint(1, 2)                                                                                #region2-1
    if e == 1:
        if a==1:
            ee = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j2-1.txt", encoding='utf-8')
            eee = ee.read()
            e1 = 4*A*B
        else:
            if a==2:
                ee = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j2-1x.txt", encoding='utf-8')
                eee = ee.read()
                e1 = 7/2*A*B
    else:
        if e == 2:
            if a==1:
                ee = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l2-1x.txt", encoding='utf-8')
                eee = ee.read()
                e1 = 5/2*A*B
            else:
                if a==2:
                    ee = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l2-1.txt", encoding='utf-8')
                    eee = ee.read()
                    e1 = 2*A*B
    #f=2
    f = random.randint(1, 2)                                                                                #region2-2
    if f == 1:
        if a==1:
            if b == 1:
                if e == 1:
                    ff = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j2-2+1111.txt", encoding='utf-8')
                    fff = ff.read()
                    f1 = 4*A*B
                else:
                    if e == 2:
                        ff = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j2-2+1121.txt", encoding='utf-8')
                        fff = ff.read()
                        f1 = 29/8*A*B
            else:
                if b == 2:
                    if e == 1:
                        ff = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j2-2+1211.txt", encoding='utf-8')
                        fff = ff.read()
                        f1 = 29/8*A*B
                    else:
                        if e == 2:
                            ff = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j2-2+1221.txt", encoding='utf-8')
                            fff = ff.read()
                            f1 = 13/4*A*B
        else:
            if a == 2:
                if b == 1:
                    if e == 1:
                        ff = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j2-2+2111.txt", encoding='utf-8')
                        fff = ff.read()
                        f1 = 31/8*A*B
                    else:
                        if e == 2:
                            ff = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j2-2+2121.txt", encoding='utf-8')
                            fff = ff.read()
                            f1 = 7/2*A*B
                else:
                    if b == 2:
                        if e == 1:
                            ff = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j2-2+2211.txt", encoding='utf-8')
                            fff = ff.read()
                            f1 = 7/2*A*B
                        else:
                            if e == 2:
                                ff = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j2-2+2221.txt",encoding='utf-8')
                                fff = ff.read()
                                f1 = 25/8*A*B
    else:
        if f == 2:
            if a == 1:
                if b == 1:
                    if e == 1:
                        ff = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l2-2+1112.txt", encoding='utf-8')
                        fff = ff.read()
                        f1 = 23/8*A*B
                    else:
                        if e == 2:
                            ff = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l2-2+1122.txt", encoding='utf-8')
                            fff = ff.read()
                            f1 = 5/2*A*B
                else:
                    if b == 2:
                        if e == 1:
                            ff = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l2-2+1212.txt", encoding='utf-8')
                            fff = ff.read()
                            f1 = 5/2*A*B
                        else:
                            if e == 2:
                                ff = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l2-2+1222.txt", encoding='utf-8')
                                fff = ff.read()
                                f1 = 17/8*A*B
            else:
                if a == 2:
                    if b == 1:
                        if e == 1:
                            ff = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l2-2+2112.txt", encoding='utf-8')
                            fff = ff.read()
                            f1 = 11/4*A*B
                        else:
                            if e == 2:
                                ff = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l2-2+2122.txt",encoding='utf-8')
                                fff = ff.read()
                                f1 = 19/8*A*B
                    else:
                        if b == 2:
                            if e == 1:
                                ff = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l2-2+2212.txt",encoding='utf-8')
                                fff = ff.read()
                                f1 = 19/8*A*B
                            else:
                                if e == 2:
                                    ff = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l2-2+2222.txt",encoding='utf-8')
                                    fff = ff.read()
                                    f1 = 2*A*B
    #g=1
    g = random.randint(1, 2)                                                                                #region2-3
    if g == 1:
        if b==1:
            if c == 1:
                if f == 1:
                    gg = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j2-3+1111.txt", encoding='utf-8')
                    ggg = gg.read()
                    g1 = 4*A*B
                else:
                    if f == 2:
                        gg = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j2-3+1121.txt", encoding='utf-8')
                        ggg = gg.read()
                        g1 = 29/8*A*B
            else:
                if c == 2:
                    if f == 1:
                        gg = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j2-3+1211.txt", encoding='utf-8')
                        ggg = gg.read()
                        g1 = 29/8*A*B
                    else:
                        if f == 2:
                            gg = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j2-3+1221.txt", encoding='utf-8')
                            ggg = gg.read()
                            g1 = 13/4*A*B
        else:
            if b == 2:
                if c == 1:
                    if f == 1:
                        gg = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j2-3+2111.txt", encoding='utf-8')
                        ggg = gg.read()
                        g1 = 31/8*A*B
                    else:
                        if f == 2:
                            gg = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j2-3+2121.txt", encoding='utf-8')
                            ggg = gg.read()
                            g1 = 7/2*A*B
                else:
                    if c == 2:
                        if f == 1:
                            gg = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j2-3+2211.txt", encoding='utf-8')
                            ggg = gg.read()
                            g1 = 7/2*A*B
                        else:
                            if f == 2:
                                gg = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j2-3+2221.txt",encoding='utf-8')
                                ggg = gg.read()
                                g1 = 25/8*A*B
    else:
        if g == 2:
            if b==1:
                if c == 1:
                    if f == 1:
                        gg = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l2-3+1112.txt", encoding='utf-8')
                        ggg = gg.read()
                        g1 = 23/8*A*B
                    else:
                        if f == 2:
                            gg = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l2-3+1122.txt", encoding='utf-8')
                            ggg = gg.read()
                            g1 = 5/2*A*B
                else:
                    if c == 2:
                        if f == 1:
                            gg = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l2-3+1212.txt", encoding='utf-8')
                            ggg = gg.read()
                            g1 = 5/2*A*B
                        else:
                            if f == 2:
                                gg = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l2-3+1222.txt", encoding='utf-8')
                                ggg = gg.read()
                                g1 = 17/8*A*B
            else:
                if b == 2:
                    if c == 1:
                        if f == 1:
                            gg = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l2-3+2112.txt", encoding='utf-8')
                            ggg = gg.read()
                            g1 = 11/4*A*B
                        else:
                            if f == 2:
                                gg = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l2-3+2122.txt",encoding='utf-8')
                                ggg = gg.read()
                                g1 = 19/8*A*B
                    else:
                        if c == 2:
                            if f == 1:
                                gg = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l2-3+2212.txt",encoding='utf-8')
                                ggg = gg.read()
                                g1 = 19/8*A*B
                            else:
                                if f == 2:
                                    gg = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l2-3+2222.txt",encoding='utf-8')
                                    ggg = gg.read()
                                    g1 = 2*A*B
    #h=2
    h = random.randint(1, 2)                                                                                #region2-4
    if h == 1:
        if c==1:
            if d == 1:
                if g == 1:
                    hh = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j2-4+1111.txt", encoding='utf-8')
                    hhh = hh.read()
                    h1 = 4*A*B
                else:
                    if g == 2:
                        hh = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j2-4+1121.txt", encoding='utf-8')
                        hhh = hh.read()
                        h1 = 29/8*A*B
            else:
                if d == 2:
                    if g == 1:
                        hh = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j2-4+1211.txt", encoding='utf-8')
                        hhh = hh.read()
                        h1 = 29/8*A*B
                    else:
                        if g == 2:
                            hh = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j2-4+1221.txt", encoding='utf-8')
                            hhh = hh.read()
                            h1 = 13/4*A*B
        else:
            if c == 2:
                if d == 1:
                    if g == 1:
                        hh = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j2-4+2111.txt", encoding='utf-8')
                        hhh = hh.read()
                        h1 = 31/8*A*B
                    else:
                        if g == 2:
                            hh = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j2-4+2121.txt", encoding='utf-8')
                            hhh = hh.read()
                            h1 = 7/2*A*B
                else:
                    if d == 2:
                        if g == 1:
                            hh = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j2-4+2211.txt", encoding='utf-8')
                            hhh = hh.read()
                            h1 = 7/2*A*B
                        else:
                            if g == 2:
                                hh = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j2-4+2221.txt",encoding='utf-8')
                                hhh = hh.read()
                                h1 = 25/8*A*B
    else:
        if h == 2:
            if c==1:
                if d == 1:
                    if g == 1:
                        hh = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l2-4+1112.txt", encoding='utf-8')
                        hhh = hh.read()
                        h1 = 23/8*A*B
                    else:
                        if g == 2:
                            hh = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l2-4+1122.txt", encoding='utf-8')
                            hhh = hh.read()
                            h1 = 5/2*A*B
                else:
                    if d == 2:
                        if g == 1:
                            hh = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l2-4+1212.txt", encoding='utf-8')
                            hhh = hh.read()
                            h1 = 5/2*A*B
                        else:
                            if g == 2:
                                hh = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l2-4+1222.txt", encoding='utf-8')
                                hhh = hh.read()
                                h1 = 17/8*A*B
            else:
                if c == 2:
                    if d == 1:
                        if g == 1:
                            hh = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l2-4+2112.txt", encoding='utf-8')
                            hhh = hh.read()
                            h1 = 11/4*A*B
                        else:
                            if g == 2:
                                hh = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l2-4+2122.txt",encoding='utf-8')
                                hhh = hh.read()
                                h1 = 19/8*A*B
                    else:
                        if d == 2:
                            if g == 1:
                                hh = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l2-4+2212.txt",encoding='utf-8')
                                hhh = hh.read()
                                h1 = 19/8*A*B
                            else:
                                if g == 2:
                                    hh = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l2-4+2222.txt",encoding='utf-8')
                                    hhh = hh.read()
                                    h1 = 2*A*B
    #l=1
    l = random.randint(1, 2)                                                                                #region3-1
    if l == 1:
        if e == 1:
            ll = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j3-1.txt", encoding='utf-8')
            lll = ll.read()
            l1 = 4*A*B
        else:
            if e == 2:
                ll = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j3-1x.txt", encoding='utf-8')
                lll = ll.read()
                l1 = 7/2*A*B
    else:
        if l == 2:
            if e == 1:
                ll = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l3-1x.txt", encoding='utf-8')
                lll = ll.read()
                l1 = 5/2*A*B
            else:
                if e == 2:
                    ll = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l3-1.txt", encoding='utf-8')
                    lll = ll.read()
                    l1 = 2*A*B
    #j=2
    j = random.randint(1, 2)                                                                                #region3-2
    if j == 1:
        if e==1:
            if f == 1:
                if l == 1:
                    jj = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j3-2+1111.txt", encoding='utf-8')
                    jjj = jj.read()
                    j1 = 4*A*B
                else:
                    if l == 2:
                        jj = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j3-2+1121.txt", encoding='utf-8')
                        jjj = jj.read()
                        j1 = 29/8*A*B
            else:
                if f == 2:
                    if l == 1:
                        jj = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j3-2+1211.txt", encoding='utf-8')
                        jjj = jj.read()
                        j1 = 29/8*A*B
                    else:
                        if l == 2:
                            jj = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j3-2+1221.txt", encoding='utf-8')
                            jjj = jj.read()
                            j1 = 13/4*A*B
        else:
            if e == 2:
                if f == 1:
                    if l == 1:
                        jj = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j3-2+2111.txt", encoding='utf-8')
                        jjj = jj.read()
                        j1 = 31/8*A*B
                    else:
                        if l == 2:
                            jj = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j3-2+2121.txt", encoding='utf-8')
                            jjj = jj.read()
                            j1 = 7/2*A*B
                else:
                    if f == 2:
                        if l == 1:
                            jj = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j3-2+2211.txt", encoding='utf-8')
                            jjj = jj.read()
                            j1 = 7/2*A*B
                        else:
                            if l == 2:
                                jj = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j3-2+2221.txt",encoding='utf-8')
                                jjj = jj.read()
                                j1 = 25/8*A*B
    else:
        if j == 2:
            if e==1:
                if f == 1:
                    if l == 1:
                        jj = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l3-2+1112.txt", encoding='utf-8')
                        jjj = jj.read()
                        j1 = 23/8*A*B
                    else:
                        if l == 2:
                            jj = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l3-2+1122.txt", encoding='utf-8')
                            jjj = jj.read()
                            j1 = 5/2*A*B
                else:
                    if f == 2:
                        if l == 1:
                            jj = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l3-2+1212.txt", encoding='utf-8')
                            jjj = jj.read()
                            j1 = 5/2*A*B
                        else:
                            if l == 2:
                                jj = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l3-2+1222.txt", encoding='utf-8')
                                jjj = jj.read()
                                j1 = 17/8*A*B
            else:
                if e == 2:
                    if f == 1:
                        if l == 1:
                            jj = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l3-2+2112.txt", encoding='utf-8')
                            jjj = jj.read()
                            j1 = 11/4*A*B
                        else:
                            if l == 2:
                                jj = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l3-2+2122.txt",encoding='utf-8')
                                jjj = jj.read()
                                j1 = 19/8*A*B
                    else:
                        if f == 2:
                            if l == 1:
                                jj = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l3-2+2212.txt",encoding='utf-8')
                                jjj = jj.read()
                                j1 = 19/8*A*B
                            else:
                                if l == 2:
                                    jj = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l3-2+2222.txt",encoding='utf-8')
                                    jjj = jj.read()
                                    j1 = 2*A*B
    #k=1
    k = random.randint(1, 2)                                                                                #region3-3
    if k == 1:
        if f==1:
            if g == 1:
                if j == 1:
                    kk = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j3-3+1111.txt", encoding='utf-8')
                    kkk = kk.read()
                    k1 = 4*A*B
                else:
                    if j == 2:
                        kk = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j3-3+1121.txt", encoding='utf-8')
                        kkk = kk.read()
                        k1 = 29/8*A*B
            else:
                if g == 2:
                    if j == 1:
                        kk = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j3-3+1211.txt", encoding='utf-8')
                        kkk = kk.read()
                        k1 = 29/8*A*B
                    else:
                        if j == 2:
                            kk = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j3-3+1221.txt", encoding='utf-8')
                            kkk = kk.read()
                            k1 = 13/4*A*B
        else:
            if f==2:
                if g == 1:
                    if j == 1:
                        kk = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j3-3+2111.txt", encoding='utf-8')
                        kkk = kk.read()
                        k1 = 31/8*A*B
                    else:
                        if j == 2:
                            kk = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j3-3+2121.txt", encoding='utf-8')
                            kkk = kk.read()
                            k1 = 7/2*A*B
                else:
                    if g == 2:
                        if j == 1:
                            kk = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j3-3+2211.txt", encoding='utf-8')
                            kkk = kk.read()
                            k1 = 7/2*A*B
                        else:
                            if j == 2:
                                kk = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j3-3+2221.txt",encoding='utf-8')
                                kkk = kk.read()
                                k1 = 25/8*A*B
    else:
        if k == 2:
            if f==1:
                if g == 1:
                    if j == 1:
                        kk = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l3-3+1112.txt", encoding='utf-8')
                        kkk = kk.read()
                        k1 = 23/8*A*B
                    else:
                        if j == 2:
                            kk = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l3-3+1122.txt", encoding='utf-8')
                            kkk = kk.read()
                            k1 = 5/2*A*B
                else:
                    if g == 2:
                        if j == 1:
                            kk = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l3-3+1212.txt", encoding='utf-8')
                            kkk = kk.read()
                            k1 = 5/2*A*B
                        else:
                            if j == 2:
                                kk = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l3-3+1222.txt", encoding='utf-8')
                                kkk = kk.read()
                                k1 = 17/8*A*B
            else:
                if f == 2:
                    if g == 1:
                        if j == 1:
                            kk = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l3-3+2112.txt", encoding='utf-8')
                            kkk = kk.read()
                            k1 = 11/4*A*B
                        else:
                            if j == 2:
                                kk = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l3-3+2122.txt",encoding='utf-8')
                                kkk = kk.read()
                                k1 = 19/8*A*B
                    else:
                        if g == 2:
                            if j == 1:
                                kk = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l3-3+2212.txt",encoding='utf-8')
                                kkk = kk.read()
                                k1 = 19/8*A*B
                            else:
                                if j == 2:
                                    kk = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l3-3+2222.txt",encoding='utf-8')
                                    kkk = kk.read()
                                    k1 = 2*A*B
    #m=2
    m = random.randint(1, 2)                                                                                #region3-4
    if m == 1:
        if g==1:
            if h == 1:
                if k == 1:
                    mm = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j3-4+1111.txt", encoding='utf-8')
                    mmm = mm.read()
                    m1 = 4*A*B
                else:
                    if k == 2:
                        mm = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j3-4+1121.txt", encoding='utf-8')
                        mmm = mm.read()
                        m1 = 29/8*A*B
            else:
                if h == 2:
                    if k == 1:
                        mm = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j3-4+1211.txt", encoding='utf-8')
                        mmm = mm.read()
                        m1 = 29/8*A*B
                    else:
                        if k == 2:
                            mm = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j3-4+1221.txt", encoding='utf-8')
                            mmm = mm.read()
                            m1 = 13/4*A*B
        else:
            if g == 2:
                if h == 1:
                    if k == 1:
                        mm = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j3-4+2111.txt", encoding='utf-8')
                        mmm = mm.read()
                        m1 = 31/8*A*B
                    else:
                        if k == 2:
                            mm = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j3-4+2121.txt", encoding='utf-8')
                            mmm = mm.read()
                            m1 = 7/2*A*B
                else:
                    if h == 2:
                        if k == 1:
                            mm = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j3-4+2211.txt", encoding='utf-8')
                            mmm = mm.read()
                            m1 = 7/2*A*B
                        else:
                            if k == 2:
                                mm = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j3-4+2221.txt",encoding='utf-8')
                                mmm = mm.read()
                                m1 = 25/8*A*B
    else:
        if m == 2:
            if g==1:
                if h == 1:
                    if k == 1:
                        mm = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l3-4+1112.txt", encoding='utf-8')
                        mmm = mm.read()
                        m1 = 23/8*A*B
                    else:
                        if k == 2:
                            mm = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l3-4+1122.txt", encoding='utf-8')
                            mmm = mm.read()
                            m1 = 5/2*A*B
                else:
                    if h == 2:
                        if k == 1:
                            mm = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l3-4+1212.txt", encoding='utf-8')
                            mmm = mm.read()
                            m1 = 5/2*A*B
                        else:
                            if k == 2:
                                mm = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l3-4+1222.txt", encoding='utf-8')
                                mmm = mm.read()
                                m1 = 17/8*A*B
            else:
                if g == 2:
                    if h == 1:
                        if k == 1:
                            mm = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l3-4+2112.txt", encoding='utf-8')
                            mmm = mm.read()
                            m1 = 11/4*A*B
                        else:
                            if k == 2:
                                mm = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l3-4+2122.txt",encoding='utf-8')
                                mmm = mm.read()
                                m1 = 19/8*A*B
                    else:
                        if h == 2:
                            if k == 1:
                                mm = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l3-4+2212.txt",encoding='utf-8')
                                mmm = mm.read()
                                m1 = 19/8*A*B
                            else:
                                if k == 2:
                                    mm = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l3-4+2222.txt",encoding='utf-8')
                                    mmm = mm.read()
                                    m1 = 2*A*B
    #n=1
    n = random.randint(1, 2)                                                                                #region4-1
    if n == 1:
        if l == 1:
            nn = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j4-1.txt", encoding='utf-8')
            nnn = nn.read()
            n1 = 4*A*B
        else:
            if l == 2:
                nn = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j4-1x.txt", encoding='utf-8')
                nnn = nn.read()
                n1 = 7/2*A*B
    else:
        if n == 2:
            if l == 1:
                nn = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l4-1x.txt", encoding='utf-8')
                nnn = nn.read()
                n1 = 5/2*A*B
            else:
                if l == 2:
                    nn = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l4-1.txt", encoding='utf-8')
                    nnn = nn.read()
                    n1 = 2*A*B
    #o=2
    o = random.randint(1, 2)                                                                                #region4-2
    if o == 1:
        if l==1:
            if j == 1:
                if n == 1:
                    oo = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j4-2+1111.txt", encoding='utf-8')
                    ooo = oo.read()
                    o1 = 4*A*B
                else:
                    if n == 2:
                        oo = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j4-2+1121.txt", encoding='utf-8')
                        ooo = oo.read()
                        o1 = 29/8*A*B
            else:
                if j == 2:
                    if n == 1:
                        oo = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j4-2+1211.txt", encoding='utf-8')
                        ooo = oo.read()
                        o1 = 29/8*A*B
                    else:
                        if n == 2:
                            oo = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j4-2+1221.txt", encoding='utf-8')
                            ooo = oo.read()
                            o1 = 13/4*A*B
        else:
            if l == 2:
                if j == 1:
                    if n == 1:
                        oo = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j4-2+2111.txt", encoding='utf-8')
                        ooo = oo.read()
                        o1 = 31/8*A*B
                    else:
                        if n == 2:
                            oo = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j4-2+2121.txt", encoding='utf-8')
                            ooo = oo.read()
                            o1 = 7/2*A*B
                else:
                    if j == 2:
                        if n == 1:
                            oo = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j4-2+2211.txt", encoding='utf-8')
                            ooo = oo.read()
                            o1 = 7/2*A*B
                        else:
                            if n == 2:
                                oo = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j4-2+2221.txt",encoding='utf-8')
                                ooo = oo.read()
                                o1 = 25/8*A*B
    else:
        if o == 2:
            if l==1:
                if j == 1:
                    if n == 1:
                        oo = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l4-2+1112.txt", encoding='utf-8')
                        ooo = oo.read()
                        o1 = 23/8*A*B
                    else:
                        if n == 2:
                            oo = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l4-2+1122.txt", encoding='utf-8')
                            ooo = oo.read()
                            o1 = 5/2*A*B
                else:
                    if j == 2:
                        if n == 1:
                            oo = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l4-2+1212.txt", encoding='utf-8')
                            ooo = oo.read()
                            o1 = 5/2*A*B
                        else:
                            if n == 2:
                                oo = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l4-2+1222.txt", encoding='utf-8')
                                ooo = oo.read()
                                o1 = 17/8*A*B
            else:
                if l == 2:
                    if j == 1:
                        if n == 1:
                            oo = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l4-2+2112.txt", encoding='utf-8')
                            ooo = oo.read()
                            o1 = 11/4*A*B
                        else:
                            if n == 2:
                                oo = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l4-2+2122.txt",encoding='utf-8')
                                ooo = oo.read()
                                o1 = 19/8*A*B
                    else:
                        if j == 2:
                            if n == 1:
                                oo = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l4-2+2212.txt",encoding='utf-8')
                                ooo = oo.read()
                                o1 = 19/8*A*B
                            else:
                                if n == 2:
                                    oo = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l4-2+2222.txt",encoding='utf-8')
                                    ooo = oo.read()
                                    o1 = 2*A*B
    #p=1
    p = random.randint(1, 2)                                                                                #region4-3
    if p == 1:
        if j==1:
            if k == 1:
                if o == 1:
                    pp = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j4-3+1111.txt", encoding='utf-8')
                    ppp = pp.read()
                    p1 = 4*A*B
                else:
                    if o == 2:
                        pp = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j4-3+1121.txt", encoding='utf-8')
                        ppp = pp.read()
                        p1 = 29/8*A*B
            else:
                if k == 2:
                    if o == 1:
                        pp = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j4-3+1211.txt", encoding='utf-8')
                        ppp = pp.read()
                        p1 = 29/8*A*B
                    else:
                        if o == 2:
                            pp = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j4-3+1221.txt", encoding='utf-8')
                            ppp = pp.read()
                            p1 = 13/4*A*B
        else:
            if j == 2:
                if k == 1:
                    if o == 1:
                        pp = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j4-3+2111.txt", encoding='utf-8')
                        ppp = pp.read()
                        p1 = 31/8*A*B
                    else:
                        if o == 2:
                            pp = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j4-3+2121.txt", encoding='utf-8')
                            ppp = pp.read()
                            p1 = 7/2*A*B
                else:
                    if k == 2:
                        if o == 1:
                            pp = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j4-3+2211.txt", encoding='utf-8')
                            ppp = pp.read()
                            p1 = 7/2*A*B
                        else:
                            if o == 2:
                                pp = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j4-3+2221.txt",encoding='utf-8')
                                ppp = pp.read()
                                p1 = 25/8*A*B
    else:
        if p == 2:
            if j==1:
                if k == 1:
                    if o == 1:
                        pp = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l4-3+1112.txt", encoding='utf-8')
                        ppp = pp.read()
                        p1 = 23/8*A*B
                    else:
                        if o == 2:
                            pp = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l4-3+1122.txt", encoding='utf-8')
                            ppp = pp.read()
                            p1 = 5/2*A*B
                else:
                    if k == 2:
                        if o == 1:
                            pp = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l4-3+1212.txt", encoding='utf-8')
                            ppp = pp.read()
                            p1 = 5/2*A*B
                        else:
                            if o == 2:
                                pp = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l4-3+1222.txt", encoding='utf-8')
                                ppp = pp.read()
                                p1 = 17/8*A*B
            else:
                if j == 2:
                    if k == 1:
                        if o == 1:
                            pp = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l4-3+2112.txt", encoding='utf-8')
                            ppp = pp.read()
                            p1 = 11/4*A*B
                        else:
                            if o == 2:
                                pp = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l4-3+2122.txt",encoding='utf-8')
                                ppp = pp.read()
                                p1 = 19/8*A*B
                    else:
                        if k == 2:
                            if o == 1:
                                pp = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l4-3+2212.txt",encoding='utf-8')
                                ppp = pp.read()
                                p1 = 19/8*A*B
                            else:
                                if o == 2:
                                    pp = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l4-3+2222.txt",encoding='utf-8')
                                    ppp = pp.read()
                                    p1 = 2*A*B
    #q=2
    q = random.randint(1, 2)                                                                                #region4-4
    if q == 1:
        if k==1:
            if m == 1:
                if p == 1:
                    qq = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j4-4+1111.txt", encoding='utf-8')
                    qqq = qq.read()
                    q1 = 4*A*B
                else:
                    if p == 2:
                        qq = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j4-4+1121.txt", encoding='utf-8')
                        qqq = qq.read()
                        q1 = 29/8*A*B
            else:
                if m == 2:
                    if p == 1:
                        qq = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j4-4+1211.txt", encoding='utf-8')
                        qqq = qq.read()
                        q1 = 29/8*A*B
                    else:
                        if p == 2:
                            qq = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j4-4+1221.txt", encoding='utf-8')
                            qqq = qq.read()
                            q1 = 13/4*A*B
        else:
            if k == 2:
                if m == 1:
                    if p == 1:
                        qq = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j4-4+2111.txt", encoding='utf-8')
                        qqq = qq.read()
                        q1 = 31/8*A*B
                    else:
                        if p == 2:
                            qq = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j4-4+2121.txt", encoding='utf-8')
                            qqq = qq.read()
                            q1 = 7/2*A*B
                else:
                    if m == 2:
                        if p == 1:
                            qq = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j4-4+2211.txt", encoding='utf-8')
                            qqq = qq.read()
                            q1 = 7/2*A*B
                        else:
                            if p == 2:
                                qq = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\j4-4+2221.txt",encoding='utf-8')
                                qqq = qq.read()
                                q1 = 25/8*A*B
    else:
        if q == 2:
            if k==1:
                if m == 1:
                    if p == 1:
                        qq = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l4-4+1112.txt", encoding='utf-8')
                        qqq = qq.read()
                        q1 = 23/8*A*B
                    else:
                        if p == 2:
                            qq = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l4-4+1122.txt", encoding='utf-8')
                            qqq = qq.read()
                            q1 = 5/2*A*B
                else:
                    if m == 2:
                        if p == 1:
                            qq = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l4-4+1212.txt", encoding='utf-8')
                            qqq = qq.read()
                            q1 = 5/2*A*B
                        else:
                            if p == 2:
                                qq = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l4-4+1222.txt", encoding='utf-8')
                                qqq = qq.read()
                                q1 = 17/8*A*B
            else:
                if k == 2:
                    if m == 1:
                        if p == 1:
                            qq = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l4-4+2112.txt", encoding='utf-8')
                            qqq = qq.read()
                            q1 = 11/4*A*B
                        else:
                            if p == 2:
                                qq = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l4-4+2122.txt",encoding='utf-8')
                                qqq = qq.read()
                                q1 = 19/8*A*B
                    else:
                        if m == 2:
                            if p == 1:
                                qq = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l4-4+2212.txt",encoding='utf-8')
                                qqq = qq.read()
                                q1 = 19/8*A*B
                            else:
                                if p == 2:
                                    qq = open("E:\\BaiduNetdiskDownload\\shujuku\\yuanshiku\\l4-4+2222.txt",encoding='utf-8')
                                    qqq = qq.read()
                                    q1 = 2*A*B
    num = i+1
    a2 = str(a1)
    b2 = str(b1)
    c2 = str(c1)
    d2 = str(d1)
    e2 = str(e1)
    f2 = str(f1)
    g2 = str(g1)
    h2 = str(h1)
    l2 = str(l1)
    j2 = str(j1)
    k2 = str(k1)
    m2 = str(m1)
    n2 = str(n1)
    o2 = str(o1)
    p2 = str(p1)
    q2 = str(q1)
    SSS = str(a1+b1+c1+d1+e1+f1+g1+h1+l1+j1+k1+m1+n1+o1+p1+q1)
    file = open("F:\\2022222\\pinjiemx"+str(i+1)+".txt",'w')
    file.write('shell mkdir ' + str(num) + "\n")
    file.write('log '+ str(num) +'/log' + str(num) + '.txt' + "\n")
    file.write('#')
    file.write(a2 + "\t")
    file.write(b2 + "\t")
    file.write(c2 + "\t")
    file.write(d2 + "\t")
    file.write(e2 + "\t")
    file.write(f2 + "\t")
    file.write(g2 + "\t")
    file.write(h2 + "\t")
    file.write(l2 + "\t")
    file.write(j2 + "\t")
    file.write(k2 + "\t")
    file.write(m2 + "\t")
    file.write(n2 + "\t")
    file.write(o2 + "\t")
    file.write(p2 + "\t")
    file.write(q2 + "\n")
    file.write('#')
    file.write(SSS + "\n")
    file.write('include chushihua.txt' + "\n")
    file.write(aaa)
    file.write('\n')
    file.write(bbb)
    file.write('\n')
    file.write(ccc)
    file.write('\n')
    file.write(ddd)
    file.write('\n')
    file.write(eee)
    file.write('\n')
    file.write(fff)
    file.write('\n')
    file.write(ggg)
    file.write('\n')
    file.write(hhh)
    file.write('\n')
    file.write(lll)
    file.write('\n')
    file.write(jjj)
    file.write('\n')
    file.write(kkk)
    file.write('\n')
    file.write(mmm)
    file.write('\n')
    file.write(nnn)
    file.write('\n')
    file.write(ooo)
    file.write('\n')
    file.write(ppp)
    file.write('\n')
    file.write(qqq)
    file.write('\n')
    file.write('mass    * 12.011150 \n')
    file.write('write_data  '+ str(num) +'/pj'+str(num)+'.dat \n')  #
    file.write('clear \n')
    file.write('jump  pinjiemx'+str(i+2)+'.txt')
    file.close()
print(a1)

